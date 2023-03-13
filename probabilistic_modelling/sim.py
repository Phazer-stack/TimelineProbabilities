# convert to numpy ??
# import numpy as np

# keep an array of pairs [a-state,b-state] where state = 0,1,2
# initially [[0,0]]  both  unborn   #  u = np.array([[0,0]])  # [a-state,b-state]
# grow until the last pair is [2,2]   # both dead
#  e.g. [[0,0],[1,1],[2,2]]  for Allen equal
#       [[0,0],[1,0],[2,1],[2,2]] for Allen meet
#       [[0,0],[1,0],[2,0],[2,1],[2,2]]  for Allen <

from random import *
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np

tally = {}  # parametrized tally with parameter = str(pBorn) + "," + str(pDie)
sulimanTally = {}

def demo():

    font_params = {
        'axes.titlesize': 8,
        'axes.labelsize': 8,
        'axes.titleweight': 'bold'
    }

    plt.rcParams.update(font_params)

    demo_live = True

    while demo_live:

        user_input = input("\nPlease Enter which hypothesis to map ('Hypothesis_0' / 'Hypothesis_1 / 'Hypothesis_2 / 'Hypothesis_3' / 'Quit'): ")

        if user_input == "Hypothesis_0":

            print("Blurring Relation Testing")
            print("arSimulate(1.0, 1.0, 1000)", arSimulate(1.0, 1.0, 100000))     #Hypothesis 0 p,q->1 then prob(eq) -> 1
            MapConstantCase()

        elif user_input == "Hypothesis_1":

            print("arSimulate(0.5,0.5,1000)", arSimulate(0.5, 0.5, 1000))       #Hypothesis 1 p=0.5=q  leads to Suliman  (as number of trials increase)print("arSimulate(0.5,0.5,1000)", arSimulate(0.5, 0.5, 5000))
            print("arSimulate(0.5,0.5,10000)", arSimulate(0.5, 0.5, 10000))
            print("arSimulate(0.5,0.5, 50000)", arSimulate(0.5, 0.5, 50000))
            print("arSimulate(0.5,0.5,200000)", arSimulate(0.5, 0.5, 200000))
            MapSullimanCase()

        elif user_input == "Hypothesis_2":

            print("Hypothesis 2 for p=q -> 0, b+bi=1/2     o+oi = 1/4 = d+di")
            print("arSimulate(0.5,0.5,1000)", arSimulate(0.5, 0.5, 1000))       #Hypothesis 2 for p=q -> 0, b+bi=1/2     o+oi = 1/4 = d+di
            print("arSimulate(0.05,0.05,1000)", arSimulate(0.05, 0.05, 1000))
            print("arSimulate(0.005,0.005,1000)", arSimulate(0.005, 0.005, 1000))
            print("arSimulate(0.0005, 0.0005,1000)", arSimulate(0.0005, 0.0005, 1000))

            print("arSimulate(0.1,0.1,1000)", arSimulate(0.1, 0.1, 1000))
            print("arSimulate(0.01,0.01,1000)", arSimulate(0.01, 0.01, 1000))
            print("arSimulate(0.001,0.001,1000)", arSimulate(0.001, 0.001, 1000))
            MapGranularityCase()


        elif user_input == "Hypothesis_3":

            print("Precision Relation Testing")

            print("arSimulate(0.2,0.1,1000)", arSimulate(0.2, 0.1, 1000))       #Hypothesis 3 for for p=2q -> 0,all same (1/6 or 1/3 combining inverses)
            print("arSimulate(0.02,0.01,1000)", arSimulate(0.02, 0.01, 1000))
            print("arSimulate(0.002, 0.001, 1000)", arSimulate(0.002, 0.001, 1000))

            print("arSimulate(0.1, 0.2, 1000)", arSimulate(0.1, 0.2, 1000))
            print("arSimulate(0.01, 0.02, 1000)", arSimulate(0.01, 0.02, 1000))
            print("arSimulate(0.001, 0.002, 1000)", arSimulate(0.01, 0.02, 1000))
            MapFernandoVogelCase()

        elif user_input == "Quit":
            demo_live = False

    print("Updated tally and probabilities in file outputPy")
    ta2file("outputPy")
    pr2file("outputPy")
    print("Iterating demo() updates tally and outputPy")

