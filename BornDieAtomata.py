from automata.fa.nfa import NFA

nfa1 = NFA(states={"uAuB", "uAliB", "uBliA", "liAliB", "uAdB", "uBdA", "liAdB", "liBdA", "dAdB"},
           input_symbols={"", "lb,", "la,", "b", "rb,", "la-rb,", "ra,", "ra-lb,", "a"},
           transitions={
               'uAuB': {"": {"uAuB"}, "lb,": {"uAliB"}, "la,": {"uBliA"}, "b": {"liAliB"}},
               'uAliB': {"": {"uAliB"}, "rb,": {"uAdB"}, "la-rb,": {"liAdB"}, "la,": {"liAliB"}},
               'uBliA': {"": {"uBliA"}, "ra,": {"uBdA"}, "ra-lb,": {"liBdA"}, "lb,": {"liAliB"}},
               'liAliB': {"": {"liAliB"}, "rb,": {"liAdB"}, "ra,": {"liBdA"}, "a": {"dAdB"}},
               'uAdB': {"": {"uAdB"}, "la,": {"liAdB"}},
               'uBdA': {"": {"uBdA"}, "lb,": {"liBdA"}},
               'liAdB': {"": {"liAdB"}, "ra,": {"dAdB"}},
               'liBdA': {"": {"liBdA"}, "rb,": {"dAdB"}},
               'dAdB': {"": {"dAdB"}}
           },
           initial_state="uAuB",
           final_states={"dAdB"}
    )

nfa1.validate()

print('String to test');
x = input();
if nfa1.accepts_input("ba"):
    print('accept')
else:
    print('not accept')

nfa1.read_input_stepwise('la-lb,ra-rb')
