class Dog:

     def __init__(self, name, age, furcolor):
          self.name = name
          self.age = age
          self.furcolor = furcolor

     def bark(self):
          print(" Bark !")


mydog = Dog("Fido", 13, "Brown")
mydog.bark()

print(mydog.age)