def initTallysTotaled():
    return arInitDic()

def CountOverTallies(tallyTotaled):

    allenRelations = ["eq", "b", "bi", "s", "si", "m", "mi",  # "dummy",
                     "o", "oi", "d", "di", "f", "fi"]
    for p in tally:
        for i in allenRelations:
            tallyTotaled[i] += tally[p][i]

def MapTotalTallyProbability(tallyTotaled):

    totalcount = 0
    allenRelations = ["eq", "b", "bi", "s", "si", "m", "mi",  # "dummy",
                      "o", "oi", "d", "di", "f", "fi"]

    for i in allenRelations:
        totalcount += tallyTotaled[i]

    for i in allenRelations:
            tallyTotaled[i] = tallyTotaled[i] / totalcount
    print("total probability")

    fig_1, axes = plt.subplots(1,2 , figsize= (10, 2.5))
    axes[0].bar(tallyTotaled.keys(), tallyTotaled.values(), edgecolor="white", linewidth=0.7)
    axes[0].xaxis.set_label_text("allen relations")
    axes[0].yaxis.set_label_text("probabilities")


    dict_sharedSemanticRelationLevel = {"eq": 2, "s": 3, "si": 3, "f": 3, "fi": 3, "m": 3, "mi": 3,
                                        "b": 4, "bi": 4, "o": 4, "oi": 4, "d": 4, "di": 4 }
    x = dict_sharedSemanticRelationLevel.values()
    dict_RelationLevelTally = {2 : 0, 3 : 0, 4 : 0}
    for i in tallyTotaled:
        value = tallyTotaled[i]
        relation = dict_sharedSemanticRelationLevel[i]
        dict_RelationLevelTally[relation] += value

    axes[1].bar(dict_RelationLevelTally.keys(), dict_RelationLevelTally.values())
    axes[1].xaxis.set_label_text("allen relations length")
    axes[1].yaxis.set_label_text("probabilities")
    plt.show()

    overlappingProb = tallyTotaled["o"] + tallyTotaled["oi"]
    duringProb = tallyTotaled ["d"] + tallyTotaled ["di"]
    beforeProb = tallyTotaled["b"] + tallyTotaled["bi"]
    remainingProb = tallyTotaled["eq"] + tallyTotaled["s"] + tallyTotaled["si"] + tallyTotaled["f"] + tallyTotaled["fi"] +  tallyTotaled["m"] + tallyTotaled["mi"]

    print("beforeProb " + str(beforeProb) + "\n" 
          "overlappingProb " + str(overlappingProb) + "\n" +
          "duringProb " + str(duringProb) + "\n" +
          "remainingProb " + str(remainingProb))


#four Hypothesis Cases Mapped region

def MapConstantCase():
    combineInvDicTallyConstant = combineInv(tally['1.0,1.0'])
    ProbCombInvTallyConstant = probDic(combineInvDicTallyConstant, trials=100000)
    fig_1, ax = plt.subplots()
    ax.bar(ProbCombInvTallyConstant.keys(), ProbCombInvTallyConstant.values(),edgecolor = "white", linewidth=0.7)
    ax.set_title("Sampled 100000 times, for Birth Probability (p) = 1, Death Probability (q) = 1")
    ax.xaxis.set_label_text("Allen Relations (Combining Inverses)")
    ax.yaxis.set_label_text("Probability")
    for bars in ax.containers:
        ax.bar_label(bars, color='orange', fontsize='6')
    plt.show()

