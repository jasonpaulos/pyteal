from .ast import Expr

def compile(ast: Expr):
    teal = ast.__teal__()

    lines = [i.assemble() for i in teal]
    return "\n".join(lines)
