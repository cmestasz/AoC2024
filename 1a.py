li = input()
ls = []
rs = []
while li != "":
    l, r = li.split()
    ls.append(int(l))
    rs.append(int(r))
    li = input()
ls.sort()
rs.sort()
s = 0
for i in range(len(ls)):
    s += abs(ls[i] - rs[i])
print(s)