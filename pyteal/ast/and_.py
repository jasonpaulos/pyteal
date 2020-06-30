from ..types import TealType, require_type
from ..errors import TealInputError
from .expr import Expr, BinaryExpr

class And(BinaryExpr):

    # default constructor
    def __init__(self, *argv):
        if len(argv) < 2:
            raise TealInputError("And requires at least two children.")
        for arg in argv:
            if not isinstance(arg, Expr):
                raise TealInputError("{} is not a pyteal expression.".format(arg))
            require_type(arg.type_of(), TealType.uint64)

        self.args = argv
        
    def __teal__(self):
        code = []
        for i, a in enumerate(self.args):
            if i == 0:
                code = a.__teal__()
            else:
                code = code + a.__teal__() +[["&&"]]
        return code

    def __str__(self):
        ret_str = "(And"
        for a in self.args:
            ret_str += " " + a.__str__()
        ret_str += ")"
        return ret_str
        
    def type_of(self):
        return TealType.uint64
