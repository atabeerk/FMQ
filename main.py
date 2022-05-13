import timeit

import scipy.sparse as ss
import numpy as np

from QueryExpander import QueryExpander
from PatternTable import PatternTable
from QueryGenerator import QueryGenerator
from NaiveSearch import NaiveSearch

qe = QueryExpander()
qg = QueryGenerator()

limits = {5: [1,2,3,4,5], 9: [1,3,5,7,9], 12: [1,4,8,10,12], 15:[1,4,8,11,15]}

for c in [5, 9, 12, 15]:
    cons_times = []
    COLUMNS = c
    for r in [250000, 500000, 750000, 1000000]:
        ROWS = r
        data = ss.random(ROWS, COLUMNS, 0.5, data_rvs=np.ones, dtype='f').astype('int8')
        data = data.toarray()
        ns = NaiveSearch(data)
        pt = PatternTable(data)

        count = 0
        ns_total_time = 0
        pt_total_time = 0
        expansion_total_time = 0
        ns_varying_length_times = []
        pt_varying_length_times = []
        expansion_times = []
        symbols_in_query = []

        for i in limits[c]:
            count += 1
            print(i)
            symbols_in_query.append(i)
            ns_curr_length_time = 0
            pt_curr_length_time = 0
            curr_length_expansion_time = 0
            for j in range(5):
                query = qg.and_generator(i, 1)

                # measure query expansion
                start = timeit.default_timer()
                queries = qe.expand(query, COLUMNS)
                end = timeit.default_timer()
                curr_length_expansion_time += end - start

                # measure pt search
                start = timeit.default_timer()
                r1 = pt.search(queries)
                end = timeit.default_timer()
                pt_curr_length_time += end - start

                start = timeit.default_timer()
                r2 = ns.search(query)
                end = timeit.default_timer()
                ns_curr_length_time += end - start

                if not np.array_equal(r1, r2):
                    print("***ERROR***")
                    print(r1)
                    print(r2)
                    print("***********")

            ns_varying_length_times.append(ns_curr_length_time)
            pt_varying_length_times.append(pt_curr_length_time)
            expansion_times.append(curr_length_expansion_time)
            ns_total_time += ns_curr_length_time
            pt_total_time += pt_curr_length_time
            expansion_total_time += curr_length_expansion_time

        print(f"rows x columns: {ROWS}x{COLUMNS}")
        print(f"Queries with {count} different lengths, 5 of each total of queries")
        print(f"NS total time for each different length query:", ns_varying_length_times)
        print(f"NS total of time: {ns_total_time}")
        print(f"PT total time for each different length query:", pt_varying_length_times)
        print(f"PT total of time: {pt_total_time}")
        print(f"Expansion total time for each different length query:", expansion_times)
        print(f"Expansion total of time: {expansion_total_time}")
        print()
        print()







