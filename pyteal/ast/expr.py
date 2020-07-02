"""
pyteal expressions

"""

from abc import ABC, abstractmethod
from enum import Enum
from typing import List

from ..types import TealType
from ..ir import TealComponent

class Expr(ABC):

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
         from .lt import Lt
         return Lt(self, other)

     def __gt__(self, other):
         from .gt import Gt
         return Gt(self, other)

     def __le__(self, other):
         from .le import Le
         return Le(self, other)

     def __ge__(self, other):
         from .ge import Ge
         return Ge(self, other)

     def __eq__(self, other):
         from .eq import Eq
         return Eq(self, other)

     def __add__(self, other):
         from .add import Add
         return Add(self, other)

     def __sub__(self, other):
         from .minus import Minus
         return Minus(self, other)

     def __mul__(self, other):
         from .mul import Mul
         return Mul(self, other)

     def __truediv__(self, other):
         from .div import Div
         return Div(self, other)

     def __mod__(self, other):
         from .mod import Mod
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

class BinaryExpr(Expr):
     pass

class UnaryExpr(Expr):
     pass

class NaryExpr(Expr):
     pass

class LeafExpr(Expr):
     pass
