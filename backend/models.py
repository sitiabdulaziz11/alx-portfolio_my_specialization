from sqlalchemy import Column, Integer, String, ForeignKey, relationship
from sqlalchemy.exe.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class Student(Base):
    """ Student model that represents student's fields/attributes.
    """
    __tablename__ = "students"
    
    id = Column(Integer, primary_key=True)
    firstname = Column(String(50), nullable=False)
    middilename = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    email = Column(String(50), unique=True)
    password = Column(String(250), unique=True)
    birth_date = Column(datetime, nullable=False, default=datetime.now().strftime('%d-%m-%Y')) # Q?
    image_file = Column(String(50), unique=True, default="default.jpg")
    # address = relationship("Address", backref="student", uselist=False)
    # address = Column(String(100), nullable=false)
    phone_no = Column(String(10), unique=True)
    conduct = Column(String(10), nullable=False)#Q?
    

class Teacher(Base):
    """ Teacher model that represents teacher's fields/attributes.
    """
    __tablename__ = "teachers"
    
    id = Column(Integer, primary_key=True)
    firstname = Column(String(50), nullable=False)
    middlename = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(250), nullable=False, unique=True)
    hire_date = Column(datetime, nullable=False, default=datetime.now().strftime('%d-%m-%Y')) # Q?
    image_file = Column(String(50), nullable=False, unique=True, default="default.jpg")
    # address = relationship("Address", ?backref="teacher", uselist=False)?
    # address = Column(String(100), nullable=false)
    phone_no = Column(String(10), nullable=False, unique=True)
    subject = Column(String(150), nullable=False)#Q?what subject does teacher teach?
    section = Column(String(150), nullable=False)#Q? what section does teacher teach?


class Parent(Base):
    """ Student's Parent Module
    """
    __tabelname__ = "parents"
    
    id = Column(Integer, primary_key=True)
    firstname = Column(String(50), nullable=False)
    middlename = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    phone_no = Column(String(10), nullable=False, unique=True)
    email = Column(String(50), unique=True)
    password = Column(String(250), unique=True)
    image_file = Column(String(50), nullable=False, unique=True, default="default.jpg")
    Address = Column(String(100), nullable=False)

class User(Base):
    """ User model that represents user's fields/attributes.
    """
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(250), nullable=False, unique=True)
    image_file = Column(String(50), nullable=False, unique=True, default="default.jpg")
    
    
class Address(Base):
    """ Address model that represents address fields/attributes.
    """
    __tablename__ = "addresses"
    
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    teacher_id = Column(Integer, ForeignKey("teachers.id"), nullable=False)
    address = Column(String(100), nullable=False)
    city = Column(String(100))
    state = Column(String(100))
    country = Column(String(100))


class CourseorSubject(Base):#Q?
    """ Subject model that represents subject's fields/attributes.
    """
    __tablename__ = "subjects"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)

# class ClassorSection(Base):#Q?
#     """ Section model that represents section's fields/attributes.
#     """
#     __tablename__ = "sections"
    
#     id = Column(Integer, primary_key=True)
#     secname = Column(String(100), nullable=False, unique=True)

class Result(Base):
    """ Result model that represents result's fields/attributes.
    """
    __tablename__ = "results"
    
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    teacher_id = Column(Integer, ForeignKey("teachers.id"), nullable=False)
    subject_id = Column(Integer, ForeignKey("subjects.id"), nullable=False)
    marks = Column(Integer, nullable=False)
    date = Column(datetime, nullable=False, default=datetime.now().strftime('%d-%m-%Y'))
    
    class Parent(Base):
        __tablename__ = 'parents'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    children = relationship('Child', back_populates='parent')

class Child(Base):
    __tablename__ = 'children'
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('parents.id'))
    parent = relationship('Parent', back_populates='children')