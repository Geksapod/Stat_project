import re


def y_verify(string: str):

    '''Return True if string contains at least 4 numbers at the beginning of the string.'''

    pattern = r"\d{4}"
    if re.match(pattern, string):
        return True


def y_clear(var: int|float|str):

    '''Return edited str of year that contains only 4 number'''

    if isinstance(var, str):
        if y_verify(var):
            return var[:4]
    elif isinstance(var, int | float):
        var = str(var)
        if y_verify(var):
            return var[:4]


def data_cleaning(number):

    '''Return number if it's int or float'''

    if isinstance(number, float | int):
        return number
