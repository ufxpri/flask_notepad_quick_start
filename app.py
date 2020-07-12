from memo import MemoManager
import time
from datetime import datetime

from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for

memoManager = MemoManager()
app = Flask(__name__)

def datetime_formater(datetime_):
    if datetime_.date() < datetime.today().date():
        return datetime_.strftime('%Y-%m-%d')
    else:
        return datetime_.strftime('%H:%M:%S')


@app.route('/list', methods=['GET'])
def memo_list():
    memo_list = memoManager.get_memo_list()
    for i, memo in enumerate(memo_list):
        last_edit_time = datetime.fromtimestamp(memo["meta"]["last_edit_time"])
        memo_list[i]["meta"]["last_edit_time"] = datetime_formater(last_edit_time)
    return render_template('list.html', memo_list=memo_list)

@app.route('/viewer', methods=['GET'])
def viewer():
    memo_id = request.args.get('id')
    memo = memoManager.get_memo_content(memo_id)
    category_list = ["A","B","C","D","E"] # TODO get category list
    last_edit_time = datetime.fromtimestamp(memo["meta"]["last_edit_time"])
    memo["meta"]["last_edit_time"] = datetime_formater(last_edit_time)
    created_time = datetime.fromtimestamp(memo["meta"]["created_time"])
    memo["meta"]["created_time"] = datetime_formater(created_time)
    return render_template('viewer.html', memo=memo, category_list=category_list)

@app.route('/create', methods=['GET'])
def create():
    return render_template('create.html')

@app.route('/')
def main():
    return redirect(url_for("memo_list"))

@app.route('/memo', methods=['POST'])
def create_memo():
    # request 에서 json 가져오기 https://stackoverflow.com/questions/20001229/how-to-get-posted-json-in-flask
    memo_object = request.get_json()
    memo_id = time.time()

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
        return "created"
    else :
        return "failed"

@app.route('/memo', methods=['PUT'])
def edit_memo():
    memo_object = request.get_json()
    memo_id = memo_object["id"]

    memo = dict()
    memo["meta"] = dict()
    memo["meta"]["title"] = memo_object["meta"]["title"]
    memo["meta"]["category"] = memo_object["meta"]["category"]
    memo["meta"]["favorite"] = memo_object["meta"]["favorite"]
    memo["content"] = memo_object["content"]

    result = memoManager.edit_memo(memo_id, memo)
    if result:
        return "success"
    else:
        return "failed"

@app.route('/memo', methods=['DELETE'])
def delete_memo():
    memo_id = request.args.get('id')
    result = memoManager.delete_memo(memo_id)
    if result:
        return "deleted"
    else:
        return "failed"
        
if __name__ == "__main__":
    app.run()