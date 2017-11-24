# -*- coding: utf-8 -*-

from flask import Flask, jsonify, render_template, request, redirect, url_for
import smtplib

app = Flask(__name__)

@app.route('/email', methods=['POST'])
def send_email():
    destination = 'david.simoes@ua.pt'
    #print("lol",request.form["email"],
    #request.form["name"],
    #request.form["message"],
    #request.form["subject"])

    sender = request.form["email"]
    receivers = [destination]

    message = "From: From "+request.form["name"]+" <"+request.form["email"]+">\nTo: To RulotesBar <"+destination+\
        ">\nSubject: SMTP e-mail test\nThis is a test e-mail message."
    print(message)

    try:
       smtpObj = smtplib.SMTP('localhost')
       smtpObj.sendmail(sender, receivers, message)
       print("Successfully sent email")
       return render_template('email.html')
    except smtplib.SMTPException:
       print("Error: unable to send email")

    return render_template('email_error.html')


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)

