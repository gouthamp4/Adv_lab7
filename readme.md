## Simple Register and Sigin Application

## Installation
Using pip install following:  Falsk Flask-WTF WTForms flask_sqlalchemy flask_bcrypt

  

## Application Functionality

1) After Installing, run the following command "python base.py", this will create a folder "instance" inside a db folder.

2) User can register or siginin on home page if already registered. If Email is already utilized a warning is given to regster with a new email.

3) Password Security check is adopted from previous assignment.

4) Used Bcrypt module to Hash the password to protect its authenticity and confidentiality.

** Used Session to Store number of attempts and used Flask flash message feature to spit the warnings and messages in realtime.

## Refference's:

1)  Developed by understanding  **Dr.Mahmut Unan's** lectuers and reffered following link for better understanding of flask.

2) Reffered [Flask](https://flask.palletsprojects.com/en/2.3.x/) docs in developing project.

3) Reffered [Flask Message Flashing](https://flask.palletsprojects.com/en/2.3.x/patterns/flashing/) for displaying warnings and errors.