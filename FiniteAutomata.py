                
class FiniteAutomata:
    

    def __init__(self,stateSet,terminalAlphabet,stateTransition,initialState,acceptanceStates):
        self.stateSet = stateSet
        self.terminalAlphabet = terminalAlphabet
        self.stateTransition = stateTransition
        self.initialState = initialState
        self.acceptenceStates = acceptanceStates

        self.__buildGraph()
    
    
    def __isDeterministic(self):
        temp = self.graph
        for m in range(0,len(temp)):
            for i in range(0,len(temp[m])):
                if(temp[m][i] ==''):
                    continue
                for j in range(0,len(temp[m][i])):
                    for u in range(i+1,len(temp[m])):
                        if(temp[m][i][j] in temp[m][u]):
                            return False

        return True    
                


    def __buildGraph(self):
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



    def __toDeterministic(self):
        delta =[[0]]
        transitions=[]
        for alphabet in self.terminalAlphabet :
            temp=[]
            transitions.append(temp)
        

        for i in range(0,len(self.terminalAlphabet)):
            temp=[]
            for j in range(0,len(self.graph[0])):
                if self.terminalAlphabet[i] in self.graph[0][j]:
                    temp.append(j)
                
                if(temp not in transitions[i]):transitions[i].append(temp)
            if(len(temp)>0):  delta.append(temp)
        i=1

        print(delta)
        while i <len(delta):
            for letter in range(0,len(self.terminalAlphabet)):
                temp=[]
                for j in range(0,len(delta[i])):
                    for w in range(0,len(self.graph[delta[i][j]])):
                        if(self.graph[delta[i][j]][w]) == '':continue
                        if(self.terminalAlphabet[letter] in self.graph[delta[i][j]][w] and w not in temp):
                            temp.append(w)
                transitions[letter].append(temp)
                if(temp not in delta and len(temp)>0):delta.append(temp)
            i+=1


        #A tebla delta serão os novos estados
        #Na entrada "0 b 0","0 a 1","0 a 2","0 b 2","1 a 1","1 b 1","2 a 1" A tabela no papel ficaria:
        #Delta          a           b
        #q0             q12         q02
        #q12            q1          q1
        #q02            q12         q02
        #q1             q1          q1

        #No nosso codigo, esta tabela se apresenta por meio de 2 matrizes: delta e transtions. 
        #A matriz delta representa os novos estados, já a transitions, as colunas a e b da tabela anterior, com o indice
        #0 sendo o do primeiro simbolo terminal (no exemplo, a), o indice 1 o segundo, e assim em diante

        #portando, a saída, nesse exemplo será:
        #delta=[                transtions=[
        #   [0],                    [[1,2],     [[0,2], 
        #   [1,2],                   [1],        [1],   
        #   [0,2],                   [1,2],      [0,2],   
        #   [1],                     [1]],       [1]]   
        #]                                                 ]

        print(f'delta = {delta}')   
        print(f'transitions = {transitions}')
            
                
    
    def stringIsPossible(self):
        if( not self.__isDeterministic()): 
            print("N deterministico")
        else:
            print("deterministico")    
        self.__toDeterministic()
        print(self.graph)
        