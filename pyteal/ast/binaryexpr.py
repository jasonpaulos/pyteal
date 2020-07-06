from ..types import TealType, require_type
from ..ir import TealOp, Op
from .expr import Expr

class BinaryExpr(Expr):
    def __init__(self, op: Op, inputType: TealType, outputType: TealType, argLeft: Expr, argRight: Expr) -> None:
        require_type(argLeft.type_of(), inputType)
        require_type(argRight.type_of(), inputType)
        self.op = op
        self.outputType = outputType
        self.argLeft = argLeft
        self.argRight = argRight

    def accept(self, visitor):
        self.argLeft.accept(visitor)
        self.argRight.accept(visitor)
        visitor.visitBinaryExpr(self)

    def __teal__(self):
        teal = self.argLeft.__teal__() + self.argRight.__teal__()
        teal.append(TealOp(self.op))
        return teal
    
    def __str__(self):
        return "({} {} {})".format(self.op.value, self.argLeft, self.argRight)
    
    def type_of(self):
        return self.outputType

def Add(left: Expr, right: Expr):
    return BinaryExpr(Op.add, TealType.uint64, TealType.uint64, left, right)

def Minus(left: Expr, right: Expr):
    return BinaryExpr(Op.minus, TealType.uint64, TealType.uint64, left, right)

def Mul(left: Expr, right: Expr):
    return BinaryExpr(Op.mul, TealType.uint64, TealType.uint64, left, right)

def Div(left: Expr, right: Expr):
    return BinaryExpr(Op.div, TealType.uint64, TealType.uint64, left, right)

def Mod(left: Expr, right: Expr):
    return BinaryExpr(Op.mod, TealType.uint64, TealType.uint64, left, right)

def Eq(left: Expr, right: Expr):
    return BinaryExpr(Op.eq, right.type_of(), TealType.uint64, left, right)

def Lt(left: Expr, right: Expr):
    return BinaryExpr(Op.lt, TealType.uint64, TealType.uint64, left, right)

def Le(left: Expr, right: Expr):
    return BinaryExpr(Op.le, TealType.uint64, TealType.uint64, left, right)

def Gt(left: Expr, right: Expr):
    return BinaryExpr(Op.gt, TealType.uint64, TealType.uint64, left, right)

def Ge(left: Expr, right: Expr):
    return BinaryExpr(Op.ge, TealType.uint64, TealType.uint64, left, right)
