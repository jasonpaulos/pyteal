from ..types import TealType
from ..ir import TealOp, Op
from .expr import LeafExpr

class Err(LeafExpr):
    """
    only used internally, not a user facing operator
    """

    #default constructor
    def __init__(self):
        pass

    def __teal__(self):
        return [TealOp(Op.err)]

    def __str__(self):
        return "(err)"

    def type_of(self):
        return TealType.anytype
