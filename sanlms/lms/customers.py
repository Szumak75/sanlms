# -*- coding: UTF-8 -*-
"""
Created on 6 oct 2020

@author: szumak@virthost.pl
"""

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import (
    INTEGER,
    SMALLINT,
    TEXT,
    TINYINT,
    VARCHAR,
)

from libs.db_models.base import LmsBase


class Customer(LmsBase):
    __tablename__: str = "customers"

    id: Mapped[int] = mapped_column(
        INTEGER(11), primary_key=True, nullable=False, autoincrement=True
    )
    extid: Mapped[str] = mapped_column(VARCHAR(32), nullable=False, default="")
    lastname: Mapped[str] = mapped_column(VARCHAR(128), nullable=False, default="")
    name: Mapped[str] = mapped_column(VARCHAR(128), nullable=False, default="")
    status: Mapped[int] = mapped_column(SMALLINT(6), nullable=False, default=0)
    type: Mapped[int] = mapped_column(SMALLINT(6), nullable=False, default=0)
    ten: Mapped[str] = mapped_column(VARCHAR(16), nullable=False, default="")
    ssn: Mapped[str] = mapped_column(VARCHAR(11), nullable=False, default="")
    regon: Mapped[str] = mapped_column(VARCHAR(255), nullable=False, default="")
    rbe: Mapped[str] = mapped_column(VARCHAR(255), nullable=False, default="")
    icn: Mapped[str] = mapped_column(VARCHAR(255), nullable=False, default="")
    rbename: Mapped[str] = mapped_column(VARCHAR(255), nullable=False, default="")
    info: Mapped[str] = mapped_column(TEXT(), nullable=False)
    creationdate: Mapped[int] = mapped_column(INTEGER(11), nullable=False, default=0)
    moddate: Mapped[int] = mapped_column(INTEGER(11), nullable=False, default=0)
    notes: Mapped[str] = mapped_column(TEXT(), nullable=False)
    creatorid: Mapped[int] = mapped_column(INTEGER(11), default=None)
    modid: Mapped[int] = mapped_column(INTEGER(11), default=None)
    deleted: Mapped[int] = mapped_column(TINYINT(1), nullable=False, default=0)
    message: Mapped[str] = mapped_column(TEXT(), nullable=False)
    cutoffstop: Mapped[int] = mapped_column(INTEGER(11), nullable=False, default=0)
    consentdate: Mapped[int] = mapped_column(INTEGER(11), nullable=False, default=0)
    pin: Mapped[str] = mapped_column(VARCHAR(255), nullable=False, default="0")
    invoicenotice: Mapped[int] = mapped_column(TINYINT(1), default=None)
    einvoice: Mapped[int] = mapped_column(TINYINT(1), default=None)
    divisionid: Mapped[int] = mapped_column(INTEGER(11), default=None)
    mailingnotice: Mapped[int] = mapped_column(TINYINT(1), default=None)
    paytype: Mapped[int] = mapped_column(SMALLINT(6), default=None)
    paytime: Mapped[int] = mapped_column(SMALLINT(6), nullable=False, default="-1")

    def __repr__(self) -> str:
        return (
            f"Customer(id='{self.id}', "
            f"extid='{self.extid}', "
            f"lastname='{self.lastname}', "
            f"name='{self.name}', "
            f"status='{self.status}', "
            f"type='{self.type}', "
            f"ten='{self.ten}', "
            f"ssn='{self.ssn}', "
            f"regon='{self.regon}', "
            f"rbe='{self.rbe}', "
            f"icn='{self.icn}', "
            f"rbename='{self.rbename}', "
            # f"info='{self.info}', "
            f"creationdate='{self.creationdate}', "
            f"moddate='{self.moddate}', "
            # f"notes='{self.notes}', "
            f"creatorid='{self.creatorid}', "
            f"modid='{self.modid}', "
            f"deleted='{self.deleted}', "
            # f"message='{self.message}', "
            f"cutoffstop='{self.cutoffstop}', "
            f"consentdate='{self.consentdate}', "
            f"pin='{self.pin}', "
            f"invoicenotice='{self.invoicenotice}', "
            f"einvoice='{self.einvoice}', "
            f"divisionid='{self.divisionid}', "
            f"mailingnotice='{self.mailingnotice}', "
            f"paytype='{self.paytype}', "
            f"paytime='{self.paytime}' ) "
        )
