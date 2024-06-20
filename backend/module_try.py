from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date, Float, Table, UniqueConstraint, CheckConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    
    student = relationship("Student", back_populates="user", uselist=False)
    teacher = relationship("Teacher", back_populates="user", uselist=False)

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), unique=True, nullable=False)
    enrollment_date = Column(Date, nullable=False)
    
    user = relationship("User", back_populates="student")
    courses = relationship("Course", secondary=student_courses, back_populates="students")
    results = relationship("Result", back_populates="student")

class Teacher(Base):
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), unique=True, nullable=False)
    hire_date = Column(Date, nullable=False)
    
    user = relationship("User", back_populates="teacher")
    courses = relationship("Course", back_populates="teacher")
    subjects = relationship('Subject', secondary=teacher_subjects, back_populates='teachers', lazy='dynamic')

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=False)
    
    teacher = relationship("Teacher", back_populates="courses")
    students = relationship("Student", secondary=student_courses, back_populates="courses")
    results = relationship("Result", back_populates="course")

class Subject(Base):
    __tablename__ = 'subjects'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    
    teachers = relationship('Teacher', secondary=teacher_subjects, back_populates='subjects')

class Term(Base):
    __tablename__ = 'terms'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)  # e.g., "Term 1", "Term 2"

class SubjectTermResult(Base):
    __tablename__ = 'subject_term_results'
    
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'), nullable=False)
    subject_id = Column(Integer, ForeignKey('subjects.id'), nullable=False)
    term_id = Column(Integer, ForeignKey('terms.id'), nullable=False)
    score = Column(Float, nullable=False)
    rank = Column(Integer, nullable=False)
    average = Column(Float, nullable=False)
    
    student = relationship("Student")
    subject = relationship("Subject")
    term = relationship("Term")

class Result(Base):
    __tablename__ = 'results'
    
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'), nullable=False)
    course_id = Column(Integer, ForeignKey('courses.id'), nullable=False)
    score = Column(Float, nullable=False)
    date = Column(Date, nullable=False)
    overall_rank = Column(Integer, nullable=True)
    overall_average = Column(Float, nullable=True)
    
    student = relationship("Student", back_populates="results")
    course = relationship("Course", back_populates="results")
    
    __table_args__ = (
        UniqueConstraint('student_id', 'course_id', name='_student_course_uc'),
        CheckConstraint('score >= 0 AND score <= 100', name='check_score_range')
    )

# Database connection
engine = create_engine('sqlite:///school.db')
Base.metadata.create_all(engine)

# Session creation
Session = sessionmaker(bind=engine)
session = Session()
