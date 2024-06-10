from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, HiddenField,IntegerField,DateField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from model import User


class SignupForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists! Please try a different username')

    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email Address already exists! Please try a different email address')

    username = StringField(label='User Name:', validators=[Length(min=5, max=30), DataRequired()])
    email_address = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    phonenumber = IntegerField(label='Phone_number:', validators=[Length(min=11, max=11), DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    confirm_password = PasswordField(label='Confirm Password:', validators=[EqualTo('password'), DataRequired()])
    submit = SubmitField(label='Create Account')


class SigninForm(FlaskForm):
    email_address = StringField(label='Email Address:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')

class SignoutForm(FlaskForm):
    pass

class ResetRequestform(FlaskForm):
    email = StringField(label="Email", validators=[DataRequired()])
    submit = SubmitField(label='Reset Password ', validators=[DataRequired()])


class ResetPasswordForm(FlaskForm):
    password = PasswordField(label='Password:', validators=[DataRequired()])
    confirm_password = PasswordField(label='Confirm Password:', validators=[EqualTo('password'), DataRequired()])
    submit = SubmitField(label='Change Password', validators=[DataRequired()])



class BookingForm(FlaskForm):
    room_id = IntegerField('room_id',validators=[DataRequired()])
    data = DateField('Date',validators=[DataRequired()])
    user_id = IntegerField('User_id',validators=[DataRequired()])
