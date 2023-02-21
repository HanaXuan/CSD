import ctypes
from random import randint
class D_Array:
    def __init__(self):
        self._size= 0
        self._capacity=1
        self._element= self._makeArray(self._capacity)
    def _makeArray(self,capacity):
        return (capacity * ctypes.py_object)()
    def showInfo(self):
        print("\n actual number of element:", self._size)
        print("\n capacity :",self._capacity)
        for i in range(self._size):
            print(" ", self._element[i],end=" ")
    def __len__(self):
        return self._size
    def __getitem__(self, i):
        if not self._size< i< 0:
            raise IndexError('sai index roi kia')
        return  self._element[i]
    def _reSize(self,capacity):
        newArray= self._makeArray(capacity)
        for i in range(self._size):
            newArray[i]= self._element[i]
        self._element= newArray
        self._capacity= capacity
    def append(self, value):
        if self._size== self._capacity:
            self._reSize(2*self._capacity)
        self._element[self._size]=value
        self._size+= 1
    def insert(self, index, value):
        if self._size== self._capacity:
            self._reSize(2*self._capacity)
        for i in range(self._size, index, -1):
            self._element[i]= self._element[i-1]
        self._element[index]= value
        self._size +=1
    def remove_value(self, value):
        for i in range(self._size):
            if self._element[i] == value:
                for j in range(i,self._size-1):
                    self._element[j]= self._element[j+1]
                self._element[self._size-1]= None
                self._size -=1
                return
        raise ValueError('Value ko tim thay')
    def remove_index(self, index):
        if index<= self._size:
            for i in range(index, self._size-1):
                self._element[i]= self._element[i+1]
            self._element[self._size-1]= None
            self._size -=1
        else:
            print('chung toi ko tim thay')
arr= D_Array()
arr.showInfo()
for i in range(10):
    arr.append(randint(0,20))
arr.showInfo()
arr.insert(1,9999)
arr.showInfo()