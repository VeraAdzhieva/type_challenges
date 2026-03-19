class Foo:
    """Hint: you don't need to write __init__"""
    bar: int   



foo = Foo()
foo.bar = 1
#foo.bar = "1"  # expect-type-error 