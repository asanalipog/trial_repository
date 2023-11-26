from dataclasses import dataclass


@dataclass
class User:
    user_id: int
    name: str
    age: int
    email: str


def cout(name:str, age :int) -> str:
  return name
name = input()
age  = int(input())
print(cout(name , age))
print("yes")
def get_tuple(lst: list[float | bool]) -> tuple[int]:
    return tuple(int(num) for num in lst)