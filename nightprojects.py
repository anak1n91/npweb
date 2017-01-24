#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template
import sqlite3 as lite
from datetime import datetime


app = Flask(__name__)

def fix_funky_timestamp(timestamp):
    return datetime.fromtimestamp(timestamp/1000).strftime('%Y/%m/%d')

def url_from_ts_title(timestamp, title):
    return "http://blog.nightprojects.org/{0}/{1}".format(fix_funky_timestamp(timestamp), title)

@app.route('/aboutsite')
def about_site():
    return render_template('aboutsite.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/chat')
def chat():
    return render_template('chat.html')


@app.route('/webdesign')
def webdesign():
    return render_template('webdesign.html')


@app.route('/example/<design>')
def design(design):
    return render_template('%s.html' % design)

@app.route('/help')
def help():
    return render_template('help.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/')
def home():
    con = lite.connect('ghost.db')
    cur = con.cursor()
    row = cur.execute("SELECT * FROM posts order by id desc").fetchone()
    post = {
        "url": url_from_ts_title(row[-2], row[3]),
        "title": row[2]
    }
    return render_template('home.html', post=post)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8082, debug=False)

