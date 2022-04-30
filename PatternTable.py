import numpy as np
import pickle

class PatternTable:
    def load(file_path):
        with open(file_path, "rb") as infile:
            return pickle.load(infile)

    def save(self, file_path):
        with open(file_path, "wb") as outfile:
            pickle.dump(self, outfile)

    def __init__(self, raw_matrix):
        self.raw_matrix = raw_matrix
        self.pattern_table = dict()
        for i, row in enumerate(raw_matrix):
            key = str(np.packbits(row))
            if key not in self.pattern_table.keys():
                self.pattern_table[key] = {i}
            else:
                self.pattern_table[key].add(i)

    def search(self, queries):
        result = set()
        for query in queries:
            result = result.union(self.get(query))

        return result

    def get(self, query):
        key = str(query)
        v = self.pattern_table.get(key)
        if v:
            return v
        return set()

    def __str__(self):
        return str(self.pattern_table)
