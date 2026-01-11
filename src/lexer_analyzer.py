from lexer_token import TokenType, Token
import lexer_recognizers as recognizers
from lexer_types import LexerTokenTypeAcceptState, LexerTokenTypeState


initial_lexer: list[LexerTokenTypeState] = []


def getFreshLexer():
    initial_lexer = []
    for x in range(len(TokenType) - 1):  # exclude INVALID
        initial_lexer.append(
            LexerTokenTypeState(LexerTokenTypeAcceptState.IN_PROGRESS, -1)
        )
    return initial_lexer


recognizer_list = []


for x in range(len(TokenType) - 1):  # exclude INVALID
    recognizer_list.append(recognizers.placeholderRecognizer)


recognizer_list[TokenType.IDENTIFIER.value] = recognizers.identifierRecognizer
recognizer_list[TokenType.WHITESPACE.value] = recognizers.whitespaceRecognizer
recognizer_list[TokenType.COMMENT.value] = recognizers.commentRecognizer
recognizer_list[TokenType.ARITHMETIC_OP.value] = recognizers.arithmeticOpRecognizer
recognizer_list[TokenType.UNARY_OP.value] = recognizers.unaryOpRecognizer
recognizer_list[TokenType.RELATIONAL_OP.value] = recognizers.relationalOpRecognizer
recognizer_list[TokenType.LOGICAL_OP.value] = recognizers.logicalOpRecognizer
recognizer_list[TokenType.ASSIGMENT_OP.value] = recognizers.assignmentOpRecognizer
recognizer_list[TokenType.NUMANTICS_OP.value] = recognizers.numanticsOpRecognizer
recognizer_list[TokenType.INT_TYPE.value] = recognizers.intTypeRecognizer
recognizer_list[TokenType.FLOAT_TYPE.value] = recognizers.floatTypeRecognizer
recognizer_list[TokenType.BOOL_TYPE.value] = recognizers.boolTypeRecognizer
recognizer_list[TokenType.CHAR_TYPE.value] = recognizers.charTypeRecognizer
recognizer_list[TokenType.STRING_TYPE.value] = recognizers.strTypeRecognizer
recognizer_list[TokenType.IF_STATEMENT.value] = recognizers.ifStatementRecognizer
recognizer_list[TokenType.ELSE_STATEMENT.value] = recognizers.elseStatementRecognizer
recognizer_list[TokenType.ELIF_STATEMENT.value] = recognizers.elifStatementRecognizer
recognizer_list[TokenType.FOR_LOOP.value] = recognizers.forLoopRecognizer
recognizer_list[TokenType.WHILE_LOOP.value] = recognizers.whileLoopRecognizer
recognizer_list[TokenType.SCAN_FUNCTION.value] = recognizers.scanFunctionRecognizer
recognizer_list[TokenType.PRINT_FUNCTION.value] = recognizers.printFunctionRecognizer
recognizer_list[TokenType.NEXT_STATEMENT.value] = recognizers.nextStatementRecognizer
recognizer_list[TokenType.STOP_STATEMENT.value] = recognizers.stopStatementRecognizer
recognizer_list[TokenType.RETURN_STATEMENT.value] = (
    recognizers.returnStatementRecognizer
)
recognizer_list[TokenType.FUNC_STATEMENT.value] = recognizers.funcStatementRecognizer
recognizer_list[TokenType.CONST_STATEMENT.value] = recognizers.constStatementRecognizer
recognizer_list[TokenType.STATIC_STATEMENT.value] = (
    recognizers.staticStatementRecognizer
)
recognizer_list[TokenType.DEFAULT_STATEMENT.value] = (
    recognizers.defaultStatementRecognizer
)
recognizer_list[TokenType.CASE_STATEMENT.value] = recognizers.caseStatementRecognizer
recognizer_list[TokenType.TRUE_LITERAL.value] = recognizers.trueStatementRecognizer
recognizer_list[TokenType.FALSE_LITERAL.value] = recognizers.falseStatementRecognizer
recognizer_list[TokenType.SWEEP_STATEMENT.value] = recognizers.sweepStatementRecognizer
recognizer_list[TokenType.RANGE_STATEMENT.value] = recognizers.rangeStatementRecognizer
recognizer_list[TokenType.JUMP_STATEMENT.value] = recognizers.jumpStatementRecognizer
recognizer_list[TokenType.SWITCH_STATEMENT.value] = (
    recognizers.switchStatementRecognizer
)
recognizer_list[TokenType.INT_LITERAL.value] = recognizers.intLiteralRecognizer
recognizer_list[TokenType.FLOAT_LITERAL.value] = recognizers.floatLiteralRecognizer
recognizer_list[TokenType.CHAR_LITERAL.value] = recognizers.charLiteralRecognizer
recognizer_list[TokenType.STRING_LITERAL.value] = recognizers.stringLiteralRecognizer
recognizer_list[TokenType.PERCENT_TYPE.value] = recognizers.percentTypeRecognizer
recognizer_list[TokenType.XPERCENT_TYPE.value] = recognizers.xpercentTypeRecognizer
recognizer_list[TokenType.POSITIVE_TYPE.value] = recognizers.positiveTypeRecognizer
recognizer_list[TokenType.NEGATIVE_TYPE.value] = recognizers.negativeTypeRecognizer
recognizer_list[TokenType.NONZERO_TYPE.value] = recognizers.nonzeroTypeRecognizer
recognizer_list[TokenType.EVEN_TYPE.value] = recognizers.evenTypeRecognizer
recognizer_list[TokenType.ODD_TYPE.value] = recognizers.oddTypeRecognizer
recognizer_list[TokenType.AUTO_TYPE.value] = recognizers.autoTypeRecognizer
recognizer_list[TokenType.TIME_TYPE.value] = recognizers.placeholderRecognizer
recognizer_list[TokenType.LENGTH_TYPE.value] = recognizers.placeholderRecognizer
recognizer_list[TokenType.VOLUME_TYPE.value] = recognizers.placeholderRecognizer
recognizer_list[TokenType.MASS_TYPE.value] = recognizers.placeholderRecognizer
recognizer_list[TokenType.TEMP_TYPE.value] = recognizers.placeholderRecognizer
recognizer_list[TokenType.FORCE_TYPE.value] = recognizers.placeholderRecognizer
recognizer_list[TokenType.COMPOUNT_UNIT_TYPE.value] = recognizers.placeholderRecognizer


