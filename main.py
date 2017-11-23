# -*- coding: utf-8 -*-

from flask import Flask, jsonify, render_template, request, redirect, url_for
import smtplib

app = Flask(__name__)

@app.route('/email', methods=['POST'])
def send_email():
    print("lol",request.form["email"],
    request.form["name"],
    request.form["message"],
    request.form["subject"])



    sender = request.form["email"]
    receivers = ['david.simoes@ua.pt']

    message = """From: From "+request.form["name"]+" <"+request.form["email"]+">
    To: To RulotesBar <david.simoes@ua.pt>
    Subject: SMTP e-mail test

    This is a test e-mail message.
    """

    try:
       smtpObj = smtplib.SMTP(localhost)
       smtpObj.sendmail(sender, receivers, message)
       print("Successfully sent email")
    except smtplib.SMTPException:
       print("Error: unable to send email")

    return redirect(url_for('index')+"#contact")

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)

