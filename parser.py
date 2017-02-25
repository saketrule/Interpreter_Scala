## Parser driver program

from parsers import *

def parse(tokens):
    return parser()(tokens,0)
    
def parser():
    return Phrase(expr)