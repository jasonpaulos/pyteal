from ..types import TealType, valid_address
from .expr import LeafExpr
from .tmpl import Tmpl

class Addr(LeafExpr):
     
    # default constructor
    def __init__(self, address) -> None:        
        if isinstance(address, Tmpl):
            self.address = address.name
        else:
            valid_address(address)
            self.address = address

    def __teal__(self):
        return [["addr", self.address]]

    def __str__(self):
        return "(address: {})".format(self.address)

    def type_of(self):
        return TealType.bytes