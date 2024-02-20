from sys import argv

ventas = {
    
 "Enero": 15000,
 "Febrero": 22000,
 "Marzo": 12000,
 "Abril": 17000,
 "Mayo": 81000,
 "Junio": 13000,
 "Julio": 21000,
 "Agosto": 41200,
 "Septiembre": 25000,
 "Octubre": 21500,
 "Noviembre": 91000,
 "Diciembre": 21000,
}

if len(argv) != 2:
    print("Parametros invalidos")
else:
    valor = argv[1]
    if not valor.isdigit():
        print("El parametro ingresado no es un número entero")
    elif int(valor) < 0:
        print("El parametro ingresado es menor a 0")
    else:
        valor = int(valor)
        umbral = {k: v for k, v in ventas.items() if v > valor}
        if len(umbral) == 0:
            print("Ningun valor que mostrar")
        else:
            print(umbral)
        
        


