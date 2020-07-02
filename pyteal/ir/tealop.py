from typing import cast, Union, List, TYPE_CHECKING

from .tealcomponent import TealComponent
from .ops import Op
from ..errors import TealInternalError
if TYPE_CHECKING:
    from ..ast import ScratchSlot

OpArg = Union[int, str, 'ScratchSlot']

class TealOp(TealComponent):
    
    def __init__(self, op: Op, *args: OpArg) -> None:
        self.op = op
        self.args = list(args)
    
    def getSlots(self) -> List['ScratchSlot']:
        from ..ast import ScratchSlot
        return [arg for arg in self.args if isinstance(arg, ScratchSlot)]
    
    def assignSlot(self, slot: 'ScratchSlot', location: int):
        for i, arg in enumerate(self.args):
            if slot == arg:
                self.args[i] = location

    def assemble(self) -> str:
        from ..ast import ScratchSlot
        parts = [self.op.value]
        for arg in self.args:
            if isinstance(arg, ScratchSlot):
                raise TealInternalError("Slot not assigned: {}".format(arg))
            
            if isinstance(arg, int):
                parts.append(str(arg))
            else:
                parts.append(arg)

        return " ".join(parts)
