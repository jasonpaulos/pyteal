from ..types import TealType, require_type
from ..ir import TealOp, Op
from .expr import Expr

class UnaryExpr(Expr):
    def __init__(self, op: Op, inputType: TealType, outputType: TealType, arg: Expr) -> None:
        require_type(arg.type_of(), inputType)
        self.op = op
        self.outputType = outputType
        self.arg = arg

    def accept(self, visitor):
        self.arg.accept(visitor)
        visitor.visitUnaryExpr(self)

    def __teal__(self):
        teal = self.arg.__teal__()
        teal.append(TealOp(self.op))
        return teal
    
    def __str__(self):
        return "({} {})".format(self.op.value, self.arg)
    
    def type_of(self):
        return self.outputType

def Btoi(arg: Expr):
    return UnaryExpr(Op.btoi, TealType.bytes, TealType.uint64, arg)

def Itob(arg: Expr):
    return UnaryExpr(Op.itob, TealType.uint64, TealType.bytes, arg)

def Len(arg: Expr):
    return UnaryExpr(Op.len, TealType.bytes, TealType.uint64, arg)

def Sha256(arg: Expr):
    return UnaryExpr(Op.sha256, TealType.bytes, TealType.bytes, arg)

def Sha512_256(arg: Expr):
    return UnaryExpr(Op.sha512_256, TealType.bytes, TealType.bytes, arg)

def Keccak256(arg: Expr):
    return UnaryExpr(Op.keccak256, TealType.bytes, TealType.bytes, arg)

def Pop(arg: Expr):
    return UnaryExpr(Op.pop, TealType.anytype, TealType.none, arg)
