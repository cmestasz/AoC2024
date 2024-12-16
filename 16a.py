import sys

dd = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def ss(me, i, j, s, ws, d, v, ei, ej):
    if (i, j,) in ws or v[i][j][d]:
        return float("inf")
    if i == ei and j == ej:
        return 0
    print(i+1, j+1, d)
    k = (i, j, d,)
    if k not in me:
        v[i][j][d] = True
        fr = 1 + ss(me, i + dd[d][0], j + dd[d][1], s, ws, d, v, ei, ej)
        d2 = (d + 1) % 4
        rr = 1001 + ss(me, i + dd[d2][0], j + dd[d2][1], s, ws, (d + 1) % 4, v, ei, ej)
        d2 = (d - 1) % 4
        rl = 1001 + ss(me, i + dd[d2][0], j + dd[d2][1], s, ws, (d - 1) % 4, v, ei, ej)
        v[i][j][d] = False
        mi = min(rr, rl, fr)
        if mi != fr:
            k = (i, j, d2,)
        me[k] = mi
    return me[k]

sys.setrecursionlimit(100000)
with open("16i.txt") as f:
    l = f.readline().strip()
    i = 0
    ws = set()
    w = len(l)
    while l != "":
        for j in range(len(l)):
            if l[j] == "#":
                ws.add((i, j,))
            elif l[j] == "S":
                s = [i,j,]
            elif l[j] == "E":
                e = [i,j,]
        i += 1
        l = f.readline().strip()
    me = {}
    v = [[[False for _ in range(4)] for _ in range(w)] for _ in range(i)]
    print(ss(me, s[0], s[1], s, ws, 0, v, e[0], e[1]))
