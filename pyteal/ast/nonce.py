from .expr import Expr
from ..ir import TealOp, Op
from .bytes import Bytes

class Nonce(Expr):

    #default constructor
    def __init__(self, base:str, nonce:str, child:Expr) -> None:
        self.child = child
        self.nonce_bytes = Bytes(base, nonce)

    def __teal__(self):
        return self.nonce_bytes.__teal__() + [TealOp(Op.pop)] + self.child.__teal__()
        
    def __str__(self):
        return "(nonce: {}) {}".format(self.nonce_bytes.__str__(), self.child.__str__())

    def type_of(self):
        return self.child.type_of()
