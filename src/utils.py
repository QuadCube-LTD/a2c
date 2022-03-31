import math
from numbers import Number
from typing import Sequence


Matrix2d = Sequence[Sequence[Number]]


def ceil(x: Number, digit: int = 0) -> Number:
    return math.floor(x * 10**(digit)) / (10**(digit))


def average(list: Sequence[Number]) -> float:
    return sum(list) / len(list)


def T(matrix: Matrix2d) -> Matrix2d:
    """
    転置行列
    """
    len_colum = len(matrix[0])
    return [[row[i] for row in matrix] 
                    for i in range(len_colum)]
