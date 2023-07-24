from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField, PasswordField
from wtforms.validators import InputRequired


class Register(FlaskForm):
    first_name = StringField(validators=[InputRequired()], render_kw={"placeholder": "first Name"})
    last_name = StringField(validators=[InputRequired()], render_kw={"placeholder": "Second Name"})
    email_addr = EmailField(render_kw={"placeholder": "Email"})
    passcode = PasswordField(render_kw={"placeholder": "Password"})
    confirmPasscode = PasswordField(render_kw={"placeholder": "Confirm Password"})


class Login(FlaskForm):
    email_addr = EmailField(render_kw={"placeholder": "Email"})
    passcode = PasswordField(render_kw={"placeholder": "Password"})
