li = input()
ls = []
rs = {}
while li != "":
    l, r = li.split()
    ls.append(int(l))
    if int(r) not in rs:
        rs[int(r)] = 1
    else:
        rs[int(r)] += 1
    li = input()
s = 0
for i in range(len(ls)):
    s += ls[i] * rs[ls[i]] if ls[i] in rs else 0
print(s)