def hello():
    print("-----------Bienvenido a mi programa-----------")

def suma_t(n):
    total_sum = 0
    for i in range(1, n+1):
        print(total_sum)
    return total_sum

def average(a,b):
    return a +b / 2

def n_p_n (a,b):
    if a < 0:print(f"{a} es negativo")
    else:print(f"{a} es positivo")
    if b< 0:print(f"{b} es negativo")
    else:print(f"{b} es positivo")

def calc_area(base, altura):
    return base * altura / 2

def n_par(n):
    return n % 2 == 0
def prom_cali (n):
    cali = 0
    notes = int(input("Ingrese calificacion: "))
    for i in range(notes):
        notes1 = n + notes / notes
        print(f"El promedio de calificaciones es: {notes1}")

def pro_menor_mayor(n):
    values = int(input("Ingrese la cantidad de valores: "))
    maximo = 0
    minimo = 0
    for i in range(values):
        num = int(input("Ingrese el numero:"))
        if num > maximo:
            maximo = num
        print(f"El numero mayor es: {maximo}")
        if num < minimo:
            minimo = num
        print(f"El numero menor es: {minimo}")

while True:
    hello()
    print ("1. Lista de numeros\n"
            "2. Calcular el área de un triángulo\n"
            "3. Verificar si un número es par o impar\n"
            "4. Calcular el promedio de n calificaciones\n"
            "5. Ingresar n números y mostrar el mayor y el menor\n"
            "6. Salir del programa.\n")
    user_op = input("Ingrese la opcion a la que desea ingresar:")
    match user_op:
        case "1":
             print("1. suma de numeros\n"
                   "2. Promedio de numeros\n"
                   "3. La cantidad de numero positivos y negativos\n"
                   "4. Salir\n ")
             opcion1 = input("Ingrese la opcion que desee usar: ")
             match opcion1 == "1":
                 case "1":
                    numero = int(input("Ingrese un numero: "))
                    suma_t(numero)
                    print(numero)
                 case "2":
                     numero1 = int(input("Ingrese el primero numero: "))
                     numero2 = int(input("Ingrese el segundo numero: "))
                     average(numero1, numero2)
                     print(average(numero1, numero2))
                 case "3":
                     numero1 = int(input("Ingrese el primer numero: "))
                     numero2 = int(input("Ingrese el segundo numero: "))
                     n_p_n(numero1, numero2)
                     print(n_p_n(numero1, numero2))
                 case "4":
                     break
                 case _:
                     print("Ingrese una opcion valida")
        case "2":
            base = int(input("Ingrese la medida de la base: "))
            altura = int(input("Ingrese la medidad de la altura: "))
            calc_area(base, altura)
            print(calc_area(base,altura))
        case "3":
            numero_par = int(input("Ingrese el numero que desea verificar"))
            n_par(numero_par)
            print(n_par(numero_par))
        case "4":
            calif = int(input("Ingrese calificiacion"))
            prom_cali(calif)
            print(prom_cali(calif))
        case "5":
            digito = int(input("Ingrese un numero"))
            pro_menor_mayor(digito)
            print(pro_menor_mayor(digito))
        case _:
            print("Ingrese una opcion valida")

            break
