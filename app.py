
"""VOC News App"""
from flask import Flask, render_template, redirect, url_for, flash, request
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required, Email
import os

app = Flask(__name__)

bootstrap = Bootstrap(app) #BootStrap Instance

port = int(os.getenv("PORT")) or 5020
SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'

app.config['SECRET_KEY'] = SECRET_KEY

class NameForm(Form):
	name = StringField('What is your name?', validators=[Required()])
	email = StringField('Enter your email address!', validators=[Required(),Email()])
	submit = SubmitField('Submit')

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/contactus', methods=['GET','POST'])
def contactus():
	form = NameForm()
	if form.validate_on_submit():
		flash('Registration successful!')
		return redirect(request.args.get('next') or url_for('contactus'))
	return render_template('contactus.html', form=form)
    
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html',e=e), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)