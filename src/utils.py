import math
from numbers import Number
from typing import List, Sequence, TypedDict

Matrix2d = Sequence[Sequence[Number]]

class Vector(TypedDict):
    x: float
    y: float
    z: float


def ceil(x: Number, digit: int = 0) -> Number:
    return math.floor(x * 10**(digit)) / (10**(digit))


def average(list: Sequence[Number]) -> float:
    return sum(list) / len(list)


def T(matrix: Matrix2d) -> Matrix2d:
    """
    転置行列
    """
    if len(matrix) == 0:
        return []

    len_colum = len(matrix[0])
    return [[row[i] for row in matrix] 
                    for i in range(len_colum)]


def join_number(list: List[Number], sep: str = "") -> str:
    return sep.join(str(n) for n in list)
