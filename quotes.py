from flask import Flask ,render_template,request,redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql+psycopg2://postgres:155517@localhost/quotes'
app.config['SQLALCHEMY_DATABASE_URI'] =' postgres://gvjpjsipepgxng:d276d8393131ef2530a125a3432870bc4f53aadc53b3f9e3b15c8d358511c9fb@ec2-54-146-73-98.compute-1.amazonaws.com:5432/dc46rqujiidul5'
app.config['SQLALCHMEY_TRACK_MODIFICATIONS']= False

db = SQLAlchemy(app)

class Favquotes(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    author = db.Column(db.String(30))
    quote = db.Column(db.String(2000))


@app.route('/')
def index():
    result = Favquotes.query.all()
    return render_template('index.html',result=result)


@app.route('/quotes')
def quotes():
    return render_template('quotes.html')

@app.route('/process',methods =['POST'])
def process():
    author = request.form['author']
    quote = request.form['quote']
    quotedata =Favquotes(author=author,quote=quote)
    db.session.add(quotedata)
    db.session.commit()

    return redirect(url_for('index'))
