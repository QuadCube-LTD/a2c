from typing import Any, Callable


class Array(list):
    def __init__(self, *args):
        super().__init__(list(args))

    def map_(self, func: Callable) -> "Array":
        return Array(*(func(n) for n in self))

    def join_(self, sep: str = "") -> str:
        return sep.join(str(n) for n in self)
