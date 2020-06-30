from ..types import TealType, require_type
from .expr import Expr, BinaryExpr

# greater than
class Gt(BinaryExpr):

    # default constructor
    def __init__(self, left:Expr, right:Expr) -> None:
        require_type(left.type_of(), TealType.uint64)
        require_type(right.type_of(), TealType.uint64) 
        self.left = left
        self.right = right

    def __teal__(self):
        return self.left.__teal__() + self.right.__teal__() + [[">"]]

    def __str__(self):
        return "(> {} {})".format(self.left, self.right)
   
    def type_of(self):
        return TealType.uint64

