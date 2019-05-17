from flask import Flask
from flask_login import LoginManager
from config import Config

app = Flask(__name__)
# 这个 Config 如果不添加, 用户登录时 flask-login 会报 no secret key 的错误
app.config.from_object(Config)

login = LoginManager(app)
login.login_view = 'login'

from app import routes
