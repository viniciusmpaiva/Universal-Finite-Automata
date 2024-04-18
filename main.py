from FiniteAutomata import FiniteAutomata

numStates = int(input("Number of states: "))
if(numStates<1 or numStates>10):
    print("Invalid number of states")
    exit()

terAlphTxt = input("Terminal symbols: ")

numTerAlph = int(terAlphTxt[0])
if(numTerAlph<1 or numTerAlph>10):
    print("Invalid number of terminal symbols")
    exit()

termAlphSet = []

for i in range(1,len(terAlphTxt)):
    if(terAlphTxt[i].isspace()):
        continue
    termAlphSet.append(terAlphTxt[i])


accStatesTxt = input("Acceptance states: ")
numAccStates = int(accStatesTxt[0])

if(numAccStates>numStates):
    print("Invalid number of acceptance states")
    exit()

accStates=[]
for i in range(1,len(accStatesTxt)):
    if(accStatesTxt[i].isspace()):
        continue
    if(int(accStatesTxt[i])>numStates):
        print("Invalid acceptance state")
        exit()
    accStates.append(int(accStatesTxt[i]))


numTrans = int(input("Number of transitions: "))
transitions=[]
if(numTrans>50 or numTrans<1):
    print("Invalid number of transitions")
    exit()

for i in range(0,numTrans):
    transitions.append(input("Transition: "))

aut = FiniteAutomata(numStates,termAlphSet,transitions,accStates)



# aut = FiniteAutomata(3,"2 a b",["0 a 1",'0 b 1','1 a 1','1 b 2','2 a 0','2 b 2'],[2]) 
#N deterministico
# aut = FiniteAutomata(4,"2 a b",["0 a 1","0 a 2","1 b 3","2 a 3"],[3]) 
#Deterministico
# aut = FiniteAutomata(3,"2 1 0",["0 0 0","0 1 1","1 0 2","1 1 0","2 1 2","2 0 1"],[2])
#Deterministico 
#N Deterministico
# aut = FiniteAutomata(3,['0','1'],["0 0 1","1 1 1","1 0 2","1 1 2"],[2])
#N Deterministico
# aut = FiniteAutomata(4,['a','b'],["0 a 0","0 b 0","0 a 1","0 b 2","1 a 3","2 b 3","3 a 3","3 b 3"],[3])
#N Deterministico


numStrings= int(input("Number of strings: "))
if(numStrings>10):
    print("Invalid number of strings")
    exit()
strings=[]
for i in range(0,numStrings):
    string = input("String: ")
    if(len(string)>20):
        print("Invalid string length")
        exit()
    strings.append(string)
    

for string in strings:
    print(aut.validateString(string))