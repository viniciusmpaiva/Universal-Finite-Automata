from FiniteAutomata import FiniteAutomata

# numStates = int(input("Number of states: "))
# terAlphTxt = input("Terminal symbols: ")

# numTerAlph = int(terAlphTxt[0])
# termAlphSet = []

# for i in range(1,len(terAlphTxt)):
#     if(terAlphTxt[i].isspace()):
#         continue

#     termAlphSet.append(terAlphTxt[i])

# print(termAlphSet)

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


# aut = FiniteAutomata(3,"2 a b",["0 a 1",'0 b 1','1 a 1','1 b 2','2 a 0','2 b 2'],[2]) 
#N deterministico
# aut = FiniteAutomata(4,"2 a b",["0 a 1","0 a 2","1 b 3","2 a 3"],[3]) 
#Deterministico
# aut = FiniteAutomata(3,"2 1 0",["0 0 0","0 1 1","1 0 2","1 1 0","2 1 2","2 0 1"],[2])
#Deterministico 
aut = FiniteAutomata(3,['a','b'],["0 b 0","0 a 1","0 a 2","0 b 2","1 a 1","1 b 1","2 a 1"],[1])
#N Deterministico
# aut = FiniteAutomata(3,['0','1'],["0 0 1","1 1 1","1 0 2","1 1 2"],[2])
#N Deterministico
# aut = FiniteAutomata(4,['a','b'],["0 a 0","0 b 0","0 a 1","0 b 2","1 a 3","2 b 3","3 a 3","3 b 3"],[3])
#N Deterministico


print(aut.validateString("bbbabaaaa"))