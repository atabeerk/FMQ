
from sympy import *
from QueryExpander import QueryExpander
from PatternTable import PatternTable
from QueryParser import QueryParser
import numpy as np


qp = QueryParser()
qe = QueryExpander()
f0 = qp.parse("g0 & g1 & (~g2 | g4)")
n = 5
g = symbols(f"g:{n}")
f0 = g[0] & g[1] & (~g[2] | g[4])

queries = qe.expand(f0, 5)


data = list(np.random.randint(2, size=(10, 5)))
pt = PatternTable(data)
print(pt.search(queries))
# pt.save("data.pt")
# pt = PatternTable.load("data.pt")
# print(pt.search(queries))

