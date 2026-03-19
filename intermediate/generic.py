from typing import TypeVar

T = TypeVar('T', int, str, list[str])

def add(a: T, b: T) -> T:
    return a


from typing import List, assert_type

assert_type(add(1, 2), int)
assert_type(add("1", "2"), str)
assert_type(add(["1"], ["2"]), List[str])
#assert_type(add(1, "2"), int)  # expect-type-error