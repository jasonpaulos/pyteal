from typing import List

from .expr import Expr

class NaryExpr(Expr):
    def __init__(self, args: List[Expr]):
        self.args = args

    def accept(self, visitor):
        for arg in self.args:
            arg.accept(visitor)
        visitor.visitLeafExpr(self)
