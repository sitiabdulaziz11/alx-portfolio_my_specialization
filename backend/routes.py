from flask_login import login_required
from flask import render_template, redirect, url_for
from models import Students, Subjects, User
from forms import StudentForm
from app import app, db, login


@login.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route('/add_student', methods=['GET', 'POST'])
@login_required
def add_student():
    """ Add new student """
    form = StudentForm()
    form.subject.choices = [(sub.id, sub.name) for sub in Subjects.query.order_by(Subjects.name).all()]
    students = Students.query.order_by(Students.name).all()

    if form.validate_submit():
        student = Students(
            name=form.name.data,
            birth_date=form.birth_date.data,
            mark=form.mark.data,
            rank=form.rank.data,
            subject_id=form.subject.data,
            status=form.status.data
        )
        db.session.add(student)
        db.session.commit()
        return redirect(url_for(''))
    return render_template('', form=form, students=students)
