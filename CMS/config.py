# encoding=utf-8

# DIALECT = 'MySQL'
# DRIVER = 'MySQLdb'

USERNAME = 'root'
PASSWORD = '123'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE='flasktest'
DB_URI="mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8".format(USERNAME,PASSWORD,HOST,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI=DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS=False # 关闭动态跟踪
# 查询会显示原始SQL语句
SQLALCHEMY_ECHO=True