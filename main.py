from FiniteAutomata import FiniteAutomata

# numStates = int(input("Number of states: "))
# terSymTxt = input("Terminal symbols: ")

# numTerSym = int(terSymTxt[0])
# termSymSet = []

# for i in range(1,len(terSymTxt)):
#     if(terSymTxt[i].isspace()):
#         continue

#     termSymSet.append(terSymTxt[i])

# accStatesTxt = input("Acceptance states: ")
# numAccStates = int(accStatesTxt[0])

# accStates=[]
# for i in range(1,len(accStatesTxt)):
#     if(accStatesTxt[i].isspace()):
#         continue
#     accStates.append(int(accStatesTxt[i]))


# numTrans = int(input("Number of transitions: "))
# transitions=[]
# for i in range(0,numTrans):
#     transitions.append(input("Transition: "))


aut = FiniteAutomata(3,"2 a b",["0 a 1",'0 b 1','1 a 1','1 b 2','2 a 0','2 b 2'],0,[2])

aut.isDeterministic()
