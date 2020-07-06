from ..types import TealType, valid_base16, valid_base32, valid_base64
from ..ir import TealOp, Op
from ..errors import TealInputError
from .leafexpr import LeafExpr
from .tmpl import Tmpl

class Bytes(LeafExpr):
     
    #default constructor
    def __init__(self, base:str, byte_str) -> None:
        if base == "base32":
            self.base = base
            if isinstance(byte_str, Tmpl):
                self.byte_str = byte_str.name
            else:
                valid_base32(byte_str)
                self.byte_str = byte_str
        elif base == "base64":
            self.base = base
            if isinstance(byte_str, Tmpl):
                self.byte_str = byte_str.name
            else:
                self.byte_str = byte_str
                valid_base64(byte_str)
        elif base == "base16":
            self.base = base
            if isinstance(byte_str, Tmpl):
                self.byte_str = byte_str.name
            elif byte_str.startswith("0x"):
                self.byte_str = byte_str[2:]
                valid_base16(self.byte_str)
            else:
                self.byte_str = byte_str
                valid_base16(self.byte_str)
        else:
            raise TealInputError("invalid base {}, need to be base32, base64, or base16.".format(base))

    def __teal__(self):
        if self.base != "base16":
            return [TealOp(Op.byte, self.base, self.byte_str)]
        else:
            return [TealOp(Op.byte, "0x" + self.byte_str)]
        
    def __str__(self):
        return "({} bytes: {})".format(self.base, self.byte_str)

    def type_of(self):
        return TealType.bytes
