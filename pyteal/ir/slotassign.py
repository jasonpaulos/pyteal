from ..ast import ASTVisitor, ScratchStore, ScratchLoad, ScratchSlot

NUM_SLOTS = 256

class SlotVisitor(ASTVisitor):
    def __init__(self):
        self.slots = set()
    
    def visitScratchStore(self, store: ScratchStore):
        self.slots.add(store.slot)

    def visitScratchLoad(self, load: ScratchLoad):
        self.slots.add(load.slot)
    
    def assign(self):
        pass
