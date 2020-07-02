from .ast import Expr
from .errors import TealInternalError

NUM_SLOTS = 256

def compile(ast: Expr):
    teal = ast.__teal__()

    slots = set()
    for stmt in teal:
        for slot in stmt.getSlots():
            slots.add(slot)
    
    if len(slots) > NUM_SLOTS:
        # TODO: identify which slots can be reused
        raise TealInternalError("Not yet implemented")
    
    location = 0
    while len(slots) > 0:
        slot = slots.pop()
        for stmt in teal:
            stmt.assignSlot(slot, location)
        location += 1

    lines = [i.assemble() for i in teal]
    return "\n".join(lines)
