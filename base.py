from flask import render_template, url_for, flash, session
from werkzeug.utils import redirect
from config import app, sqlDb, pwdHasher, Customer
from application_forms import Register, Login

# Logic starts from here
warnings = []


# password conditions check, from lab 06
def passwordValidate(password):
    del warnings[:]
    if not any(x.isupper() for x in password):
        warnings.append('Password missing Uppercase.')
    if not (password[-1].isdigit()):
        warnings.append('Password Should end with Number.')
    if not any(x.islower() for x in password):
        warnings.append('Password missing lowercase.')
    return True if len(warnings) == 0 else False

# Hashed Paswords are compared
def hashCompare(hashed, password):
    try:
        if not hashed or not password:
            raise Exception("Missing Data")
        return True if (pwdHasher.check_password_hash(hashed, password)) else False
    except Exception as error:
        print(error)
        flash(error, "danger")
        return redirect(url_for('homePage'))


def generateSaltPasscode(passcode):
    try:
       hashedPass = pwdHasher.generate_password_hash(passcode)
       return hashedPass
    except Exception as error:
        flash(error, "danger")
        return redirect(url_for('homePage'))

# Checks if user is already registered with this email
def existingCustomer(email):
    existingData = Customer.query.filter_by(email_addr=email).first()
    return True if existingData else False

@app.get('/')
def homePage():
    return render_template('home.html', signupform=Register(), loginform=Login(), warnings=warnings)

@app.get('/registartion-success')
def registrationSuccess():
    return render_template('registration_success.html')

@app.get('/secret')
def secret():
    if session['logged']:
        return render_template('secret.html')
    else:
        return redirect(url_for('homePage'))


@app.route('/login', methods=['GET', 'POST'])
def signInFunc():
    del warnings[:]
    sigin_in_form = Login()
    if sigin_in_form.validate_on_submit():
        customerData = Customer.query.filter_by(email_addr=sigin_in_form.email_addr.data).first()
        if customerData:
            if hashCompare(customerData.passcode, sigin_in_form.passcode.data):
                session['logged'] = True
                session['username'] = customerData.email_addr
                return redirect(url_for('secret'))
            else:
                flash("Couldn't Signin, Invalid Password", 'danger')
                return redirect(url_for('homePage'))
        else:
            flash("Invalid Email, Provide email used to Register", 'warning')
            return redirect(url_for('homePage'))


@app.route('/register', methods=["POST"])
def RegistrationFunc():
    try:
        del warnings[:]
        registration_form = Register()
        if not passwordValidate(registration_form.passcode.data):
            return redirect(url_for('homePage'))
        if registration_form.passcode.data != registration_form.confirmPasscode.data:
            # print("Password dont match")
            warnings.append("Your Passwords do not match")
            return redirect(url_for('homePage'))
        if registration_form.validate_on_submit() and not existingCustomer(registration_form.email_addr.data):
            passcode_bcrypt = generateSaltPasscode(registration_form.passcode.data)
            
            sqlDb.session.add(Customer(first_name=registration_form.first_name.data, last_name=registration_form.last_name.data,
                           email_addr=registration_form.email_addr.data, passcode=passcode_bcrypt))
            sqlDb.session.commit()
            flash("Registration success, Please Login", 'success')
            return redirect(url_for("registrationSuccess"))
        else:
            flash("Someone Already Registered with email", 'danger')
            return redirect(url_for('homePage'))
    except Exception as error:
        print(error)
        flash('Registration Failed, Try again', 'danger')
        return redirect(url_for('homePage'))


if __name__ == "__main__":
    app.run(debug=True)
