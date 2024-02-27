# -*- coding: utf-8 -*-
"""
  parser.py
  Author : Jacek 'Szumak' Kotlarski --<szumak@virthost.pl>
  Created: 27.02.2024, 14:36:10
  
  Purpose: 
"""

import hashlib
import re
import string

from typing import Pattern, Optional, Any, List, Dict, Match

from jsktoolbox.attribtool import NoDynamicAttributes


class BzwbkMt940(NoDynamicAttributes):
    """Parser for MT940 files (BZWBK)"""

    __re61: Pattern[str] = None  # type: ignore
    __re8620: Pattern[str] = None  # type: ignore
    __re8631: Pattern[str] = None  # type: ignore
    __re8632: Pattern[str] = None  # type: ignore
    __db: List[Any] = []
    __data = None  # type: ignore

    def __init__(self, data=None) -> None:
        self.__re61 = re.compile(":61:(\d{6})(\D)(\D)([0-9,]*).*")
        self.__re8620 = re.compile("(.*)EIN(.*)")
        self.__re8631 = re.compile("")
        self.__re8632 = re.compile("")

        if data is not None:
            self.__data = data

    def parse(self, data=None) -> None:
        if data is not None:
            self.__data = data
        lines = self.__data.split("\r\n")
        # print lines
        ind = 0
        trans = -1
        self.__db: List[Any] = []
        _buffer: Dict[Any, Any] = {}

        for l_ind, line in enumerate(lines):
            if line.startswith(("\x01{1:", "{1:")):
                """SOH - start section"""
                self.__db.append({})
                self.__db[ind]["trans"] = []
                continue
            if line.startswith(":20:"):
                """16x - date + file number"""
                self.__db[ind]["ref"] = line[4:]
                continue
            if line.startswith(":25:"):
                """35x - account ident"""
                self.__db[ind]["acc"] = line[4:]
                continue
            if line.startswith(":28C:"):
                """35x - file number/seqnum"""
                self.__db[ind]["seq"] = line[5:]
                continue
            if line.startswith(":60"):
                """1!a6!n3!a15d  - start balance"""
                continue
            if line.startswith((":61:", ":62F:", ":62M:")):
                """6!n[4!n]2a[1!a]15d4!c16x[//16x[34x]]  - start balance"""
                # print("BUFFER: {}".format(_buffer))
                if _buffer:
                    out: Optional[Match[str]] = self.__re8620.match(_buffer["title"])
                    if out is not None:
                        (_buffer["title"], _tein) = out.groups()
                        if "ein" not in _buffer:
                            _buffer["ein"] = _tein
                    _buffer["acc_id"] = _buffer["ein"][-4:]
                    _buffer["date"] = (
                        _buffer["date"][4:]
                        + "-"
                        + _buffer["date"][2:4]
                        + "-20"
                        + _buffer["date"][:2]
                    )
                    h = hashlib.new("md5")
                    h.update(str(_buffer))  # type: ignore
                    _buffer["hash"] = h.hexdigest()
                    self.__db[ind]["trans"].append(_buffer)
                    _buffer = {}
            if line.startswith((":62M:")):
                continue
            if line.startswith(":61:"):
                """6!n[4!n]2a[1!a]15d4!c16x[//16x[34x]]  - start balance"""
                (date, side, curr, value) = self.__re61.match(line).groups()
                _buffer.update(
                    {
                        "date": date,
                        "side": side,
                        "curr": curr,
                        "value": value,
                    }
                )
                continue
            if line.startswith(":86:>20"):
                _buffer.update({"title": line[7:]})
                continue
            if line.startswith(">31"):
                _buffer.update({"help_acc": line[3:]})
                continue
            if line.startswith(">32"):
                _buffer.update({"name": line[3:]})
                continue
            if line.startswith(">38"):
                _buffer.update({"ein": line[3:]})
                continue
            if line.startswith(":62F:"):
                continue
            if line.startswith((":64", "-}")):
                ind += 1
                continue

            prev_line = lines[l_ind - 1]
            if prev_line.startswith(":86:>20"):
                _buffer.update({"title": _buffer["title"] + line})
            if prev_line.startswith(">32"):
                _buffer.update({"name": _buffer["name"] + line})

    def __str__(self) -> str:
        return str(self.__db)

    @property
    def db(self) -> List[Any]:
        return self.__db


# #[EOF]#######################################################################
