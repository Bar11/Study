#encoding=utf-8
from wtforms import Form
from wtforms import StringField,BooleanField
from wtforms.validators import InputRequired,Length

class LoginForm(Form):
    username= StringField(
        label='账号', validators=[InputRequired('账号不能为空！'), Length(4,15,'长度在6~15')]
    )
    password = StringField(
        label='密码', validators=[InputRequired('密码不能为空！'), Length(4,12,'长度在4~12')]

    )
