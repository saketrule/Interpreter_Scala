import sys
from basic_parser_combinators import *
from base_parsers import *
from lexer_tokens import *

def expr():
    return inFixExpr()
    
def inFixExpr():
    ##add prefix expression
    ##add super postfix
    return litExp()
    
def litExp():
    return precedence(aexp_term(),
                      aexp_precedence_levels,
                      infix_num_op)
                      
def aexp_term():
    return numLit() | aexp_group()
    
def numLit():
    return intLit() | floatLit()
    
def intLit():
    return Tag(INT) ^ (lambda i: IntLit(int(i)))
    
def floatLit():
    return Tag(FLOAT) ^ (lambda i: FloatLit(float(i)))

def aexp_group():
    return Reserved('(',PAREN) + Lazy(litExp) + Reserved(')',PAREN) ^ process_group


def precedence(value_parser, precedence_levels, combine):
    def op_parser(precedence_level):
        return any_operator_in_list(precedence_level) ^ combine
    parser = value_parser * op_parser(precedence_levels[0])
    for precedence_level in precedence_levels[1:]:
        parser = parser * op_parser(precedence_level)
    return parser
    
def any_operator_in_list(ops):
    op_parsers = [Reserved(op,OPCHAR) for op in ops]
    parser = reduce(lambda l, r: l | r, op_parsers)
    return parser
    
def process_group(parsed):
    ((_, p), _) = parsed
    return p
    
def infix_num_op(op):
    return (lambda l,r : InfixNumOp(l,op,r))