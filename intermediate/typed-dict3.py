from typing import TypedDict, NotRequired

class Person(TypedDict):
    name: str
    age: NotRequired[int]
    gender: NotRequired[str]
    address: NotRequired[str]
    email: NotRequired[str]


a: Person = {
    "name": "Capy",
    "age": 1,
    "gender": "Male",
    "address": "earth",
    "email": "capy@bara.com",
}
#a: Person = {"name": "Capy"}
# fmt: off
#a: Person = {"age": 1, "gender": "Male", "address": "", "email": ""} # expect-type-error    