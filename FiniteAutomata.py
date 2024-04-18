                
class FiniteAutomata:
    

    def __init__(self,stateSet,terminalAlphabet,stateTransition,acceptanceStates):
        self.stateSet = stateSet
        self.terminalAlphabet = terminalAlphabet
        self.stateTransition = stateTransition
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

        self.graph = []

        for i in range(0,self.stateSet+1):
            a=[]
            for j in range(0,self.stateSet+1):
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
        for i in range(0,len(self.terminalAlphabet)) :
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

        self.__updateAutomata(delta,transitions)
        
        
            # self.__updateAutomata(delta,transitions)         
        #A tabela delta serão os novos estados
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

    


    def __updateAutomata(self,delta,transitions):
        self.stateSet = len(delta)
        u=0
        j=0
        count=0
    
        for trans in transitions:
            count+=len(trans)
        count_blank=0
        if(len(self.stateTransition)>count):
            del self.stateTransition[count:]
        elif(len(self.stateTransition)<count):
            for item in transitions:
                count_blank += item.count([])
            for i in range(0,count-len(self.stateTransition)-count_blank):
                self.stateTransition.append("")

        newState = self.stateSet -1
        hashMap={}
        for item in delta:
            if(len(item)>1 and f'{item}' not in hashMap):
                hashMap[f'{item}'] = newState
                item_txt = newState
                newState+=1
            elif(len(item)>1):
                item_txt = hashMap[f'{item}']
            else:
                item_txt=', '.join(map(str,item))

            for i in range(0,len(self.terminalAlphabet)):
                if(transitions[i][j] == []): continue
                if(f"{transitions[i][j]}" not in hashMap and len(transitions[i][j])>1):
                    hashMap[f'{transitions[i][j]}'] = newState
                    transitions_txt = newState
                    newState+=1
                elif(len(transitions[i][j])>1):
                    transitions_txt = hashMap[f'{transitions[i][j]}']
                else:
                    transitions_txt = f'{transitions[i][j][0]}'
                self.stateTransition[u] = f'{item_txt} {self.terminalAlphabet[i]} {transitions_txt}'
                u+=1
            j+=1
                

        temp_accStates = self.acceptenceStates
        for acc in temp_accStates:
            for item in delta:
                if(acc in item and len(item)>1 ):
                    self.acceptenceStates.append(hashMap[f'{item}'])
        self.__buildGraph()
            
    
    def validateString(self,string):
        if(self.__isDeterministic()):
            self.__toDeterministic()
        

        currentState = 0
        for letter in string:
            for i in range(0,len(self.graph[currentState])):
                if(letter in self.graph[currentState][i]):
                    currentState = i
                    break
        for state in self.acceptenceStates:
            if(currentState == state):
                return True
        return False