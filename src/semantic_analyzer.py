from __future__ import annotations
from semantic_types import (
    BuiltInTypes,
    Function,
    ModifierTypes,
    Parameter,
    Scope,
    Symbol,
    Type,
)
from ast_types import ASTNode, ASTNodeType
from collections import Counter


def resolveFile(tree: ASTNode, code: str):
    scope = Scope()
    has_error = False

    def nonFatalError(*args):
        nonlocal has_error
        print(*args)
        has_error = True

    def define(scope: Scope, name: str, symbol: Symbol):
        if scope.symbols.get(name):
            nonFatalError(
                f"ERROR: redefinition of symbol {name}", scope.symbols.get(name)
            )
            return
        scope.symbols[name] = symbol

    def reference(scope: Scope, name: str, error_on_empty=False) -> Symbol | None:
        top_scope = scope
        while top_scope:
            result = top_scope.symbols.get(name)
            if result:
                return result
            top_scope = top_scope.parent_scope
        if error_on_empty:
            nonFatalError(f"ERROR: undefined symbol '{name}'")

        return None

    def resolveStatement(tree: ASTNode, scope: Scope):
        if tree.kind == ASTNodeType.DECLARATION:
            resolveDeclaration(tree, scope)
        elif tree.kind == ASTNodeType.IF_STMT:
            resolveIfStmt(tree, scope)
        elif tree.kind == ASTNodeType.SWITCH_STMT:
            resolveSwitchStmt(tree, scope)
        elif tree.kind == ASTNodeType.SWEEP_STMT:
            resolveSweepStmt(tree, scope)
        elif tree.kind == ASTNodeType.WHILE_STMT:
            resolveWhileStmt(tree, scope)
        elif tree.kind == ASTNodeType.FUNCTION_STMT:
            resolveFunctionStmt(tree, scope)
        elif tree.kind == ASTNodeType.FOR_STMT:
            resolveForStmt(tree, scope)
        elif tree.kind == ASTNodeType.BLOCK:
            resolveBlock(tree, scope)
        elif tree.kind == ASTNodeType.NEXT_STMT:
            resolveNextStmt(tree, scope)
        elif tree.kind == ASTNodeType.STOP_STMT:
            resolveStopStmt(tree, scope)
        elif tree.kind == ASTNodeType.RETURN_STMT:
            resolveReturnStmt(tree, scope)
        # elif tree.kind == ASTNodeType.FUNCTION_CALL:
        #     resolveFunctionCall(tree, scope)
        # elif tree.kind == ASTNodeType.ARRAY_INDEX:
        #     resolveArrayIndex(tree, scope)
        # elif tree.kind == ASTNodeType.BINARY_OP:
        #     resolveBinaryOp(tree, scope)
        # elif tree.kind == ASTNodeType.UNARY_OP:
        #     resolveUnaryOp(tree, scope)

    def resolveIfStmt(tree: ASTNode, scope: Scope):
        resolveExpression(tree.data.expr, scope)
        resolveBlock(tree.data.block, scope)
        for expr, block in tree.data.elif_stmts:
            resolveExpression(expr, scope)
            resolveBlock(block, scope)
        if tree.data.else_stmt:
            resolveBlock(tree.data.else_stmt, scope)

    def resolveSwitchStmt(tree: ASTNode, scope: Scope):
        resolveBlock(tree.data.block, scope)
        for expr, node in tree.data.case_stmts:
            resolveExpression(expr, scope)
            resolveStatement(node, scope)
        if tree.data.default_stmt:
            resolveStatement(tree.data.default_stmt, scope)

    def resolveSweepStmt(tree: ASTNode, scope: Scope):
        resolveBlock(tree.data.block, scope)
        for expr, node in tree.data.case_stmts:
            resolveExpression(expr, scope)
            resolveStatement(node, scope)
        if tree.data.default_stmt:
            resolveStatement(tree.data.default_stmt, scope)

    def resolveWhileStmt(tree: ASTNode, scope: Scope):
        resolveExpression(tree.data.left_expr, scope)
        if tree.data.right_expr:
            resolveExpression(tree.data.right_expr, scope)
        resolveBlock(tree.data.block, scope)

    def resolveForStmt(tree: ASTNode, scope: Scope):
        if tree.data.init:
            if tree.data.init.kind == ASTNodeType.DECLARATION:
                resolveDeclaration(tree.data.init, scope)
            else:
                resolveExpression(tree.data.init, scope)
        if tree.data.condition:
            resolveExpression(tree.data.condition, scope)
        if tree.data.update:
            resolveExpression(tree.data.update, scope)
        resolveBlock(tree.data.block, scope)

    def resolveBlock(tree: ASTNode, scope: Scope):
        tree.scope = Scope(parent_scope=scope)
        scope.children.append(tree.scope)
        for node in tree.data.statements:
            resolveStatement(node, scope)

    def resolveNextStmt(tree: ASTNode, scope):
        pass

    def resolveStopStmt(tree: ASTNode, scope):
        pass

    def resolveReturnStmt(tree: ASTNode, scope):
        resolveExpression(tree.data.expression, scope)

    def resolveFunctionStmt(tree: ASTNode, scope: Scope):
        tree.scope = Scope(parent_scope=scope)
        scope.children.append(tree.scope)
        func_name = resolveIdentifier(tree.data.name, scope)
        resolveType(tree.data.return_type, scope)
        params: list[Parameter] = []
        for type, name_node in tree.data.parameters:
            name = resolveIdentifier(name_node, scope)
            resolveType(type, scope)
            symbol = Symbol(name=name, type=type, scope=tree.scope)
            params.append(Parameter(type, name))
        symbol = Symbol(
            name=func_name,
            type=Function(return_type=tree.data.return_type, parameters=params),
            scope=scope,
        )
        define(scope, func_name, symbol)
        resolveBlock(tree.data.block, tree.scope)

    def resolveDeclaration(tree: ASTNode, scope: Scope):
        resolveType(tree.data.type, scope)
        name = resolveIdentifier(tree.data.name, scope)
        expr = None
        if tree.data.name:
            expr = resolveExpression(tree.data.name, scope)
        if expr:
            isTypeMatched(tree.data.type, expr)
        symbol = Symbol(name=name, type=tree.data.type, scope=scope)
        define(scope, name, symbol)

    def resolveIdentifier(tree: ASTNode, scope: Scope):
        return code[tree.token.start : tree.token.end]

    def resolveExpression(tree: ASTNode, scope: Scope):
        return Type(builtin=BuiltInTypes.INT_TYPE)

    def resolveType(type: Type, scope: Scope) -> Type | None:
        filtered_modifiers = set()
        has_percent = False
        percent_types = [ModifierTypes.PERCENT_TYPE, ModifierTypes.XPERCENT_TYPE]
        has_sign = False
        sign_types = [ModifierTypes.POSITIVE_TYPE, ModifierTypes.NEGATIVE_TYPE]
        has_nonzero = False  # non-dependent
        nonzero_types = [ModifierTypes.NONZERO_TYPE]
        has_parity = False
        parity_types = [ModifierTypes.EVEN_TYPE, ModifierTypes.ODD_TYPE]
        has_auto = False
        auto_type = [ModifierTypes.AUTO_TYPE]
        has_time = False
        time_types = [
            ModifierTypes.SECOND_TYPE,
            ModifierTypes.MINUTE_TYPE,
            ModifierTypes.HOUR_TYPE,
            ModifierTypes.DAY_TYPE,
            ModifierTypes.WEEK_TYPE,
            ModifierTypes.MONTH_TYPE,
            ModifierTypes.YEAR_TYPE,
        ]
        has_distance = False
        distance_types = [
            ModifierTypes.METER_TYPE,
            ModifierTypes.MM_TYPE,
            ModifierTypes.CM_TYPE,
            ModifierTypes.KM_TYPE,
            ModifierTypes.FT_TYPE,
            ModifierTypes.INCH_TYPE,
        ]
        has_volume = False
        volume_types = [
            ModifierTypes.LITER_TYPE,
            ModifierTypes.ML_TYPE,
            ModifierTypes.CL_TYPE,
            ModifierTypes.KL_TYPE,
        ]
        has_mass = False
        mass_types = [
            ModifierTypes.GRAM_TYPE,
            ModifierTypes.MG_TYPE,
            ModifierTypes.CG_TYPE,
            ModifierTypes.KG_TYPE,
        ]
        has_temp = False
        temp_types = [
            ModifierTypes.CELC_TYPE,
            ModifierTypes.FAHR_TYPE,
            ModifierTypes.KELV_TYPE,
        ]
        has_force = False
        force_types = [
            ModifierTypes.NEWT_TYPE,
            ModifierTypes.KGF_TYPE,
            ModifierTypes.LBF_TYPE,
        ]
        has_velocity = False
        velocity_types = [
            ModifierTypes.MPS_TYPE,
            ModifierTypes.FPS_TYPE,
        ]
        has_accel = False  # non-dependent
        accel_types = [ModifierTypes.MPS2_TYPE]

        for modifier in type.modifiers:
            if modifier in filtered_modifiers:
                nonFatalError("ERROR: Duplicate modifier in compound type")
            if modifier in percent_types:
                if has_percent:
                    nonFatalError(
                        "ERROR: Multiple modifier in same type category (percent)"
                    )
                has_percent = True
            elif modifier in sign_types:
                if has_sign:
                    nonFatalError(
                        "ERROR: Multiple modifier in same type category (sign)"
                    )
                has_sign = True
            elif modifier in nonzero_types:
                has_nonzero = True
            elif modifier in parity_types:
                if has_parity:
                    nonFatalError(
                        "ERROR: Multiple modifier in same type category (parity)"
                    )
                has_parity = True
            elif modifier in time_types:
                if has_time:
                    nonFatalError(
                        "ERROR: Multiple modifier in same type category (time)"
                    )
                has_time = True
            elif modifier in distance_types:
                if has_distance:
                    nonFatalError(
                        "ERROR: Multiple modifier in same type category (distance)"
                    )
                has_distance = True
            elif modifier in volume_types:
                if has_volume:
                    nonFatalError(
                        "ERROR: Multiple modifier in same type category (volume)"
                    )
                has_volume = True
            elif modifier in mass_types:
                if has_mass:
                    nonFatalError(
                        "ERROR: Multiple modifier in same type category (mass)"
                    )
                has_mass = True
            elif modifier in temp_types:
                if has_temp:
                    nonFatalError(
                        "ERROR: Multiple modifier in same type category (temperature)"
                    )
                has_temp = True
            elif modifier in force_types:
                if has_force:
                    nonFatalError(
                        "ERROR: Multiple modifier in same type category (force)"
                    )
                has_force = True
            elif modifier in velocity_types:
                if has_velocity:
                    nonFatalError(
                        "ERROR: Multiple modifier in same type category (velocity)"
                    )
                has_velocity = True
            elif modifier in accel_types:
                if has_accel:
                    nonFatalError(
                        "ERROR: Multiple modifier in same type category (acceleration)"
                    )
                has_accel = True
            elif modifier in auto_type:
                if (
                    has_percent
                    or has_sign
                    or has_nonzero
                    or has_parity
                    or has_time
                    or has_distance
                    or has_volume
                    or has_mass
                    or has_temp
                    or has_force
                    or has_velocity
                    or has_accel
                ):
                    nonFatalError("ERROR: Auto modifier cannot be with other modifiers")

            filtered_modifiers.add(modifier)

    def isTypeMatched(type1: Type, type2: Type) -> bool:
        if type1.builtin != type2.builtin:
            return False
        return Counter(type1.modifiers) == Counter(type2.modifiers)

    def isTypeCompatible(dest: Type, src: Type) -> bool:
        if len(src.modifiers) == 0 and len(dest.modifiers) == 0:
            if (
                dest.builtin == BuiltInTypes.FLOAT_TYPE
                and src.builtin == BuiltInTypes.INT_TYPE
            ):
                return True
            if dest.builtin == BuiltInTypes.BOOL_TYPE and src.builtin in [
                BuiltInTypes.INT_TYPE,
                BuiltInTypes.FLOAT_TYPE,
                BuiltInTypes.BOOL_TYPE,
                BuiltInTypes.CHAR_TYPE,
                BuiltInTypes.STRING_TYPE,
            ]:
                return True
            if (
                dest.builtin == BuiltInTypes.INT_TYPE
                and src.builtin == BuiltInTypes.CHAR_TYPE
            ):
                return True
        return False

    assert tree.kind == ASTNodeType.FILE
    for node in tree.data.children:
        if node.kind == ASTNodeType.FUNCTION_STMT:
            resolveFunctionStmt(node, scope)
        elif node.kind == ASTNodeType.DECLARATION:
            resolveDeclaration(node, scope)
    print(scope)
