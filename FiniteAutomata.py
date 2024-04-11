                
class FiniteAutomata:
    

    def __init__(self,stateSet,terminalAlphabet,stateTransition,initialState,acceptanceStates):
        self.stateSet = stateSet
        self.terminalAlphabetic = terminalAlphabet
        self.stateTransition = stateTransition
        self.initialState = initialState
        self.acceptenceStates = acceptanceStates


        self.graph=[]
        for i in range(0,self.stateSet):
            a=[]
            for j in range(0,self.stateSet):
                a.append('')
            self.graph.append(a)
        

        for i in self.stateTransition:
            parts = i.split()
            source = int(parts[0])
            destiny = int(parts[2])
            symbol = parts[1]
            if(self.graph[source][destiny] == ''):
                self.graph[source][destiny] = [symbol]
                
            else:
                self.graph[source][destiny].append(symbol)
        # print(self.graph)
    
    
    def __isDeterministic(self):
        temp = self.graph
        for m in range(0,len(temp)):
            print(temp[m])
            for i in range(0,len(temp[m])):
                if(temp[m][i] ==''):
                    continue
                for j in range(0,len(temp[m][i])):
                    for u in range(i+1,len(temp[m])):
                        if(temp[m][i][j] in temp[m][u]):
                            return False

        return True    
                
    def __toDeterministic(self):
        delta =[]

    
    def stringIsPossible(self):
        # print(self.graph)
        if(not self.__isDeterministic()):
            # self.toDeterministic()
            return "Não deterministico"
        else:
            return "Deterministico"
        