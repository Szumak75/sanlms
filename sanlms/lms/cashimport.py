# -*- coding: UTF-8 -*-
"""
Created on 6 oct 2020

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


class CashImport(LmsBase):
    __tablename__: str = "cashimport"

    id: Mapped[int] = mapped_column(
        INTEGER(11), primary_key=True, nullable=False, autoincrement=True
    )
    date: Mapped[int] = mapped_column(INTEGER(11), nullable=False, default=0)
    value: Mapped[float] = mapped_column(DECIMAL(9, 2), nullable=False, default=0.00)
    customer: Mapped[str] = mapped_column(TEXT(), nullable=False)
    description: Mapped[str] = mapped_column(TEXT(), nullable=False)
    customerid: Mapped[int] = mapped_column(INTEGER(11), default=None)
    hash: Mapped[str] = mapped_column(VARCHAR(50), nullable=False, default="")
    closed: Mapped[int] = mapped_column(TINYINT(1), nullable=False, default=0)
    sourcefileid: Mapped[int] = mapped_column(INTEGER(11), default=None)
    sourceid: Mapped[int] = mapped_column(INTEGER(11), default=None)

    def __repr__(self) -> str:
        return (
            f"CashImport(id='{self.id}', "
            f"date='{self.date}', "
            f"value='{self.value}', "
            f"customer='{self.customer}', "
            f"description='{self.description}', "
            f"customerid='{self.customerid}', "
            f"hash='{self.hash}', "
            f"closed='{self.closed}', "
            f"sourcefileid='{self.sourcefileid}', "
            f"sourceid='{self.sourceid}' ) "
        )
