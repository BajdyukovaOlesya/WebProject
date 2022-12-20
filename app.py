from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
import jinja2 



app = Flask(__name__, template_folder="templates")


app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:Minerva17@localhost/Library"
db = SQLAlchemy(app)


@app.route('/')
@app.route('/index')
def index():
	return render_template("index.html")


@app.route('/1984')
def inf():
	b =  db.Table("Books",db.metadata,autoload=True,autoload_with=db.engine)
	u=db.session.query(b).all()
	book=u[0]
	return render_template('base.html',book=book)



if __name__=="__main__": app.run(debug=True)