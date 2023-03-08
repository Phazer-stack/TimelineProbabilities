from superpAtomata import *
from automata.fa.nfa import NFA
import graphviz
import pydot


class Timeline_NFA:

    def __init__(self, input_symbols, states, nfa):
        self.states = states
        self.input_symbols = input_symbols
        self.nfa = nfa

    def getNFA(self):
        return self.nfa

def allen(x, y, rel):

    if rel == "b":
        return before(x,y).getNFA()

    elif rel == "o":
        return overlaps(x,y).getNFA()

    elif rel == "m":
        return meets(x,y).getNFA()

    elif rel == "d":
        return during(x,y).getNFA()

    elif rel == "s":
        return starts(x,y).getNFA()

    elif rel == "f":
        return finishes(x,y).getNFA()

    if rel == "bi":
        return before_inverse(x,y).getNFA()

    elif rel == "oi":
        return overlaps_inverse(x,y).getNFA()

    elif rel == "mi":
        return meets_inverse(x,y).getNFA()

    elif rel == "di":

        return during_inverse(x,y).getNFA()

    elif rel == "si":
        return starts_inverse(x,y).getNFA()

    elif rel == "fi":
        return finishes_inverse(x,y).getNFA()

    elif rel == "eq":
        return equals(x,y).getNFA()

def l(x):
    return "l" + str(x)


def r(x):
    return "r" + str(x)


def u(x):
    return "u" + str(x)


def li(x):
    return "li" + str(x)


def d(x):
    return "d" + str(x)

def before(x,y):
    lx = l(x)
    rx = r(x)
    ux = u(x)
    lix = li(x)
    dx = d(x)

    ly = l(y)
    ry = r(y)
    uy = u(y)
    liy = li(y)
    dy = d(y)

    s1 = ux + "-" + uy
    s2 = lix + "-" + uy
    s3 = dx + "-" + uy
    s4 = dx + "-" + liy
    s5 = dx + "-" + dy

    input_symbols = {lx, rx, ly, ry}
    states = {s1, s2, s3, s4, s5}
    bnfa = NFA(states=states,
               input_symbols=input_symbols,
               transitions={
                   s1: {lx: {s2}},
                   s2: {rx: {s3}},
                   s3: {ly: {s4}},
                   s4: {ry: {s5}},
                   s5: {}
               },
               initial_state=s1,
               final_states={s5}
               )
    my_bnfa = Timeline_NFA(input_symbols=input_symbols, states=states,nfa= bnfa)
    return my_bnfa

def overlaps(x,y):
    lx = l(x)
    rx = r(x)
    ux = u(x)
    lix = li(x)
    dx = d(x)

    ly = l(y)
    ry = r(y)
    uy = u(y)
    liy = li(y)
    dy = d(y)
    s1 = ux + "-" + uy
    s2 = lix + "-" + uy
    s3 = lix + "-" + liy
    s4 = dx + "-" + liy
    s5 = dx + "-" + dy
    input_symbols = {lx, rx, ly, ry}
    states = {s1, s2, s3, s4, s5}
    onfa = NFA(states=states,
               input_symbols=input_symbols,
               transitions={
                   s1: {lx: {s2}},
                   s2: {ly: {s3}},
                   s3: {rx: {s4}},
                   s4: {ry: {s5}},
                   s5: {}
               },
               initial_state=s1,
               final_states={s5}
               )
    my_onfa = Timeline_NFA(input_symbols=input_symbols, states=states, nfa=onfa)
    return my_onfa

def meets(x,y):
    lx = l(x)
    rx = r(x)
    ux = u(x)
    lix = li(x)
    dx = d(x)

    ly = l(y)
    ry = r(y)
    uy = u(y)
    liy = li(y)
    dy = d(y)

    rxly = rx + ly
    input_symbols = {lx, rxly, ry}
    s1 = ux + "-" + uy
    s2 = lix + "-" + uy
    s3 = dx + "-" + liy
    s4 = dx + "-" + dy
    states = {s1, s2, s3, s4}
    mnfa = NFA(states=states,
               input_symbols=input_symbols,
               transitions={
                   s1: {lx: {s2}},
                   s2: {rxly: {s3}},
                   s3: {ry: {s4}},
                   s4: {}
               },
               initial_state=s1,
               final_states={s4}
               )
    my_mnfa = Timeline_NFA(input_symbols=input_symbols, states=states, nfa=mnfa)
    return my_mnfa

