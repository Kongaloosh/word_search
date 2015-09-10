#!/usr/bin/python
# coding: utf-8
import sqlite3
import os
from flask import Flask, request, session, g, redirect, url_for, \
    render_template, flash, Response, send_file
from domain_getter import domainify

app = Flask(__name__)
app.config.from_object(__name__)
app.config['STATIC_FOLDER'] = os.getcwd()
cfg = None

@app.route('/')
def name_me():
    domain = domainify()
    return render_template('name_me.html', domain=domain)


if __name__ == "__main__":
    app.run(debug=True)
