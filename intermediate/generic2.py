from typing import TypeVar
T2 = TypeVar('T2', int, str)

def add(a: T2, b: T2) -> T2:
    return a


from typing import assert_type

assert_type(add(1, 2), int)
assert_type(add("1", "2"), str)

#add(["1"], ["2"])  # expect-type-error
#add("1", 2)  # expect-type-error    