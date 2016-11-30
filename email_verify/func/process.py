# coding:utf-8
import requests, json, datetime
from account.models import Account


API_USER = 'shine_forever_test_zFZOBK' # input your apt_user
API_KEY = 'su9zZf98O0ooT5i8' # input your spi_key
url = "http://www.sendcloud.net/webapi/mail.send_template.json"
base_link = "http:127.0.0.1:8000/account/do_verificatin?"

one_day_in_second = 5184000

def send_email(name, email,token,authcode):
    print "send_email......."
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
    print r.content
    if r.status_code == 200 and json.loads(r.content)["message"] == "success":
        return True
    else:
        return False


def verify_email(token, authcode):
    print("verify_email..")
    try:
        account = Account.objects.get(token=token,authcode=authcode)
        account.verification_status = 1
        account.save()
        return True
    except:
        return False





