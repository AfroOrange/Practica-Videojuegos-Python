import re

class Usuarios:
    def __init__(self, dni, nombre, apellidos, telefono, correo):

        # Restricción para que el DNI tenga el patrón correcto
        if not re.match(r'^[0-9]{8}[A-Z]', dni):
            raise ValueError("Formato de DNI inválido")

        # Restricción para que el número de teléfono sea una serie de números enteros de 9 cifras
        if not re.match(r'^[0-9]{9}', telefono):
            raise ValueError("El número de teléfono introducido es inválido")

        # Restricción para el correo electrónico
        if not re.match(r"^\S+@\S+\.\S+$", correo):
            raise ValueError("Dirección de correo electrónico no válida")
        
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos
        self.telefono = telefono 
        self.correo = correo
    
    # Método para ver todos los videojuegos/usuarios del txt
    def mostrar_usuarios():
        with open('txtfiles/usuarios.txt') as filePath:
            for line in filePath:
                print(line)

    # Método para agregar videojuegos/usuarios al txt
    def agregar_usuarios(self):
        with open('txtfiles/usuarios.txt', 'a+') as filePath:
            filePath.write(f"{self.dni}, {self.nombre}, {self.apellidos}, {self.telefono}, {self.correo} \n")

    # Método para buscar videojuegos/usuarios a través del DNI
    def buscar_usuario(dni):
        with open('txtfiles/usuarios.txt', 'r') as filePath:
            for line in filePath:
                if dni in line:
                    print(line)

    # Método para eliminar los usuaiors a través del DNI
    def eliminar_usuario(dni):
        datos = [] # La variable datos será un array donde guardaremos todas las líneas del documento

        # Una vez encuentre el DNI introducido, borrará el documento
        with open('txtfiles/usuarios.txt', 'r') as filePath:
            for line in filePath:
                if dni not in line:
                    datos.append(line)

        # Luego lo reescribirá con los datos guardados
        with open('txtfiles/usuarios.txt', 'w') as filePath:
            for line in datos:
                filePath.write(line)