from ..types import TealType, require_type
from ..errors import TealInputError
from .expr import NaryExpr
from .err import Err
from .if_ import If

class Cond(NaryExpr):

    # default constructor
    def __init__(self, *argv):

        if len(argv) < 1:
            raise TealInputError("Cond requires at least one [condition, value]")

        value_type = 0

        for arg in argv:
            msg = "Cond should be in the form of Cond([cond1, value1], [cond2, value2], ...), error in {}"
            if not isinstance(arg, list):
                raise TealInputError(msg.format(arg))
            if len(arg) != 2:
                raise TealInputError(msg.format(arg))
            
            require_type(arg[0].type_of(), TealType.uint64) # cond_n should be int

            if value_type == 0: # the types of all branches should be the same
                value_type = arg[1].type_of()
            else:
                require_type(arg[1].type_of(), value_type)

        self.value_type = value_type        
        self.args = argv        

    def __teal__(self):
        # converting cond to if first
        def make_if(conds):
            if len(conds) == 0:
                return Err()
            else:
                e = conds[0]
                return If(e[0], e[1], make_if(conds[1:]))

        desugared = make_if(self.args)
        return desugared.__teal__()

    def __str__(self):
        ret_str = "(Cond"
        for a in self.args:
            ret_str += " [" + a[0].__str__() + ", " + a[1].__str__() + "]"
        ret_str += ")"
        return ret_str
        
    def type_of(self):
        return self.value_type
