from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FloatField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo

# Define form classes here
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

class TransactionForm(FlaskForm):
    amount = FloatField('Amount', validators=[DataRequired()])
    category = SelectField('Category', choices=[('food', 'Food'), ('shopping', 'Shopping'), ('bills', 'Bills'), ('other', 'Other')])

class BudgetForm(FlaskForm):
    category = SelectField('Category', choices=[('food', 'Food'), ('shopping', 'Shopping'), ('bills', 'Bills'), ('other', 'Other')])
    limit = FloatField('Budget Limit', validators=[DataRequired()])
