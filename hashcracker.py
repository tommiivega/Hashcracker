import hashlib

hash_file = "8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918"

dic_file = input("Ingrese la dirección del archivo del diccionario: ")

encontrado = False

with open(dic_file, "r") as file:
    for password in file:
        password = password.strip()
        hash_calculado = hashlib.sha256(password.encode()).hexdigest()

        if hash_calculado == hash_file:
            print(f"La contraseña es: {password}")
            encontrado = True
            break

if not encontrado:
    print("La contraseña no está en el diccionario")
