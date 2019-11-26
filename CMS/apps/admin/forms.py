#encoding=utf-8

from wtforms import Form
from wtforms import StringField, BooleanField
from wtforms.validators import InputRequired,Length,Email

class LoginForm(Form):
    username=StringField(label='用户名', validators=[InputRequired('用户名不能为空！'), Length(4,20,'用户名长度为4~20')])
    password = StringField(label='密码', validators=[InputRequired('密码不能为空！'), Length(6,12, '密码长度为6~12') ])
