from flask import Flask, request, render_template, redirect
from scripts import openapi as op
from scripts import eaxmples as ex
import requests
from scripts import bank_data as bd
import os
import json
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

app = Flask(__name__)
@app.route('/prompt')
def hello_world():
    return render_template("home.html", answers="")

@app.route("/")
def classify():
    return render_template("classify.html", answers="")

@app.route('/ask_classify', methods=["POST", "GET"])
def ask_classify():
    if request.method == "GET":
        return "Wrong place mate"
    else:
        answer = ""
        r = request.form.to_dict()
        question = r['qtn']
        classes = ex.bank_classes

        d, response = op.classfiy(question, classes)
        print(d['label'])
        print(response)
        answer = d['label'] #d['choices'][0]['text']
        return render_template("classify.html", answers="../static/catVamt.png")


@app.route("/get_transactions", methods=["POST", "GET"])
def get_transactions():
    at = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjE0NTk4OUIwNTdDOUMzMzg0MDc4MDBBOEJBNkNCOUZFQjMzRTk1MTBSUzI1NiIsInR5cCI6ImF0K2p3dCIsIng1dCI6IkZGbUpzRmZKd3poQWVBQ291bXk1X3JNLWxSQSJ9.eyJuYmYiOjE2MTk3OTIwMzIsImV4cCI6MTYxOTc5NTYzMiwiaXNzIjoiaHR0cHM6Ly9hdXRoLnRydWVsYXllci1zYW5kYm94LmNvbSIsImF1ZCI6ImRhdGFfYXBpIiwiY2xpZW50X2lkIjoic2FuZGJveC1wdXRvdXQ3Ym9va2xpc3Q2YWZsYW1lLTc1NDdmYiIsInN1YiI6Ik5yZXUzeGcra0ZtOHZod2VsSWI2SGNmLzIyejh0d254azl1VWdyWFV0S0E9IiwiYXV0aF90aW1lIjoxNjE5NzcwMjE2LCJpZHAiOiJsb2NhbCIsImp0aSI6IkE0RjRCMkUwRUFDNzFCNEQ1NjRBRkEwREI0Q0YxMzhFIiwic2lkIjoiYXV0aC1YZjl5ZGI3LVhUUmJST0RJMmk0bExjX3NhU3hvVXlCT3AybW9qdWtOaXFjIiwiaWF0IjoxNjE5NzcwMjE3LCJjb25uZWN0b3JfaWQiOiJtb2NrIiwiY3JlZGVudGlhbHNfa2V5IjoiMTk2YzM0NDUwNjM4YTg2NjVjMDk3MjFhM2FkY2U5NjJmOTEwZGQ0OGI0NGU0YzQ3Mzg2ZTcyZDJhODIxOWFmMiIsInByaXZhY3lfcG9saWN5IjoiRmViMjAxOSIsImNvbnNlbnRfaWQiOiI3MmYzZGMyMi1jODI3LTRhOTctODA0OC0zZWUyYjE3MDEyNWYiLCJzY29wZSI6WyJpbmZvIiwiYWNjb3VudHMiLCJiYWxhbmNlIiwiY2FyZHMiLCJ0cmFuc2FjdGlvbnMiLCJkaXJlY3RfZGViaXRzIiwic3RhbmRpbmdfb3JkZXJzIiwib2ZmbGluZV9hY2Nlc3MiXSwiYW1yIjpbInB3ZCJdfQ.0iiFEGmotv6MiXkEnEAenfGRzMiIuTqmnmqVDM3zF49oONmK8hcQgG_x-_7Orjcg_jrYBIS2s4hzMi-QMb1T2wQ_lwV22e48i4XmyZNC3L9RILP3TLTDpWHa2KUyj_TAEbAOucjnXc0JwwLAmSxv5nzAkOSxzrzybOb4CvrQF_yDtTx1WJX3D1dSU4k7bQOD70QEBg98VoAxpNmjy8FlbYc6w3YgGCh4T51UKuYeRMVjDDsmbCpBghEoFkzdqpV58NjhV942Nu8RTXTUROuu6LTK6oR_6_fiBtFNBVcoVYFqwO3KYkGexfGSRgy02-W8xs36DjtmfNzOI2CREe732w"
    headers = {'at':at,"acid":"56c7b029e0f8ec5a2334fb0ffc2fface"}
    #r = requests.post("http://localhost:3000/get_account_transactions", headers=headers)
    #print(type(r.json()))
    #dfh = bd.import_bank_transactions(r.json())
    return render_template("classify.html", answers="../static/catVamt.png")


@app.route('/ask', methods=["POST", "GET"])
def ask():
    if request.method == "GET":
        return "Wrong place mate"
    else:
        answer = ""
        r = request.form.to_dict()
        question = r['qtn']
        words = r['words']
        print(words)
        d, response = op.query_open_ai(question, int(words))
        answer = d['choices'][0]['text']
        return render_template("home.html", answers=answer)

if __name__ == '__main__':
    app.run()

# run with
# FLASK_ENV=development FLASK_APP=app.py  flask run
# change port with: FLASK_RUN_PORT=3000
