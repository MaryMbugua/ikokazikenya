from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import Required,Email,EqualTo
from ..models import  Employee,Employer
from wtforms import ValidationError

class RegistrationemployeeForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    username = StringField('Enter your username',validators= [Required()])
    firstname = StringField('Enter your firstname',validators= [Required()])
    lastname = StringField('Enter your lastname',validators= [Required()])
    password = PasswordField('Password',validators=[Required(),
    EqualTo('password_confirm',message= 'Passwords must match')])
    password_confirm = PasswordField('Confirm Password',validators=[Required()])
    submit = SubmitField('Sign Up')

    def validate_email(self,data_field):
        if Employee.query.filter_by(email = data_field.data).first():
            raise ValidationError('There is an account with that email')

    def validate_username(self,data_field):
        if Employee.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')       
class LoginemployeeForm(FlaskForm):
    email = StringField('Your email address',validators=[Required()])
    password = PasswordField('Password',validators =[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')

class RegistrationemployerForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    username = StringField('Enter your username',validators= [Required()])
    firstname = StringField('Enter your firstname',validators= [Required()])
    lastname = StringField('Enter your lastname',validators= [Required()])
    password = PasswordField('Password',validators=[Required(),
    EqualTo('password_confirm',message= 'Passwords must match')])
    password_confirm = PasswordField('Confirm Password',validators=[Required()])
    submit = SubmitField('Sign Up')

    def validate_email(self,data_field):
        if Employee.query.filter_by(email = data_field.data).first():
            raise ValidationError('There is an account with that email')

    def validate_username(self,data_field):
        if Employee.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')       
class LoginemployerForm(FlaskForm):
    email = StringField('Your email address',validators=[Required()])
    password = PasswordField('Password',validators =[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')