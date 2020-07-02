from ..types import TealType, require_type
from ..ir import TealOp, Op
from .expr import Expr, BinaryExpr

class Div(BinaryExpr):
    
    def __init__(self, left:Expr, right:Expr) -> None:
        require_type(left.type_of(), TealType.uint64)
        require_type(right.type_of(), TealType.uint64)
        self.left = left
        self.right = right

    def __teal__(self):
        return self.left.__teal__() + self.right.__teal__() + [TealOp(Op.div)]

    def __str__(self):
        return "(/ {} {})".format(self.left, self.right)

    def type_of(self):
        return TealType.uint64
