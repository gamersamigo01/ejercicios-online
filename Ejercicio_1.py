from Operaciones import menu,calcular
salir = False
while not salir:
    menu()
    
    opt = int(input("Ingrese una opcion: "))
    if opt == 5:
        salir = True

    else:
        try:
            num1 = int(input("Ingrese el primer numero: "))
            num2 = int(input("Ingrese el segundo numero: "))
        except ValueError:
            print("Error, ingrese un numero entero")
        except ZeroDivisionError:
            print("Error, no se puede dividir por 0")
        else:
            calcular(num1,num2,opt)