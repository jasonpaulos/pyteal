from ..types import TealType
from .expr import LeafExpr

class ScratchSlot:

    slotId = 0

    def __init__(self):
        self.id = ScratchSlot.slotId
        ScratchSlot.slotId += 1

    def store(self):
        return ScratchStore(self)

    def load(self, type: TealType = TealType.anytype):
        return ScratchLoad(self, type)
    
    def __str__(self):
        return "slot#{}".format(self.id)
    
    def __eq__(self, other):
        if isinstance(other, ScratchSlot):
            return self.id == other.id
        return False
    
    def __hash__(self):
        return hash(self.id)

class ScratchLoad(LeafExpr):

    def __init__(self, slot: ScratchSlot, type: TealType = TealType.anytype):
        self.slot = slot
        self.type = type

    def __str__(self):
        return "(Load {})".format(self.slot.__str__())

    def __teal__(self):
        from ..ir import TealOp, Op
        return [TealOp(Op.load, self.slot)]

    def type_of(self):
        return self.type

class ScratchStore(LeafExpr):

    def __init__(self, slot: ScratchSlot):
        self.slot = slot

    def __str__(self):
        return "(Store {})".format(self.slot.__str__())

    def __teal__(self):
        from ..ir import TealOp, Op
        return [TealOp(Op.store, self.slot)]

    def type_of(self):
        return TealType.none
