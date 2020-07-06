from ..types import TealType, require_type
from ..errors import TealInputError
from ..ir import TealOp, Op
from .expr import Expr
from .naryexpr import NaryExpr

class And(NaryExpr):

    # default constructor
    def __init__(self, *argv):
        if len(argv) < 2:
            raise TealInputError("And requires at least two children.")
        for arg in argv:
            if not isinstance(arg, Expr):
                raise TealInputError("{} is not a pyteal expression.".format(arg))
            require_type(arg.type_of(), TealType.uint64)

        super().__init__(argv)
        
    def __teal__(self):
        code = []
        for i, a in enumerate(self.args):
            code += a.__teal__()
            if i != 0:
                code.append(TealOp(Op.logic_and))
        return code

    def __str__(self):
        ret_str = "(And"
        for a in self.args:
            ret_str += " " + a.__str__()
        ret_str += ")"
        return ret_str
        
    def type_of(self):
        return TealType.uint64
