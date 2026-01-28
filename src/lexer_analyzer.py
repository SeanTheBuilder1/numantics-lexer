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
recognizer_list[TokenType.NEWLINE.value] = recognizers.newlineRecognizer
recognizer_list[TokenType.COMMENT.value] = recognizers.commentRecognizer
recognizer_list[TokenType.PLUS_SYMBOL.value] = recognizers.plusSymbolRecognizer
recognizer_list[TokenType.MINUS_SYMBOL.value] = recognizers.minusSymbolRecognizer
recognizer_list[TokenType.STAR_SYMBOL.value] = recognizers.starSymbolRecognizer
recognizer_list[TokenType.SLASH_SYMBOL.value] = recognizers.slashSymbolRecognizer
recognizer_list[TokenType.PERCENT_SYMBOL.value] = recognizers.percentSymbolRecognizer
recognizer_list[TokenType.CARET_SYMBOL.value] = recognizers.caretSymbolRecognizer
recognizer_list[TokenType.INCREMENT_OP.value] = recognizers.incrementOpRecognizer
recognizer_list[TokenType.DECREMENT_OP.value] = recognizers.decrementOpRecognizer
recognizer_list[TokenType.LESS_OP.value] = recognizers.lessOpRecognizer
recognizer_list[TokenType.LESS_OR_EQUAL_OP.value] = recognizers.lessOrEqualOpRecognizer
recognizer_list[TokenType.GREATER_OP.value] = recognizers.greaterOpRecognizer
recognizer_list[TokenType.GREATER_OR_EQUAL_OP.value] = (
    recognizers.greaterOrEqualOpRecognizer
)
recognizer_list[TokenType.NOT_EQUAL_OP.value] = recognizers.notEqualOpRecognizer
recognizer_list[TokenType.EQUAL_OP.value] = recognizers.equalOpRecognizer
recognizer_list[TokenType.NOT_OP.value] = recognizers.notOpRecognizer
recognizer_list[TokenType.AND_OP.value] = recognizers.andOpRecognizer
recognizer_list[TokenType.OR_OP.value] = recognizers.orOpRecognizer
recognizer_list[TokenType.ASSIGNMENT_OP.value] = recognizers.assignmentOpRecognizer
recognizer_list[TokenType.PLUS_ASSIGNMENT_OP.value] = (
    recognizers.plusAssignmentOpRecognizer
)
recognizer_list[TokenType.MINUS_ASSIGNMENT_OP.value] = (
    recognizers.minusAssignmentOpRecognizer
)
recognizer_list[TokenType.MULTIPLY_ASSIGNMENT_OP.value] = (
    recognizers.multiplyAssignmentOpRecognizer
)
recognizer_list[TokenType.DIVIDE_ASSIGNMENT_OP.value] = (
    recognizers.divideAssignmentOpRecognizer
)
recognizer_list[TokenType.MODULO_ASSIGNMENT_OP.value] = (
    recognizers.moduloAssignmentOpRecognizer
)
recognizer_list[TokenType.PERCENT_SCALE_OP.value] = recognizers.percentScaleOpRecognizer
recognizer_list[TokenType.MARKUP_OP.value] = recognizers.markupOpRecognizer
recognizer_list[TokenType.MARKDOWN_OP.value] = recognizers.markdownOpRecognizer
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
recognizer_list[TokenType.SECOND_TYPE.value] = recognizers.secondTypeRecognizer
recognizer_list[TokenType.MINUTE_TYPE.value] = recognizers.minuteTypeRecognizer
recognizer_list[TokenType.HOUR_TYPE.value] = recognizers.hourTypeRecognizer
recognizer_list[TokenType.DAY_TYPE.value] = recognizers.dayTypeRecognizer
recognizer_list[TokenType.WEEK_TYPE.value] = recognizers.weekTypeRecognizer
recognizer_list[TokenType.MONTH_TYPE.value] = recognizers.monthTypeRecognizer
recognizer_list[TokenType.YEAR_TYPE.value] = recognizers.yearTypeRecognizer
recognizer_list[TokenType.METER_TYPE.value] = recognizers.meterTypeRecognizer
recognizer_list[TokenType.MM_TYPE.value] = recognizers.mmTypeRecognizer
recognizer_list[TokenType.CM_TYPE.value] = recognizers.cmTypeRecognizer
recognizer_list[TokenType.KM_TYPE.value] = recognizers.kmTypeRecognizer
recognizer_list[TokenType.FT_TYPE.value] = recognizers.ftTypeRecognizer
recognizer_list[TokenType.INCH_TYPE.value] = recognizers.inchTypeRecognizer
recognizer_list[TokenType.LITER_TYPE.value] = recognizers.literTypeRecognizer
recognizer_list[TokenType.ML_TYPE.value] = recognizers.mlTypeRecognizer
recognizer_list[TokenType.CL_TYPE.value] = recognizers.clTypeRecognizer
recognizer_list[TokenType.KL_TYPE.value] = recognizers.klTypeRecognizer
recognizer_list[TokenType.GRAM_TYPE.value] = recognizers.gramTypeRecognizer
recognizer_list[TokenType.MG_TYPE.value] = recognizers.mgTypeRecognizer
recognizer_list[TokenType.CG_TYPE.value] = recognizers.cgTypeRecognizer
recognizer_list[TokenType.KG_TYPE.value] = recognizers.kgTypeRecognizer
recognizer_list[TokenType.CELC_TYPE.value] = recognizers.celcTypeRecognizer
recognizer_list[TokenType.FAHR_TYPE.value] = recognizers.fahrTypeRecognizer
recognizer_list[TokenType.KELV_TYPE.value] = recognizers.kelvTypeRecognizer
recognizer_list[TokenType.NEWT_TYPE.value] = recognizers.newtTypeRecognizer
recognizer_list[TokenType.KGF_TYPE.value] = recognizers.kgfTypeRecognizer
recognizer_list[TokenType.LBF_TYPE.value] = recognizers.lbfTypeRecognizer
recognizer_list[TokenType.MPS_TYPE.value] = recognizers.mpsTypeRecognizer
recognizer_list[TokenType.FPS_TYPE.value] = recognizers.fpsTypeRecognizer
recognizer_list[TokenType.MPS2_TYPE.value] = recognizers.mps2TypeRecognizer
recognizer_list[TokenType.COMMA_DELIMITER.value] = recognizers.commaDelimiterRecognizer
recognizer_list[TokenType.SEMI_COLON_DELIMITER.value] = (
    recognizers.semiColonDelimiterRecognizer
)
recognizer_list[TokenType.COLON_DELIMITER.value] = recognizers.colonDelimiterRecognizer
recognizer_list[TokenType.OPEN_PARENTHESIS_DELIMITER.value] = (
    recognizers.openParenthesisDelimiterRecognizer
)
recognizer_list[TokenType.CLOSED_PARENTHESIS_DELIMITER.value] = (
    recognizers.closedParenthesisDelimiterRecognizer
)
recognizer_list[TokenType.OPEN_SQUARE_DELIMITER.value] = (
    recognizers.openSquareDelimiterRecognizer
)
recognizer_list[TokenType.CLOSED_SQUARE_DELIMITER.value] = (
    recognizers.closedSquareDelimiterRecognizer
)
recognizer_list[TokenType.OPEN_ANGLE_DELIMITER.value] = (
    recognizers.openAngleDelimiterRecognizer
)
recognizer_list[TokenType.CLOSED_ANGLE_DELIMITER.value] = (
    recognizers.closedAngleDelimiterRecognizer
)
recognizer_list[TokenType.OPEN_CURLY_DELIMITER.value] = (
    recognizers.openCurlyDelimiterRecognizer
)
recognizer_list[TokenType.CLOSED_CURLY_DELIMITER.value] = (
    recognizers.closedCurlyDelimiterRecognizer
)
recognizer_list[TokenType.VERTICAL_BAR_DELIMITER.value] = (
    recognizers.verticalBarDelimiterRecognizer
)
recognizer_list[TokenType.ENDMARKER.value] = recognizers.nullRecognizer


