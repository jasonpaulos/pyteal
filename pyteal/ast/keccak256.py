from ..types import TealType, require_type
from ..ir import TealOp, Op
from .expr import Expr, UnaryExpr

class Keccak256(UnaryExpr):    

    # default constructor
    def __init__(self, child:Expr) -> None:
        require_type(child.type_of(), TealType.bytes)
        self.child = child

    def __teal__(self):
        return self.child.__teal__() + [TealOp(Op.keccak256)]
         
    def __str__(self):
         return "(keccak {})".format(self.child)

    def type_of(self):
        return TealType.bytes
