#encoding=utf-8

from flask import Blueprint,render_template,request,Response,session,redirect,url_for,make_response
from .models import UserInfo
from .forms import LoginForm
from io import BytesIO
from utils.captcha import create_validate_code
bp=Blueprint('admin',__name__, url_prefix='/admin')

@bp.route('/index')
def index():
    return render_template('index.html')



@bp.route('/login/', methods=['GET', 'POST'])
def login():
    error = None
    form = LoginForm(request.form)
    if request.method == 'GET':
        return render_template('login.html',form=form)
    else:
        captcha=request.form.get('captcha')
        if session.get('captcha_image').lower()!= captcha.lower():
            return render_template('login.html', message='验证码错误！')
        # 表单验证
        if form.validate():
            uname = form.username.data
            pwd = form.password.data
            user = UserInfo.query.filter_by(username=uname).first()
            if user:
                if user.username==uname and user.check_password(pwd):
                    session['user_id']=user.uid
                    return redirect(url_for('admin.index'))
                else:
                    error = '用户名或密码错误！'
                    return render_template('login.html', message=error)
            else:
                error='用户名不存在！'
                return render_template('login.html', message=error)
        else:
            # 返回表单验证的错误信息form.errors
            return render_template('login.html', form=form)


@bp.route('/code')
def get_code():
    code_img, strs = create_validate_code()
    buf = BytesIO()
    code_img.save(buf, 'JPEG', quality=70)
    buf_str = buf.getvalue()
    resp = make_response(buf_str)
    resp.headers['Content-Type'] = 'image/jpeg'
    session['captcha_image'] = strs
    return resp