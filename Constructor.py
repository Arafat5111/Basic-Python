class Person:
    def __init__(self, n, o):
        print("Hey I am Arafat")
        self.name = n
        self.occupation = o

    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = Person("Alvee", "Enginieer")
b = Person("Tuktukey", "HR")
# c = Person(1, 2)
# print(a.name)
# a.name = "Alvee"
# a.occupation = "HR"
a.info()
b.info()
# c.info()
