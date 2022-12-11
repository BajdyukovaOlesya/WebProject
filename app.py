from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:Minerva17@localhost/Library"
db = SQLAlchemy(app)


with app.app_context(): book =  db.Table("Books",db.metadata,autoload=True,autoload_with=db.engine)


with app.app_context():u=db.session.query(book).all()
print(u[0].Номер)

@app.route('/')
@app.route('/index')
def index():
	return render_template("index.html")


if __name__=="__main__": app.run(debug=True)