def superpose(automata1, automata2, voc1, voc2):
    if len(automata1.input_symbols) == len(automata2.input_symbols) == 0:
        return automata1
    else:
        temp = []
        if len(automata1.input_symbols) > 0:
            h1 = automata1.input_symbols[0]
            t1 = automata1.input_symbols[1:]
            h1v2 = h1.intersection(voc2)
            if len(h1v2) == 0:
                for res in superpose(t1,automata2.input_symbols,voc1,voc2):
                    temp.append([h1] + res) ##d1
            if len(automata2.input_symols) > 0:
                h2 = automata2.input_symols[0]
                t2 = automata2.input_symols[1:]
                h3 = h1.union(h2) ##component wise union
                if h1v2.issubset(h2):
                    h2v1 = h2.intersection(voc1)
                    if h2v1.issubset(h1):
                        for res in superpose(t1,t2,voc1,voc2):
                            temp.append([h3] + res)  ##d2
        if len(automata2.input_symbols) > 0:
            h2 = automata2.input_symbols[0]
            t2 = automata2.input_symbols[1:]
            h2v1 = h2.intersection(voc1)
            if len(h2v1) == 0:
                for res in superpose(automata1.input_symbols,t2,voc1,voc2):
                    temp.append([h2] + res)
        return temp

def super(automata1,automata2):
    return superpose(automata1,automata2,voc(automata1),voc(automata2))

def voc(automata):
    if len(automata.input_symbols) == 0:
        return {}
    else:
        return automata.input_symbols[0].union(voc(automata.input_symbols[1:]))

def proj(automata,set):
    if len(automata.input_symbols) == 0:
        return automata
    else:
        h1 = string[0].intersection(set)
        if len(h1) == 0:
            return proj(string[1:],set)
        else:
            return [h1] + proj(string[1:],set)
            return [h1] + proj(string[1:],set)