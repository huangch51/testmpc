from random import Random # 用于生成随机码 
from django.core.mail import send_mail # 发送邮件模块
from ..models import EmailVerifyRecord # 邮箱验证model
from django.conf import settings  # setting.py添加的的配置信息

# 生成随机字符串
def random_str(randomlength=6):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0, length)]
    return str


def send_register_email(email, send_type="register"):
    email_record = EmailVerifyRecord()
    # 将给用户发的信息保存在数据库中
    code = random_str(6)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()
    # 初始化为空
    email_title = ""
    email_body = ""
    # 如果为注册类型
    if send_type == "register":
        email_title = "注册激活链接"
        email_body = "请点击下面的链接激活你的账号:http://127.0.0.1:8000/registerv2/active/{0}".format(code)
        # 发送邮件
        send_status = send_mail(email_title, email_body, settings.EMAIL_FROM, [email])
        if send_status:
            pass