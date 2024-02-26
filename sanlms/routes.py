# -*- coding: utf-8 -*-
"""
  routes.py
  Author : Jacek 'Szumak' Kotlarski --<szumak@virthost.pl>
  Created: 24.02.2024, 10:17:22
  
  Purpose: 
"""

import os
from functools import wraps
from pathlib import Path
from typing import Optional

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
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.engine import URL
from sqlalchemy.util import immutabledict

from sanlms.tools import SanConfig


basedir: Path = Path(__file__).resolve().parent

# configuration
conf = SanConfig()
DATABASE: str = conf.db_database if conf.db_database else ""
USERNAME: str = conf.db_login if conf.db_login else ""
PASSWORD: str = conf.db_password if conf.db_password else ""
HOST: str = str(conf.db_host) if conf.db_host else ""
PORT: int = conf.db_port if conf.db_port else 3306
SALT: int = conf.salt if conf.salt else 0

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

if not conf.errors:

    from sanlms import models

    @app.route("/hello")
    def hello():
        # out = ""
        # for item in models.User.all():
        #     out += str(item) + "<br>"
        # return out
        return "Hello, World!"

else:

    @app.route("/")
    def index():

        return "Internal error."


# #[EOF]#######################################################################