def during(x,y):
    lx = l(x)
    rx = r(x)
    ux = u(x)
    lix = li(x)
    dx = d(x)

    ly = l(y)
    ry = r(y)
    uy = u(y)
    liy = li(y)
    dy = d(y)
    input_symbols = {lx, rx, ly, ry}
    s1 = ux + "-" + uy
    s2 = ux + "-" + liy
    s3 = lix + "-" + liy
    s4 = dx + "-" + liy
    s5 = dx + "-" + dy
    states = {s1, s2, s3, s4, s5}
    dnfa = NFA(states=states,
               input_symbols=input_symbols,
               transitions={
                   s1: {ly: {s2}},
                   s2: {lx: {s3}},
                   s3: {rx: {s4}},
                   s4: {ry: {s5}},
                   s5: {}
               },
               initial_state=s1,
               final_states={s5}
               )
    my_dnfa = Timeline_NFA(input_symbols=input_symbols, states=states, nfa=dnfa)
    return my_dnfa

def starts(x,y):
    lx = l(x)
    rx = r(x)
    ux = u(x)
    lix = li(x)
    dx = d(x)

    ly = l(y)
    ry = r(y)
    uy = u(y)
    liy = li(y)
    dy = d(y)
    lxly = lx + ly
    input_symbols = {lxly, rx, ry}
    s1 = ux + "-" + uy
    s2 = lix + "-" + liy
    s3 = dx + "-" + liy
    s4 = dx + "-" + dy
    states = {s1, s2, s3, s4}
    snfa = NFA(states=states,
               input_symbols=input_symbols,
               transitions={
                   s1: {lxly: {s2}},
                   s2: {rx: {s3}},
                   s3: {ry: {s4}},
                   s4: {},
               },
               initial_state=s1,
               final_states={s4}
               )
    my_snfa = Timeline_NFA(input_symbols=input_symbols, states=states, nfa=snfa)
    return my_snfa

def finishes(x,y):
    lx = l(x)
    rx = r(x)
    ux = u(x)
    lix = li(x)
    dx = d(x)

    ly = l(y)
    ry = r(y)
    uy = u(y)
    liy = li(y)
    dy = d(y)
    rxry = rx + ry
    input_symbols = {lx, ly, rxry}
    s1 = ux + "-" + uy
    s2 = ux + "-" + liy
    s3 = lix + "-" + liy
    s4 = dx + "-" + dy
    states = {s1, s2, s3, s4}
    fnfa = NFA(states=states,
               input_symbols=input_symbols,
               transitions={
                   s1: {ly: {s2}},
                   s2: {lx: {s3}},
                   s3: {rxry: {s4}},
                   s4: {},
               },
               initial_state=s1,
               final_states={s4}
               )
    my_fnfa = Timeline_NFA(input_symbols=input_symbols, states=states, nfa=fnfa)
    return my_fnfa

def before_inverse(x,y):
    lx = l(x)
    rx = r(x)
    ux = u(x)
    lix = li(x)
    dx = d(x)

    ly = l(y)
    ry = r(y)
    uy = u(y)
    liy = li(y)
    dy = d(y)

    s1 = ux + "-" + uy
    s2 = ux + "-" + liy
    s3 = ux + "-" + dy
    s4 = lix + "-" + dy
    s5 = dx + "-" + dy

    input_symbols = {lx, rx, ly, ry}
    states = {s1, s2, s3, s4, s5}
    binfa = NFA(states=states,
                input_symbols=input_symbols,
                transitions={
                    s1: {ly: {s2}},
                    s2: {ry: {s3}},
                    s3: {lx: {s4}},
                    s4: {rx: {s5}},
                    s5: {}
                },
                initial_state=s1,
                final_states={s5}
                )
    my_binfa = Timeline_NFA(input_symbols=input_symbols, states=states, nfa=binfa)
    return my_binfa

def overlaps_inverse(x,y):
    lx = l(x)
    rx = r(x)
    ux = u(x)
    lix = li(x)
    dx = d(x)

    ly = l(y)
    ry = r(y)
    uy = u(y)
    liy = li(y)
    dy = d(y)

    s1 = ux + "-" + uy
    s2 = ux + "-" + liy
    s3 = lix + "-" + liy
    s4 = lix + "-" + dy
    s5 = dx + "-" + dy
    input_symbols = {lx, rx, ly, ry}
    states = {s1, s2, s3, s4, s5}
    oinfa = NFA(states=states,
                input_symbols=input_symbols,
                transitions={
                    s1: {ly: {s2}},
                    s2: {lx: {s3}},
                    s3: {ry: {s4}},
                    s4: {rx: {s5}},
                    s5: {}
                },
                initial_state=s1,
                final_states={s5}
                )
    my_oinfa = Timeline_NFA(input_symbols=input_symbols, states=states, nfa=oinfa)
    return my_oinfa

