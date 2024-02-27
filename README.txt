
[Flask]

# Sessions
https://flask.palletsprojects.com/en/3.0.x/quickstart/#sessions

How to generate good secret keys
A secret key should be as random as possible. Your operating system has ways to generate pretty random data based on a cryptographic random generator. Use the following command to quickly generate a value for Flask.secret_key (or SECRET_KEY):

$ python -c 'import secrets; print(secrets.token_hex())'
'192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'


[Flask-SQLAlchemy]

https://pypi.org/project/Flask-SQLAlchemy/

[Flask-Navigation]

https://www.geeksforgeeks.org/navigation-bars-in-flask/

[Flask-Menu]

https://flask-menu.readthedocs.io/en/latest/

[Quick Tutorial]

https://pythonhow.com/python-tutorial/flask/web-development-with-python-and-flask/

[WTForms] & [flask-wtf] & [flask-login]

https://wtforms.readthedocs.io/en/3.1.x/
https://flask-wtf.readthedocs.io/en/1.2.x/
https://flask-login.readthedocs.io/en/latest/

[crypt]

crypt.crypt('mojehaslo', password) == password