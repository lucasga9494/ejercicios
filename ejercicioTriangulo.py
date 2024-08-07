class triangulo():
    def __init__(self,lado1,lado2,lado3):
        self.lado1=lado1
        self.lado2=lado2
        self.lado3=lado3
        self.eie()
    def eie(self):
        if self.lado1==self.lado2 and self.lado1==self.lado3 and self.lado2==self.lado1 and self.lado2==self.lado3:
            print('Equilatero')
        if self.lado1!=self.lado2 and self.lado1!=self.lado3 and self.lado2!=self.lado1 and self.lado2!=self.lado3:
            print('Escaleno')
        if self.lado1==self.lado2 and self.lado1!=self.lado3 or self.lado2==self.lado3 and self.lado2!=self.lado1:
            print('Isoseles')
            


def menu():
    lado1=int(input('Lado 1: '))
    lado2=int(input('Lado 2: '))
    lado3=int(input('Lado 3: '))
    
    triangulo(lado1,lado2,lado3)
menu()