def MapGranularityCase():

    combineInvDicTallypointfive = combineInv(tally['0.5,0.5'])
    ProbCombInvTallypointfive = probDic(combineInvDicTallypointfive, trials=1000)
    fig_2, axes = plt.subplots(2,2, figsize= (20,10))
    axes[0,0].bar(ProbCombInvTallypointfive.keys(),ProbCombInvTallypointfive.values(),edgecolor="white", linewidth=0.7)
    axes[0, 0].set_title("Sampled 1000 times, for Birth Probability = 0.5, Death Probability = 0.5")
    axes[0, 0].xaxis.set_label_text("Allen Relations (Combining Inverses)")
    axes[0,0].yaxis.set_label_text("Probability")
    for bars in axes[0,0].containers:
        axes[0,0].bar_label(bars, color= 'orange', fontsize='6')

    combineInvDicTallypointZerofive = combineInv(tally['0.05,0.05'])
    ProbCombInvTallypointZerofive = probDic(combineInvDicTallypointZerofive, trials=1000)
    axes[0, 1].bar(ProbCombInvTallypointZerofive.keys(), ProbCombInvTallypointZerofive.values(), edgecolor="white",
                   linewidth=0.7)
    axes[0, 1].set_title("Sampled 1000 times, for Birth Probability = 0.05, Death Probability = 0.05")
    axes[0, 1].xaxis.set_label_text("Allen Relations (Combining Inverses)")
    axes[0, 1].yaxis.set_label_text("Probability")
    for bars in axes[0, 1].containers:
        axes[0, 1].bar_label(bars, color='orange', fontsize='6')


    combineInvDicTallypointZeroZerofive = combineInv(tally['0.005,0.005'])
    ProbCombInvTallypointZeroZerofive = probDic(combineInvDicTallypointZeroZerofive, trials=1000)
    axes[1, 0].bar(ProbCombInvTallypointZeroZerofive.keys(), ProbCombInvTallypointZeroZerofive.values(), edgecolor="white",
                   linewidth=0.7)
    axes[1, 0].set_title("Sampled 1000 times, for Birth Probability = 0.005, Death Probability = 0.005")
    axes[1, 0].xaxis.set_label_text("Allen Relations (Combining Inverses)")
    axes[1, 0].yaxis.set_label_text("Probability")
    for bars in axes[1, 0].containers:
        axes[1, 0].bar_label(bars, color='orange', fontsize='6')

    combineInvDicTallypointZeroZeroZerofive = combineInv(tally['0.0005,0.0005'])
    ProbCombInvTallypointZeroZeroZerofive = probDic(combineInvDicTallypointZeroZeroZerofive, trials=1000)
    axes[1, 1].bar(ProbCombInvTallypointZeroZeroZerofive.keys(), ProbCombInvTallypointZeroZeroZerofive.values(), edgecolor="white",
                   linewidth=0.7)
    axes[1, 1].set_title("Sampled 1000 times, for Birth Probability = 0.0005, Death Probability = 0.0005")
    axes[1, 1].xaxis.set_label_text("Allen Relations (Combining Inverses)")
    axes[1, 1].yaxis.set_label_text("Probability")
    for bars in axes[1, 1].containers:
        axes[1, 1].bar_label(bars, color='orange', fontsize='6')

    fig_2.tight_layout(pad=5.0)
    plt.show()

