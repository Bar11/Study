#encoding=utf-8

import config
from flask import Blueprint,render_template,request, redirect,url_for,session,make_response
from .forms import LoginForm
from .models import UserInfo
from utils.captcha import create_validate_code
from io import BytesIO
from datetime import timedelta
from flask import g
from utils.others import login_required


bp=Blueprint('admin',__name__,url_prefix='/admin')

@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/login',methods=['GET','POST'])
def login():
    context = {}
    errorInfo = None
    form=LoginForm(request.form)
    context['form'] = form
    if request.method == "GET":
        context['form']=form
        return render_template('login.html', context=context)
    else:

        if form.validate():
            username = form.username.data
            pwd = form.password.data
            keep_alive = request.form.get('keep_alive')
            user = UserInfo.query.filter_by(username=username).first()
            captcha = request.form.get('captcha')
            if session.get('image_code').lower() != captcha.lower():
                context['error'] = '验证码输入有误！请刷新后重试！'
                return render_template('login.html', context=context)
            if user:
                if user.username == username and user.check_password(pwd):
                    session[config.ADMIN_USER_ID] = user.uid
                    # 是否保持登录状态
                    if keep_alive:
                        session.permanent = True
                        bp.permanent_session_lifetime = timedelta(days=7)
                    return redirect(url_for('admin.index'))
                else:
                    context['error'] = '账号或者密码错误！'

                    return render_template('admin/login.html', context=context)
            else:
                context['error'] = '账号不存在！'
                return render_template('admin/login.html', context=context)


        else:
            context['error'] = form.errors
            return render_template('admin/login.html', context=context)

@bp.route('/code/')
def get_code():
    code_img,strs = create_validate_code()
    buf = BytesIO()
    code_img.save(buf, 'JPEG',quality=70)
    buf_str = buf.getvalue()
    resp = make_response(buf_str)
    resp.headers['Content-Type'] = 'image/jpeg'
    session['image_code'] = strs
    return resp

@bp.route('/logout')
def logout():
    del session['uid']
    return redirect(url_for('admin.login'))

@bp.route('/profile/')
def profile():
    user=UserInfo.query.filter_by(uid=session.get(config.ADMIN_USER_ID)).first()
    return render_template('admin/profile.html',user=user)