def meets_inverse(x,y):
    lx = l(x)
    rx = r(x)
    ux = u(x)
    lix = li(x)
    dx = d(x)

    ly = l(y)
    ry = r(y)
    uy = u(y)
    liy = li(y)
    dy = d(y)

    rylx = ry + lx
    input_symbols = {ly, rylx, rx}
    s1 = ux + "-" + uy
    s2 = ux + "-" + liy
    s3 = lix + "-" + dy
    s4 = dx + "-" + dy
    states = {s1, s2, s3, s4}
    minfa = NFA(states=states,
                input_symbols=input_symbols,
                transitions={
                    s1: {ly: {s2}},
                    s2: {rylx: {s3}},
                    s3: {rx: {s4}},
                    s4: {}
                },
                initial_state=s1,
                final_states={s4}
                )
    my_minfa = Timeline_NFA(input_symbols=input_symbols, states=states, nfa=minfa)
    return my_minfa

def during_inverse(x,y):
    lx = l(x)
    rx = r(x)
    ux = u(x)
    lix = li(x)
    dx = d(x)

    ly = l(y)
    ry = r(y)
    uy = u(y)
    liy = li(y)
    dy = d(y)

    input_symbols = {lx, rx, ly, ry}
    s1 = ux + "-" + uy
    s2 = lix + "-" + uy
    s3 = lix + "-" + liy
    s4 = lix + "-" + dy
    s5 = dx + "-" + dy
    states = {s1, s2, s3, s4, s5}
    dinfa = NFA(states=states,
                input_symbols=input_symbols,
                transitions={
                    s1: {lx: {s2}},
                    s2: {ly: {s3}},
                    s3: {ry: {s4}},
                    s4: {rx: {s5}},
                    s5: {}
                },
                initial_state=s1,
                final_states={s5}
                )
    my_dinfa = Timeline_NFA(input_symbols=input_symbols, states=states, nfa=dinfa)
    return my_dinfa

def starts_inverse(x,y):

    lx = l(x)
    rx = r(x)
    ux = u(x)
    lix = li(x)
    dx = d(x)

    ly = l(y)
    ry = r(y)
    uy = u(y)
    liy = li(y)
    dy = d(y)

    lylx = ly + lx
    input_symbols = {lylx, rx, ry}
    s1 = ux + "-" + uy
    s2 = lix + "-" + liy
    s3 = lix + "-" + dy
    s4 = dx + "-" + dy
    states = {s1, s2, s3, s4}
    sinfa = NFA(states=states,
                input_symbols=input_symbols,
                transitions={
                    s1: {lylx: {s2}},
                    s2: {ry: {s3}},
                    s3: {rx: {s4}},
                    s4: {},
                },
                initial_state=s1,
                final_states={s4}
                )
    my_sinfa = Timeline_NFA(input_symbols=input_symbols, states=states, nfa=sinfa)
    return my_sinfa

def finishes_inverse(x,y):

    lx = l(x)
    rx = r(x)
    ux = u(x)
    lix = li(x)
    dx = d(x)

    ly = l(y)
    ry = r(y)
    uy = u(y)
    liy = li(y)
    dy = d(y)

    rxry = rx + ry
    input_symbols = {lx, ly, rxry}
    s1 = ux + "-" + uy
    s2 = lix + "-" + uy
    s3 = lix + "-" + liy
    s4 = dx + "-" + dy
    states = {s1, s2, s3, s4}
    finfa = NFA(states=states,
                input_symbols=input_symbols,
                transitions={
                    s1: {lx: {s2}},
                    s2: {ly: {s3}},
                    s3: {rxry: {s4}},
                    s4: {},
                },
                initial_state=s1,
                final_states={s4}
                )
    my_finfa = Timeline_NFA(input_symbols=input_symbols, states=states, nfa=finfa)
    return my_finfa

