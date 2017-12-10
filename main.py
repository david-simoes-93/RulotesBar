# -*- coding: utf-8 -*-

from flask import Flask, jsonify, render_template, request, redirect, url_for
import smtplib

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

	message = "CC: "+request.form["name"]+" <"+request.form["email"]+">\nTo: RulotesBar <"+destination+\
	    ">\nSubject: "+request.form["subject"]+"\n"+request.form["message"]
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

	message = "CC: "+request.form["name"]+" <"+request.form["email"]+">\nTo: RulotesBar <"+destination+\
	    ">\nSubject: "+request.form["subject"]+"\n"+request.form["message"]
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

