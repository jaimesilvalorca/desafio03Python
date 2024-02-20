preguntas = [
    "¿Responde a Estímulos?",
    "¿Respira?",
    "¿Signos de Vida?",
    "¿Llegó la Ambulancia?"
    ]

pos = 0 

while pos < len(preguntas):
    print(pos)
    respuesta = input(f"{preguntas[pos]} s/n:").lower()

    while respuesta != "n" and respuesta != "s":
        print("Ingrese parámetro válido: 's' o 'n'")
        respuesta = input(f"{preguntas[pos]} s/n: ")

    if pos == 0:
        if respuesta == "s":
        # if respuesta == "n" or respuesta == "N"
            print("Valorar la necesidad de llevarlo al hospital más cercano")
            break
        else:            
            print("Abrir la vía Aérea")

    if pos == 1:
        if respuesta == "s":
        # if respuesta == "n" or respuesta == "N"    
            print("Permitirle posición de suficiente ventilación")
            break
        else:
            print("Administrar 5 Ventilaciones y llamar a la Ambulancia")

    if pos == 2:
        if respuesta == "s":
        # if respuesta == "n" or respuesta == "N"    
            print("Reevaluar a la espera de la Ambulancia")
        else:
            print("Administrar Compresiones Torácicas hasta que llegue la ambulancia")


    if pos == 3:
        if respuesta == "s":
        # if respuesta == "n" or respuesta == "N"
            pos = 1
            print("Fin del programa")
            break
        else:
            pos = 1
    pos = pos + 1
    
print("Fin")