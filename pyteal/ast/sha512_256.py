from ..types import TealType, require_type
from ..ir import TealOp, Op
from .expr import Expr, UnaryExpr

class Sha512_256(UnaryExpr):    

    # default constructor
    def __init__(self, child:Expr) -> None:
        require_type(child.type_of(), TealType.bytes)
        self.child = child

    def __teal__(self):
        return self.child.__teal__() + [TealOp(Op.sha512_256)]
         
    def __str__(self):
         return "(sha512_256 {})".format(self.child)

    def type_of(self):
        return TealType.bytes
