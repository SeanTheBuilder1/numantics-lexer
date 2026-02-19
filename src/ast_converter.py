from __future__ import annotations

from semantic_types import Type, mapTokenToBuiltInType, mapTokenToModifierType
from syntax_types import Node, NodeType
from ast_types import (
    ASTNode,
    ASTOperator,
    ASTNodeType,
    ASTLiteral,
    IdentifierData,
    FileData,
    DeclarationData,
    LiteralData,
    IfStmtData,
    SwitchStmtData,
    SweepStmtData,
    WhileStmtData,
    FunctionStmtData,
    ForStmtData,
    BlockData,
    NextStmtData,
    StopStmtData,
    ReturnStmtData,
    FunctionCallData,
    ArrayIndexData,
    BinaryOpData,
    UnaryOpData,
)


def mapNodeTypeToOperatorType(type: NodeType) -> ASTOperator | None:
    if type == NodeType.ADD_OPERATOR:
        return ASTOperator.ADD_OPERATOR
    elif type == NodeType.SUB_OPERATOR:
        return ASTOperator.SUB_OPERATOR
    elif type == NodeType.MULT_OPERATOR:
        return ASTOperator.MULT_OPERATOR
    elif type == NodeType.DIV_OPERATOR:
        return ASTOperator.DIV_OPERATOR
    elif type == NodeType.MOD_OPERATOR:
        return ASTOperator.MOD_OPERATOR
    elif type == NodeType.EXP_OPERATOR:
        return ASTOperator.EXP_OPERATOR
    elif type == NodeType.POSITIVE_OPERATOR:
        return ASTOperator.POSITIVE_OPERATOR
    elif type == NodeType.NEGATIVE_OPERATOR:
        return ASTOperator.NEGATIVE_OPERATOR
    elif type == NodeType.PRE_INCREMENT_OPERATOR:
        return ASTOperator.PRE_INCREMENT_OPERATOR
    elif type == NodeType.POST_INCREMENT_OPERATOR:
        return ASTOperator.POST_INCREMENT_OPERATOR
    elif type == NodeType.PRE_DECREMENT_OPERATOR:
        return ASTOperator.PRE_DECREMENT_OPERATOR
    elif type == NodeType.POST_DECREMENT_OPERATOR:
        return ASTOperator.POST_DECREMENT_OPERATOR
    elif type == NodeType.LESS_OPERATOR:
        return ASTOperator.LESS_OPERATOR
    elif type == NodeType.LESS_OR_EQUAL_OPERATOR:
        return ASTOperator.LESS_OR_EQUAL_OPERATOR
    elif type == NodeType.GREATER_OPERATOR:
        return ASTOperator.GREATER_OPERATOR
    elif type == NodeType.GREATER_OR_EQUAL_OPERATOR:
        return ASTOperator.GREATER_OR_EQUAL_OPERATOR
    elif type == NodeType.NOT_EQUAL_OPERATOR:
        return ASTOperator.NOT_EQUAL_OPERATOR
    elif type == NodeType.EQUAL_OPERATOR:
        return ASTOperator.EQUAL_OPERATOR
    elif type == NodeType.NOT_OPERATOR:
        return ASTOperator.NOT_OPERATOR
    elif type == NodeType.AND_OPERATOR:
        return ASTOperator.AND_OPERATOR
    elif type == NodeType.OR_OPERATOR:
        return ASTOperator.OR_OPERATOR
    elif type == NodeType.ASSIGNMENT_OPERATOR:
        return ASTOperator.ASSIGNMENT_OPERATOR
    elif type == NodeType.PLUS_ASSIGNMENT_OPERATOR:
        return ASTOperator.PLUS_ASSIGNMENT_OPERATOR
    elif type == NodeType.MINUS_ASSIGNMENT_OPERATOR:
        return ASTOperator.MINUS_ASSIGNMENT_OPERATOR
    elif type == NodeType.MULTIPLY_ASSIGNMENT_OPERATOR:
        return ASTOperator.MULTIPLY_ASSIGNMENT_OPERATOR
    elif type == NodeType.DIVIDE_ASSIGNMENT_OPERATOR:
        return ASTOperator.DIVIDE_ASSIGNMENT_OPERATOR
    elif type == NodeType.MODULO_ASSIGNMENT_OPERATOR:
        return ASTOperator.MODULO_ASSIGNMENT_OPERATOR
    elif type == NodeType.PERCENT_SCALE_OPERATOR:
        return ASTOperator.PERCENT_SCALE_OPERATOR
    elif type == NodeType.MARKUP_OPERATOR:
        return ASTOperator.MARKUP_OPERATOR
    elif type == NodeType.MARKDOWN_OPERATOR:
        return ASTOperator.MARKDOWN_OPERATOR
    return None


