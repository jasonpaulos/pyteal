"""
pyteal expressions

"""

from abc import ABC, abstractmethod
from enum import Enum
from typing import List, TYPE_CHECKING

from ..types import TealType
from ..ir import TealComponent
if TYPE_CHECKING:
    from .astvisitor import ASTVisitor

class Expr(ABC):

    @abstractmethod
    def accept(self, visitor: 'ASTVisitor'):
        pass

    @abstractmethod
    def type_of(self) -> TealType:
        """Returns a TealType enum describing the expression's return type
        """
        pass

    @abstractmethod
    def __str__(self) -> str:
        """Returns the string representation of the experssion
        """
        pass
    
    def __lt__(self, other):
        from .binaryexpr import Lt
        return Lt(self, other)

    def __gt__(self, other):
        from .binaryexpr import Gt
        return Gt(self, other)

    def __le__(self, other):
        from .binaryexpr import Le
        return Le(self, other)

    def __ge__(self, other):
        from .binaryexpr import Ge
        return Ge(self, other)

    def __eq__(self, other):
        from .binaryexpr import Eq
        return Eq(self, other)

    def __add__(self, other):
        from .binaryexpr import Add
        return Add(self, other)

    def __sub__(self, other):
        from .binaryexpr import Minus
        return Minus(self, other)

    def __mul__(self, other):
        from .binaryexpr import Mul
        return Mul(self, other)

    def __truediv__(self, other):
        from .binaryexpr import Div
        return Div(self, other)

    def __mod__(self, other):
        from .binaryexpr import Mod
        return Mod(self, other)
    
    @abstractmethod
    def __teal__(self) -> List[TealComponent]:
        """Assemble teal IR"""
        pass

    # get teal program string
    def teal(self):
        from ..compiler import compile
        return compile(self)
       
    # logic and
    def And(self, other):
        from .and_ import And
        return And(self, other)

    # logic or
    def Or(self, other):
        from .or_ import Or
        return Or(self, other)
