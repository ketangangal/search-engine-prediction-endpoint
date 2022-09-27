import os, sys
from flask import Flask,send_file, abort, render_template, request,url_for,flash,redirect


app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/image', methods=['GET', 'POST'])
def upload_file():
    print(request.files)
    print(request.method)
    
    return ""

if __name__=="__main__":
    app.run(debug=True)