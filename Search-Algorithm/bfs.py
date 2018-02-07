def walk(G, s, S=set()):
    P, Q = dict(), set()
    P[s] = None  
    Q.add(s)  
    while Q:
        u = Q.pop() 
        for v in G[u].difference(P, S): 
            Q.add(v)
            P[v] = u 
    return P
def components(G):
    comp = []
    seen = set()
    for u in range(9):
        if u in seen: continue
        C = walk(G, u)
        seen.update(C) 
        comp.append(C)
    return comp
if __name__ == "__main__":
    a, b, c, d, e, f, g, h, i = range(9)
    N = [
        {b, c, d},  
        {a, d},  
        {a, d}, 
        {a, c, d}, 
        {g, f},  
        {e, g},  
        {e, f},  
        {i},  
        {h}  
    ]
    comp = components(N)
    print(comp)
