from flask import render_template,redirect,url_for,flash
from . import auth
from ..models import Admin
from .forms import RegistrationForm,LoginForm
from .. import db
from flask_login import login_user,logout_user,login_required

@auth.route('/adminlogin',methods = ["GET","POST"])
def login():
  
    title = "blog admin login"
    return render_template('auth/admin_login.html',login_form=login_form,title=title)