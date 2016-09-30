from flask import Flask, flash, render_template, request, session, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/test")
def test():
    return render_template('index.html')

@app.route("/test2")
def test2():
    return render_template('index2.html')

if __name__ == "__main__":
    app.run()
