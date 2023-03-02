import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
app.run(host= '0.0.0.0')

openai.api_key = "" #这里填写 api_key

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        message = request.form["message"]
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": message}
            ]
        )
        return redirect(url_for("index", result=response['choices'][0]['message']['content']))

    result = request.args.get("result")
    return render_template("index.html", result=result)