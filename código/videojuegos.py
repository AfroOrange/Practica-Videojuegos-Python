import random

class Videojuegos:
    idVideojuego = random.randint(1, 100000)
    estados_validos = ["En venta", "Agotado", "Obsoleto"]  # Lista para agregar los estados de los code/txtfiles/juegos
    nombres_validos = ["PlayStation", "PS4", "PS5", "XBOX", "XBOX ONE", "Nintendo", "Switch", "PC", "Todas"]  # Lista para agregar consolas

    def __init__(self, nombre, consola, estado, stock):
        if consola not in Videojuegos.nombres_validos:
            raise ValueError(f"Los nombres válidos son: {', '.join(Videojuegos.nombres_validos)}")

        if estado not in Videojuegos.estados_validos:
            raise ValueError(f"Los valores válidos son: {', '.join(Videojuegos.estados_validos)}")

        if stock <= 0:
            estado = 'Agotado'

        self.nombre = nombre
        self.consola = consola
        self.estado = estado
        self.stock = stock

    # Método para mostrar todos los datos de txtfiles/juegos.txt
    def mostrar_videojuegos():
        with open('txtfiles/juegos.txt') as juegosPath:
            for line in juegosPath:
                print(line)

    # Método para añadir videojuegos nuevos 
    def añadir_videojuego(self):
        # Guarda los números de serie de los code/txtfiles/juegos
        numeros_seriales = set()

        # Lee el archivo para comprobar si existen números de serie iguales
        with open('txtfiles/juegos.txt', 'r') as juegosPath:
            for line in juegosPath:
                serial = line.split(", ")[-1].strip()
                numeros_seriales.add(int(serial))
        
        # Establece el siguiente número de serie disponible
        while Videojuegos.idVideojuego in numeros_seriales:
            Videojuegos.idVideojuego = random.randint(1, 100000)

        self.serial = Videojuegos.idVideojuego

        # Finalmente añade una entrada nueva a txtfiles/juegos.txt con el videojuego
        with open('txtfiles/juegos.txt', 'a+') as juegosPath:
            juegosPath.write(f"{self.nombre}, {self.consola}, {self.estado}, {self.stock}, {self.serial}\n")

    # Método para cambiar manualmente el estado de un videojuego
    def actualizar_stock(serial, nuevo_estado, nuevo_stock):
        datos = []
        game_name = ""
        with open('txtfiles/juegos.txt', 'r') as juegosPath:
            for line in juegosPath:
                if str(serial) in line:
                    dividir_lineas = line.split(", ")
                    game_name = dividir_lineas[0]
                    dividir_lineas[3] = nuevo_stock
                    dividir_lineas[2] = nuevo_estado  # Cambia el estado del videojuego
                    line = ", ".join(dividir_lineas)
                datos.append(line)
        print(f"El juego {game_name} se ha actualizado con {nuevo_stock} unidades")       

        # Reescribe el archivo con las líneas modificadas
        with open('txtfiles/juegos.txt', 'w') as juegosPath:
            for line in datos:
                juegosPath.write(line)
                
Videojuegos.mostrar_videojuegos()