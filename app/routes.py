from app import app
from flask import render_template, request, redirect, url_for
from config import Config
from func_pack import get_api_info
from flask_login import current_user, login_user, login_required
from app.models import User
import requests


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET'])
def login_view():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    return render_template('login.html')


@app.route('/price', methods=['GET'])
@login_required
def price_view():
    return render_template('price.html')


@app.route('/login', methods=['POST'])
def login_validation():
    # check whether user has already login
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    # get POST infos
    data_received = request.values.to_dict()

    # assemble url
    api_format = '/users/validation/'
    validation_url = 'http://' + Config.DB_SOURCE_IP + ':' + Config.DB_SOURCE_PORT + api_format

    # POST to DB source API
    result = requests.post(validation_url, data=data_received)

    # get validation infos from api
    validation_result = get_api_info(result)[0]
    # print(validation_result)
    # print(type(validation_result))
    # print(validation_result['validation'])
    # print(type(validation_result['validation']))

    # verify
    if validation_result['validation'] == 'True':
        verified_user = User(validation_result['uid'])
        login_user(verified_user)
        return redirect(url_for('index'))
    else:
        return render_template('login.html')

