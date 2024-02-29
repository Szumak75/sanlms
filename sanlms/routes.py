# -*- coding: utf-8 -*-
"""
  routes.py
  Author : Jacek 'Szumak' Kotlarski --<szumak@virthost.pl>
  Created: 24.02.2024, 10:17:22
  
  Purpose: 
"""

from crypt import methods
import os, secrets, tempfile

from functools import wraps
from pathlib import Path
from typing import Optional, List, Any

from jsktoolbox.datetool import DateTime
from jsktoolbox.stringtool.crypto import SimpleCrypto

from flask import (
    Flask,
    render_template,
    request,
    session,
    flash,
    redirect,
    url_for,
    abort,
    jsonify,
)
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename

from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.engine import URL
from sqlalchemy.util import immutabledict

from logging.config import dictConfig

from sanlms.tools import SanConfig
from sanlms.parser import BzWbkMt940

basedir: Path = Path(__file__).resolve().parent

# configuration
conf = SanConfig()
DATABASE: str = conf.db_database if conf.db_database else ""
USERNAME: str = conf.db_login if conf.db_login else ""
PASSWORD: str = conf.db_password if conf.db_password else ""
HOST: str = str(conf.db_host) if conf.db_host else ""
PORT: int = conf.db_port if conf.db_port else 3306
SALT: int = conf.salt if conf.salt else 0
SECRET_KEY: bytes = secrets.token_bytes()

url = URL(
    "mysql+pymysql",
    username=USERNAME,
    password=SimpleCrypto.multiple_decrypt(SALT, PASSWORD),
    host=HOST,
    database=DATABASE,
    port=PORT,
    query=immutabledict({"charset": "utf8mb4"}),
)

SQLALCHEMY_DATABASE_URI = url
SQLALCHEMY_ECHO = True
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Create and initialize a new Flask app
app = Flask(__name__)

# load the config
app.config.from_object(__name__)
# init sqlalchemy
db = SQLAlchemy(app)

dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
            }
        },
        "handlers": {
            "wsgi": {
                "class": "logging.StreamHandler",
                "stream": "ext://flask.logging.wsgi_errors_stream",
                "formatter": "default",
            }
        },
        "root": {"level": "INFO", "handlers": ["wsgi"]},
    }
)


# Forms
class LoginForm(FlaskForm):

    login = StringField(
        label="Login", validators=[DataRequired()], description="User login name."
    )
    passwd = PasswordField(
        label="Hasło", validators=[DataRequired()], description="User password."
    )
    submit = SubmitField(label="Zaloguj się")


class DataForm(FlaskForm):

    class _Cash:
        date: str = ""
        value: float = 0.00
        customer: str = ""
        desc: str = ""

    __menu_items: List[Any] = []
    __data_items: List[Any] = []
    file = FileField(validators=[FileRequired()])
    submit = SubmitField(label="Prześlij")

    @property
    def cash_import(self) -> List[Any]:
        return self.__data_items

    @cash_import.setter
    def cash_import(self, values: List[Any]) -> None:
        self.__data_items.clear()

        for item in values:
            obj = self._Cash()
            obj.date = str(DateTime.datetime_from_timestamp(item.date))
            obj.customer = item.customer
            obj.value = item.value
            obj.desc = item.description
            self.__data_items.append(obj)


if not conf.errors:

    from sanlms import models

    @app.route("/", methods=["GET", "POST"])
    def index():
        if "username" not in session:
            return redirect(url_for("login"))

        data_form = DataForm()
        if data_form.validate_on_submit():
            if conf.debug:
                app.logger.info("data form validated successfully")
            uploaded_file = data_form.file.data

            file_name = secure_filename(uploaded_file.filename)
            with tempfile.NamedTemporaryFile(delete=False) as fp:
                fp.close()
                uploaded_file.save(fp.name)

                has_import = False

                # open file
                with open(fp.name, mode="rb") as file:
                    if conf.debug:
                        app.logger.info(f"File name to open: {fp.name}")
                    tmp: bytes = file.read()
                    app.logger.info(f"{tmp.decode()}")
                    # process MT940
                    mt940 = BzWbkMt940()
                    mt940.parse(tmp.decode())
                    if conf.debug:
                        app.logger.info(f"{mt940.db}")
                    for section in mt940.db:
                        count_imp = 0
                        count_dup = 0
                        for record in section["trans"]:
                            if record["side"] != "C":
                                continue
                            if not models.CashImport.has_hash(record["hash"]):
                                count_imp += 1
                                # create new CI
                                obj = models.CashImport.new(record)
                                if conf.debug:
                                    app.logger.info(f"New import: {obj}")
                                db.session.add(obj)
                            else:
                                count_dup += 1
                        if count_imp > 0:
                            has_import = True
                            app.logger.info(f"import {count_imp} records")
                        if count_dup > 0:
                            app.logger.info(f"found {count_dup} duplicates")

                # commit new records to database
                if has_import:
                    db.session.commit()

                # clean up
                if os.path.exists(fp.name):
                    os.remove(fp.name)
        else:
            if conf.debug:
                app.logger.info("data form validation error")

        data_form.cash_import = models.CashImport.all()
        return render_template("index.html", form=data_form)

    @app.route("/login", methods=["GET", "POST"])
    def login():
        if "username" in session:
            return redirect("/")
        form = LoginForm()
        if form.validate_on_submit():
            if (
                form.login.data
                and form.passwd.data
                and models.User.check_login(form.login.data, form.passwd.data)
            ):
                session["username"] = form.login.data
                if conf.debug or conf.verbose:
                    app.logger.info(f"{form.login.data} logged in successfully")
                return redirect("/")
        return render_template("login.html", form=form)

    @app.route("/logout")
    def logout():
        session.pop("username", None)
        return redirect(url_for("index"))

    @app.route("/hello")
    def hello():
        # out = ""
        # for item in models.User.all():
        #     out += str(item) + "<br>"
        # return out
        return "Hello, World!"

else:

    @app.route("/")
    def index_ie():

        return "Internal error."


# #[EOF]#######################################################################
