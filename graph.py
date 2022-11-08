G = {
    1: {
        2: 7,
        3: 9,
        6: 14
    },
    2: {
        1: 7,
        3: 10
    },
    3: {
        1: 9,
        2: 10,
        6: 2
    },
    6: {
        1: 14,
        3: 2
    }
}
 
 
start = 1
D = {i: 1000 for i in G.keys() }
D[start] = 0
U = {i: False for i in G.keys() }
 
for _ in range(len(G.keys())):
    candidates = [k for k in U.keys() if not U[k]]
    min_k = min(candidates, key=lambda x: D[x])
 
    for v, l in G[min_k].items():
        if D[v] > D[min_k] + l:
            D[v] = D[min_k] + l
 
    U[min_k] = True
 
print(D)
