#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Leslee
# @Email    : leelovesc@gmail.com
# @Time    : 2019.11.21 17:25

from flask import Flask

app = Flask(__name__)

# 路由
@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello_flask():
    return 'Hello,Flask!'

# 变量规则
@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id

# 唯一URL和重定向。
@app.route('/project/')
def projects():
    return 'The project page'
# 访问一个没有斜杠的url的时候，flask会自动重定向，在尾部加上一个斜杠
@app.route('/about')
def about():
    return 'The about page'
# 如果在about后面加上斜杠，会有一个404错误。






if __name__ == '__main__':
    # app.run()
    # # 开启公开ip监听
    # app.run(host='0.0.0.0')
    # 开启debug模式
    app.run(debug=True)