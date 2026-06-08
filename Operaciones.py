def menu():
    print("#####Bienvenido a la calculadora######")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

def calcular(num1,num2,opt):
    if opt == 1:
        resultado = num1 + num2
        print(f"El resultado es: {resultado}")
    elif opt == 2:
        resultado = num1 - num2
        print(f"El resultado es: {resultado}")
    elif opt == 3:
        resultado = num1 * num2
        print(f"El resultado es: {resultado}")
    elif opt == 4:
        while num1 != 0:
            resultado = num1 / num2
            print(f"El resultado es: {resultado}")
        else:
            print("Error, no se puede dividir por 0")        
