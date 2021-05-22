from abc import ABC,abstractclassmethod
class Computer(ABC):
    def common(self):
        print("im computer")
    @abstractclassmethod
    def process(self):
        pass
class Laptop(Computer):
    def process(self):
        print("this is laptop and very handy to carry")
class Desktop(Computer):
    def process(self):
        print("this is desktop and good for stndalone desk")
comp1= Laptop()
print (comp1.process())