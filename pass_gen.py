import random
import string
palabras = ["cola", "marino", "hoy", "manzana", "cabeza", "cisterna", 
"vals"]



def contra_fuerte():
    x = random.choice(string.ascii_letters + string.ascii_uppercase + 
string.digits + string.punctuation + string.ascii_lowercase + 
string.digits + string.ascii_letters + string.punctuation + 
string.ascii_letters)
    return x

def contra_debil():
    contraseña = ""
    contraseña = contraseña + random.choice(palabras)
    print("primera impresion de contra", contraseña)
    x = random.choice(palabras)
    print("Primera impresiond e x", x)

    while x in contraseña:
        x = random.choice(palabras)
    contraseña = contraseña + x
    
    return contraseña






print("1. Contraseña debil")
print("2. Contraseña fuerte")
while True:
    try:
        op = int(input("Elige tu opción"))
        break
    except ValueError:
        print("Intenta de nuevo")

if op == 1:
    print(f'Tu contraseña es  {contra_debil()} ')
else: 
    print(f'Tu contraseña es {contra_fuerte()}')
