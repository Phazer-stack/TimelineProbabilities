from automata.fa.nfa import NFA

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


if __name__ == "__main__":

    a = "1"
    la = l(a)
    ra = r(a)
    ua = u(a)
    lia = li(a)
    da = d(a)

    states = {ua, lia, da}
    input_symbols = {la, ra}
    fa1 = NFA(states=states,
            input_symbols=input_symbols,
            transitions={
                ua: {la: {lia}},
                lia: {ra: {da}},
                da: {}
            },
            initial_state=ua,
            final_states={da}
            )

    start = ua+lia
    fa2 = NFA(states={start,lia,da},
            input_symbols=input_symbols,
            transitions={
                start: {la: {lia}},
                lia: {ra: {da}},
                da: {}
            },
            initial_state=start,
            final_states={da}
            )

    if fa1 == fa2:
        print("same")
    else : print("notsame")