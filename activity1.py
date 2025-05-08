from abc import ABC, abstractmethod
class absclass(ABC):
   def print(self,x):
      print("the number is",x)

   @abstractmethod
   def display(self):
      print("abstract method")

class testclass(absclass):
    def display(self):
        print("I am inside the test class")

c1= testclass()
c1.print(10)
c1.display()