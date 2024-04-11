                
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
            
    
    
            

        


    def isDeterministic(self):
        print("Deterministic")
        print(self.stateTransition)

    def toDeterministic(self):
        ...
    
    def stringIsPossible(self):
        ...