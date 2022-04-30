from sympy import *
from sympy.logic.boolalg import truth_table
import numpy as np


class QueryExpander:
    def __init__(self):
        pass

    def expand(self, query, n):
        variables = symbols(f"g:{n}")
        bitmaps = np.array(list(map(
            lambda x: x[0],
            filter(
                lambda x: x[1],
                list(truth_table(query, variables))
            )
        )))

        return np.packbits(bitmaps, axis=1)

