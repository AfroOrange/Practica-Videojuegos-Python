from usuarios import Usuarios
from videojuegos import Videojuegos
from gestor import GestorCompras

def main_menu():
    while True:
        print("\n------------ Inicio de sesión ------------ \n ¿Qué desea hacer?")
        print("1. Mostrar lista de videojuegos")
        print("2. Añadir nuevo videojuego")
        print("3. Mostrar lista de usuarios")
        print("4. Añadir nuevo usuario")
        print("5. Comprar videojuego ")
        print("6. Cerrar sesión")

        choice = input("Introducir opción: (1-6): ")

        if choice == "1":
            Videojuegos.mostrar_videojuegos()
        elif choice == "2":
            add_new_game_menu()
        elif choice == "3":
            Usuarios.mostrar_usuarios()
        elif choice == "4":
            add_new_user_menu()
        elif choice == "5":
            buy_game_menu()
        elif choice == "6":
            print("Sesión finalizada")
            break
        else:
            print("Opción no válida. Introduce un nuevo número del (1-6)")

def add_new_game_menu():
    try:
        nombre = input("Introducir nombre del videojuego: ")
        consola = input("Introducir nombre de la consola", Videojuegos.nombres_validos)
        estado = input("Introducir estado del videojuego (En venta, Agotado, Obsoleto): ")
        stock = int(input("Introducir Stock: "))
        
        new_game = Videojuegos(nombre, consola, estado, stock)
        new_game.añadir_videojuego()

        print("Videojuego añadido a la lista")
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(f"Error encontrado: {e}")

def add_new_user_menu():
    try:
        dni = input("Introducir DNI del usuario: ")
        nombre = input("Introducir nombre de usuario: ")
        apellidos = input("Introducir apellido de usuario: ")
        telefono = input("Introducir número de teléfono: ")
        correo = input("Introducir el email: ")

        new_user = Usuarios(dni, nombre, apellidos, telefono, correo)
        new_user.agregar_usuarios()

        print("Usuario añadido con éxito")
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(f"Error encontrado: {e}")

def buy_game_menu():
    try:
        dni = input("Introducir DNI: ")
        serial = int(input("Introducir el número de serie: "))

        GestorCompras.comprar_juegos(dni, serial)
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(f"Error encontrado: {e}")
