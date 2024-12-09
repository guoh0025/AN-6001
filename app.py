from flask import Flask
from flask import render_template,request
import textblob
import os

#api = os.getenv("maskersuiter")

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/main",methods=["GET","POST"])
def main():
    name = request.form.get("q")
    return(render_template("main.html"))

@app.route("/GenAI",methods=["GET","POST"])
def GenAI():
    return(render_template("GenAI.html"))

@app.route("/SA",methods=["GET","POST"])
def SA():
    return(render_template("SA.html"))

@app.route("/SA_result",methods=["GET","POST"])
def SA_result():
    q = request.form.get("q")
    score = textblob.TextBlob(q).sentiment
    return(render_template("SA_result.html", score = score))

if __name__ == "__main__":
    app.run()