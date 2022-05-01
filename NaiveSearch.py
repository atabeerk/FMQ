

class NaiveSearch:
    def __init__(self, raw_matrix):
        self.raw_matrix = raw_matrix

    def search(self, query):
        result = set()
        symbol_values = {}
        # substitute each binary symbol with its corresponding value for each row
        for i, row in enumerate(self.raw_matrix):
            for symbol in query.binary_symbols:
                symbol_values[symbol] = row[self.__get_column(symbol)]
            if query.subs(symbol_values):
                result.add(i)

        return result

    @staticmethod
    def __get_column(symbol):
        return int(str(symbol)[1:])
