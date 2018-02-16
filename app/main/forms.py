from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,FileField,RadioField,BooleanField,DateTimeField,DateField,IntegerField
from wtforms.validators import Required,AnyOf
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename
from ..models import Jobad,Employee




class JobadForm(FlaskForm):
    username = StringField('Your employee Account Username',validators=[Required()])
    adtitle = StringField('Ad Title',validators=[Required()])
    dateposted = StringField('Date',validators=[Required()])
    category = RadioField('Category',choices=[('clean','Cleaning Services'),('garden','Landscaping and Garden Services'),('security','Security and Night Watch Services')],validators=[Required()])  
    adcontent = TextAreaField('Your Job Ad -Short Description of What you can do.',validators=[Required()])
    submit = SubmitField('Submit')

class EditprofileForm(FlaskForm):
    skill = TextAreaField('Your Skill',validators=[Required()])
    experience = TextAreaField('Places and People you have worked with before',validators=[Required()])
    contact = StringField('Contact',validators=[Required()])
    category = RadioField('Category',choices=[('clean','Cleaning Services'),('garden','Landscaping and Garden Services'),('security','Security and Night Watch Services')],validators=[Required()])  
    age = IntegerField('Age',validators=[Required()])
    gender = RadioField('Category',choices=[('female','Female'),('male','Male')],validators=[Required()])  
    status = StringField('Times you are available for work,e.g,weekends,permanent monthly employee,biweekly..',validators=[Required()])
    location = StringField('Your Location',validators=[Required()])
    submit = SubmitField('Submit')
