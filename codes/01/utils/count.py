# count.py
from utils.function import add

def count_word(text: str, char: str) -> int:

    assert isinstance(text, str)
    assert isinstance(char, str) and len(char) == 1

    count = 0
    for c in text:
        if c == char:
            count = add(count, 1)
    return count


