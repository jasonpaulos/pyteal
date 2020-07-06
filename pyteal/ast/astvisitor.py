from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .leafexpr import LeafExpr
    from .unaryexpr import UnaryExpr
    from .binaryexpr import BinaryExpr
    from .naryexpr import NaryExpr
    from .if_ import If
    from .cond import Cond
    from .scratch import ScratchLoad, ScratchStore

class ASTVisitor(ABC):

    def visitLeafExpr(self, expr: 'LeafExpr'):
        pass

    def visitUnaryExpr(self, expr: 'UnaryExpr'):
        pass

    def visitBinaryExpr(self, expr: 'BinaryExpr'):
        pass

    def visitNaryExpr(self, expr: 'NaryExpr'):
        pass
    
    def visitIf(self, expr: 'If'):
        pass

    def visitCond(self, expr: 'Cond'):
        pass
    
    def visitScratchLoad(self, expr: 'ScratchLoad'):
        pass

    def visitScratchStore(self, expr: 'ScratchStore'):
        pass
