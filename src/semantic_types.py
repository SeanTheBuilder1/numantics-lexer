from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum, auto
from lexer_token import Token, TokenType


class BuiltInTypes(Enum):
    VOID_TYPE = 1
    INT_TYPE = auto()
    FLOAT_TYPE = auto()
    BOOL_TYPE = auto()
    CHAR_TYPE = auto()
    STRING_TYPE = auto()


class ModifierTypes(Enum):
    PERCENT_TYPE = 1  # PERCENT
    XPERCENT_TYPE = auto()  # PERCENT
    POSITIVE_TYPE = auto()  # SIGN
    NEGATIVE_TYPE = auto()  # SIGN
    NONZERO_TYPE = auto()  # NONZERO
    EVEN_TYPE = auto()  # PARITY
    ODD_TYPE = auto()  # PARITY
    AUTO_TYPE = auto()  # AUTO
    SECOND_TYPE = auto()  # TIME
    MINUTE_TYPE = auto()  # TIME
    HOUR_TYPE = auto()  # TIME
    DAY_TYPE = auto()  # TIME
    WEEK_TYPE = auto()  # TIME
    MONTH_TYPE = auto()  # TIME
    YEAR_TYPE = auto()  # TIME
    METER_TYPE = auto()  # DISTANCE
    MM_TYPE = auto()  # DISTANCE
    CM_TYPE = auto()  # DISTANCE
    KM_TYPE = auto()  # DISTANCE
    FT_TYPE = auto()  # DISTANCE
    INCH_TYPE = auto()  # DISTANCE
    LITER_TYPE = auto()  # VOLUME
    ML_TYPE = auto()  # VOLUME
    CL_TYPE = auto()  # VOLUME
    KL_TYPE = auto()  # VOLUME
    GRAM_TYPE = auto()  # MASS
    MG_TYPE = auto()  # MASS
    CG_TYPE = auto()  # MASS
    KG_TYPE = auto()  # MASS
    CELC_TYPE = auto()  # TEMP
    FAHR_TYPE = auto()  # TEMP
    KELV_TYPE = auto()  # TEMP
    NEWT_TYPE = auto()  # FORCE
    KGF_TYPE = auto()  # FORCE
    LBF_TYPE = auto()  # FORCE
    MPS_TYPE = auto()  # VELOCITY
    FPS_TYPE = auto()  # VELOCITY
    MPS2_TYPE = auto()  # ACCELERATION


@dataclass
class Type:
    builtin: BuiltInTypes
    modifiers: list[ModifierTypes] = field(default_factory=list)


@dataclass
class Parameter:
    type: Type
    name: str


@dataclass
class Function:
    return_type: Type
    parameters: list[Parameter]


@dataclass
class Scope:
    symbols: dict[str, Symbol] = field(default_factory=dict)
    parent_scope: Scope | None = None
    children: list[Scope] = field(default_factory=list)


@dataclass
class Symbol:
    name: str
    type: Type | Function
    scope: Scope | None


def mapTokenToBuiltInType(token: Token) -> BuiltInTypes | None:
    if token.type == TokenType.VOID_TYPE:
        return BuiltInTypes.VOID_TYPE
    if token.type == TokenType.INT_TYPE:
        return BuiltInTypes.INT_TYPE
    if token.type == TokenType.FLOAT_TYPE:
        return BuiltInTypes.FLOAT_TYPE
    if token.type == TokenType.BOOL_TYPE:
        return BuiltInTypes.BOOL_TYPE
    if token.type == TokenType.CHAR_TYPE:
        return BuiltInTypes.CHAR_TYPE
    if token.type == TokenType.STRING_TYPE:
        return BuiltInTypes.STRING_TYPE
    return None


def mapTokenToModifierType(token: Token) -> ModifierTypes | None:
    if token.type == TokenType.PERCENT_TYPE:
        return ModifierTypes.PERCENT_TYPE
    if token.type == TokenType.XPERCENT_TYPE:
        return ModifierTypes.XPERCENT_TYPE
    if token.type == TokenType.POSITIVE_TYPE:
        return ModifierTypes.POSITIVE_TYPE
    if token.type == TokenType.NEGATIVE_TYPE:
        return ModifierTypes.NEGATIVE_TYPE
    if token.type == TokenType.NONZERO_TYPE:
        return ModifierTypes.NONZERO_TYPE
    if token.type == TokenType.EVEN_TYPE:
        return ModifierTypes.EVEN_TYPE
    if token.type == TokenType.ODD_TYPE:
        return ModifierTypes.ODD_TYPE
    if token.type == TokenType.AUTO_TYPE:
        return ModifierTypes.AUTO_TYPE
    if token.type == TokenType.SECOND_TYPE:
        return ModifierTypes.SECOND_TYPE
    if token.type == TokenType.MINUTE_TYPE:
        return ModifierTypes.MINUTE_TYPE
    if token.type == TokenType.HOUR_TYPE:
        return ModifierTypes.HOUR_TYPE
    if token.type == TokenType.DAY_TYPE:
        return ModifierTypes.DAY_TYPE
    if token.type == TokenType.WEEK_TYPE:
        return ModifierTypes.WEEK_TYPE
    if token.type == TokenType.MONTH_TYPE:
        return ModifierTypes.MONTH_TYPE
    if token.type == TokenType.YEAR_TYPE:
        return ModifierTypes.YEAR_TYPE
    if token.type == TokenType.METER_TYPE:
        return ModifierTypes.METER_TYPE
    if token.type == TokenType.MM_TYPE:
        return ModifierTypes.MM_TYPE
    if token.type == TokenType.CM_TYPE:
        return ModifierTypes.CM_TYPE
    if token.type == TokenType.KM_TYPE:
        return ModifierTypes.KM_TYPE
    if token.type == TokenType.FT_TYPE:
        return ModifierTypes.FT_TYPE
    if token.type == TokenType.INCH_TYPE:
        return ModifierTypes.INCH_TYPE
    if token.type == TokenType.LITER_TYPE:
        return ModifierTypes.LITER_TYPE
    if token.type == TokenType.ML_TYPE:
        return ModifierTypes.ML_TYPE
    if token.type == TokenType.CL_TYPE:
        return ModifierTypes.CL_TYPE
    if token.type == TokenType.KL_TYPE:
        return ModifierTypes.KL_TYPE
    if token.type == TokenType.GRAM_TYPE:
        return ModifierTypes.GRAM_TYPE
    if token.type == TokenType.MG_TYPE:
        return ModifierTypes.MG_TYPE
    if token.type == TokenType.CG_TYPE:
        return ModifierTypes.CG_TYPE
    if token.type == TokenType.KG_TYPE:
        return ModifierTypes.KG_TYPE
    if token.type == TokenType.CELC_TYPE:
        return ModifierTypes.CELC_TYPE
    if token.type == TokenType.FAHR_TYPE:
        return ModifierTypes.FAHR_TYPE
    if token.type == TokenType.KELV_TYPE:
        return ModifierTypes.KELV_TYPE
    if token.type == TokenType.NEWT_TYPE:
        return ModifierTypes.NEWT_TYPE
    if token.type == TokenType.KGF_TYPE:
        return ModifierTypes.KGF_TYPE
    if token.type == TokenType.LBF_TYPE:
        return ModifierTypes.LBF_TYPE
    if token.type == TokenType.MPS_TYPE:
        return ModifierTypes.MPS_TYPE
    if token.type == TokenType.FPS_TYPE:
        return ModifierTypes.FPS_TYPE
    if token.type == TokenType.MPS2_TYPE:
        return ModifierTypes.MPS2_TYPE
    return None
