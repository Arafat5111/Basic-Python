class Person:
    name = "Arafat"
    occupation = ("Computer Enginieer")
    networth = 10
    def info(self):
        print(f"{self.name} is a {self.occupation} and his networth is {self.networth} Doller")


a = Person()
b = Person()
c = Person()

a.name = "Alvee"
a.occupation = "Electric Enginieer"
a.networth = 30

b.name = "Tuktukey"
b.occupation = "GF"
b.networth = 50
# print(a.name, a.occupation)
a.info()
b.info()
c.info()