def equals(x,y):

    lx = l(x)
    rx = r(x)
    ux = u(x)
    lix = li(x)
    dx = d(x)

    ly = l(y)
    ry = r(y)
    uy = u(y)
    liy = li(y)
    dy = d(y)

    lxly = lx + ly
    rxry = rx + ry
    input_symbols = {lxly, rxry}
    s1 = ux + "-" + uy
    s2 = lix + "-" + liy
    s3 = dx + "-" + dy
    states = {s1, s2, s3}
    eqnfa = NFA(states=states,
                input_symbols=input_symbols,
                transitions={
                    s1: {lxly: {s2}},
                    s2: {rxry: {s3}},
                    s3: {}
                },
                initial_state=s1,
                final_states={s3}
                )
    my_eqnfa = Timeline_NFA(input_symbols=input_symbols, states=states, nfa=eqnfa)
    return my_eqnfa


def allInv(automata, x, y):

    if automata == before(x,y).getNFA():
        return "b"
    elif automata == overlaps(x,y).getNFA():
        return "o"
    elif automata == meets(x,y).getNFA():
        return "m"
    elif automata == during(x,y).getNFA():
        return "d"
    elif automata == starts(x,y).getNFA():
        return "s"
    elif automata == finishes(x,y).getNFA():
        return "f"
    elif automata == before_inverse(x,y).getNFA():
        return "bi"
    elif automata == overlaps_inverse(x,y).getNFA():
        return "oi"
    elif automata == meets_inverse(x,y).getNFA():
        return "mi"
    elif automata == during_inverse(x,y).getNFA():
        return "di"
    elif automata == starts_inverse(x,y).getNFA():
        return "si"
    elif automata == finishes_inverse(x,y).getNFA():
        return "fi"
    elif automata == equals(x,y).getNFA():
        return "eq"


def tt(r1, r2):
    temp = []
    for s in super(allen(0, 1, r1), allen(1, 2, r2)):
        temp.append(allInv(proj(s, {l(0), r(0), l(2), r(2)}), 0, 2))
    return temp


def show(r1, r2):
    s1 = allen(0, 1, r1)
    s2 = allen(1, 2, r2)
    print(" ", s1, "(depicting 0", r1, "1) and")
    print(" ", s2, "(depicting 1", r2, "2)")
    s1.show_diagram(path='C:/college/final year project/nfa/s1.png')
    s2.show_diagram(path='C:/college/final year project/nfa/s2.png')
    # for s in super(s1, s2):
    #     print("   0", allInv(proj(s, {l(0), r(0), l(2), r(2)}), 0, 2), "2 from ", s)


def test():

    #print(" super(allen(0,1,'d'), allen(1,2,'m'))  is ")
    #print(" ", super(s1, s2))

    #for s in al:
    #    print(" ", allInv(s, 0, 1), s)
    #print('Allen transitivity table tt(r1,r2)')
    #print('e.g. tt("b",d") =', tt("b", "d"), 'by superposing')
    show("d", "d")

    t1 = allen(0, 1, "b")
    t1.show_diagram(path='C:/college/final year project/nfa/before.png')
    t2 = allen(0,1, "o")
    t2.show_diagram(path='C:/college/final year project/nfa/overlaps.png')
    t3 = allen(0, 1, "m")
    t3.show_diagram(path='C:/college/final year project/nfa/meets.png')
    t4 = allen(1, 2, "d")
    t4.show_diagram(path='C:/college/final year project/nfa/during.png')
    t5 = allen(0, 1, "s")
    t5.show_diagram(path='C:/college/final year project/nfa/starts.png')
    t6 = allen(0, 1, "f")
    t6.show_diagram(path='C:/college/final year project/nfa/finishes.png')

    t1i = allen(0, 1, "bi")
    t1i.show_diagram(path='C:/college/final year project/nfa/before_i.png')
    t2i = allen(0,1, "oi")
    t2i.show_diagram(path='C:/college/final year project/nfa/overlaps_i.png')
    t3i = allen(0, 1, "mi")
    t3i.show_diagram(path='C:/college/final year project/nfa/meets_i.png')
    t4i = allen(0, 1, "di")
    t4i.show_diagram(path='C:/college/final year project/nfa/during_i.png')
    t5i = allen(0, 1, "si")
    t5i.show_diagram(path='C:/college/final year project/nfa/starts_i.png')
    t6i = allen(0, 1, "fi")
    t6i.show_diagram(path='C:/college/final year project/nfa/finishes_i.png')

    t7 = allen(0, 1, "eq")
    t7.show_diagram(path='C:/college/final year project/nfa/equals.png')



if __name__ == "__main__":
    test()
