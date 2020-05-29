from typing import Callable, Iterator


class MatrixIterator(Iterator):

    def __init__(self, fn: Callable[[int, int], bool], row_count, col_count, row_first=True):
        self.fn = fn
        self.row_count = row_count
        self.col_count = col_count
        self.i = 0
        self.j = 0
        self.row_first = row_first
        self.first_call = True

    def chain_and(self, fn: Callable[[int, int], bool]):
        def _chain_and(i, j):
            return self.fn(i, j) and fn(i, j)

        return MatrixIterator(_chain_and, self.row_count, self.col_count)

    def chain_or(self, fn: Callable[[int, int], bool]):
        def _chain_or(i, j):
            return self.fn(i, j) or fn(i, j)

        return MatrixIterator(_chain_or, self.row_count, self.col_count)

    def _set_next_entry(self):
        if self.row_first and self.j == self.col_count - 1:
            if self.i == self.row_count - 1:
                raise StopIteration
            self.i += 1
            self.j = 0
        elif self.row_first:
            self.j += 1
        if not self.row_first and self.i == self.row_count - 1:
            if self.j == self.row_count - 1:
                raise StopIteration
            self.j += 1
            self.i = 0
        elif not self.row_first:
            self.i += 1

    def __next__(self):
        if not self.first_call:
            self._set_next_entry()
        self.first_call = False
        while True:
            if self.fn(self.i, self.j):
                return self.i, self.j
            self._set_next_entry()
