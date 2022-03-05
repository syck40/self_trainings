"""
adjacency list
a: [b,c]
a -> b -> d -> f
|
c
|
e
b,c -> c
f,
g, i
g, g, k

k -> i -> j
"""
graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}

def get_graph(g, starting):
    qq = [starting]
    ret = [starting]
    while qq:
        val = qq.pop(0)
        for vv in g[val]:
            ret.append(vv)
            qq.append(vv)
    print(ret)
#get_graph(graph, "a")
def recurs(g, starting):
    print(starting)
    for ii in g[starting]:
        recurs(g, ii)
recurs(graph,"a")
