from automata.fa.nfa import NFA
import graphviz
import pydot
from pathlib import Path
from allenDAtomata import *

nfaAID = 1;
nfaAInput = [{"la"}, {"ra"}]
nfaALife = NFA(
    states={"Ua", "LIa", "Da"},
    input_symbols= {'la', 'ra'},
    transitions={
        "Ua": { 'la' : {"LIa"}},
        "LIa": {'ra' : {"Da"}},
    },
    initial_state="Ua",
    final_states={"Da"}
)

if nfaALife.accepts_input(''):
    print('acceptA')
else:
    print('not acceptA')

nfaBID = 2;
nfaBInput = [{"lb"}, {"rb"}]
nfaBLife = NFA(
    states={"Ub", "LIb", "Db"},
    input_symbols= {"lb", "rb"},
    transitions={
        "Ub": {"lb" : {"LIb"}},
        # Use '' as the key name for empty string (lambda/epsilon) transitions
        "LIb": {"rb" : {"Db"}},
    },
    initial_state="Ub",
    final_states={"Db"}
)
if nfaBLife.accepts_input("lbrb"):
    print('acceptB')
else:
    print('not acceptB')

al = super(nfaAInput,nfaBInput);
for s in al:
    print(" ", allInv(s, "a", "b"),s)


