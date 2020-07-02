from ..types import TealType, require_type
from ..ir import TealOp, Op
from .expr import Expr, UnaryExpr

class Btoi(UnaryExpr):

    # default constructor
    def __init__(self, child:Expr) -> None:
        require_type(child.type_of(), TealType.bytes)
        self.child = child

    def __teal__(self):
        teal = self.child.__teal__()
        teal.append(TealOp(Op.btoi))
        return teal
         
    def __str__(self):
         return "(btoi {})".format(self.child)

    def type_of(self):
        return TealType.uint64
