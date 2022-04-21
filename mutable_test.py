import unittest
from lab1.mutable import fun_dynamicarray as fun_dynamicarray
import lab1.DynamicArray as DynamicArray
from functools import reduce
import numpy as np



class Testfunction(unittest.TestCase):



    def test_add(self):
        func =fun_dynamicarray()
        func.insert(0, 1)
        func.insert(1, 4)
        func.insert(2, 5)
        func.insert(3, 3)
        #display(func)

    def test_delete(self):
        func = fun_dynamicarray()
        func.insert(0, 1)
        func.insert(1, 4)
        func.insert(2, 5)
        func.insert(3, 3)
        #display(func)
        func.deleteindex(2)
        #display(func)
        func.deletevalue(1)
        #display(func)

    def test_size(self):
        func = fun_dynamicarray()
        func.insert(0, 1)
        func.insert(1, 4)
        func.insert(2, 5)
        func.insert(3, 3)
        #print(func.size())

    def test_reverse(self):
        func = fun_dynamicarray()
        func.insert(0, 1)
        func.insert(1, 4)
        func.insert(2, 5)
        func.insert(3, 3)
        func1=func.reverse()
        #display(func1)

    def test_from_list(self):
        list = [5,6]
        func = fun_dynamicarray()
        func.from_list(list)
        self.assertEqual(func.A[0], 5)
        self.assertEqual(func.A[1], 6)
        #display(func)

    def test_to_list(self):
        func = fun_dynamicarray()
        func.insert(0, 1)
        func.insert(1, 4)
        func.insert(2, 5)
        func.insert(3, 3)
        ls=func.to_list()
        ls1={}
        for i in range(func.size()):
            ls1[i]=func.A[i]
        self.assertEqual(ls1, ls)
        #display(func)

    def test_find(self):
        func = fun_dynamicarray()
        func.insert(0, 1)
        func.insert(1, 4)
        func.insert(2, 5)
        func.insert(3, 3)
        x=func.find_value(3)
        y=func.find_key(3)
        self.assertEqual(x, y)
        x1= func.find_value(1)
        y1= func.A[1]
        self.assertEqual(x1, y1)

    def test_filter_func(self):
        func = fun_dynamicarray()
        func.insert(0, 1)
        func.insert(1, 4)
        func.insert(2, 5)
        func.insert(3, 3)
        #func.filter_func(func.value_is_odd)
        #func.filter_func(func.value_is_even)
        func.filter_func(func.is_sqr)
        #display(func)

    def test_map_func(self):
        func = fun_dynamicarray()
        func.insert(0, 1)
        func.insert(1, 4)
        func.insert(2, 5)
        func.insert(3, 3)
        func1 = func.map_func(func.square)
        #display(func1)

    def test_reduce_func(self):
        func = fun_dynamicarray()
        func.insert(0, 1)
        func.insert(1, 4)
        func.insert(2, 5)
        func.insert(3, 3)
        sum = func.reduce_func(func.add)
        #print(sum)

    def test_iter(self):
        func = fun_dynamicarray()
        func.insert(0, 1)
        func.insert(1, 4)
        func.insert(2, 5)
        func.insert(3, 3)
        func.__iter__()
        #print(func.next())
        #print(func.next())
        #print(func.next())
        #print(func.next())

    def test_mempty(self):
        func = fun_dynamicarray()
        func.insert(0, 1)
        func.insert(1, 4)
        func.insert(2, 5)
        func.insert(3, 3)
        #self.assertEqual(func.mempty(), None)

    def test_mconcat(self):
        func = fun_dynamicarray()
        func.insert(0, 1)
        func.insert(1, 4)
        func.insert(2, 5)
        func.insert(3, 3)
        #display(func)
        func1 = fun_dynamicarray()
        func1.insert(0, 6)
        func1.insert(1, 7)
        #display(func1)
        func = func.mconcat(func1)
        #display(func)

def display(self):
    if not DynamicArray:
        return
    for i in range(self.size()):
        print(self.A[i])

if __name__ == '__main__':
        unittest.main()