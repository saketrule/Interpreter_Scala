class Literal:
    def __init__(self,val):
        self.val = val
        
    def __eval__(self,env):
        return self.val
    
class IntLit(Literal):        
    def __repr__(self):
        return 'IntLit(%d) ' % self.val
        
class BoolLit(Literal):
    def __repr__(self):
        return 'BoolLit(%d) ' % self.val
        
class CharLit(Literal):
    def __repr__(self):
        return 'CharLit(%d) ' % self.val
        
class StringLit(Literal):
    def __repr__(self):
        return 'StringLit(%d) ' % self.val
        
class FloatLit(Literal):
    def __repr__(self):
        return 'FloatLit(%d) ' % self.val
        
aexp_precedence_levels = [
    ['*', '/'],
    ['+', '-'],
]

class InfixNumOp():
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

    def __repr__(self):
        return 'Infixnumop(%s, %s, %s)' % (self.op, self.left, self.right)

    def eval(self, env):
        left_value = self.left.eval(env)
        right_value = self.right.eval(env)
        if self.op == '+':
            value = left_value + right_value
        elif self.op == '-':
            value = left_value - right_value
        elif self.op == '*':
            value = left_value * right_value
        elif self.op == '/':
            value = left_value / right_value
        else:
            raise RuntimeError('unknown operator: ' + self.op)
        return value