def ss(t, m, co, v, l, i, j):
    if i < 0 or i >= l or j < 0 or j >= l:
        return
    v[i][j] = True
    if i + 1 < l and m[i + 1][j] == t:
        if not v[i + 1][j]:
            ss(t, m, co, v, l, i + 1, j)
    else:
        co.add((i, j, i + 1, j))
    if i - 1 >= 0 and m[i - 1][j] == t:
        if not v[i - 1][j]:
            ss(t, m, co, v, l, i - 1, j)
    else:
        co.add((i, j, i - 1, j))
    if j + 1 < l and m[i][j + 1] == t:
        if not v[i][j + 1]:
            ss(t, m, co, v, l, i, j + 1)
    else:
        co.add((i, j, i, j + 1))
    if j - 1 >= 0 and m[i][j - 1] == t:
        if not v[i][j - 1]:
            ss(t, m, co, v, l, i, j - 1)
    else:
        co.add((i, j, i, j - 1))

with open("12i.txt") as f:
    m = [li.strip() for li in f]
    l = len(m)

v = [[False for _ in range(l)] for _ in range(l)]
cc = 0
for i in range(l):
    for j in range(l):
        if v[i][j]:
            continue
        co = set()
        ss(m[i][j], m, co, v, l, i, j)
        lc = len(co)
        dh = {}
        dv = {}
        u = set()
        for c in co:
            if (c[0], c[1]) not in u:
                u.add((c[0], c[1]))
            if c[1] == c[3]:                
                k1 = (c[0], c[2])
                if k1 not in dh:
                    dh[k1] = set()
                    dh[k1].add(c[1])
                else:
                    e = dh[k1]
                    if (k1[0], c[1]-1, k1[1], c[1]-1) in co or (k1[0], c[1]+1, k1[1], c[1]+1) in co:
                        lc -= 1
                    else:
                        e.add(c[1])
            elif c[0] == c[2]:
                k2 = (c[1], c[3])
                if k2 not in dv:
                    dv[k2] = set()
                    dv[k2].add(c[0])
                else:
                    e = dv[k2]
                    if (c[0]-1, k2[0], c[0]-1, k2[1]) in co or (c[0]+1, k2[0], c[0]+1, k2[1]) in co:
                        lc -= 1
                    else:
                        e.add(c[0])
        lu = len(u)
        lu = 1 if lu == 0 else lu
        cc += lu * lc

print(cc)
