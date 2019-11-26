# encoding=utf-8
import  os,sys
os.sys.path.append('/Users/zxg/Desktop/py3-Flask-venv/lib/python3.7/site-packages/')
os.sys.path.append('/Users/zxg/Desktop/inDevelopment/Study/CMS/')

from flask_migrate import Migrate,MigrateCommand
from flask_script import  Manager
from app import create_app
from app import db
from apps.admin import models as admin_models



app=create_app()
manager=Manager(app)
Migrate(app,db)
manager.add_command('db',MigrateCommand)
@manager.option('-u', '--username', dest='username')
@manager.option('-p', '--password', dest='password')
@manager.option('-e', '--email', dest='email')
def create_user(username,password,email):
    user=admin_models.UserInfo(username=username,password=password,email=email)
    db.session.add(user)
    db.session.commit()
    print("用户添加成功！")

'''
python manager.py db init
python manager.py db migrate
python manager.py db upgrade
python manager.py create_user -u admin -p 123456 -e 472888778@qq.com
'''
if __name__=='__main__':
    manager.run()