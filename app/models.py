from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return Employee.query.get(int(user_id))



class Employee(UserMixin,db.Model):
    __tablename__ = 'employees'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    firstname = db.Column(db.String(255),index = True)
    lastname = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    password_hash = db.Column(db.String(255))
    skill = db.Column(db.String(255))
    experience = db.Column(db.String(255))
    contact = db.Column(db.String(255))
    profilepic_path = db.Column(db.String(255))
    gender = db.Column(db.String(255))
    age = db.Column(db.String(255))
    status = db.Column(db.String(255))
    location = db.Column(db.String(255))
    category = db.Column(db.String(255))
    jobad = db.relationship("Jobad",backref='employee',lazy="dynamic")
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)
        
    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)
    def __repr__(self):
        return f'Employee {self.username}'

class Employer(UserMixin,db.Model):
    __tablename__ = 'employers'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    firstname = db.Column(db.String(255),index = True)
    lastname = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    password_hash = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)
        
    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)
    def __repr__(self):
        return f'Employer {self.username}'

class Jobad(UserMixin,db.Model):
    __tablename__ = 'jobads'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    adtitle = db.Column(db.String())
    adcontent = db.Column(db.String())
    category = db.Column(db.String())
    dateposted = db.Column(db.String())
    employee_id = db.Column(db.Integer,db.ForeignKey('employees.id'))
    
    def __repr__(self):
        return f'{self.adtitle}'

    def save_jobads(self):
        db.session.add(self)
        db.session.commit()

    def delete_jobads(self):
        db.session.delete(self)
        db.session.commit()