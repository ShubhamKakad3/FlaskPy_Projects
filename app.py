from flask import Flask,request,url_for,render_template,redirect
from datetime import datetime
# from flask_sqlalchemy import SQLALchemy

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello from Flask!'

@app.route('/about')
def about():
    return render_template('index.html')

if __name__ == "__main__":
 app.run(host='0.0.0.0', port=81 , debug=True)
 