def mapNodeTypeToLiteralType(type: NodeType) -> ASTLiteral | None:
    if type == NodeType.TRUE_LITERAL:
        return ASTLiteral.TRUE_LITERAL
    elif type == NodeType.FALSE_LITERAL:
        return ASTLiteral.FALSE_LITERAL
    elif type == NodeType.INT_LITERAL:
        return ASTLiteral.INT_LITERAL
    elif type == NodeType.FLOAT_LITERAL:
        return ASTLiteral.FLOAT_LITERAL
    elif type == NodeType.CHAR_LITERAL:
        return ASTLiteral.CHAR_LITERAL
    elif type == NodeType.STRING_LITERAL:
        return ASTLiteral.STRING_LITERAL
    return None


def convertBlock(tree: Node) -> ASTNode:
    statements: list[ASTNode] = []
    for node in tree.children:
        statement = convertStatement(node)
        statements.append(statement)
    return ASTNode(
        kind=ASTNodeType.BLOCK, token=tree.token, data=BlockData(statements=statements)
    )


def convertParameterList(tree: Node) -> list[tuple[Type, ASTNode]]:
    index = 0
    types: list[tuple[Type, ASTNode]] = []
    assert len(tree.children) % 2 == 0
    while index + 1 < len(tree.children):
        type = convertType(tree.children[index])
        assert type
        name = convertIdentifier(tree.children[index + 1])
        assert name
        index = index + 2
        types.append((type, name))
    return types


def convertFunctionStmt(tree: Node) -> ASTNode:
    assert len(tree.children) == 4

    name_node = tree.children[0]
    name = convertIdentifier(name_node)
    parameters_node = tree.children[1]
    parameters = convertParameterList(parameters_node)
    return_node = tree.children[2]
    return_type = convertType(return_node)
    assert return_type
    block_node = tree.children[3]
    block = convertBlock(block_node)
    return ASTNode(
        kind=ASTNodeType.FUNCTION_STMT,
        token=tree.token,
        data=FunctionStmtData(
            name=name, parameters=parameters, return_type=return_type, block=block
        ),
    )


def convertIfStmt(tree: Node) -> ASTNode:
    assert len(tree.children) >= 2
    expr_node = tree.children[0]
    expr = convertExpression(expr_node)
    block_node = tree.children[1]
    block = convertBlock(block_node)
    if len(tree.children) == 3:
        elif_or_else_node = tree.children[2]
        if elif_or_else_node.kind == NodeType.ELIF_STMT:
            elif_stmts, else_stmt = convertElifStmt(elif_or_else_node)
            return ASTNode(
                kind=ASTNodeType.IF_STMT,
                token=tree.token,
                data=IfStmtData(
                    expr=expr, block=block, elif_stmts=elif_stmts, else_stmt=else_stmt
                ),
            )
        elif elif_or_else_node.kind == NodeType.ELSE_STMT:
            else_stmt = convertElseStmt(elif_or_else_node)
            return ASTNode(
                kind=ASTNodeType.IF_STMT,
                token=tree.token,
                data=IfStmtData(
                    expr=expr, block=block, elif_stmts=[], else_stmt=else_stmt
                ),
            )
        assert False
    else:
        return ASTNode(
            kind=ASTNodeType.IF_STMT,
            token=tree.token,
            data=IfStmtData(expr=expr, block=block, elif_stmts=[], else_stmt=None),
        )


