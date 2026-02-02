from __future__ import annotations
from dataclasses import dataclass
from enum import Enum, auto
from typing import Any
from line_starts import index_to_line_col_batch
from lexer_token import Token


class NodeType(Enum):
    IDENTIFIER = 0
    TRUE_LITERAL = auto()
    FALSE_LITERAL = auto()
    INT_LITERAL = auto()
    FLOAT_LITERAL = auto()
    CHAR_LITERAL = auto()
    STRING_LITERAL = auto()
    ADD_OPERATOR = auto()
    SUB_OPERATOR = auto()
    MULT_OPERATOR = auto()
    DIV_OPERATOR = auto()
    MOD_OPERATOR = auto()
    EXP_OPERATOR = auto()
    POSITIVE_OPERATOR = auto()
    NEGATIVE_OPERATOR = auto()
    PRE_INCREMENT_OPERATOR = auto()
    POST_INCREMENT_OPERATOR = auto()
    PRE_DECREMENT_OPERATOR = auto()
    POST_DECREMENT_OPERATOR = auto()
    LESS_OPERATOR = auto()
    LESS_OR_EQUAL_OPERATOR = auto()
    GREATER_OPERATOR = auto()
    GREATER_OR_EQUAL_OPERATOR = auto()
    NOT_EQUAL_OPERATOR = auto()
    EQUAL_OPERATOR = auto()
    NOT_OPERATOR = auto()
    AND_OPERATOR = auto()
    OR_OPERATOR = auto()
    ASSIGNMENT_OPERATOR = auto()
    PLUS_ASSIGNMENT_OPERATOR = auto()
    MINUS_ASSIGNMENT_OPERATOR = auto()
    MULTIPLY_ASSIGNMENT_OPERATOR = auto()
    DIVIDE_ASSIGNMENT_OPERATOR = auto()
    MODULO_ASSIGNMENT_OPERATOR = auto()
    PERCENT_SCALE_OPERATOR = auto()
    MARKUP_OPERATOR = auto()
    MARKDOWN_OPERATOR = auto()
    FILE = auto()
    EXTERNAL_DECLARATION = auto()
    DECLARATION_STMT = auto()
    DECLARATION = auto()
    IF_STMT = auto()
    ELIF_STMT = auto()
    ELSE_STMT = auto()
    SWITCH_STMT = auto()
    SWITCH_BODY = auto()
    SWITCH_CASE = auto()
    SWITCH_DEFAULT = auto()
    SWEEP_STMT = auto()
    SWEEP_BODY = auto()
    SWEEP_CASE = auto()
    SWEEP_DEFAULT = auto()
    WHILE_STMT = auto()
    FUNCTION_STMT = auto()
    PARAMETER_LIST = auto()
    FOR_STMT = auto()
    BLOCK = auto()
    NEXT_STMT = auto()
    STOP_STMT = auto()
    RETURN_STMT = auto()
    STATEMENT = auto()
    TYPE = auto()
    COMPOUND_TYPE = auto()
    BUILTIN_TYPE = auto()
    MODIFIER_TYPE = auto()
    EXPRESSION_STMT = auto()
    EXPRESSION = auto()
    NUMANTICS_OPERATION = auto()
    ASSIGNMENT = auto()
    ASSIGNMENT_OP = auto()
    OR_OPERATION = auto()
    AND_OPERATION = auto()
    NOT_OPERATION = auto()
    RELATION = auto()
    RELATION_OP = auto()
    SUM = auto()
    TERM = auto()
    FACTOR = auto()
    POWER = auto()
    PREFIX = auto()
    POSTFIX = auto()
    ARGUMENTS = auto()
    PRIMARY = auto()
    ATOM = auto()
    ERROR = auto()


@dataclass
class Node:
    kind: NodeType
    children: list[Node]
    token: Token
    data: Any

    def pretty(
        self, code: str, line_starts: list, indent: int = 0, current: int = 0
    ) -> str:
        pad = " " * current

        line = f"{pad}{self.kind.name}"

        if self.data is not None:
            line += f"{pad}data={self.data}"

        if self.token is not None:
            start_line, start_col = index_to_line_col_batch(
                self.token.start, line_starts
            )
            line += f" @ {self.token.type.name} @ '{code[self.token.start : self.token.end]}' @ {start_line}:{start_col}"

        lines = [line]

        for child in self.children:
            lines.append(child.pretty(code, line_starts, indent, current + indent))

        return "\n".join(lines)

    def errors(self, code: str, line_starts: list) -> str:
        line = ""
        if self.data is not None and self.kind is NodeType.ERROR:
            start_line, start_col = index_to_line_col_batch(
                self.token.start, line_starts
            )
            line += f"{self.kind.name}: {self.data} @ {start_line}:{start_col}\n"
        lines = [line]
        for child in self.children:
            lines.append(child.errors(code, line_starts))
        return "".join(lines)
