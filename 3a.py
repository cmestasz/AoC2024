import re
with open("3i.txt") as f:
    i = f.read()
ms = re.findall(r"(mul|do|don't)\((|\d+,\d+\))", i)
s = 0
e = True
for m in ms:
    a, b = map(int, re.findall(r"\d+", m))
    s += a * b
print(s)