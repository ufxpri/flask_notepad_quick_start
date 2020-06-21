from memo import Memo
import time

from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for

memo = Memo()
app = Flask(__name__)

def memo_list():
    return " 메모 목록과 프리뷰만 보여주는 UI "

@app.route('/')
def main():
    return redirect(url_for(get_memo_list))

@app.route('/create_memo', methods=['GET'])
def create_memo():
    # request 에서 json 가져오기 https://stackoverflow.com/questions/20001229/how-to-get-posted-json-in-flask
    id_ = time.time()
    head = dict()
    head["id"] = id_
    head["title"] = ""
    head["writer"] = "temp_user"
    head["time"] = time.time()
    content = dict()
    content["head"] = head
    content["body"] = ""

    memo_temp = content
    if memo_temp:
        return render_template("memo_view.html", memo=memo_temp)
    else :
        return render_template("memo_message.html", message="failed")

@app.route('/memo_list', methods=['GET'])
def get_memo_list():
    # 쿼리 스트링 가져오기 https://stackoverflow.com/questions/11774265/how-do-you-get-a-query-string-on-flask
    # query_string = request.args.get('from')
    # query_string = request.args.get('to')
    result = memo.get_memo_list()
    return render_template("memo_list.html", memo_list=result)

@app.route('/memo_view', methods=['GET'])
def get_memo_content():
    # 쿼리 스트링 가져오기 https://stackoverflow.com/questions/11774265/how-do-you-get-a-query-string-on-flask
    memo_id = request.args.get('id')
    result = memo.get_memo_content(memo_id)
    if result:
        return render_template("memo_view.html", memo=result)
    else:
        return render_template("memo_message.html", message="failed to get memo")

@app.route('/edit_memo', methods=['POST'])
def edit_memo():
    id_ = request.form["id"]
    head = dict()
    head["id"] = id_
    head["title"] = request.form["title"]
    head["writer"] = request.form["user"]
    head["time"] = time.time()
    content = dict()
    content["head"] = head
    content["body"] = request.form["body"]

    result = memo.edit_memo(id_, content)
    if result:
        return render_template("memo_message.html", message="success")
    else:
        return render_template("memo_message.html", message="failed")

@app.route('/delete_memo', methods=['GET'])
def delete_memo():
    memo_id = request.args.get('id')
    result = memo.delete_memo(memo_id)
    if result:
        return render_template("memo_message.html", message="success")
    else:
        return render_template("memo_message.html", message="failed")
        
if __name__ == "__main__":
    app.run()