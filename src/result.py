from typing import TypeVar, Generic, TypeAlias

TOK = TypeVar("TOK")
TERR = TypeVar("TERR")


class Ok(Generic[TOK]):
    _value: TOK

    def __init__(self, value: TOK):
        self._value = value

    def is_ok(self) -> bool:
        return isinstance(self, Ok)

    def ok_value(self) -> TOK:
        return self._value


class Error(Generic[TERR]):
    _err: TERR

    def __init__(self, err: TERR):
        self._err = err

    def is_ok(self) -> bool:
        return isinstance(self, Ok)

    def error_value(self) -> TERR:
        return self._err


Result: TypeAlias = Ok[TOK] | Error[TERR]
