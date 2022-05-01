
from sympy import *
import numpy as np
from QueryExpander import QueryExpander
from PatternTable import PatternTable
from QueryParser import QueryParser
from QueryGenerator import QueryGenerator
from NaiveSearch import NaiveSearch



# qp = QueryParser()
qe = QueryExpander()
qg = QueryGenerator()

for i in range(500):
    # query = qg.naive_generator(5)
    query = qg.expr_generator(5, 3)
    # query = qg.or_generator(5)
    # print(query)
    queries = qe.expand(query, 5)

    data = list(np.random.randint(2, size=(10, 5)))
    pt = PatternTable(data)
    ns = NaiveSearch(data)

    pt_result = pt.search(queries)
    ns_result = ns.search(query)
    if not(pt_result == ns_result):
        print(data)
        print(pt_result)
        print(ns_result)





