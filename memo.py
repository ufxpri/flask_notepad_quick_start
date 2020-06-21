import os
import glob
import time
import json

class Memo():
    def __init__(self):
        pass

    def get_memo_list(self):
        memo_head_list = list()
        memo_path_list = glob.glob("./memo/*.json")
        for memo_path in memo_path_list:
            f = open(memo_path, 'r').read()
            memo = json.loads(f)
            memo_head_list.append(memo["head"])
        return memo_head_list

    def get_memo_content(self, ID):
        try:
            f = open("./memo/{}.json".format(ID)).read()
            memo = json.loads(f)
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

    def create_memo(self, ID, content):
        try:
            file_name = "./memo/{}.json".format(ID)
            f = open(file_name, 'w')
            f.write(content)
            return True
        except Exception as e:
            print(e)
            return False

    def edit_memo(self, ID, content):
        try:
            content = json.dumps(content)
            self.delete_memo(ID)
            self.create_memo(ID, content)
            return True
        except Exception as identifier:
            print(identifier)
            return False
