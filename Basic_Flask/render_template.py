#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/21 23:21
# @Author  : Leslee

from flask import render_template
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html',name=name)

if __name__ == '__main__':
    app.run(debug=True)













