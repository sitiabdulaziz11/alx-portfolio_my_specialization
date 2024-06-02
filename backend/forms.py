from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, DateField, SubmitField, SelectField, PasswordField
from wtforms.validators import DataRequired, Email


class StudentForm(FlaskForm):
    """ Form for adding students """
    name = StringField('Name', validators=[DataRequired()])
    # email = StringField('Email: ', validators=Email())
    # password = PasswordField('Password: ')
    birth_date = DateField('Birth date: ',
                           validators=[DataRequired()])
    mark = FloatField('Mark: ', validators=[DataRequired()])
    rank = IntegerField('Rank: ')
    subject = SelectField('Subject', choices=[])
    status = SelectField('Learning status',
                         choices=[
                             ('free', 'Free'),
                             ('pay', 'Paid')
                         ])
    submit = SubmitField('Add')

