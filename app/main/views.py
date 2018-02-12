from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from .. import db,photos
from ..models import Employee,Employer
from flask_login import login_required





#Views
@main.route('/')
def index():
    '''
    view  root page function that returns 
    the index page and its data
    '''

    title = 'blog!'
     

    
    return render_template('index.html',title = title)
@main.route('/employeedashboard/<uname>')
# @login_required
def employee(uname):
    employee = Employee.query.filter_by(username = uname).first()

    if employee is None:
        abort(404)
    title = 'Employee Dashboard'

    return render_template('employeedashboard.html',title = title,employee = employee)