def analyzeSource(code: str):
    tokens: list[Token] = []
    start_index = 0
    current_state = getFreshLexer()

    index = 0
    while index < len(code):
        valid_states: list[TokenType] = []
        for state_index in range(len(current_state)):
            type = TokenType(state_index)
            state = current_state[state_index]

            if state.acceptance == LexerTokenTypeAcceptState.REJECTED:
                continue
            state = recognizer_list[type.value](state, code[index])
            # print(state, type)

            if state.acceptance == LexerTokenTypeAcceptState.ACCEPTED:
                state.end_at = index
            if state.acceptance != LexerTokenTypeAcceptState.REJECTED:
                valid_states.append(type)
            current_state[state_index] = state
        # print()
        # print(index)
        # print(valid_states)
        # print(tokens)
        if valid_states:
            index += 1
            continue

        longest = -1
        longest_type = TokenType.INVALID
        for state_index in range(len(current_state)):
            type = TokenType(state_index)
            state = current_state[state_index]
            if state.end_at == -1:
                continue
            if state.end_at > longest or (
                state.end_at == longest and type.value > longest_type.value
            ):
                longest = state.end_at
                longest_type = type
        if longest == -1 or longest_type == TokenType.INVALID:
            tokens.append(Token(longest_type, start_index, index))
            start_index = index + 1
            index = start_index
            current_state = getFreshLexer()
            continue
        tokens.append(
            Token(longest_type, start_index, current_state[longest_type.value].end_at)
        )
        start_index = current_state[longest_type.value].end_at + 1
        index = start_index
        current_state = getFreshLexer()

    return tokens
