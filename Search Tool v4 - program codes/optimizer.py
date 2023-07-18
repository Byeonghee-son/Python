from setup import Setup

class HillClimbing:
    def __init__(self):
        Setup.__init__(self)
        self._pType = 0
        self._limitStuck = 0

        self._numExp = 0
        self._numRestart = 0

    def setVariables(self, parameters):
        Setup.setVariables(self, parameters)
        self._pType = parameters['pType']
        self._limitStuck = parameters['limitStuck']
        self._numExp = parameters['numExp']
        self._numRestart = parameters['numRestart']
        
    def run(self):
        pass

    def randomRestart(self, p):
        self.run(p)
        bestSolution = p.getSolution()
        bestMinimum = p.getValue()
        numEval = p.getNumEval()
        for _ in range(1,self._numRestart):
            self.run(p)
            newSolution = p.getSolution()
            newMinimum = p.getValue()
            numEval += p.getNumEval()
            if newMinimum < bestMinimum:
                bestMinimum = newMinimum
                bestSolution = newSolution
        p.storeResult(bestSolution, bestMinimum)

    def displaySetting(self):
        if self._pType == 1:
            print()
            print("Mutation step size:", self._delta)
        elif self._pType == 2:
            print()
            print("Mutation step size:", self._delta)
        elif self._pType == 3:
            print()
            print("Update rate:", self._alpha)

    def displayNumExp(self):
        print()
        print("Number of experiments: ", self._numExp)

    def getNumExp(self):
        return self._numExp


class SteepestAscent(HillClimbing):
    def run(self, p):
        current = p.randomInit() # 'current' is a list of values
        valueC = p.evaluate(current)
        while True:
            neighbors = p.mutants(current)
            successor, valueS = self.bestOf(neighbors, p)
            if valueS >= valueC:
                break
            else:
                current = successor
                valueC = valueS
        p.storeResult(current, valueC)

    def bestOf(self,neighbors,p): ###
        best = neighbors[0]
        bestValue = p.evaluate(best)
        for i in range(1,len(neighbors)):
            newValue = p.evaluate(neighbors[i])
            if newValue < bestValue:
                best = neighbors[i]
                bestValue = newValue
        return best, bestValue
    
    def displaySetting(self):
        print()
        print("Search algorithm: Steepest-Ascent Hill Climbing")
        HillClimbing.displaySetting(self)

class FirstChoice(HillClimbing):
    def run(self, p):
        current = p.randomInit()   # 'current' is a list of values
        valueC = p.evaluate(current)
        i = 0
        while i < self._limitStuck:
            successor = p.randomMutant(current)
            valueS = p.evaluate(successor)
            if valueS < valueC:
                current = successor
                valueC = valueS
                i = 0              # Reset stuck counter
            else:
                i += 1
        p.storeResult(current, valueC)
    
    def displaySetting(self):
        print()
        print("Search algorithm: First-Choice Hill Climbing")
        HillClimbing.displaySetting(self)

class GradientDescent(HillClimbing):
    def run(self, p):
        current = p.randomInit() # 'current' is a list of values
        valueC = p.evaluate(current)
        while True:
            successor = p.takeStep(current, valueC)
            valueS = p.evaluate(successor)
            if valueS >= valueC:
                break
            else:
                current = successor
                valueC = valueS
        p.storeResult(current, valueC)
    
    def displaySetting(self):
        print()
        print("Search algorithm: Gradient-descent Hill Climbing")
        HillClimbing.displaySetting(self)
        print("Increment for calculating derivatives: " , self._dx)