from typing import Callable, TypeVar, ParamSpec
P = ParamSpec('P')
R = TypeVar('R')
def decorator(func: Callable[P, R]) -> Callable[P, R]:
    return func


@decorator
def foo(a: int, *, b: str) -> None:
    ...


@decorator
def bar(c: int, d: str) -> None:
    ...


foo(1, b="2")
bar(c=1, d="2")

#foo(1, "2")  # expect-type-error
#foo(a=1, e="2")  # expect-type-error
#decorator(1)  # expect-type-error