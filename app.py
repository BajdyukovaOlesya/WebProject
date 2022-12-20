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
	return render_template('base.html',book=u[0])

@app.route('/Метрвые души')
def inf1():
	b =  db.Table("Books",db.metadata,autoload=True,autoload_with=db.engine)
	u=db.session.query(b).all()
	return render_template('base.html',book=u[1])

@app.route('/Портрет Дроиана Грея')
def inf2():
	b =  db.Table("Books",db.metadata,autoload=True,autoload_with=db.engine)
	u=db.session.query(b).all()
	return render_template('base.html',book=u[2])

@app.route('/Отцы и дети')
def inf3():
	b =  db.Table("Books",db.metadata,autoload=True,autoload_with=db.engine)
	u=db.session.query(b).all()
	return render_template('base.html',book=u[3])


@app.route('/Убийство в Восточном экспрессе')
def inf4():
	b =  db.Table("Books",db.metadata,autoload=True,autoload_with=db.engine)
	u=db.session.query(b).all()
	return render_template('base.html',book=u[4])

@app.route('/Шерлок Холмс')
def inf5():
	b =  db.Table("Books",db.metadata,autoload=True,autoload_with=db.engine)
	u=db.session.query(b).all()
	return render_template('base.html',book=u[5])


@app.route('/Золотой Жук')
def inf6():
	b =  db.Table("Books",db.metadata,autoload=True,autoload_with=db.engine)
	u=db.session.query(b).all()
	return render_template('base.html',book=u[6])

@app.route('/Солярис')
def inf7():
	b =  db.Table("Books",db.metadata,autoload=True,autoload_with=db.engine)
	u=db.session.query(b).all()
	return render_template('base.html',book=u[7])

@app.route('/451 шрадус по Фаренгейту')
def inf8():
	b =  db.Table("Books",db.metadata,autoload=True,autoload_with=db.engine)
	u=db.session.query(b).all()
	return render_template('base.html',book=u[8])

@app.route('/Ковен озера Шамплейн')
def inf9():
	b =  db.Table("Books",db.metadata,autoload=True,autoload_with=db.engine)
	u=db.session.query(b).all()
	return render_template('base.html',book=u[9])

@app.route('/Алиса в стране чудес')
def inf10():
	b =  db.Table("Books",db.metadata,autoload=True,autoload_with=db.engine)
	u=db.session.query(b).all()
	return render_template('base.html',book=u[10])

@app.route('/Дракула')
def inf11():
	b =  db.Table("Books",db.metadata,autoload=True,autoload_with=db.engine)
	u=db.session.query(b).all()
	return render_template('base.html',book=u[11])

@app.route('/Сумерки')
def inf12():
	b =  db.Table("Books",db.metadata,autoload=True,autoload_with=db.engine)
	u=db.session.query(b).all()
	return render_template('base.html',book=u[12])

@app.route('/После')
def inf13():
	b =  db.Table("Books",db.metadata,autoload=True,autoload_with=db.engine)
	u=db.session.query(b).all()
	return render_template('base.html',book=u[13])

@app.route('/Save me')
def inf14():
	b =  db.Table("Books",db.metadata,autoload=True,autoload_with=db.engine)
	u=db.session.query(b).all()
	return render_template('base.html',book=u[14])

@app.route('/ Жизнь Пи')
def inf15():
	b =  db.Table("Books",db.metadata,autoload=True,autoload_with=db.engine)
	u=db.session.query(b).all()
	return render_template('base.html',book=u[15])


@app.route('/Таинственный остров')
def inf16():
	b =  db.Table("Books",db.metadata,autoload=True,autoload_with=db.engine)
	u=db.session.query(b).all()
	return render_template('base.html',book=u[16])



@app.route('/Часодеи ')
def inf17():
	b =  db.Table("Books",db.metadata,autoload=True,autoload_with=db.engine)
	u=db.session.query(b).all()
	return render_template('base.html',book=u[17])


@app.route('/classic')
def infС():
	b =  db.Table("Books",db.metadata,autoload=True,autoload_with=db.engine)
	u=db.session.query(b).all()
	return render_template('base2.html',book1=u[1],book2=u[2],book3=u[3],x1='Классика')


@app.route('/detective')
def infD():
	b =  db.Table("Books",db.metadata,autoload=True,autoload_with=db.engine)
	u=db.session.query(b).all()
	return render_template('base2.html',book1=u[4],book2=u[5],book3=u[6],x1='Детектив')

@app.route('/fantastic')
def infFan():
	b =  db.Table("Books",db.metadata,autoload=True,autoload_with=db.engine)
	u=db.session.query(b).all()
	return render_template('base2.html',book1=u[0],book2=u[7],book3=u[8],x1='Фантастика')

@app.route('/fentezi')
def infFen():
	b =  db.Table("Books",db.metadata,autoload=True,autoload_with=db.engine)
	u=db.session.query(b).all()
	return render_template('base2.html',book1=u[9],book2=u[10],book3=u[11],x1='Фэнтези')

@app.route('/romantic')
def infRom():
	b =  db.Table("Books",db.metadata,autoload=True,autoload_with=db.engine)
	u=db.session.query(b).all()
	return render_template('base2.html',book1=u[12],book2=u[13],book3=u[14],x1='Романтика')

@app.route('/adventures')
def infAdv():
	b =  db.Table("Books",db.metadata,autoload=True,autoload_with=db.engine)
	u=db.session.query(b).all()
	return render_template('base2.html',book1=u[15],book2=u[16],book3=u[17],x1='Приключения')

if __name__=="__main__": app.run(debug=True)