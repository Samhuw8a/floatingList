from __future__ import annotations
from typing import Union

ListItem = Union[int, float, str]

class FloatingList(list):
    # generate all list relevant methods and raise a not implemented error in the body of the method

    
    def __init__(self, *args):
        super().__init__(*args)
    
    @classmethod
    def interpolate(cls, a: ListItem, b:ListItem, t: float) -> ListItem:
        """
        Interpolates between two ListItems a and b by a factor of t (0 <= t <= 1).
        """

        match (a, b):

            case (int() | float(), int()|float()):
                raise NotImplementedError("This method is not implemented yet")

            case (float(), str()):
                raise NotImplementedError("This method is not implemented yet")
            case (str(), float()):
                raise NotImplementedError("This method is not implemented yet")

            case (int(), str()):
                raise NotImplementedError("This method is not implemented yet")
            case (str(), int()):
                raise NotImplementedError("This method is not implemented yet")

            case (str(), str()):
                raise NotImplementedError("This method is not implemented yet")

            case _:
                raise TypeError("Unsupported types for interpolation")


    def __getitem__(self, key):
        raise NotImplementedError("This method is not implemented yet")

    def __setitem__(self, key, value):
        raise NotImplementedError("This method is not implemented yet")
    
    def __delitem__(self, key):
        raise NotImplementedError("This method is not implemented yet")

    def __len__(self):
        raise NotImplementedError("This method is not implemented yet")

    def append(self, item):
        raise NotImplementedError("This method is not implemented yet")

    def extend(self, iterable):
        raise NotImplementedError("This method is not implemented yet")

    def insert(self, index, item):
        raise NotImplementedError("This method is not implemented yet")

    def remove(self, item):
        raise NotImplementedError("This method is not implemented yet")

    def pop(self, index=-1):
        raise NotImplementedError("This method is not implemented yet")

    def clear(self):
        raise NotImplementedError("This method is not implemented yet")

    def index(self, item, start=0, end=None):
        raise NotImplementedError("This method is not implemented yet")

    def count(self, item):
        raise NotImplementedError("This method is not implemented yet")

    def sort(self, *, key=None, reverse=False):
        raise NotImplementedError("This method is not implemented yet")

    def reverse(self):
        raise NotImplementedError("This method is not implemented yet")
