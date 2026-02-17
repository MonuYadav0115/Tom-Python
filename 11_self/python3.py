
class Dog:
    def __init__(self,name):
        self.name = name
    def Bark(self):
        return f"{self.name} say woofs" 
        
my_dog = Dog("Buddy")
print(my_dog.Bark())
