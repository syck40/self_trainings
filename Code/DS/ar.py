import ctypes

class DynamicArray:
    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)


    def __len__(self):
        return self._n
    def __getitem__(self, k):
        return self._A[k]
    def __repr__(self):
        return " ".join([str(self._A[i]) for i in range(self._n)])
    def _make_array(self, c):
        return (c * ctypes.py_object)()
    def _resize(self):
        b = self._make_array(self._capacity * 2)
        for i in range(len(self._A)):
            b[i] = self._A[i]
        self._A = b
        self._capacity = self._capacity * 2
    def append(self, obj):
        if self._n == self._capacity:
            self._resize()
        self._A[self._n] = obj
        self._n += 1

ab = DynamicArray()
ab.append(5)
ab.append(6)
ab.append("abc")
ab.append("gg")
print(ab[2])
print(ab)
