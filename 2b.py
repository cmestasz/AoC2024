with open("2i.txt") as f:
    li = f.readline()
    s = 0
    while li != "":
        r = [int(x) for x in li.split()]
        uv = dv = p = True
        c = False
        f = 0
        l = 0
        i = 1
        while i < len(r):
            d = (r[i] - r[l]) if l >= 0 else 1
            l = i
            if uv and not (1 <= d and d <= 3):
                if p or c:
                    p = False
                    if not c:
                        f = i
                        c = True
                        l = f - 1
                    else:
                        c = False
                        i = f - 1
                        l = i - 1
                else:
                    uv = False
                    break
            i += 1

        if not uv:
            i = 1
            l = 0
            f = 0
            p = True
            c = False
            while i < len(r):
                d = (r[l] - r[i]) if l >= 0 else 1
                l = i
                if dv and not (1 <= d and d <= 3):
                    if p or c:
                        p = False
                        if not c:
                            f = i
                            c = True
                            l = f - 1
                        else:
                            c = False
                            i = f - 1
                            l = i - 1
                    else:
                        dv = False
                        break
                i += 1
        s += uv or dv
        print(uv or dv)
        li = f.readline()
    print(s)