def convertElifStmt(tree: Node) -> tuple[list[tuple[ASTNode, ASTNode]], ASTNode | None]:
    assert len(tree.children) >= 2
    expr_node = tree.children[0]
    expr = convertExpression(expr_node)
    block_node = tree.children[1]
    block = convertBlock(block_node)
    if len(tree.children) == 3:
        elif_or_else_node = tree.children[2]
        if elif_or_else_node.kind == NodeType.ELIF_STMT:
            elif_stmts, else_stmt = convertElifStmt(elif_or_else_node)
            return [(expr, block), *elif_stmts], else_stmt
        elif elif_or_else_node.kind == NodeType.ELSE_STMT:
            else_stmt = convertElseStmt(elif_or_else_node)
            return [(expr, block)], else_stmt
        assert False
    else:
        return [(expr, block)], None


def convertElseStmt(tree: Node) -> ASTNode:
    assert len(tree.children) == 1
    block_node = tree.children[0]
    block = convertBlock(block_node)
    return block


def convertWhileStmt(tree: Node) -> ASTNode:
    if len(tree.children) == 2:
        expr_node = tree.children[0]
        left_expr = convertExpression(expr_node)
        block_node = tree.children[1]
        block = convertBlock(block_node)
        return ASTNode(
            kind=ASTNodeType.WHILE_STMT,
            token=tree.token,
            data=WhileStmtData(left_expr=left_expr, right_expr=None, block=block),
        )
    elif len(tree.children) == 3:
        expr_node = tree.children[0]
        left_expr = convertExpression(expr_node)
        expr_node = tree.children[1]
        right_expr = convertExpression(expr_node)
        block_node = tree.children[2]
        block = convertBlock(block_node)
        return ASTNode(
            kind=ASTNodeType.WHILE_STMT,
            token=tree.token,
            data=WhileStmtData(left_expr=left_expr, right_expr=right_expr, block=block),
        )

    assert False


def convertSwitchStmt(tree: Node) -> ASTNode:
    assert len(tree.children) == 2
    expr_node = tree.children[0]
    expr = convertExpression(expr_node)
    body = tree.children[1]
    cases = []
    default = None
    for node in body.children:
        if node.kind == NodeType.SWITCH_CASE:
            assert len(node.children) == 2
            case_expr = convertExpression(node.children[0])
            case_block = convertStatement(node.children[1])
            cases.append((case_expr, case_block))

        elif node.kind == NodeType.SWITCH_DEFAULT:
            assert len(node.children) == 1
            default_block = node.children[0]
            default = convertStatement(default_block)

    return ASTNode(
        kind=ASTNodeType.SWITCH_STMT,
        token=tree.token,
        data=SwitchStmtData(expr, case_stmts=cases, default_stmt=default),
    )


def convertSweepStmt(tree: Node) -> ASTNode:
    assert len(tree.children) == 2
    expr_node = tree.children[0]
    expr = convertExpression(expr_node)
    body = tree.children[1]
    ranges = []
    default = None
    for node in body.children:
        if node.kind == NodeType.SWEEP_RANGE:
            assert len(node.children) == 2
            range_expr = convertExpression(node.children[0])
            range_block = convertStatement(node.children[1])
            ranges.append((range_expr, range_block))

        elif node.kind == NodeType.SWEEP_DEFAULT:
            assert len(node.children) == 1
            default_block = node.children[0]
            default = convertStatement(default_block)

    return ASTNode(
        kind=ASTNodeType.SWEEP_STMT,
        token=tree.token,
        data=SweepStmtData(expr, range_stmts=ranges, default_stmt=default),
    )


def convertForStmt(tree: Node) -> ASTNode:
    assert len(tree.children) == 4
    init_node = tree.children[0]
    init = None
    if init_node.kind == NodeType.DECLARATION:
        init = convertDeclaration(init_node)
    elif init_node.kind == NodeType.EXPRESSION:
        init = convertExpression(init_node)
    condition_node = tree.children[1]
    condition = None
    if condition_node.kind == NodeType.EXPRESSION:
        condition = convertExpression(condition_node)
    update_node = tree.children[2]
    update = None
    if update_node.kind == NodeType.EXPRESSION:
        update = convertExpression(update_node)
    block_node = tree.children[3]
    block = convertBlock(block_node)
    return ASTNode(
        kind=ASTNodeType.FOR_STMT,
        token=tree.token,
        data=ForStmtData(init=init, condition=condition, update=update, block=block),
    )


