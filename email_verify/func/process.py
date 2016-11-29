# coding:utf-8
from func.db import DataBase
import requests, json, datetime

host = 'localhost'
user = 'root'
pwd = '123456'
base = 'shiyanlou'
table = 'user'

API_USER = 'shine_forever_test_zFZOBK' # input your apt_user
API_KEY = 'su9zZf98O0ooT5i8' # input your spi_key
url = "http://www.sendcloud.net/webapi/mail.send_template.json"
base_link = "http:127.0.0.1:8000/do_verificatin?"

one_day_in_second = 5184000


def write_data(name, email):
    database = DataBase(host, user, pwd, base)
    database.set_table(table)
    outcome = database.insert_record(name, email)
    database.close()
    return outcome


def send_email(name, email):
    database = DataBase(host, user, pwd, base)
    database.set_table(table)
    record = database.query_by_email(name, email)
    database.close()
    name = record[1]
    email = record[2]
    token = record[3]
    authcode = record[5]

    link = base_link + 'token=%s&authcode=%s' % (token, authcode)
    sub_vars = {
        'to': [email],
        'sub': {
            '%name%': [name],
            '%url%': [link],
        }
    }
    params = {
        "api_user": API_USER,
        "api_key": API_KEY,
        "template_invoke_name": "test_template_active",
        "substitution_vars": json.dumps(sub_vars),
        "from": "service@sendcloud.im",
        "fromname": "shiyanlou",
        "subject": "Welcome to Shiyanlou",
        "resp_email_id": "true",
    }

    r = requests.post(url, data=params)
    if r.status_code == 200 and json.loads(r.content)["message"] == "success":
        return True
    else:
        return False


def verify_email(token, authcode):
    database = DataBase(host, user, pwd, base)
    database.set_table(table)
    record = database.query_by_token(token, authcode)
    created_time = record[6]
    d = (datetime.datetime.now() - created_time).total_seconds()
    if d > one_day_in_second:
        database.close()
        return False
    else:
        database.update(token, authcode)
        database.close()
        return True



if __name__ == '__main__':
    send_email('test','guoletao@126.com')
