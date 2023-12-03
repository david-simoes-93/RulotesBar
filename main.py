# -*- coding: utf-8 -*-

from flask import Flask, jsonify, render_template, request, redirect, url_for
import smtplib
from email.mime.text import MIMEText
from email.header import Header

app = Flask(__name__)

@app.route('/email', methods=['POST'])
def send_email():
	if request.form["captcha"].strip() != "7":
		return render_template('email_error.html')

	myemail = 'rulotesbar@gmail.com'
	client = request.form["email"]

	message2 = "To: "+Header(request.form["name"], "utf-8").encode()+" <"+request.form["email"]+\
	    ">\nSubject: "+Header(request.form["subject"], "utf-8").encode()+"\n"+MIMEText(
	    "Esta é uma mensagem automática.\n\n"+\
	    "Recebemos a sua mensagem e vamos contactá-lo o mais rápido possível.\n\n"+\
	    "Obrigado pela sua atenção,\nRulotesBar", _charset="UTF-8").as_string()

	message = "CC: "+Header(request.form["name"], "utf-8").encode()+" <"+request.form["email"]+\
		">\nTo: RulotesBar <"+myemail+\
	    ">\nSubject: "+Header(request.form["subject"], "utf-8").encode()+"\n"+\
	    MIMEText(request.form["message"], _charset="UTF-8").as_string()
	app.logger.info(message)

	try:
	   smtpObj = smtplib.SMTP('localhost')
	   smtpObj.sendmail("rulotesbar@gmail.com", myemail, message)
	   smtpObj.sendmail("rulotesbar@gmail.com", client, message2)
	   app.logger.warn("Successfully sent email from",client)
	   return render_template('email.html')
	except Exception as e:
	   app.logger.error("Error: unable to send email", e)

	return render_template('email_error.html')


@app.route('/email_en', methods=['POST'])
def send_email_en():
	if request.form["captcha"].strip() != "8":
		return render_template('email_error.html')

	myemail = 'rulotesbar@gmail.com'
	client = request.form["email"]

	message2 = "To: "+Header(request.form["name"], "utf-8").encode()+" <"+request.form["email"]+\
	    ">\nSubject: "+Header(request.form["subject"], "utf-8").encode()+"\nThis is an automated message.\n\n"+\
	    "We have received your e-mail and will contact you as soon as possible.\n\n"+\
	    "Thank you for your attention,\nRulotesBar"

	message = "CC: "+Header(request.form["name"], "utf-8").encode()+" <"+request.form["email"]+\
		">\nTo: RulotesBar <"+myemail+\
	    ">\nSubject: "+Header(request.form["subject"], "utf-8").encode()+"\n"+\
	    MIMEText(request.form["message"], _charset="UTF-8").as_string()
	app.logger.info(message)

	try:
	   smtpObj = smtplib.SMTP('localhost')
	   smtpObj.sendmail("rulotesbar@gmail.com", myemail, message)
	   smtpObj.sendmail("rulotesbar@gmail.com", client, message2)
	   app.logger.warn("Successfully sent email from",client)
	   return render_template('email_en.html')
	except Exception as e:
	   app.logger.error("Error: unable to send email", e)

	return render_template('email_error_en.html')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/en')
def index_en():
    return render_template('index_en.html')


if __name__ == "__main__":
    app.run(host='127.0.0.1',port=5000)

