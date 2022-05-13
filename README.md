# Fast Matrix Querying (FMQ)

Given an `NxM` sparse matrix `S`, and set of query `Q` in the form of a logical expressions containing symbols corresponding to
columns, find the set of rows that satisfy Q.

Our proposed approach `Pattern-Based Search` creates a pattern table (`PatternTable.py`) out of `S`. Then for each query `Q` (`QueryGenerator.py`), expands this 
query (`QueryExpander.py`) into a set of queries and extracts the corresponding entries in the pattern table.

To install required python libraries, `pip install -r requirements.txt`

Example use:
    
    import scipy.sparse as ss
    import numpy as np
    
    from QueryExpander import QueryExpander
    from PatternTable import PatternTable
    from QueryGenerator import QueryGenerator
    from NaiveSearch import NaiveSearch


    rows, columns = 500000, 5 
    # create random sparse data
    data = ss.random(rows, columns, 0.01, data_rvs=np.ones, dtype='f').astype('int8')
    data = data.toarray()    

    qe = QueryExpander()
    qg = QueryGenerator()
    
    # generate a random expression and expand it
    query = qg.expr_generator(5, 3)
    queries = qe.expand(query, 5)
     
    pt = PatternTable(data)
    ns = NaiveSearch(data)
    
    # search using the naive method and the Pattern-Based Search
    pt_result = pt.search(queries)
    ns_result = ns.search(query)

### main.py

To replicate all the experiments simply run the main.py, the results will be printed to standard output. No input file is 
required, random data matrices with varying sizes will be generated for each experiment.
Total run time may be up to 18 hours.   

### NaiveSearch.py

Contains the implementation for the naive search. This method goes row by row and at each row, substitutes
the column values into corresponding variables into Q and checks if it evaluates to true. 

### Pattern Table

Contains the implementation for constructing and searching the pattern table. It exposes `load`, `save` and `search` interfaces over the Pattern Table Objects.

### Query Expander

Given a raw query, `Query Expander` provides a list of valuations resulting in `True`. It exposes the `expand` interface.

### Query Generator

Query Generator is a random generator object that creates logical formulas. It's used for evaluation and testing.

### Benchmark

Benchmark contains an early implementation of our evaluation strategy. This implementation now takes place in `main.py`.
