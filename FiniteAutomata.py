                
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
        print(self.graph)
    
    
    def isDeterministic(self):
        for d1 in self.graph:
            for i in range(0,len(d1)):
                if(d1[i] ==''):
                    continue
                for j in range(i+1,len(d1)):
                    if(d1[i]==d1[j]):
                        return False

        return True

    def toDeterministic(self):
        ...
    
    def stringIsPossible(self):
        ...