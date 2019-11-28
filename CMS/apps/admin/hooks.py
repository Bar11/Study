#encoding = utf-8
from flask import g, session
import config
from .views import bp
from .models import UserInfo

@bp.before_request
def before_request_save_userinfo():
    if config.ADMIN_USER_ID in session:
        user_id = session.get(config.ADMIN_USER_ID)
        user = UserInfo.query.get(user_id)
        if user:
            g.admin_user=user