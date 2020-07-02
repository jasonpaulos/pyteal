from .tealcomponent import TealComponent

class TealLabel(TealComponent):

    def __init__(self, label: str) -> None:
        self.label = label
    
    def assemble(self) -> str:
        return self.label + ":"
