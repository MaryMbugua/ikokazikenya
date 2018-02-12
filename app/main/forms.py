from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,FileField,RadioField,BooleanField
from wtforms.validators import Required,AnyOf
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename

