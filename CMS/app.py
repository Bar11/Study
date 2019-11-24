from flask import Flask
from flask import Blueprint
from admin.views import bp as admin_app
from common.views import bp as common_app
from front.views import bp as front_app
from exts import db

def create_app():
    app=Flask(__name__)
    app = Flask(__name__)
    app.register_blueprint(admin_app)
    app.register_blueprint(common_app)
    app.register_blueprint(front_app)
    app.config.from_object('config')
    db.init_app(app)
    return app


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app=create_app()
    app.run()
