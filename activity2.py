from abc import ABC, abstractmethod

class animal(ABC):
    def move(self):
        pass

class dog(animal):
    def move(self):
        print("Dog runs")

class human(animal):
    def move(self):
        print("Human walks and can run")

class lion(animal):
    def move(self):
        print(" walks and can run")

class snake(animal):
    def move(self):
        print("slithers")

k=dog()
p=human()
s=snake()
l=lion()

for n in (k,p,s,l):
    n.move()