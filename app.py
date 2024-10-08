from flask import Flask, render_template, request, redirect, url_for, flash
import os


# initialize flask application
app = Flask(__name__)
server = app


# home screen route
@app.route("/")
def run_website():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
