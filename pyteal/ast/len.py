from ..types import TealType, require_type
from .expr import Expr, UnaryExpr

# return the length of a bytes value
class Len(UnaryExpr):

    # default constructor
    def __init__(self, child:Expr) -> None:
        require_type(child.type_of(), TealType.bytes)
        self.child = child

    def __teal__(self):
        return self.child.__teal__() + [["len"]]
         
    def __str__(self):
         return "(len {})".format(self.child)

    def type_of(self):
        return TealType.uint64
