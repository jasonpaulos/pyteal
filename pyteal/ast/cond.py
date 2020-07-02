from ..types import TealType, require_type
from ..ir import TealOp, Op, TealLabel
from ..errors import TealInputError
from ..util import new_label
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
        teal = []

        labels = []
        for arg in self.args:
            l = new_label()
            cond = arg[0]

            teal += cond.__teal__()
            teal.append(TealOp(Op.bnz, l))

            labels.append(l)

        # err if no conditions are met
        teal.append(TealOp(Op.err))

        # end label
        labels.append(new_label())
        
        for i, arg in enumerate(self.args):
            label = TealLabel(labels[i])
            branch = arg[1]

            teal.append(label)
            teal += branch.__teal__()
            if i + 1 != len(self.args):
                teal.append(TealOp(Op.b, labels[-1]))

        teal.append(TealLabel(labels[-1]))

        return teal

    def __str__(self):
        ret_str = "(Cond"
        for a in self.args:
            ret_str += " [" + a[0].__str__() + ", " + a[1].__str__() + "]"
        ret_str += ")"
        return ret_str
        
    def type_of(self):
        return self.value_type
