flavors = ["Vanila", "Chocolate", "Orange", "s2", "s1", "s5"]

class Scope():
    """This is class"""
    def __init__(self, flavor):
        self.flavor = flavor
    def __repr__(self) -> str:
        return "".join("Flavor of the scope is " + self.flavor)

class Bowl():
    """Has list of scopes and add scope"""
    def __init__(self, max_scope=3):
        self.max_scopes = max_scope
        self.scopes = []

    def __repr__(self):
        return "\t".join([str(ss) for ss in self.scopes])

    def add_scope(self, scope):
        if len(self.scopes) < self.max_scopes:
            self.scopes.append(scope)

class BigBowl(Bowl):
    def __init__(self, max_scope=5):
        super().__init__(max_scope)

def gen_class(num):
    return [Scope(flavors[i]) for i in range(num)]
    
if __name__ == "__main__":
    s = gen_class(3)
    [print(ss) for ss in s]
    b1 = Bowl()
    [b1.add_scope(ss) for ss in s]
    print(b1)
    bb1 = BigBowl()
    bb1.add_scope(Scope("Special"))
    ss2 = gen_class(5)
    [bb1.add_scope(ss22) for ss22 in ss2]
    print(bb1)
