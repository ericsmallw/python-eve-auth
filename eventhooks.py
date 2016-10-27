import bcrypt
import sys
import time

def hash_pass_and_token(items):
    for item in items:
        try:
            token = item["password"] + item["username"] + str(time.time())
            item['token'] = bcrypt.hashpw(token.encode('utf-8'), bcrypt.gensalt())
            item["password"] = bcrypt.hashpw(item["password"].encode('utf-8'), bcrypt.gensalt())
            print(item["token"])
            print(item["role"])

        except:
            print("Unexpected error:", sys.exc_info()[0])
            print("Unexpected error:", sys.exc_info()[1])
            print("Unexpected error:", sys.exc_info()[2])