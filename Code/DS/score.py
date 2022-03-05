class GameEntry:
    def __init__(self, score, name):
        self._score = score
        self._name = name
    def get_name(self):
        return self._name
    def get_score(self):
        return self._score
    def __repr__(self):
        return " ".join([self._name, str(self._score)])

ge = GameEntry(12, "john")
print(ge)

class ScoreBoard:
    def __init__(self, capacity=3):
        self._capacity = capacity
        self._B = [None] * self._capacity
        self._position = 0

    def append(self, ge):
        if self._position == 0:
            self._B.append(ge)
            self._position += 1
        elif self._position < self._capacity:
            j = 1
            while self._B[self._position - j] < self._B[self._position] and self._position - j >= 0:
                self._B[self._position - j], self._B[self._position] = self._B[self._position], self._B[self._position - j]
                j += 1

def sortme():
    l1 = [1, 2, 3,4,55,8,34,332,12,9]
    #po = len(l1) - 1
    for k in range(1, len(l1)):
        cur = l1[k]
        j = k
        while j > 0 and l1[j-1] > cur:
            l1[j] = l1[j-1]
            j -= 1
        l1[j] = cur 
        
    print(l1)

sortme()