def convertStatement(tree: Node) -> ASTNode:
    assert len(tree.children) == 1
    statement = tree.children[0]
    if statement.kind == NodeType.EXPRESSION_STMT:
        assert len(statement.children) == 1
        expression_node = statement.children[0]
        expression = convertExpression(expression_node)
        return expression
    elif statement.kind == NodeType.IF_STMT:
        if_stmt = convertIfStmt(statement)
        return if_stmt
    elif statement.kind == NodeType.SWITCH_STMT:
        switch_stmt = convertSwitchStmt(statement)
        return switch_stmt
    elif statement.kind == NodeType.SWEEP_STMT:
        sweep_stmt = convertSweepStmt(statement)
        return sweep_stmt
    elif statement.kind == NodeType.WHILE_STMT:
        while_stmt = convertWhileStmt(statement)
        return while_stmt
    elif statement.kind == NodeType.FUNCTION_STMT:
        function_stmt = convertFunctionStmt(statement)
        return function_stmt
    elif statement.kind == NodeType.FOR_STMT:
        for_stmt = convertForStmt(statement)
        return for_stmt
    elif statement.kind == NodeType.DECLARATION_STMT:
        declaration = convertDeclarationStmt(statement)
        return declaration
    elif statement.kind == NodeType.BLOCK:
        block = convertBlock(statement)
        return block
    elif statement.kind == NodeType.NEXT_STMT:
        return ASTNode(
            kind=ASTNodeType.NEXT_STMT, token=statement.token, data=NextStmtData()
        )
    elif statement.kind == NodeType.STOP_STMT:
        return ASTNode(
            kind=ASTNodeType.STOP_STMT, token=statement.token, data=StopStmtData()
        )
    elif statement.kind == NodeType.RETURN_STMT:
        expression = None
        if len(statement.children) == 1:
            expression = convertExpression(statement.children[0])
        return ASTNode(
            kind=ASTNodeType.RETURN_STMT,
            token=statement.token,
            data=ReturnStmtData(expression=expression),
        )
    assert False


def convertExpression(tree: Node) -> ASTNode:
    if tree.kind == NodeType.EXPRESSION:
        assert len(tree.children) == 1
        tree = tree.children[0]
    if tree.kind in [
        NodeType.NUMANTICS_OPERATION,
        NodeType.ASSIGNMENT_OP,
        NodeType.OR_OPERATION,
        NodeType.AND_OPERATION,
        NodeType.RELATION,
        NodeType.SUM,
        NodeType.TERM,
    ]:
        assert len(tree.children) == 3
        lhs = convertExpression(tree.children[0])
        operator = mapNodeTypeToOperatorType(tree.children[1].kind)
        assert operator
        rhs = convertExpression(tree.children[2])
        return ASTNode(
            kind=ASTNodeType.BINARY_OP,
            token=tree.token,
            data=BinaryOpData(lhs=lhs, operator=operator, rhs=rhs),
        )
    elif tree.kind == NodeType.NOT_OPERATION:
        assert len(tree.children) == 1
        operand = convertExpression(tree.children[0])
        operator = ASTOperator.NOT_OPERATOR
        return ASTNode(
            kind=ASTNodeType.UNARY_OP,
            token=tree.token,
            data=UnaryOpData(operand=operand, operator=operator),
        )
    elif tree.kind == NodeType.FACTOR:
        assert len(tree.children) == 2
        operator = mapNodeTypeToOperatorType(tree.children[0].kind)
        assert operator
        operand = convertExpression(tree.children[1])
        return ASTNode(
            kind=ASTNodeType.UNARY_OP,
            token=tree.token,
            data=UnaryOpData(operand=operand, operator=operator),
        )
    elif tree.kind == NodeType.POWER:
        assert len(tree.children) == 2
        lhs = convertExpression(tree.children[0])
        operator = ASTOperator.EXP_OPERATOR
        rhs = convertExpression(tree.children[1])
        return ASTNode(
            kind=ASTNodeType.BINARY_OP,
            token=tree.token,
            data=BinaryOpData(lhs=lhs, operator=operator, rhs=rhs),
        )
    elif tree.kind == NodeType.PREFIX:
        assert len(tree.children) == 2
        operator = mapNodeTypeToOperatorType(tree.children[0].kind)
        assert operator
        operand = convertExpression(tree.children[1])
        return ASTNode(
            kind=ASTNodeType.UNARY_OP,
            token=tree.token,
            data=UnaryOpData(operand=operand, operator=operator),
        )
    elif tree.kind == NodeType.POSTFIX:
        assert len(tree.children) == 2
        operand = convertExpression(tree.children[0])
        operator = tree.children[1].kind
        if operator in [
            NodeType.POST_INCREMENT_OPERATOR,
            NodeType.POST_DECREMENT_OPERATOR,
        ]:
            operator = mapNodeTypeToOperatorType(tree.children[1].kind)
            assert operator
            return ASTNode(
                kind=ASTNodeType.UNARY_OP,
                token=tree.token,
                data=UnaryOpData(operand=operand, operator=operator),
            )

        elif operator == NodeType.EXPRESSION:
            expr = convertExpression(tree.children[1])
            return ASTNode(
                kind=ASTNodeType.ARRAY_INDEX,
                token=tree.token,
                data=ArrayIndexData(array=operand, index=expr),
            )

        elif operator == NodeType.ARGUMENTS:
            args = []
            for node in tree.children[1].children:
                args.append(convertExpression(node))

            return ASTNode(
                kind=ASTNodeType.FUNCTION_CALL,
                token=tree.token,
                data=FunctionCallData(function=operand, arguments=args),
            )
        assert False
    elif tree.kind == NodeType.PRIMARY:
        assert len(tree.children) == 1
        return convertExpression(tree.children[0])
    elif tree.kind == NodeType.IDENTIFIER:
        return ASTNode(
            kind=ASTNodeType.IDENTIFIER, token=tree.token, data=IdentifierData()
        )
    else:
        literal_type = mapNodeTypeToLiteralType(tree.kind)
        assert literal_type
        return ASTNode(
            kind=ASTNodeType.LITERAL,
            token=tree.token,
            data=LiteralData(literal_type=literal_type),
        )


