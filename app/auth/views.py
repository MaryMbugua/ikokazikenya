from flask import render_template,redirect,url_for,flash
from . import auth
from ..models import Employee,Employer
from .forms import RegistrationemployeeForm,LoginemployeeForm,RegistrationemployerForm,LoginemployerForm
from .. import db
from flask_login import login_user,logout_user,login_required

@auth.route('/employeelogin',methods = ["GET","POST"])
def login():
    login_form = LoginemployeeForm()
    if login_form.validate_on_submit():
        user = Employee.query.filter_by(email=login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(url_for('main.employee',uname=current_employee.username))
        flash('Invalid username or Password')

    title = "Employee Login"
    return render_template('auth/employee_login.html',login_form=login_form,title=title)


@auth.route('/employeeregister',methods = ["GET","POST"])
def register():
    form = RegistrationemployeeForm()
    if form.validate_on_submit():
        user = Employee(email = form.email.data,username = form.username.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
        title = "New Employee Account"
    return render_template('auth/employee_register.html',registration_form = form)

@auth.route('/employeelogout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth/employeelogin.html"))


@auth.route('/employerlogin',methods = ["GET","POST"])
def login_employer():
    login_form = LoginemployerForm()
    if login_form.validate_on_submit():
        user = Employer.query.filter_by(email=login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(url_for('main.index'))
        flash('Invalid username or Password')

    title = "Employer Login"
    return render_template('auth/employer_login.html',loginemployer_form=login_form,title=title)


@auth.route('/employerregister',methods = ["GET","POST"])
def register_employer():
    form = RegistrationemployerForm()
    if form.validate_on_submit():
        user = Employer(email = form.email.data,username = form.username.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login_employer'))
        title = "New Employee Account"
    return render_template('auth/employer_register.html',registrationemployer_form = form)

@auth.route('/employerlogout')
@login_required
def logout_employer():
    logout_user()
    return redirect(url_for("auth/employerlogin.html"))