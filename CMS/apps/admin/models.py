# encoding=UTF-8
from exts import db
from random import Random
from werkzeug.security import generate_password_hash,check_password_hash

class UserInfo(db.Model):
    __tablename__ = 'userinfo'
    uid =db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(50), nullable=False,unique=True)
    _password = db.Column(db.String(100),nullable=False)
    salt = db.Column(db.String(5),nullable=False)

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.salt = self.get_salt()
        self.email=email
        self.set_password(self.get_password)

    # 随机生成盐值
    def get_salt(self, length=5):
        salt = ''
        chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
        len_chars = len(chars) - 1
        random = Random()
        for i in range(0,length):
            # 每次从chars中随机取一位
            salt += chars[random.randint(0, len_chars)]
        return salt

    # 返回原密码加盐值一次加密后的值
    @property
    def get_password(self):
        print("getpassword", self.password, self.salt)
        return self.password+self.salt

    # 进行二次加密
    def set_password(self, raw_password):
        self._password = generate_password_hash(raw_password)
        # print(self._password,'************')

    def check_password(self,raw_password):
        result = check_password_hash(self._password, raw_password+self.salt)
        return result


if __name__ == '__main__':
    a = UserInfo()
    b = a.get_salt(5)
    print(b)