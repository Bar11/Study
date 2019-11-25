# encoding=UTF-8
from exts import db


class UserInfo(db.Model):
    __tablename__ = 'jq_userinfo'
    uid =db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(50), nullable=False,unique=True)