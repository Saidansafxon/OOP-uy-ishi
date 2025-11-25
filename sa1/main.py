#1
class Book:
    def __init__(self,muallif,nom,narx):
        self.muallif=muallif
        self.nom=nom
        self.narx=narx
sa=Book("Alisher Navoiy","asar",1000000)
print(sa.muallif,sa.nom,sa.narx)
#2
class Person:
    def __init__(self,ism,yosh):
        self.ism=ism
        self.yosh=yosh
    def __str__(self):
        return f'ismim {self.ism} yoshim {self.yosh}'
sa1=Person("Saidansaf",10)
print(sa1)
#3
class Rectangle:
    def __init__(self,eni,boyi):
        self.eni=eni
        self.boyi=boyi
sa3=Rectangle(43,32)
print(sa3.eni*sa3.boyi)
#4
class Sa2:
    def __init__(self,ism,yosh):
        self.ism=ism
        self.yosh=yosh
    def __str__(self):
        return f'ismim {self.ism} yoshim {self.yosh}'
sa1=Sa2("Umar",16)
print(sa1)
#5