def MapSullimanCase():

    sulimanSimulate(0.5, 0.5, 1000)
    sulimanSimulate(0.5, 0.5, 10000)
    sulimanSimulate(0.5, 0.5, 50000)
    sulimanSimulate(0.5, 0.5, 200000)

    combineInvDicTallySulliman1 = combineInv(sulimanTally['0.5,0.5,1000'])
    ProbCombInvTallySulliman1 = probDic(combineInvDicTallySulliman1, trials=1000)
    fig_3, axes = plt.subplots(2, 2, figsize=(20, 10))
    axes[0, 0].bar(ProbCombInvTallySulliman1.keys(), ProbCombInvTallySulliman1.values(), edgecolor="white",
                   linewidth=0.7)
    axes[0, 0].set_title("Sampled 1000 times, for Birth Probability = 0.5, Death Probability = 0.5")
    axes[0, 0].xaxis.set_label_text("Allen Relations (Combining Inverses)")
    axes[0, 0].yaxis.set_label_text("Probability")
    for bars in axes[0, 0].containers:
        axes[0, 0].bar_label(bars, color='orange', fontsize='6')

    combineInvDicTallySulliman2 = combineInv(sulimanTally['0.5,0.5,10000'])
    ProbCombInvTallySulliman2 = probDic(combineInvDicTallySulliman2, trials=10000)
    axes[0, 1].bar(ProbCombInvTallySulliman2.keys(), ProbCombInvTallySulliman2.values(), edgecolor="white",
                   linewidth=0.7)
    axes[0, 1].set_title("Sampled 10000 times, for Birth Probability = 0.5, Death Probability = 0.5")
    axes[0, 1].xaxis.set_label_text("Allen Relations (Combining Inverses)")
    axes[0, 1].yaxis.set_label_text("Probability")
    for bars in axes[0, 1].containers:
        axes[0, 1].bar_label(bars, color='orange', fontsize='6')

    combineInvDicTallySulliman3 = combineInv(sulimanTally['0.5,0.5,50000'])
    ProbCombInvTallySulliman3 = probDic(combineInvDicTallySulliman3, trials=50000)
    axes[1, 0].bar(ProbCombInvTallySulliman3.keys(), ProbCombInvTallySulliman3.values(),
                   edgecolor="white",
                   linewidth=0.7)
    axes[1, 0].set_title("Sampled 50000 times, for Birth Probability = 0.5, Death Probability = 0.5")
    axes[1, 0].xaxis.set_label_text("Allen Relations (Combining Inverses)")
    axes[1, 0].yaxis.set_label_text("Probability")
    for bars in axes[1, 0].containers:
        axes[1, 0].bar_label(bars, color='orange', fontsize='6')

    combineInvDicTallySulliman4 = combineInv(sulimanTally['0.5,0.5,200000'])
    ProbCombInvTallySulliman4 = probDic(combineInvDicTallySulliman4, trials=200000)
    axes[1, 1].bar(ProbCombInvTallySulliman4.keys(), ProbCombInvTallySulliman4.values(),
                   edgecolor="white",
                   linewidth=0.7)
    axes[1, 1].set_title("Sampled 200000 times, for Birth Probability = 0.5, Death Probability = 0.5")
    axes[1, 1].xaxis.set_label_text("Allen Relations (Combining Inverses)")
    axes[1, 1].yaxis.set_label_text("Probability")
    for bars in axes[1, 1].containers:
        axes[1, 1].bar_label(bars, color='orange', fontsize='6')

    fig_3.tight_layout(pad=5.0)
    plt.show()

