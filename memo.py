import os
import glob
import time
import json

# {
#     "meta": {
#         "title": "new memo",
#         "category": "aa",
#         "favorite": true,
#         "created_time": 1592411559.8346415,
#         "last_edit_time": 1592411559.8346415
#     },
#     "content": "memo is here\r\n"
# }

# memo = dict()
# memo["meta"] = dict()
# memo["meta"]["title"]
# memo["meta"]["category"]
# memo["meta"]["favorite"]
# memo["meta"]["created_time"]
# memo["meta"]["last_edit_time"]
# memo["content"]


class MemoManager():
    def __init__(self):
        pass

    def get_memo_list(self):
        memo_list = list()
        memo_path_list = glob.glob("./memo/*.json")
        for memo_path in memo_path_list:
            f = open(memo_path, 'r').read()
            memo_file = json.loads(f)
            memo_id = float(os.path.splitext( os.path.basename(memo_path) )[0])
            
            memo = dict()
            memo["id"] = memo_id
            memo["meta"] = dict()
            memo["meta"]["title"] = memo_file["meta"]["title"]
            memo["meta"]["category"] = memo_file["meta"]["category"]
            memo["meta"]["favorite"] = memo_file["meta"]["favorite"]
            memo["meta"]["created_time"] = memo_file["meta"]["created_time"]
            memo["meta"]["last_edit_time"] = memo_file["meta"]["last_edit_time"]
            memo["content"] = memo_file["content"]

            memo_list.append(memo)
        return memo_list

    def get_memo_content(self, memo_id):
        try:
            f = open("./memo/{}.json".format(memo_id)).read()
            memo_file = json.loads(f)
            memo = dict()
            memo["id"] = memo_id
            memo["meta"] = dict()
            memo["meta"]["title"] = memo_file["meta"]["title"]
            memo["meta"]["category"] = memo_file["meta"]["category"]
            memo["meta"]["favorite"] = memo_file["meta"]["favorite"]
            memo["meta"]["created_time"] = memo_file["meta"]["created_time"]
            memo["meta"]["last_edit_time"] = memo_file["meta"]["last_edit_time"]
            memo["content"] = memo_file["content"]
            return memo
        except Exception as identifier:
            print(identifier)
            return False

    def delete_memo(self, ID):
        if os.path.exists("./memo/{}.json".format(ID)):
            os.remove("./memo/{}.json".format(ID))
            return True
        else:
            print("The file does not exist")
            return False

    def create_memo(self, ID, memo_object):
        try:
            memo = dict()
            memo["meta"] = dict()
            memo["meta"]["title"] = memo_object["meta"]["title"]
            memo["meta"]["category"] = memo_object["meta"]["category"]
            memo["meta"]["favorite"] = memo_object["meta"]["favorite"]
            memo["meta"]["created_time"] = time.time()
            memo["meta"]["last_edit_time"] = time.time()
            memo["content"] = memo_object["content"]
            
            file_name = "./memo/{}.json".format(ID)
            f = open(file_name, 'w')
            f.write(json.dumps(memo))
            return True
        except Exception as e:
            print(e)
            return False

    def edit_memo(self, memo_id, memo_object):
        try:
            memo = self.get_memo_content(memo_id)
            memo["id"]=memo_id
            memo["meta"]["title"] = memo_object["meta"]["title"]
            memo["meta"]["category"] = memo_object["meta"]["category"]
            memo["meta"]["favorite"] = memo_object["meta"]["favorite"]
            memo["meta"]["last_edit_time"] = time.time()
            memo["content"] = memo_object["content"]
            self.delete_memo(memo_id)
            file_name = "./memo/{}.json".format(memo_id)
            with open(file_name, 'w') as f:
                f.write(json.dumps(memo))
            return True
        except Exception as identifier:
            print(identifier)
            return False
