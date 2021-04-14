import random
import math
class DNA:

    def __init__(self, numberOfGenes):
        self.genes = []
        self.fitness = 0
        self.numberOfGenes = numberOfGenes
        for i in range(self.numberOfGenes):
            self.genes.append(self.generateRandomChar())
    
    def generateRandomChar(self):
        randomInt = random.randint(31,122)
        return chr(randomInt)   
    
    def getElement(self):
        return self.genes
    
    def calculateFitness(self, targetGenes):
        fitness = 0
        for genome, targetGenome in zip(self.genes, targetGenes):
            if genome == targetGenome:
                fitness += 1
        self.fitness = fitness / len(targetGenes)
    
    
    def crossover(self, element):
        child = DNA(self.numberOfGenes)
        midpoint = math.floor(
            random.randint(0,self.numberOfGenes)
            )
        for i in range(self.numberOfGenes):
            if i>midpoint:
                child.genes[i] = self.genes[i]
            else:
                child.genes[i] = element.genes[i]
        return child
    
    
    def mutate(self, mutationRate):
        for i in range(self.numberOfGenes):
            if random.randint(0,100) < mutationRate:
                self.genes[i] = self.generateRandomChar()
        
        
        
        
        
        
def main():
    dna = DNA(4)
    print(dna.calculateFitness("dupa"))


if __name__ == "__main__":
    main()
