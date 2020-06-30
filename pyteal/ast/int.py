from ..types import TealType
from ..errors import TealInputError
from .expr import LeafExpr
from .tmpl import Tmpl

class Int(LeafExpr):
     
    # default contructor
    def __init__(self, value):
        if isinstance(value, Tmpl):
            self.value = value.name
        elif type(value) is not int:
            raise TealInputError("invalid input type {} to Int".format(
                 type(value))) 
        elif value >= 0 and value < 2 ** 64:
             self.value = value
        else:
            raise TealInputError("Int {} is out of range".format(value))

    def __teal__(self):
        return [["int", str(self.value)]]
       
    def __str__(self):
        return "(Int: {})".format(self.value)

    def type_of(self):
        return TealType.uint64
