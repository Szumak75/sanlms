# -*- coding: utf-8 -*-
"""
  models.py
  Author : Jacek 'Szumak' Kotlarski --<szumak@virthost.pl>
  Created: 25.02.2024, 09:51:47
  
  Purpose: 
"""

from typing import List, Any

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.mysql import (
    BIGINT,
    BINARY,
    BIT,
    BLOB,
    BOOLEAN,
    CHAR,
    DATE,
    DATETIME,
    DECIMAL,
    DECIMAL,
    DOUBLE,
    ENUM,
    FLOAT,
    INTEGER,
    LONGBLOB,
    LONGTEXT,
    MEDIUMBLOB,
    MEDIUMINT,
    MEDIUMTEXT,
    NCHAR,
    NUMERIC,
    NVARCHAR,
    REAL,
    SET,
    SMALLINT,
    TEXT,
    TIME,
    TIMESTAMP,
    TINYBLOB,
    TINYINT,
    TINYTEXT,
    VARBINARY,
    VARCHAR,
    YEAR,
)
from sanlms.routes import db


class User(db.Model):
    tablename: str = "__users__"

    # Table schema
    id = db.Column(INTEGER(11), primary_key=True, nullable=False)
    login = db.Column(VARCHAR(32), nullable=False, default="")
    firstname = db.Column(VARCHAR(64), nullable=False, default="")
    lastname = db.Column(VARCHAR(64), nullable=False, default="")
    email = db.Column(VARCHAR(255), nullable=False, default="")
    phone = db.Column(VARCHAR(32), nullable=False, default="")
    position = db.Column(VARCHAR(255), nullable=False, default="")
    rights = db.Column(TEXT(), nullable=False)
    hosts = db.Column(VARCHAR(255), nullable=False, default="")
    passwd = db.Column(VARCHAR(255), nullable=False, default="")
    ntype = db.Column(SMALLINT(6), default=None)
    lastlogindate = db.Column(INTEGER(11), nullable=False, default=0)
    lastloginip = db.Column(VARCHAR(16), nullable=False, default="")
    failedlogindate = db.Column(INTEGER(11), nullable=False, default=0)
    failedloginip = db.Column(VARCHAR(16), nullable=False, default="")
    deleted = db.Column(TINYINT(1), nullable=False, default=0)
    passwdexpiration = db.Column(INTEGER(11), nullable=False, default=0)
    passwdlastchange = db.Column(INTEGER(11), nullable=False, default=0)
    access = db.Column(TINYINT(1), nullable=False, default=1)
    accessfrom = db.Column(INTEGER(11), nullable=False, default=0)
    accessto = db.Column(INTEGER(11), nullable=False, default=0)
    settings = db.Column(MEDIUMTEXT(), nullable=False)
    persistentsettings = db.Column(MEDIUMTEXT(), nullable=False)

    # Instance methods
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id:{self.id}, login:{self.login})"

    # Class methods
    @classmethod
    def all(cls):
        return cls.query.all()

    @classmethod
    def find_by_login(cls, login: str):
        return cls.query.filter(cls.login == login)

    @classmethod
    def check_login(cls, login: str, password: str):
        pass


# #[EOF]#######################################################################
