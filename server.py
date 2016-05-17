#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
belong to

                                                                                                    
                        888888                        88888                   88              88    
                       8888888                        88888                8888             8888    
                          888                           888             8888888          8888888    
                           88                           888             8888888          888888     
        88888 8888        888          88888  888       888 888             888             888     
      888888888888        888          88888888888      888888888           88              888     
     8888  88888          888            888888888     88888 8888          888              888     
     888    8888          88             8888          888    888          888              88      
    888      88           88             88            888    888          888             888      
    88      888          888            888            88     88           88              888      
    888     888          888            888           888    888          888              888      
    888    8888          888            888           888    888          888              88       
    8888888888       88888888888     8888888888      88888  88888      888888888       8888888888   
     888888888       88888888888     8888888888     88888888888888    8888888888       8888888888   
           888                                                                                      
           888                                                                                      
     88888888                                                                                       
     8888888  

https://github.com/glrh111/

'''  

from flask import *
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from datetime import datetime
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask.ext.sqlalchemy import SQLAlchemy

class NameForm(Form):
	name = StringField("What's your name?", validators=[Required()])
	submit = SubmitField('Submit')

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config['SECRET_KEY'] = 'hah ni ma qu'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://glrh11:qwe123@localhost/glrh11'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)

class Role(db.Model):
	__tablename__ = 'roles'
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(64), unique = True)

	def __repr__(self):
		return '<Role %r>' % self.name

class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(64), unique = True, index = True)

	def __repr__(self):
		return '<User %r>' % self.username


     
# 定义一个公共的根目录


@app.route('/')
def index():
    return render_template('index.html', current_time=datetime.utcnow())


# 定义私人空间

@app.route('/usr', methods=['GET', 'POST'])
def usr():
	form = NameForm()
	if form.validate_on_submit():
		old_name = session.get('name')
		if (old_name != None) and (old_name != form.name.data):
			flash('name has changed')
		session['name'] = form.name.data
		return redirect(url_for('usr'))
	return render_template('usr.html', form = form, name = session.get('name'))

@app.route('/usr/nb')
def nb():
	return redirect('http://localhost:5000/usr')   

# exception
@app.errorhandler(400)
def page_not_found(e):
	return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'), 500		 

# enterence

if __name__ == '__main__':
    app.run(debug=True)
