from dataclasses import dataclass
from enum import Enum, auto
from typing import Any
from lexer_token import Token
from semantic_types import Scope, Symbol, Type


class ASTOperator(Enum):
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


class ASTLiteral(Enum):
    TRUE_LITERAL = 0
    FALSE_LITERAL = auto()
    INT_LITERAL = auto()
    FLOAT_LITERAL = auto()
    CHAR_LITERAL = auto()
    STRING_LITERAL = auto()


class ASTNodeType(Enum):
    IDENTIFIER = 0  # DONE
    FILE = auto()  # DONE
    DECLARATION = auto()  # DONE
    LITERAL = auto()
    IF_STMT = auto()
    SWITCH_STMT = auto()
    SWEEP_STMT = auto()
    WHILE_STMT = auto()
    FUNCTION_STMT = auto()  # DONE
    FOR_STMT = auto()
    BLOCK = auto()
    NEXT_STMT = auto()
    STOP_STMT = auto()
    RETURN_STMT = auto()
    FUNCTION_CALL = auto()
    ARRAY_INDEX = auto()
    BINARY_OP = auto()
    UNARY_OP = auto()


@dataclass
class ASTNode:
    kind: ASTNodeType
    token: Token
    data: Any
    scope: Scope | None = None

@dataclass
class IdentifierData:
    symbol: Symbol | None = None


@dataclass
class FileData:
    children: list[ASTNode]


@dataclass
class DeclarationData:
    type: Type
    name: ASTNode
    expression: ASTNode | None


@dataclass
class LiteralData:
    literal_type: ASTLiteral


@dataclass
class IfStmtData:
    expr: ASTNode
    block: ASTNode
    elif_stmts: list[tuple[ASTNode, ASTNode]]
    else_stmt: ASTNode | None


@dataclass
class SwitchStmtData:
    expr: ASTNode
    case_stmts: list[tuple[ASTNode, ASTNode]]
    default_stmt: ASTNode | None


@dataclass
class SweepStmtData:
    expr: ASTNode
    case_stmts: list[tuple[ASTNode, ASTNode]]
    default_stmt: ASTNode | None


@dataclass
class WhileStmtData:
    left_expr: ASTNode
    right_expr: ASTNode | None
    block: ASTNode


@dataclass
class FunctionStmtData:
    name: ASTNode
    parameters: list[tuple[Type, ASTNode]]
    return_type: Type
    block: ASTNode


@dataclass
class ForStmtData:
    init: ASTNode | None
    condition: ASTNode | None
    update: ASTNode | None
    block: ASTNode


@dataclass
class BlockData:
    statements: list[ASTNode]


@dataclass
class NextStmtData:
    target: ASTNode | None = None


@dataclass
class StopStmtData:
    target: ASTNode | None = None


@dataclass
class ReturnStmtData:
    expression: ASTNode | None
    target: ASTNode | None = None


@dataclass
class FunctionCallData:
    function: ASTNode
    arguments: list[ASTNode]


@dataclass
class ArrayIndexData:
    array: ASTNode
    index: ASTNode


@dataclass
class BinaryOpData:
    lhs: ASTNode
    rhs: ASTNode
    operator: ASTOperator


@dataclass
class UnaryOpData:
    operand: ASTNode
    operator: ASTOperator
