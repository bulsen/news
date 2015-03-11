# -*- coding:utf-8 -*-
import sys, time, os,db
reload(sys)
sys.setdefaultencoding("utf-8")

from flask import Flask, render_template,send_from_directory

app = Flask(__name__)

@app.route("/")
def main():
	data = db.querries()
	return render_template("entries.html",data = data)

if __name__ == '__main__':
	app.run()

