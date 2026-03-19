from typing import ClassVar

class Foo:
    """Hint: No need to write __init__"""
    bar: ClassVar[int] = 0


Foo.bar = 1
#Foo.bar = "1"  # expect-type-error
#Foo().bar = 1  # expect-type-error