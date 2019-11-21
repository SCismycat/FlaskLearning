#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/21 23:52
# @Author  : Leslee

import sqlite3
from flask import Flask,request,session,g,redirect,url_for,\
    abort,render_template,flash
from contextlib import closing


DATABASE = "/tmp/flasky.db"
DDEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
# 检查给定的对象(如果对象是str就直接导入)，不推荐
# app.config.from_object(__name__)
# 导入配置文件的形式，推荐。
app.config.from_envvar('FLASKY_SETTINGS',silent=True)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql',mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g,'db',None)
    if db is not None:
        db.close()
# 显示条目，从sql中查询出数据，传输到模板中显示
@app.route('/')
def show_entires():
    cur = g.db.execute('select title text from entries order by id desc')
    entries = [dict(title=row[0],text=row[1]) for row in cur.fetchall()]
    return render_template('show_entries.html',entries=entries)

# 新增一个新条目,然后重定向到显示页面上。
app.route('/add',methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('insert into entries (title,text) values (?,?)',
                 [request.form['title'],request.form['text']])
    g.db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entires'))

# 登录和销毁
@app.route('/login',methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in']= True
            flash('You were logged in')
            return redirect(url_for('show_entires'))
    return render_template('login.html',error=error)
# 登出
@app.route('/logout')
def logout():
    session.pop('logged_in',None)
    flash('You were logged out')
    return redirect(url_for('show_entires'))
















if __name__ == '__main__':
    app.run()















