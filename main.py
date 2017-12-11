# -*- coding: utf-8 -*-

from flask import Flask, jsonify, render_template, request, redirect, url_for
import smtplib
from email.mime.text import MIMEText
from email.header import Header

app = Flask(__name__)

@app.route('/email', methods=['POST'])
def send_email():
    # https://stackoverflow.com/questions/8329741/issue-with-smtplib-sending-mail-with-unicode-characters-in-python-3-1
	destination = 'gamecloner@gmail.com'
	#print("lol",request.form["email"],
	#request.form["name"],
	#request.form["message"],
	#request.form["subject"])

	sender = request.form["email"]
	receivers = [destination]

	message = "CC: "+Header(request.form["name"], "utf-8")+" <"+Header(request.form["email"], "utf-8")+\
		">\nTo: RulotesBar <"+destination+\
	    ">\nSubject: "+Header(request.form["subject"], "utf-8")+"\n"+\
	    MIMEText(request.form["message"], _charset="UTF-8")
	print(message)

	try:
	   smtpObj = smtplib.SMTP('localhost')
	   smtpObj.sendmail(sender, receivers, message)
	   print("Successfully sent email")
	   return render_template('email.html')
	except:
	   print("Error: unable to send email")

	return render_template('email_error.html')


@app.route('/email_en', methods=['POST'])
def send_email_en():
	destination = 'gamecloner@gmail.com'
	#print("lol",request.form["email"],
	#request.form["name"],
	#request.form["message"],
	#request.form["subject"])

	sender = request.form["email"]
	receivers = [destination]

	message = "CC: "+Header(request.form["name"], "utf-8")+" <"+Header(request.form["email"], "utf-8")+\
		">\nTo: RulotesBar <"+destination+\
	    ">\nSubject: "+Header(request.form["subject"], "utf-8")+"\n"+\
	    MIMEText(request.form["message"], _charset="UTF-8")
	print(message)

	try:
	   smtpObj = smtplib.SMTP('localhost')
	   smtpObj.sendmail(sender, receivers, message)
	   print("Successfully sent email")
	   return render_template('email_en.html')
	except:
	   print("Error: unable to send email")

	return render_template('email_error_en.html')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/en')
def index_en():
    return render_template('index_en.html')


if __name__ == "__main__":
    app.run(host='127.0.0.1',port=5000)

