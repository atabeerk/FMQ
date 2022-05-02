

import timeit

from QueryGenerator import QueryGenerator as qg

from QueryExpander import QueryExpander


def timer_func(func):
    def function_timer(*args, **kwargs):
        start = timeit.default_timer()
        value = func(*args, **kwargs)
        end = timeit.default_timer()
        runtime = end - start
        msg = "{func} took {time} seconds to complete its execution"
        print(msg.format(func = func.__name__,time = runtime))
        return value
    return function_timer


from PatternTable import *

@timer_func
def timed_create_pattern_table(data):
    _pt = PatternTable(data)

@timer_func
def timed_search_random_query(pt: PatternTable, query, columns):
    qe = QueryExpander()
    queries = qe.expand(query, columns)
    _result = pt.search(queries)



def bench_create_pattern_table():
    for i in range(10, 51, 5):
        data = list(np.random.randint(2, size=(i**3, 5)))
        timed_create_pattern_table(data)

def bench_search_naive_query():
    for i in range(1, 5):
        columns = 2*i
        for r in range(1, 5):
            rows = columns * 10 * (r ** 2)
            data = list(np.random.randint(2, size=(rows, columns)))
            pt = PatternTable(data)
            query = qg.and_generator(columns, 1)
            print(f"Data: {rows}x{columns}")
            print(query)
            timed_search_random_query(pt, query, columns)



# bench_create_pattern_table()
bench_search_naive_query()



