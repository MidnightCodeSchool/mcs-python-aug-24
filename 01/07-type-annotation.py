"""
Advanced topic skippable for beginners.
"""
def sum(a: int, b: int) -> bool:
    """
    Sum two numbers.
    """

    if not isinstance(a, int):
        raise TypeError("a is not an integer")
    if not isinstance(b, int):
        raise TypeError("b is not an integer")

    return a + b

print(sum(5, 6.1111))