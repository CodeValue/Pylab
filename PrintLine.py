import inspect

def print_line():
    """Returns the current line number in our program."""
    return "Line {0}: ".format(inspect.currentframe().f_back.f_lineno)

