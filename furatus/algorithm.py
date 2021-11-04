import random
import string

def rand(minlen: int, maxlen: int):
    """Generates endless random codes (iterable)"""
    chars = list(string.ascii_lowercase)
    chars.extend(string.digits)
    codes = []
    while True:
        code = ""
        for i in range(random.randint(minlen, maxlen)):
            code += random.choice(chars)
        yield code