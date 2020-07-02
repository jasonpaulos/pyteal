from ..types import TealType, require_type
from ..ir import TealOp, Op
from ..errors import TealInputError
from .expr import Expr, BinaryExpr

class Or(BinaryExpr):

    # default constructor
    def __init__(self, *argv):
        if len(argv) < 2:
            raise TealInputError("Or requires at least two children.")
        for arg in argv:
            if not isinstance(arg, Expr):
                raise TealInputError("{} is not a pyteal expression.".format(arg))
            require_type(arg.type_of(), TealType.uint64)

        self.args = argv

    def __teal__(self):
        code = []
        for i, a in enumerate(self.args):
            code += a.__teal__()
            if i != 0:
                code.append(TealOp(Op.logic_or))
        return code
        
    def __str__(self):
        ret_str = "(Or"
        for a in self.args:
            ret_str += " " + a.__str__()
        ret_str += ")"
        return ret_str 

    def type_of(self):
        return TealType.uint64
