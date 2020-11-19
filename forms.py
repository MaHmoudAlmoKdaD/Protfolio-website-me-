from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError

class EmailForm(FlaskForm):
    name = StringField('Your Name (Required) :', validators=[DataRequired()])
    email = StringField('Your Email (Required) :', validators=[ Email()])
    subject = StringField('Subject (Required) :', validators=[DataRequired()])
    message = TextAreaField('Your Message (Required) :', validators=[DataRequired()])
    submit = SubmitField('SEND')

    # def validate_email(self, email):
    