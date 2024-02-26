# -*- coding: UTF-8 -*-
"""
Created on 9 oct 2020

@author: szumak@virthost.pl
"""

from sqlalchemy import ForeignKey, Integer, Text, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.mysql import (
    DECIMAL,
    INTEGER,
    MEDIUMTEXT,
    SMALLINT,
    TEXT,
    TINYINT,
    VARCHAR,
)

from libs.db_models.base import LmsBase


class User(LmsBase):
    __tablename__: str = "users"

    id: Mapped[int] = mapped_column(
        INTEGER(11), primary_key=True, nullable=False, autoincrement=True
    )
    login: Mapped[str] = mapped_column(VARCHAR(32), nullable=False, default="")
    firstname: Mapped[str] = mapped_column(VARCHAR(64), nullable=False, default="")
    lastname: Mapped[str] = mapped_column(VARCHAR(64), nullable=False, default="")
    email: Mapped[str] = mapped_column(VARCHAR(255), nullable=False, default="")
    phone: Mapped[str] = mapped_column(VARCHAR(32), nullable=False, default="")
    position: Mapped[str] = mapped_column(VARCHAR(255), nullable=False, default="")
    rights: Mapped[str] = mapped_column(TEXT(), nullable=False)
    hosts: Mapped[str] = mapped_column(VARCHAR(255), nullable=False, default="")
    passwd: Mapped[str] = mapped_column(VARCHAR(255), nullable=False, default="")
    ntype: Mapped[int] = mapped_column(SMALLINT(6), default=None)
    lastlogindate: Mapped[int] = mapped_column(INTEGER(11), nullable=False, default=0)
    lastloginip: Mapped[str] = mapped_column(VARCHAR(16), nullable=False, default="")
    failedlogindate: Mapped[int] = mapped_column(INTEGER(11), nullable=False, default=0)
    failedloginip: Mapped[str] = mapped_column(VARCHAR(16), nullable=False, default="")
    deleted: Mapped[int] = mapped_column(TINYINT(1), nullable=False, default=0)
    passwdexpiration: Mapped[int] = mapped_column(
        INTEGER(11), nullable=False, default=0
    )
    passwdlastchange: Mapped[int] = mapped_column(
        INTEGER(11), nullable=False, default=0
    )
    access: Mapped[int] = mapped_column(TINYINT(1), nullable=False, default=1)
    accessfrom: Mapped[int] = mapped_column(INTEGER(11), nullable=False, default=0)
    accessto: Mapped[int] = mapped_column(INTEGER(11), nullable=False, default=0)
    settings: Mapped[str] = mapped_column(MEDIUMTEXT(), nullable=False)
    persistentsettings: Mapped[str] = mapped_column(MEDIUMTEXT(), nullable=False)

    def __repr__(self) -> str:
        return (
            f"User(id='{self.id}', "
            f"login='{self.login}', "
            f"firstname='{self.firstname}', "
            f"lastname='{self.lastname}', "
            f"email='{self.email}', "
            f"phone='{self.phone}', "
            f"position='{self.position}', "
            f"rights='{self.rights}', "
            f"hosts='{self.hosts}', "
            f"passwd='{self.passwd}', "
            f"ntype='{self.ntype}', "
            f"lastlogindate='{self.lastlogindate}', "
            f"lastloginip='{self.lastloginip}', "
            f"failedlogindate='{self.failedlogindate}', "
            f"failedloginip='{self.failedloginip}', "
            f"deleted='{self.deleted}', "
            f"passwdexpiration='{self.passwdexpiration}', "
            f"passwdlastchange='{self.passwdlastchange}', "
            f"access='{self.access}', "
            f"accessfrom='{self.accessfrom}', "
            f"accessto='{self.accessto}', "
            f"settings='{self.settings}', "
            f"persistentsettings='{self.persistentsettings}' ) "
        )