def analyzeSource(code: str):
    tokens: list[Token] = []
    start_index = 0
    current_state = getFreshLexer()

    def pickLongestState(current_state):
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
            return (None, TokenType.INVALID)
        else:
            return (longest, longest_type)

    index = 0

    while index < len(code):
        valid_states: list[TokenType] = []
        for state_index in range(len(current_state)):
            type = TokenType(state_index)
            state = current_state[state_index]

            if state.acceptance == LexerTokenTypeAcceptState.REJECTED:
                continue
            state = recognizer_list[type.value](state, code[index])

            if state.acceptance == LexerTokenTypeAcceptState.ACCEPTED:
                state.end_at = index + 1
            if state.acceptance != LexerTokenTypeAcceptState.REJECTED:
                valid_states.append(type)
            current_state[state_index] = state
        if valid_states:
            index += 1
            continue

        longest_end, longest_type = pickLongestState(current_state)
        if longest_end is None or longest_type == TokenType.INVALID:
            invalid_start = start_index if start_index == index else index
            tokens.append(Token(longest_type, invalid_start, invalid_start + 1))
            start_index = invalid_start + 1
            index = start_index
            current_state = getFreshLexer()
            continue
        tokens.append(Token(longest_type, start_index, longest_end))
        start_index = longest_end
        index = start_index
        current_state = getFreshLexer()

    # Potentially cut off state
    longest_end, longest_type = pickLongestState(current_state)
    if longest_end is None or longest_type == TokenType.INVALID:
        if start_index < len(code):
            tokens.append(Token(longest_type, start_index, len(code)))
    else:
        tokens.append(Token(longest_type, start_index, longest_end))

    tokens.append(Token(TokenType.ENDMARKER, len(code), len(code)))

    return tokens
