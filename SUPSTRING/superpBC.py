def superpose(string1, string2, voc1, voc2):
    if len(string1) == len(string2) == 0:
        return [string1]
    else:
        temp = []
        if len(string1) > 0:
            h1 = string1[0]
            t1 = string1[1:]
            if len(string2) > 0:
                h2 = string2[0]
                t2 = string2[1:]
                h3 = h1.union(h2)
                h1v2 = h1.intersection(voc2)
                if h1v2.issubset(h2):
                    h2v1 = h2.intersection(voc1)
                    if h2v1.issubset(h1):
                        for res in superpose(t1, t2, voc1, voc2):
                            temp.append([h3] + res)
                        for res in superpose(string1, t2, voc1, voc2):
                            temp.append([h3] + res)
                        for res in superpose(t1, string2, voc1, voc2):
                            temp.append([h3] + res)
        return temp


def super(s1, s2):
    return superpose(s1, s2, voc(s1), voc(s2))


def voc(str):
    if len(str) == 0:
        return {}
    else:
        return str[0].union(voc(str[1:]))


def red(str, set):
    if len(str) == 0:
        return str
    else:
        h1 = str[0].intersection(set)
        return [h1] + red(str[1:], set)


def bc(str):
    if len(str) < 2:
        return str
    else:
        h, t = str[0], str[1:]
        if h == t[0]:
            return bc(t)
        else:
            return [h] + bc(t)


def allen(x, y, r):
    e = set({})
    if r == "b":
        return [e, {x}, e, {y}, e]
    elif r == "o":
        return [e, {x}, {x, y}, {y}, e]
    elif r == "m":
        return [e, {x}, {y}, e]
    elif r == "d":
        return [e, {y}, {x, y}, {y}, e]
    elif r == "s":
        return [e, {x, y}, {y}, e]
    elif r == "f":
        return [e, {y}, {x, y}, e]
    if r == "bi":
        return [e, {y}, e, {x}, e]
    elif r == "oi":
        return [e, {y}, {x, y}, {x}, e]
    elif r == "mi":
        return [e, {y}, {x}, e]
    elif r == "di":
        return [e, {x}, {x, y}, {x}, e]
    elif r == "si":
        return [e, {x, y}, {x}, e]
    elif r == "fi":
        return [e, {x}, {x, y}, e]
    elif r == "eq":
        return [e, {x, y}, e]


def allInv(string, x, y):
    e = set({})
    if string == [e, {x}, e, {y}, e]:
        return "b"
    elif string == [e, {x}, {x, y}, {y}, e]:
        return "o"
    elif string == [e, {x}, {y}, e]:
        return "m"
    elif string == [e, {y}, {x, y}, {y}, e]:
        return "d"
    elif string == [e, {x, y}, {y}, e]:
        return "s"
    elif string == [e, {y}, {x, y}, e]:
        return "f"
    elif string == [e, {x}, e, {y}, e]:
        return "bi"
    elif string == [e, {y}, {x, y}, {x}, e]:
        return "oi"
    elif string == [e, {y}, {x}, e]:
        return "mi"
    elif string == [e, {x}, {x, y}, {x}, e]:
        return "di"
    elif string == [e, {x, y}, {x}, e]:
        return "si"
    elif string == [e, {x}, {x, y}, e]:
        return "fi"
    elif string == [e, {x, y}, e]:
        return "eq"


def tt(r1, r2):
    temp = []
    for s in super(allen(0, 1, r1), allen(1, 2, r2)):
        temp.append(allInv(bc(red(s, {0, 2})), 0, 2))
    return temp


def test():
    print("Examples:")
    s1 = allen(0, 1, 'd')
    print(" allen(0,1,'d')  is ", s1)
    s2 = allen(1, 2, 'm')
    print(" allen(1,2,'m')  is ", s2)
    print(" super(allen(0,1,'d'), allen(1,2,'m'))  is ")
    print(" ", super(s1, s2))
    print(" bc(red([...],{0,2}))  is ",
          bc(red(super(s1, s2)[0], {0, 2})))

    print(" tt('d','m')  is ", tt("d", "m"))
    print(" tt('b','d')  is ", tt("b", "d"))
    print(" tt('fi','d') is ", tt("fi", "d"))
    print(" tt('s','di') is ", tt("s", "di"))

if __name__ == "__main__":
    test()