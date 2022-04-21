import DynamicArray
import math
import numpy as np
from functools import reduce

dynamicArray = DynamicArray.DynamicArray


class fun_dynamicarray(dynamicArray):

    def __init__(self):
        """"Initialzes"""
        dynamicArray.__init__(self)

    # 1. add a new element
    def insert(self, key, value):
        dynamicArray.insert(self, key, value)

    # 2. remove an element
    def deleteindex(self, key):
        if (self._len_() < key):
            print("key is out of range")
            return
        self.pop(key)

    def deletevalue(self, value):
        self.remove(value)

    # 3. size
    def size(self):
        return (self._len_())

    # 4.ismember
    def ismember(self, value):
        for k in range(self.n):
            if self.A[k] == value:
                return True
        return False

    # 5.reverse
    def reverse(self):
        for i in range(int(self.size() / 2)):
            num = self.A[i]
            self.A[i] = self.A[self.size() - i - 1]
            self.A[self.size() - i - 1] = num
        return self

    # 6. conversion from and to python lists
    def from_list(self, list):
        for i in range(len(list)):
            self.insert(i, list[i])

    def to_list(self):
        ls = {}
        for i in range(self.size()):
            ls[i] = self.A[i]
        return ls

    # 7. find element by specific predicate
    def find_value(self, key):
        if key >= self.n or key < 0:
            raise ValueError('invalid index')
        return self.A[key]

    def find_key(self, value):
        for k in range(self.n):
            if self.A[k] == value:
                return k
        return False

    # 8. filter data structure by specific predicate
    def value_is_odd(self, n):
        return n % 2 == 1

    def value_is_even(self, n):
        return n % 2 == 0

    def is_sqr(self, x):
        return math.sqrt(x) % 1 == 0

    def filter_func(self, fun):
        arr = np.zeros((self.size()))
        for i in range(self.size()):
            arr[i] = self.A[i]
        newlist = filter(fun, arr)
        for i in newlist:
            self.deletevalue(i)

    # 9. map structure by specific function
    def square(self, x):
        return x ** 2

    def map_func(self, fun):
        arr = np.zeros((self.size()))
        for i in range(self.size()):
            arr[i] = self.A[i]
        newlist = map(fun, arr)
        func = fun_dynamicarray()
        j = 0
        for i in newlist:
            func.insert(j, i)
            j = j + 1
        return func

    # 10. reduce – process structure elements to build a return value by
    # specific functions
    def add(self, x, y):
        return x + y

    def reduce_func(self, func):
        arr = np.zeros((self.size()))
        for i in range(self.size()):
            arr[i] = self.A[i]
        sum = reduce(func, arr)
        return sum

    # 11. iterator
    def __iter__(self):
        self.num = -1
        return self

    def next(self):
        self.num = self.num + 1
        return self.A[self.num]

    # 12. mempty and mconcat
    def mempty(self):
        self = None
        return self

    def mconcat(self, a):
        if self is None:
            return a
        elif a is None:
            return self
        else:
            arr = np.zeros((a.size()))
            for i in range(a.size()):
                arr[i] = a.A[i]
            j = self.size()
            for i in arr:
                self.insert(j, i)
                j = j + 1
            return self
