from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class TestForm(Form):
    test_form = StringField('test_form', validators=[DataRequired()])