def convertIdentifier(tree: Node) -> ASTNode:
    return ASTNode(kind=ASTNodeType.IDENTIFIER, token=tree.token, data=IdentifierData())


def convertDeclarationStmt(tree: Node) -> ASTNode:
    assert len(tree.children) == 1
    declaration = tree.children[0]
    return convertDeclaration(declaration)


def convertDeclaration(tree: Node) -> ASTNode:
    assert len(tree.children) == 2 or len(tree.children) == 3

    type_node = tree.children[0]
    type = convertType(type_node)
    assert type

    name_node = tree.children[1]
    name = convertIdentifier(name_node)
    expression = None
    if len(tree.children) == 3:
        expression_node = tree.children[2]
        expression = convertExpression(expression_node)

    ast = ASTNode(
        kind=ASTNodeType.DECLARATION,
        token=tree.token,
        data=DeclarationData(type=type, name=name, expression=expression),
    )
    return ast


def convertType(tree: Node) -> Type | None:
    if tree.kind == NodeType.BUILTIN_TYPE:
        type = mapTokenToBuiltInType(tree.token)
        assert type
        return Type(builtin=type)

    elif tree.kind == NodeType.COMPOUND_TYPE:
        assert len(tree.children) >= 2
        builtin_node = tree.children[0]
        builtin_type = mapTokenToBuiltInType(builtin_node.token)
        assert builtin_type
        type = Type(builtin=builtin_type)
        index = 1
        while index < len(tree.children):
            next_node = tree.children[index]
            if next_node.kind != NodeType.MODIFIER_TYPE:
                break
            modifier_type = mapTokenToModifierType(next_node.token)
            assert modifier_type
            type.modifiers.append(modifier_type)
            index += 1
        return type
    return


def convertCstToAst(tree: Node):
    ast = ASTNode(kind=ASTNodeType.FILE, token=tree.token, data=FileData(children=[]))
    for node in tree.children:
        if node.kind == NodeType.FUNCTION_STMT:
            ast.data.children.append(convertFunctionStmt(node))
        elif node.kind == NodeType.DECLARATION_STMT:
            ast.data.children.append(convertDeclarationStmt(node))
    return ast
