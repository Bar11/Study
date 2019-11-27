import config
from flask import session,redirect,url_for
from apps.admin.models import UserInfo



def login_required(func):
    def inner():
        if config.ADMIN_USER_ID in session:
            return func()
        else:
            return redirect(url_for('apps.admin.login'))
    return inner()