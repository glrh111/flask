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

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config['SECRET_KEY'] = 'hah ni ma qu'

     
# 定义一个公共的根目录


@app.route('/')
def index():
#    user_agent = request.headers.get('User-Agent')
    return render_template('index.html', current_time=datetime.utcnow())


# 定义私人空间

@app.route('/usr/<name>')
def usr(name):
    return render_template('usr.html', name=name)

@app.route('/usr/nb')
def nb():
	return redirect('http://localhost:5000/usr/wl')   

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
