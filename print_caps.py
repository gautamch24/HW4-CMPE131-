
from print_caps import allcaps

def allcaps(func):
    def innerfunc():
        func()
        return "hello World!"
    return innerfunc()
    
