from DNA import DNA
import random
import math

class Population:
    def __init__(self, sizeOfAPopulation, numberOfGenes, target):
        self.sizeOfAPopulation = sizeOfAPopulation
        self.numberOfGenes = numberOfGenes
        self.population = []
        self.matingPool = []
        self.mutationRate = 1
        self.target = target
        
    def generatePopulation(self):
        for i in range(self.sizeOfAPopulation):
            newElement = DNA(self.numberOfGenes)
            self.population.append(newElement)
            
    def getPopulation(self):
        return self.population


    def calculateFitnessForPopulation(self):
        for element in self.population:
            element.calculateFitness(self.target)
            

    def findMaxFitnessForPopulation(self):
        self.calculateFitnessForPopulation()
        maxFitness = 0
        for element in self.population:
            if element.fitness > maxFitness:
                maxFitness = element.fitness
        return maxFitness
    
    def scaleValue(self, value, istart, istop, ostart, ostop):
        return ostart + (ostop - ostart) * ((value - istart) / (istop - istart))
    
    def naturalSelection(self):
        self.matingPool = []
        maxFitness = self.findMaxFitnessForPopulation()
        
        for element in self.population:
            newScaledFitness = self.scaleValue(element.fitness, 0, maxFitness, 0, 1)
            n = math.floor(newScaledFitness * 100)
            for i in range(n):
                self.matingPool.append(element)
        

    def makeNewGeneration(self):
        for i in range(len(self.population)):
            partnerA, partnerB = random.choices(self.matingPool, k=2)
            child = partnerA.crossover(partnerB)
            child.mutate(self.mutationRate)
            self.population[i] = child
        
def main():
    phrase = "konstantynopolitanczykowianeczka"
    
    file1 = open("output.txt","a")
    pop = Population(1000, len(phrase), phrase)
    pop.generatePopulation()
    foundTarget = False
    while not foundTarget:
        pop.naturalSelection()
        pop.makeNewGeneration()
        for element in pop.getPopulation():
            print("".join(element.genes))
            file1.write("".join(element.genes)+"\n")
            if element.genes == list(phrase):
                foundTarget = True
                break
    
    
    
if __name__ == "__main__":
    main()