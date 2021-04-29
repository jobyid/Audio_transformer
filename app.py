from flask import Flask, request, render_template
from scripts import openapi as op
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("home.html", answers="")

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
