from ..types import TealType, require_type
from ..ir import TealOp, Op
from .expr import Expr, NaryExpr

# ed25519 signature verification
class Ed25519Verify(NaryExpr):

    # default constructor
    def __init__(self, arg0:Expr, arg1:Expr, arg2:Expr) -> None:
        require_type(arg0.type_of(), TealType.bytes)
        require_type(arg1.type_of(), TealType.bytes)
        require_type(arg2.type_of(), TealType.bytes)
         
        self.args = [arg0, arg1, arg2]

    def __teal__(self):
        return self.args[0].__teal__() + \
               self.args[1].__teal__() + \
               self.args[2].__teal__() + \
               [TealOp(Op.ed25519verify)]

    def __str__(self):
        return "(ed25519verify {} {} {})".format(self.args[0],
                                                 self.args[1], self.args[2])
    
    def type_of(self):
        return TealType.uint64
