from ..types import TealType, require_type, types_match
from ..errors import TealTypeMismatchError
from ..util import new_label
from .expr import Expr, NaryExpr

class If(NaryExpr):

    #default constructor
    def __init__(self, arg0:Expr, arg1:Expr, arg2:Expr) -> None:
        require_type(arg0.type_of(), TealType.uint64)

        t1 = arg1.type_of()
        t2 = arg2.type_of()
        if not types_match(t1, t2):
            raise TealTypeMismatchError(t1, t2)

        self.args = [arg0, arg1, arg2]

    def __teal__(self):
        cond = self.args[0].__teal__()
        l1 = new_label()
        t_branch = self.args[1].__teal__()
        e_branch = self.args[2].__teal__()
        l2 = new_label()
        # TODO: remove pop if teal check is removed
        ret = cond + [["bnz", l1]] + e_branch + [["int", "1"]] + \
              [["bnz", l2], ["pop"], [l1+":"]] + t_branch + [[l2+":"]]
        return ret

    def __str__(self):
        return "(If {} {} {})".format(self.args[0], self.args[1], self.args[2])

    def type_of(self):
        return self.args[1].type_of()
