
class NumerosNaturales:
    def __init__(self, valor):
        self.valor = valor

    def mostrar(self):
        if self.valor == 0 :
            print(f"el : {self.valor} es un Número nulo")
            
        elif self.valor%3 == 0 and self.valor%5==0:
            print(f"el :{self.valor} es multiplo de 3 y de 5")
        elif self.valor%3 == 0:
            print(f"el :{self.valor} es multiplo de 3 ")
        elif self.valor%5==0:
            print(f"el :{self.valor} es multiplo de 5 ")
        else :
            print(f"el :{self.valor} no es multiplo de 3 ni de 5")
        print("_"*50)
        

def main():
    i = 0
    while i <= 10:
        numero = NumerosNaturales(i)
        numero.mostrar()
        i+= 1

if __name__ == "__main__":
    main()
