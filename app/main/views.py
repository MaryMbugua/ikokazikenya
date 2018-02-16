from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from .. import db,photos
from ..models import Employee,Employer,Jobad
from flask_login import login_required,login_user,logout_user,current_user
from .forms import JobadForm,EditprofileForm




#Views
@main.route('/')
def index():
    '''
    view  root page function that returns 
    the index page and its data
    '''
    title = 'Iko Kazi Kenya'
    allposts = Jobad.query.all()
    return render_template('index.html',title = title,allposts=allposts)
@main.route('/employeedashboard/<employee>')
# @login_required
def employee(employee):
    employee = Employee.query.filter_by(username = employee).first()

    if employee is None:
        abort(404)
    title = 'Employee Dashboard'
    return render_template('employeedashboard.html',title = title,employee = employee)
@main.route('/employeedashboard/<int:id>/postad',methods = ['GET','POST'])
def post_ad(id):
    employee = Employee.query.filter_by(id=id).one()
    form = JobadForm()
    if form.validate_on_submit():
        post = Jobad(adtitle = form.adtitle.data,dateposted = form.dateposted.data,adcontent = form.adcontent.data,category = form.category.data,username = form.username.data,employee_id = id)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('main.index'))

    return render_template('postad.html',postad_form=form)
@main.route('/employeedashboard/<employee>/editprofile',methods = ['GET','POST'])
def edit_profile(employee):
    employee = Employee.query.filter_by(username = employee).first()
    form = EditprofileForm()
    if form.validate_on_submit():
        employee.skill = form.skill.data
        # employee = Employee(skill = form.skill.data,experience = form.experience.data,contact = form.contact.data,category = form.category.data,age = form.age.data,gender = form.gender.data,status = form.status.data,location = form.location.data)
        db.session.add(employee)
        db.session.commit()
        return redirect(url_for('main.index'))

    return render_template('editprofile.html',edit_form=form)
