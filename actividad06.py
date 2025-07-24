def saludar():
    print("-----------Bienvenido a mi programa-----------")

def suma_t(n):
    for x in n:
        return suma_t(n + n)

def promedio_t(n):
    for y in n:
        print("Ingrese un número")
    return promedio_t(n)

def n_p_n (n):
    for z in n:
        print(f"El numero mayor es: {n_p_n(n)}")

def calc_area(base, altura):
    return base * altura / 2

def n_par(n):
    return n % 2 == 0
def pro_n_():

    while True:
        saludar()
        print ("1. Sumar numeros\n"
              "2. Sacar promedio\n"
              "3. Verificar numero mayor y menor\n"
              "4. Calcular el area de un triangulo\n"
              "5. Verificar si un numero es par\n"
              "6. Salir del programa.\n")
        user_op = input("Ingrese la opcion a la que desea ingresar:")
        match user_op:
            case "1":
                n1 = input("Ingrese un numero: ")
                print(suma_t(n))
