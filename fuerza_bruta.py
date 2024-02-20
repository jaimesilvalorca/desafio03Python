from string import ascii_lowercase
from getpass import getpass
from sys import argv

contrasena = getpass("Ingrese contraseña: ")
#contrasena = argv[1].lower()
intentos = 0
contrasena_encontrada = ""

i = 0

while i < len(contrasena):
    
    for caracter in ascii_lowercase:
        intentos += 1
        if caracter == contrasena[i]:
            contrasena_encontrada += caracter
            i = i + 1
            break

print(f"Intentos: {intentos}")
print(f"Contraseña encontrada: {contrasena_encontrada}")
