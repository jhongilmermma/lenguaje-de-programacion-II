class CalculadoraSuma:
    def __init__(self):
        self.total = 0  

    def sumanumeros(self):
        print("Calcula la suma de los números ingresados:")
        print("Escribe números para sumar. Escribe 'fin' para terminar.")
        while True:
            entrada = input("Ingresa un número: ")
            if entrada.lower() == "fin":
                break
            elif entrada.isdigit():
                self.total += int(entrada)

            if numero %2 == 0 :
                print("numero ingresado es par")
            elif numero % 2 == 0 :
                print("numero ingresado es impar")
            else:
                print("Entrada inválida: escribe un número o 'fin'")
        print(f"La suma total es: {self.total}")


def main():
    calculadora = CalculadoraSuma()
    calculadora.sumanumeros()


if __name__ == "__main__":
    main()
