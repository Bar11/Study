# encoding=UTF-8
from .exts import db
from datetime import datetime

class UserInfo(db.Model):
    __tablename__ = 'jq_userinfo'
    uid =db.Column(db.Integer, primary_key=True, autoincrement=True)
    username 