def MapFernandoVogelCase():
    combineInvDicTallyTwoToOne1 = combineInv(tally['0.2,0.1'])
    ProbCombInvTallyTwoToOne1 = probDic(combineInvDicTallyTwoToOne1, trials=1000)
    fig_4, axes = plt.subplots(2, 2, figsize=(20, 10))
    axes[0, 0].bar(ProbCombInvTallyTwoToOne1.keys(), ProbCombInvTallyTwoToOne1.values(), edgecolor="white",
                   linewidth=0.7)
    axes[0, 0].set_title("Sampled 1000 times, for Birth Probability = 0.2, Death Probability = 0.1")
    axes[0, 0].xaxis.set_label_text("Allen Relations (Combining Inverses)")
    axes[0, 0].yaxis.set_label_text("Probability")
    for bars in axes[0, 0].containers:
        axes[0, 0].bar_label(bars, color='orange', fontsize='6')

    combineInvDicTallyTwoToOne2 = combineInv(tally['0.02,0.01'])
    ProbCombInvTallyTwoToOne2 = probDic(combineInvDicTallyTwoToOne2, trials=1000)
    axes[0, 1].bar(ProbCombInvTallyTwoToOne2.keys(), ProbCombInvTallyTwoToOne2.values(), edgecolor="white",
                   linewidth=0.7)
    axes[0, 1].set_title("Sampled 1000 times, for Birth Probability = 0.02, Death Probability = 0.01")
    axes[0, 1].xaxis.set_label_text("Allen Relations (Combining Inverses)")
    axes[0, 1].yaxis.set_label_text("Probability")
    for bars in axes[0, 1].containers:
        axes[0, 1].bar_label(bars, color='orange', fontsize='6')

    combineInvDicTallyTwoToOne3 = combineInv(tally['0.002,0.001'])
    ProbCombInvTallyTwoToOne3 = probDic(combineInvDicTallyTwoToOne3, trials=1000)
    axes[1, 0].bar(ProbCombInvTallyTwoToOne3.keys(), ProbCombInvTallyTwoToOne3.values(),
                   edgecolor="white",
                   linewidth=0.7)
    axes[1, 0].set_title("Sampled 1000 times, for Birth Probability = 0.002, Death Probability = 0.001")
    axes[1, 0].xaxis.set_label_text("Allen Relations (Combining Inverses)")
    axes[1, 0].yaxis.set_label_text("Probability")
    for bars in axes[1, 0].containers:
        axes[1, 0].bar_label(bars, color='orange', fontsize='6')

    fig_4.tight_layout(pad=5.0)
    plt.show()

#end of Hypothesis region


def sulimanSimulate(probBorn, probDie, trials):

    redRuns = simulateRed(probBorn,probDie,trials)
    dic = scoreRed(redRuns)
    p = probDic(dic,trials)
    print(" Probabilities combining inverses ", combineInv(p))
    updateSuliman(probBorn, probDie, trials, dic)
    print(" New tally for ",probBorn,probDie,trials," is ", sulimanTally[str(probBorn)+","+str(probDie) +"," + str(trials)])
    return dic

def updateSuliman(pBorn, pDie, trials, dic):
    pStr = str(pBorn) + "," + str(pDie) + "," + str(trials)  # converts pair to string for dictionary
    if not (pStr in sulimanTally):
        sulimanTally[pStr] = arInitDic()
    for i in ["eq", "b", "bi", "s", "si", "m", "mi",  # "dummy",
              "o", "oi", "d", "di", "f", "fi"]:
        sulimanTally[pStr][i] = sulimanTally[pStr][i] + dic[i]

def arSimulate(probBorn, probDie, trials):
    redRuns = simulateRed(probBorn, probDie, trials)
    dic = scoreRed(redRuns)
    p = probDic(dic, trials)
    print(" Probabilities combining inverses ", combineInv(p))
    updateTally(probBorn, probDie, dic)
    print(" New tally for ",probBorn,probDie," is ", tally[str(probBorn)+","+str(probDie)])
    return dic

def simulateRed(pBorn, pDie, trials):
    temp = []
    for run in range(trials):
        hist = [[0, 0]]
        while not (hist[-1] == [2, 2]):
            first = updateState(hist[-1][0], pBorn, pDie)
            second = updateState(hist[-1][1], pBorn, pDie)
            if not (hist[-1] == [first, second]):  # no need to reduce/destutter
                hist.append([first, second])
        temp.append(hist)
    return temp

def updateState(state, pBorn, pDie):
    toss = random()
    if state == 0 and toss < pBorn:
        return 1
    elif state == 1 and toss < pDie:
        return 2
    else:
        return state

def scoreRed(reducedRuns):
    dic = arInitDic()
    for r in reducedRuns:
        dic[arCode(r)] += 1
    return dic


