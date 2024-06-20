from flask import Flask
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, relationship
from werkzeug.security import generate_password_hash, check_password_hash


Base = declarative_base()


class Student(Base):
    """ Student model that represents student's fields/attributes.
    """
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False, index=True)
    email = Column(String(250), unique=True)
    password = Column(String(250), unique=True)
    birth_date = Column(String(250), nullable=False, default=datetime.now().strftime('%Y-%m-%d'))

    
    # class Result = Column(Integer, nullable=False, default=0), first term ...
    subject_id = Column(Integer, ForeignKey('subject.id'), nullable=False)
    status = Column(String(10), nullable=False, default='')
    image_file = Column(String(20), nullable=False, default='default.jpg')
    phno, conduct, address

class Subject(Base):
    """ Subject model """
    __tablename__ = 'subject'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    teacher_id = Column(Integer, ForeignKey('teacher.id'), nullable=False)
    student = relationship('Students', backref='subjects', lazy=True)
    score = Column(float, nullable=False, default=3.5)


class Teacher(Base):
    """ Teacher model """
    __tablename__ = 'teacher'

    id = Column(Integer, primary_key=True)
    firest, lastname = Column(String(250), nullable=False)
    email = Column(String(250), unique=True)
    password = Column(String(250), nullable=False, unique=True)
    subject = relationship('Subject', backref='teachers', lazy=True)

class User(Base):
    """ User model """
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(String(128), nullable=False, unique=True)
    password = Column(String(128), nullable=False, unique=True)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

parent