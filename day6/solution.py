
from rich.progress import track
import numpy as np
class School:
    def __init__(self):
        self.population = [0,0,0,0,0,0,0,0,0]
    
    def add(self, array):
        for value in array:
            self.population[int(value)] += 1 
    
    def advanceOneday(self):
        babies = self.population.pop(0)
        self.population.append(babies)
        self.population[6] += babies


f = open("input.txt")
data = f.readlines()
fishes = data[0].split(",")
mySchool = School()
mySchool.add(fishes)


for day in track(range(1, 257), description="Calling through days..."):
    mySchool.advanceOneday()

print(sum(mySchool.population))