def arCode(Hist):
    if Hist == [[0, 0], [1, 1], [2, 2]]:
        return "eq"
    elif Hist == [[0, 0], [1, 0], [2, 0], [2, 1], [2, 2]]:
        return "b"
    elif Hist == [[0, 0], [0, 1], [0, 2], [1, 2], [2, 2]]:
        return "bi"
    elif Hist == [[0, 0], [1, 0], [1, 1], [2, 1], [2, 2]]:
        return "o"
    elif Hist == [[0, 0], [0, 1], [1, 1], [1, 2], [2, 2]]:
        return "oi"
    elif Hist == [[0, 0], [1, 0], [2, 1], [2, 2]]:
        return "m"
    elif Hist == [[0, 0], [0, 1], [1, 2], [2, 2]]:
        return "mi"
    elif Hist == [[0, 0], [0, 1], [1, 1], [2, 1], [2, 2]]:
        return "d"
    elif Hist == [[0, 0], [1, 0], [1, 1], [1, 2], [2, 2]]:
        return "di"
    elif Hist == [[0, 0], [1, 1], [2, 1], [2, 2]]:
        return "s"
    elif Hist == [[0, 0], [1, 1], [1, 2], [2, 2]]:
        return "si"
    elif Hist == [[0, 0], [0, 1], [1, 1], [2, 2]]:
        return "f"
    elif Hist == [[0, 0], [1, 0], [1, 1], [2, 2]]:
        return "fi"


def arInitDic():
    dic = {}
    for i in ["eq", "b", "bi", "s", "si", "m", "mi",  # "dummy",
              "o", "oi", "d", "di", "f", "fi"]:
        dic[i] = 0
    return dic


def updateTally(pBorn, pDie, dic):
    pStr = str(pBorn) + "," + str(pDie)  # converts pair to string for dictionary
    if not (pStr in tally):
        tally[pStr] = arInitDic()
    for i in ["eq", "b", "bi", "s", "si", "m", "mi",  # "dummy",
              "o", "oi", "d", "di", "f", "fi"]:
        tally[pStr][i] = tally[pStr][i] + dic[i]


def probDic(dic, trials):
    temp = {}
    for k in dic:
        temp[k] = dic[k] / trials
    return temp


def combineInv(dic):
    temp = {}
    temp["eq"] = dic["eq"]
    temp["b"] = dic["b"] + dic["bi"]
    temp["o"] = dic["o"] + dic["oi"]
    temp["d"] = dic["d"] + dic["di"]
    temp["s"] = dic["s"] + dic["si"]
    temp["m"] = dic["m"] + dic["mi"]
    temp["f"] = dic["f"] + dic["fi"]
    #   print("Sum is",checkSum(temp))
    return temp


def talProb():
    temp = {}
    for k in tally:
        temp[k] = score2prob(combineInv(tally[k]))  # combining inverses
    return temp


def score2prob(dic):
    trials = checkSum(dic)
    temp = {}
    for k in dic:
        temp[k] = dic[k] / trials
    return temp


def tal(pBorn, pDie):
    return tally[str(pBorn) + "," + str(pDie)]


def tallyProb(pBorn, pDie):
    return score2prob(tally[str(pBorn) + "," + str(pDie)])


def checkSum(dic):
    sum = 0
    for i in dic:
        sum = sum + dic[i]
    return sum


def ta2file(file):
    w2file(file, "Raw tally")
    for p in tally:
        w2file(file, str(checkSum(tally[p])) + " trials of " + p)
        w2file(file, tally[p])
    w2file(file, "\n")


def pr2file(file):
    dic = talProb()
    w2file(file, "Tally probabilities (combining inverses)")
    for p in dic:
        w2file(file, p + ":")
        w2file(file, dic[p])
    w2file(file, "\n")


def w2file(file, dic):
    try:
        geeky_file = open(file, 'a')
        geeky_file.write(str(dic) + "\n")
        geeky_file.close()
    except:
        print("Unable to append to file")


if __name__ == "__main__":
    demo()