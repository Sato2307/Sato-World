
usuario = False

while usuario == False:
    usuario = input("ingrese nombre de usuario: ").strip()
    if len(usuario) >= 6 and " " not in usuario:
        usuario_valido = True
        print("Usuario Aceptado")
    else:
        print("El usuario debe tener al menos 6 caracteres y no debe contener espacios.")