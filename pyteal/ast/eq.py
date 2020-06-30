from ..types import TealType, types_match
from ..errors import TealTypeMismatchError
from .expr import Expr, BinaryExpr

# a polymorphic eq
class Eq(BinaryExpr):

    # default constructor
    def __init__(self, left:Expr, right:Expr) -> None:
         # type checking
        t1 = left.type_of()
        t2 = right.type_of()
        if not types_match(t1, t2):
            raise TealTypeMismatchError(t1, t2)

        self.left = left
        self.right = right

    def __teal__(self):
        return self.left.__teal__() + self.right.__teal__() + [["=="]]
        
    def __str__(self):
         return "(== {} {})".format(self.left, self.right)
    
    def type_of(self):
        return TealType.uint64
