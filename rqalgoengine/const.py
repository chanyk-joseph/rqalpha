# -*- coding: utf-8 -*-

from enum import Enum


ORDER_STATUS = Enum("ORDER_STATUS", [
    "OPEN",
    "FILLED",
    "REJECTED",
    "CANCELLED",
])


EVENT_TYPE = Enum("EVENT_TYPE", [
    "DAY_START",
    "HANDLE_BAR",
    "DAY_END",
])