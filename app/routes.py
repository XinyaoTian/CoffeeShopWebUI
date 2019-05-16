from app import app
from flask import render_template, request
from config import Config
from func_pack import get_api_info
import requests


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET'])
def login_view():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login_validation():
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
        return render_template('index.html')
    else:
        return render_template('login.html')

