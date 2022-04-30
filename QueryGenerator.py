
import random
import sympy as sp

class Binop:
    def __init__(self, id, op):
        self.id = id
        self.op = op


class QueryGenerator:
    def __init__(self):
        pass

    @staticmethod
    def atom_generator(i, p=1.0):
        if random.random() < p:
            return random.choice([sp.symbols(f"g{i}"), sp.Not(sp.symbols(f"g{i}"))])

    @staticmethod
    def naive_generator(size):
        return QueryGenerator.and_generator(size, 0)

    @staticmethod
    def and_generator(size, p=0.5):
        return QueryGenerator.binop_generator(Binop(sp.true, sp.And), 0, size, p)

    @staticmethod
    def or_generator(size, p=0.5):
        return QueryGenerator.binop_generator(Binop(sp.false, sp.Or), 0, size, p)

    @staticmethod
    def binop_generator(binop, left, right,  p=0.5):
        expr = binop.id
        for i in range(left, right):
            atom = QueryGenerator.atom_generator(i, p)
            if atom:
                expr = binop.op(expr, atom)
        return expr

    @staticmethod
    def expr_generator(size, depth=2, p=1.0):
        if random.random() > p:
            return None

        binop = random.choices([Binop(sp.false, sp.Or), Binop(sp.true, sp.And)], [1, 4])[0]
        new_size = size - int(size * p)
        left = random.randint(0, size - new_size)
        right = left + new_size
        if depth == 1:
            return QueryGenerator.binop_generator(binop, left, right, p)

        complex_expr = binop.id
        for i in range(size):
            expr = QueryGenerator.expr_generator(size, depth-1, p/2)
            if expr:
                complex_expr = binop.op(complex_expr, expr)

        return complex_expr