def saludar():
    print("-----------Bienvenido a mi programa-----------")

def suma_t(n):
    total_sum = 0
    for i in range(1, n+1):
        print(total_sum)
    return total_sum

def promedio_t(a,b):
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
    saludar()
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
                   "3. La cantidad de numero positivos y negativos\n ")
             opcion1 = input("Ingrese la opcion que desee usar: ")
             if opcion1 == "1":
                numero = int(input("Ingrese un numero: "))
                suma_t(numero)
                print(numero)
             elif opcion1 == "2":
                 numero1 = int(input("Ingrese el primero numero: "))
                 numero2 = int(input("Ingrese el segundo numero: "))
                 promedio_t(numero1, numero2)
                 print(promedio_t(numero1, numero2))
        case "2":
            numero1 = int(input("Ingrese el numero 1: "))
            numero2 = int(input("Ingrese el numero 2: "))
            promedio_t(numero1,numero2)
            print(promedio_t(numero1, numero2))
        case "3":
