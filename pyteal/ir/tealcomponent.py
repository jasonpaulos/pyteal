from abc import ABC, abstractmethod
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from ..ast import ScratchSlot

class TealComponent(ABC):

    def getSlots(self) -> List['ScratchSlot']:
        return []
    
    def assignSlot(self, slot: 'ScratchSlot', location: int):
        pass
    
    @abstractmethod
    def assemble(self) -> str:
        pass
