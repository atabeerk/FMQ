import os
import csv
from sympy import *
from scipy.io import mmread
import numpy as np

from QueryExpander import QueryExpander
from PatternTable import PatternTable
from QueryParser import QueryParser
from QueryGenerator import QueryGenerator
from NaiveSearch import NaiveSearch

MTX_DIR = 'raw_feature_bc_matrix'

def read_sparse_matrix(mtx_dir):
    data = mmread(os.path.join(mtx_dir, 'matrix.mtx'))
    data = data.toarray()

    genes_path = os.path.join(MTX_DIR, "features.tsv")
    gene_ids = [row[0] for row in csv.reader(open(genes_path), delimiter="\t")]
    gene_names = [row[1] for row in csv.reader(open(genes_path), delimiter="\t")]

    barcodes_path = os.path.join(MTX_DIR, "barcodes.tsv")
    barcodes = [row[0] for row in csv.reader(open(barcodes_path), delimiter="\t")]

    return data, gene_ids, gene_names, barcodes


# qp = QueryParser()
qe = QueryExpander()
qg = QueryGenerator()

# query = qg.naive_generator(5)
query = qg.expr_generator(5, 3)
# query = qg.or_generator(5)
# print(query)
queries = qe.expand(query, 5)

# data = list(np.random.randint(2, size=(10, 5)))

data, _, _, _ = read_sparse_matrix(MTX_DIR)

pt = PatternTable(data)
ns = NaiveSearch(data)

pt_result = pt.search(queries)
ns_result = ns.search(query)

pt.save()

print(data)
print(pt_result)
print(ns_result)





