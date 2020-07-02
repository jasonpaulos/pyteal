from ..types import TealType
from ..ir import TealOp, Op
from ..errors import TealInputError
from .expr import LeafExpr

class Arg(LeafExpr):
    
    # default constructor
    def __init__(self, index:int) -> None:
        if type(index) is not int:
            raise TealInputError("invalid arg input type {}".format(
                 type(index)))

        if index < 0 or index > 255:
            raise TealInputError("invalid arg index {}".format(index))

        self.index = index

    def __teal__(self):
        return [TealOp(Op.arg, self.index)]
        
    def __str__(self):
        return "(arg {})".format(self.index)

    def type_of(self):
        return TealType.bytes
