from typing import Literal

def foo(direction: Literal["left", "right"]):
    ...


foo("left")
foo("right")

a = "".join(["l", "e", "f", "t"])
#foo(a)  # expect-type-error