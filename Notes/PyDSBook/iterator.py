class Progression():
    def __init__(self, start=0):
        self._current = start
    def _advance(self):
        self._current += 1

    def __next__(self):
        if self._current == None:
            raise StopIteration()
        else:
            self._advance()
            answer = self._current
            return answer
    
    def __iter__(self):
        return self

class ArithmaticProgression(Progression):
    def __init__(self, increment=1, start=0):
        super().__init__(start=start)
        self._incre = increment
    
    def _advance(self):
        self._current += self._incre

class FibProgression(Progression):
    def __init__(self, first=0, second=1):
        super().__init__(first+second)
        self._second = second
    
    def _advance(self):
        print('insid')
        self._current = self._current + self._second
        #self._second = self._current




a = FibProgression()
for i in a:
    if i > 15:
        break
    print(i)
l1 =['a','b',3]
l2 = list(l1)
l2.append('apple')
l2[2] = 4
print(l1,l2)
