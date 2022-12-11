from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app=Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgresql:Minerva17@localhost/Library"
db = SQLAlchemy()
db.init_app(app)

class Book(db.Model):
	id=db.Column(db.Integer, primary_key=True)
	name=db.Column(db.String(10000))
	autor=db.Column(db.String(10000))
    count_str=db.Column(db.Integer)
    reit=db.Column(db.String(10000))
    descript=db.Column(db.String(10000))
    date=db.Column(db.Date)
    genre=db.Column(db.String(10000))
    topic=db.Column(db.String(10000))
    link=db.Column(db.String(10000))
    image=db.Column(db.String(10000))

    def __init__(self,name,autor,count_str,reit,descript,date,genre.topic.link.image):
    	self.autor=autor
    	self.name=name
    	self.count_str=count_str
    	self.reit=reit
    	self.descript=descript
    	self.date=date
    	self.genre=genre
    	self.topic=topic
    	self.link=link
    	self.image=image

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")




if __name__=="__main__": app.run()