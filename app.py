from flask import Flask,request,url_for,render_template,redirect,jsonify
from datetime import datetime
# from flask_sqlalchemy import SQLALchemy

app = Flask(__name__)

JOBS = [
   {
   'id' : 1,
   'title' : 'data analyst',
   'location':'banglore,india',
   'salory':'Rs. 11,00,000'
   },
   {
   'id' : 2,
   'title' : 'data scientist',
   'location':'remote',
    # 'salory':'usd 120,000'
   },
   {
   'id' : 3,
   'title' : 'data architecture',
   'location':'america,new york city',
   'salory':'usd 130,000'
   },
   {
   'id' : 1,
   'title' : 'frontend developer',
   'location':'banglore,india',
   'salory':'Rs. 15,00,000'
   }
]

@app.route('/')
def about():
    return render_template('index.html' ,jobs = JOBS , ab = 'CAREER' )

@app.route('/api/jobs')
def jobs():
   return jsonify(JOBS)

if __name__ == "__main__":
 app.run(host='0.0.0.0', port=81 , debug=True)
 