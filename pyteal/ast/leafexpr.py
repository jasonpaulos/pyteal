from .expr import Expr

class LeafExpr(Expr):
    def accept(self, visitor):
        visitor.visitLeafExpr(self)
