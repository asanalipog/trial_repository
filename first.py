from dataclasses import dataclass
from typing import Generic, TypeAlias, TypeVar

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
"""
The multiply function takes any number of inputs of int and multiply it together.
Comparison with multiply(a, b) it can take any number of inputs
As, I understood we can use any names instead of *args -> such as *name, etc.
"""
def multiply(*args:int):
  z = 1
  for num in args:
    z = z * num
  return z

"""
the **kwargs let us to control the inputs we will give to the function, however it is may be unordered.
"""
def print_values(**kwargs):
    for key, value in kwargs.items():
        print("The value of {} is {}".format(key, value))
print_values(my_name="Sammy", your_name="Casey",
            a = "Hui", b= "chlen")
@dataclass
class Hui:
  name:str
  length:int