#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Leslee
# @Email    : leelovesc@gmail.com
# @Time    : 2019.11.21 17:48

from flask import Flask,url_for
import requests
from requests import request
app = Flask(__name__)

@app.route('/')
def index():
    pass

@app.route('/login')
def login():
    pass

@app.route('/user/<username>')
def profile(username):
    pass

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login',next='/'))
    print(url_for('profile',username="lee"))

# @app.route('/login',methods=['GET','POST'])
# def login1():
#     if request.method == 'POST':
#         do_the_login()
#     else:
#         show_the_login()







