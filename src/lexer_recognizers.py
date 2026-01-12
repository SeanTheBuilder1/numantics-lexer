from lexer_types import LexerTokenTypeState, LexerTokenTypeAcceptState


def placeholderRecognizer(state: LexerTokenTypeState, character: str):
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def identifierRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character.isalpha() or character == "_":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character.isalnum() or character == "_":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def whitespaceRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character.isspace():
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character.isspace():
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def commentRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "/":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state

    if state.current_state == "q1":
        if character == "/":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        elif character == "*":
            state.current_state = "q3"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state

    if state.current_state == "q2":
        if character != "\n":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state

    if state.current_state == "q3":
        if character == "*":
            state.current_state = "q4"
        else:
            state.current_state = "q3"
        state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        return state

    if state.current_state == "q4":
        if character == "/":
            state.current_state = "q5"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        elif character == "*":
            state.current_state = "q4"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.current_state = "q3"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        return state

    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def arithmeticOpRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character in ["^", "*", "/", "%", "+", "-"]:
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state

    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def unaryOpRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "+":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        elif character == "-":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "+":
            state.current_state = "q3"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q2":
        if character == "-":
            state.current_state = "q3"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state

    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def relationalOpRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "=":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        elif character == "!":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        elif character == "<":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        elif character == ">":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "=":
            state.current_state = "q3"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q2":
        if character == "=":
            state.current_state = "q3"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def logicalOpRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "!":
            state.current_state = "q3"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        elif character == "&":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        elif character == "|":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "&":
            state.current_state = "q3"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q2":
        if character == "|":
            state.current_state = "q3"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def assignmentOpRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "=":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        elif character == "+":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        elif character == "-":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        elif character == "*":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        elif character == "/":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        elif character == "%":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "=":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def numanticsOpRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "*":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        elif character == "+":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        elif character == "-":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "%":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def intTypeRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "i":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "n":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q2":
        if character == "t":
            state.current_state = "q3"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q3":
        if character == "e":
            state.current_state = "q4"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q4":
        if character == "g":
            state.current_state = "q5"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q5":
        if character == "e":
            state.current_state = "q6"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q6":
        if character == "r":
            state.current_state = "q7"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def floatTypeRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "f":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "l":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q2":
        if character == "o":
            state.current_state = "q3"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q3":
        if character == "a":
            state.current_state = "q4"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q4":
        if character == "t":
            state.current_state = "q5"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def boolTypeRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "b":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "o":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q2":
        if character == "o":
            state.current_state = "q3"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q3":
        if character == "l":
            state.current_state = "q4"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q4":
        if character == "e":
            state.current_state = "q5"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q5":
        if character == "a":
            state.current_state = "q6"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q6":
        if character == "n":
            state.current_state = "q7"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def charTypeRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "c":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "h":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q2":
        if character == "a":
            state.current_state = "q3"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q3":
        if character == "r":
            state.current_state = "q4"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q4":
        if character == "a":
            state.current_state = "q5"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q5":
        if character == "c":
            state.current_state = "q6"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q6":
        if character == "t":
            state.current_state = "q7"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q7":
        if character == "e":
            state.current_state = "q8"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q8":
        if character == "r":
            state.current_state = "q9"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def strTypeRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "s":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "t":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q2":
        if character == "r":
            state.current_state = "q3"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q3":
        if character == "i":
            state.current_state = "q4"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q4":
        if character == "n":
            state.current_state = "q5"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q5":
        if character == "g":
            state.current_state = "q6"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state

    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def ifStatementRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "i":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "f":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def elseStatementRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "e":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "l":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q2":
        if character == "s":
            state.current_state = "q3"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q3":
        if character == "e":
            state.current_state = "q4"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def elifStatementRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "e":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "l":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q2":
        if character == "i":
            state.current_state = "q3"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q3":
        if character == "f":
            state.current_state = "q4"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def forLoopRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "f":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "o":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q2":
        if character == "r":
            state.current_state = "q3"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def whileLoopRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "w":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "h":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q2":
        if character == "i":
            state.current_state = "q3"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q3":
        if character == "l":
            state.current_state = "q4"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q4":
        if character == "e":
            state.current_state = "q5"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def scanFunctionRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "s":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "c":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q2":
        if character == "a":
            state.current_state = "q3"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q3":
        if character == "n":
            state.current_state = "q4"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def printFunctionRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "p":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "r":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q2":
        if character == "i":
            state.current_state = "q3"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q3":
        if character == "n":
            state.current_state = "q4"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q4":
        if character == "t":
            state.current_state = "q5"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def nextStatementRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "n":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "e":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q2":
        if character == "x":
            state.current_state = "q3"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q3":
        if character == "t":
            state.current_state = "q4"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def stopStatementRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "s":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "t":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q2":
        if character == "o":
            state.current_state = "q3"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q3":
        if character == "p":
            state.current_state = "q4"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def returnStatementRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "r":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "e":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q2":
        if character == "t":
            state.current_state = "q3"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q3":
        if character == "u":
            state.current_state = "q4"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q4":
        if character == "r":
            state.current_state = "q5"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q5":
        if character == "n":
            state.current_state = "q6"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def funcStatementRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "f":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "u":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q2":
        if character == "n":
            state.current_state = "q3"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q3":
        if character == "c":
            state.current_state = "q4"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q4":
        if character == "t":
            state.current_state = "q5"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q5":
        if character == "i":
            state.current_state = "q6"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q6":
        if character == "o":
            state.current_state = "q7"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q7":
        if character == "n":
            state.current_state = "q8"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def constStatementRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "c":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "o":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q2":
        if character == "n":
            state.current_state = "q3"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q3":
        if character == "s":
            state.current_state = "q4"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q4":
        if character == "t":
            state.current_state = "q5"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q5":
        if character == "a":
            state.current_state = "q6"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q6":
        if character == "n":
            state.current_state = "q7"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q7":
        if character == "t":
            state.current_state = "q8"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def staticStatementRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "s":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "t":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q2":
        if character == "a":
            state.current_state = "q3"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q3":
        if character == "t":
            state.current_state = "q4"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q4":
        if character == "i":
            state.current_state = "q5"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q5":
        if character == "c":
            state.current_state = "q6"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def defaultStatementRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "d":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "e":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q2":
        if character == "f":
            state.current_state = "q3"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q3":
        if character == "a":
            state.current_state = "q4"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q4":
        if character == "u":
            state.current_state = "q5"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q5":
        if character == "l":
            state.current_state = "q6"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q6":
        if character == "t":
            state.current_state = "q7"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def caseStatementRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "c":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "a":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q2":
        if character == "s":
            state.current_state = "q3"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q3":
        if character == "e":
            state.current_state = "q4"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def trueStatementRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "t":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "r":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q2":
        if character == "u":
            state.current_state = "q3"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q3":
        if character == "e":
            state.current_state = "q4"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def falseStatementRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "f":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "a":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q2":
        if character == "l":
            state.current_state = "q3"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q3":
        if character == "s":
            state.current_state = "q4"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q4":
        if character == "e":
            state.current_state = "q5"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def sweepStatementRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "s":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "w":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q2":
        if character == "e":
            state.current_state = "q3"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q3":
        if character == "e":
            state.current_state = "q4"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q4":
        if character == "p":
            state.current_state = "q5"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def rangeStatementRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "r":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "a":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q2":
        if character == "n":
            state.current_state = "q3"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q3":
        if character == "g":
            state.current_state = "q4"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q4":
        if character == "e":
            state.current_state = "q5"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def jumpStatementRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "j":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "u":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q2":
        if character == "m":
            state.current_state = "q3"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q3":
        if character == "p":
            state.current_state = "q4"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def switchStatementRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "s":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "w":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q2":
        if character == "i":
            state.current_state = "q3"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q3":
        if character == "t":
            state.current_state = "q4"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q4":
        if character == "c":
            state.current_state = "q5"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q5":
        if character == "h":
            state.current_state = "q6"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def intLiteralRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "0":
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        elif character.isdigit() and character != "0":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q2":
        if character.isdigit():
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def floatLiteralRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character.isdigit():
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        elif character == ".":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character.isdigit():
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        elif character == ".":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q2":
        if character.isdigit():
            state.current_state = "q3"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q3":
        if character.isdigit():
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state

    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def charLiteralRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "'":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "\\":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        elif character != "'" and character != "\n":
            state.current_state = "q3"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q2":
        if character != "\n":
            state.current_state = "q3"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q3":
        if character == "'":
            state.current_state = "q4"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state

    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def stringLiteralRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == '"':
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "\\":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        elif character == '"':
            state.current_state = "q3"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        elif character != "\n":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q2":
        if character != "\n":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def percentTypeRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "p":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "e":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q2":
        if character == "r":
            state.current_state = "q3"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q3":
        if character == "c":
            state.current_state = "q4"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q4":
        if character == "e":
            state.current_state = "q5"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q5":
        if character == "n":
            state.current_state = "q6"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q6":
        if character == "t":
            state.current_state = "q7"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def xpercentTypeRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "x":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "p":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q2":
        if character == "e":
            state.current_state = "q3"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q3":
        if character == "r":
            state.current_state = "q4"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q4":
        if character == "c":
            state.current_state = "q5"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q5":
        if character == "e":
            state.current_state = "q6"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q6":
        if character == "n":
            state.current_state = "q7"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q7":
        if character == "t":
            state.current_state = "q8"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def positiveTypeRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "p":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "o":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q2":
        if character == "s":
            state.current_state = "q3"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q3":
        if character == "i":
            state.current_state = "q4"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q4":
        if character == "t":
            state.current_state = "q5"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q5":
        if character == "i":
            state.current_state = "q6"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q6":
        if character == "v":
            state.current_state = "q7"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q7":
        if character == "e":
            state.current_state = "q8"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def negativeTypeRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "n":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "e":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q2":
        if character == "g":
            state.current_state = "q3"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q3":
        if character == "a":
            state.current_state = "q4"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q4":
        if character == "t":
            state.current_state = "q5"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q5":
        if character == "i":
            state.current_state = "q6"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q6":
        if character == "v":
            state.current_state = "q7"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q7":
        if character == "e":
            state.current_state = "q8"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def nonzeroTypeRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "n":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "o":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q2":
        if character == "n":
            state.current_state = "q3"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q3":
        if character == "z":
            state.current_state = "q4"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q4":
        if character == "e":
            state.current_state = "q5"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q5":
        if character == "r":
            state.current_state = "q6"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q6":
        if character == "o":
            state.current_state = "q7"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def evenTypeRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "e":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "v":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q2":
        if character == "e":
            state.current_state = "q3"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q3":
        if character == "n":
            state.current_state = "q4"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def oddTypeRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "o":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "d":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q2":
        if character == "d":
            state.current_state = "q3"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def autoTypeRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "a":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "u":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q2":
        if character == "t":
            state.current_state = "q3"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q3":
        if character == "o":
            state.current_state = "q4"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q4":
        if character == "m":
            state.current_state = "q5"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q5":
        if character == "a":
            state.current_state = "q6"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q6":
        if character == "t":
            state.current_state = "q7"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q7":
        if character == "i":
            state.current_state = "q8"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q8":
        if character == "c":
            state.current_state = "q9"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def secondTypeRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "s":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "e":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q2":
        if character == "c":
            state.current_state = "q3"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q3":
        if character == "o":
            state.current_state = "q4"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q4":
        if character == "n":
            state.current_state = "q5"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q5":
        if character == "d":
            state.current_state = "q6"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def minuteTypeRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "m":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "i":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q2":
        if character == "n":
            state.current_state = "q3"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q3":
        if character == "u":
            state.current_state = "q4"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q4":
        if character == "t":
            state.current_state = "q5"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q5":
        if character == "e":
            state.current_state = "q6"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def hourTypeRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "h":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "o":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q2":
        if character == "u":
            state.current_state = "q3"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q3":
        if character == "r":
            state.current_state = "q4"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def dayTypeRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "d":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "a":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q2":
        if character == "y":
            state.current_state = "q3"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def weekTypeRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "w":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "e":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q2":
        if character == "e":
            state.current_state = "q3"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q3":
        if character == "k":
            state.current_state = "q4"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def monthTypeRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "m":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "o":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q2":
        if character == "n":
            state.current_state = "q3"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q3":
        if character == "t":
            state.current_state = "q4"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q4":
        if character == "h":
            state.current_state = "q5"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def yearTypeRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "y":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "e":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q2":
        if character == "a":
            state.current_state = "q3"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q3":
        if character == "r":
            state.current_state = "q4"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def meterTypeRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "m":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "e":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q2":
        if character == "t":
            state.current_state = "q3"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q3":
        if character == "e":
            state.current_state = "q4"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q4":
        if character == "r":
            state.current_state = "q5"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def mmTypeRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "m":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "m":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def cmTypeRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "c":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "m":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def kmTypeRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "k":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "m":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def ftTypeRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "f":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "t":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def inchTypeRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "i":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "n":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q2":
        if character == "c":
            state.current_state = "q3"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q3":
        if character == "h":
            state.current_state = "q4"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def literTypeRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "l":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "i":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q2":
        if character == "t":
            state.current_state = "q3"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q3":
        if character == "e":
            state.current_state = "q4"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q4":
        if character == "r":
            state.current_state = "q5"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def mlTypeRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "m":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "l":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def clTypeRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "c":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "l":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def klTypeRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "k":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "l":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def gramTypeRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "g":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "r":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q2":
        if character == "a":
            state.current_state = "q3"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q3":
        if character == "m":
            state.current_state = "q4"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def mgTypeRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "m":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "g":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def cgTypeRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "c":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "g":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def kgTypeRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "k":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "g":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def celcTypeRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "c":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "e":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q2":
        if character == "l":
            state.current_state = "q3"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q3":
        if character == "c":
            state.current_state = "q4"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def fahrTypeRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "f":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "a":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q2":
        if character == "h":
            state.current_state = "q3"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q3":
        if character == "r":
            state.current_state = "q4"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def kelvTypeRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "k":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "e":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q2":
        if character == "l":
            state.current_state = "q3"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q3":
        if character == "v":
            state.current_state = "q4"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def newtTypeRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "n":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "e":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q2":
        if character == "w":
            state.current_state = "q3"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q3":
        if character == "t":
            state.current_state = "q4"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def kgfTypeRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "k":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "g":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q2":
        if character == "f":
            state.current_state = "q3"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def lbfTypeRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "l":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "b":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q2":
        if character == "f":
            state.current_state = "q3"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def mpsTypeRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "m":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "p":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q2":
        if character == "s":
            state.current_state = "q3"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def fpsTypeRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "f":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "p":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q2":
        if character == "s":
            state.current_state = "q3"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def mps2TypeRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "m":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q1":
        if character == "p":
            state.current_state = "q2"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q2":
        if character == "s":
            state.current_state = "q3"
            state.acceptance = LexerTokenTypeAcceptState.IN_PROGRESS
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    if state.current_state == "q3":
        if character == "2":
            state.current_state = "q4"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def commaDelimiterRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == ",":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def semiColonDelimiterRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == ";":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def colonDelimiterRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == ":":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def openParenthesisDelimiterRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "(":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def closedParenthesisDelimiterRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == ")":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def openSquareDelimiterRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "[":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def closedSquareDelimiterRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "]":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def openAngleDelimiterRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "<":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def closedAngleDelimiterRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == ">":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def hyphenDelimiterRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "-":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state


def verticalBarDelimiterRecognizer(state: LexerTokenTypeState, character: str):
    if state.current_state == "q0":
        if character == "|":
            state.current_state = "q1"
            state.acceptance = LexerTokenTypeAcceptState.ACCEPTED
        else:
            state.acceptance = LexerTokenTypeAcceptState.REJECTED
        return state
    state.acceptance = LexerTokenTypeAcceptState.REJECTED
    return state
