from memo import MemoManager
import time

from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for

memoManager = MemoManager()
app = Flask(__name__)

@app.route('/list', methods=['GET'])
def memo_list():
    memo_list = memo.get_memo_list()
    return render_template('list.html', memo_list=memo_list)

@app.route('/viewer', methods=['GET'])
def viewer():
    memo_id = request.args.get('id')
    memo = memo.get_memo_content(memo_id)
    return render_template('viewer.html', memo=memo)

@app.route('/')
def main():
    return redirect(url_for(get_memo_list))

@app.route('/memo', methods=['POST'])
def create_memo():
    # request 에서 json 가져오기 https://stackoverflow.com/questions/20001229/how-to-get-posted-json-in-flask
    
    memo_id = request.form["id"]

    memo = dict()
    memo["meta"] = dict()
    memo["meta"]["title"] = memo_object["meta"]["title"]
    memo["meta"]["category"] = memo_object["meta"]["category"]
    memo["meta"]["favorite"] = memo_object["meta"]["favorite"]
    memo["meta"]["created_time"] = time.time()
    memo["meta"]["last_edit_time"] = time.time()
    memo["content"] = memo_object["content"]

    result = memoManager.create_memo(memo_id, memo)
    if result:
        return render_template("memo_message.html", message="created")
    else :
        return render_template("memo_message.html", message="failed")

# @app.route('/memo_list', methods=['GET'])
# def get_memo_list():
#     # 쿼리 스트링 가져오기 https://stackoverflow.com/questions/11774265/how-do-you-get-a-query-string-on-flask
#     # query_string = request.args.get('from')
#     # query_string = request.args.get('to')
#     result = memo.get_memo_list()
#     return render_template("memo_list.html", memo_list=result)

# @app.route('/memo_view', methods=['GET'])
# def get_memo_content():
#     # 쿼리 스트링 가져오기 https://stackoverflow.com/questions/11774265/how-do-you-get-a-query-string-on-flask
#     memo_id = request.args.get('id')
#     result = memo.get_memo_content(memo_id)
#     if result:
#         return render_template("memo_view.html", memo=result)
#     else:
#         return render_template("memo_message.html", message="failed to get memo")

@app.route('/memo', methods=['PUT'])
def edit_memo():
    memo_id = request.form["id"]

    memo = dict()
    memo["meta"] = dict()
    memo["meta"]["title"] = memo_object["meta"]["title"]
    memo["meta"]["category"] = memo_object["meta"]["category"]
    memo["meta"]["favorite"] = memo_object["meta"]["favorite"]
    memo["meta"]["created_time"] = memo["meta"]["created_time"]
    memo["meta"]["last_edit_time"] = time.time()
    memo["content"] = memo_object["content"]

    result = memo.edit_memo(memo_id, memo)
    if result:
        return render_template("memo_message.html", message="success")
    else:
        return render_template("memo_message.html", message="failed")

@app.route('/memo', methods=['DELETE'])
def delete_memo():
    memo_id = request.args.get('id')
    result = memo.delete_memo(memo_id)
    if result:
        return render_template("memo_message.html", message="success")
    else:
        return render_template("memo_message.html", message="failed")
        
if __name__ == "__main__":
    app.run()