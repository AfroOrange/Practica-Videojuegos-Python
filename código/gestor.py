class GestorCompras:

    def mostrar_compra():
        with open('txtfiles/compras.txt') as comprasPath:
            for line in comprasPath:
                print(line)

    @staticmethod
    def comprar_juegos(dni, serial):
        try:
            # Comprobar si el DNI existe en usuarios.txt
            dni_exists = False
            with open('txtfiles/usuarios.txt', 'r') as usuariosPath:
                for line in usuariosPath:
                    if dni in line:
                        dni_exists = True
                        break

            if not dni_exists:
                print("DNI no encontrado. No se puede completar la compra.")
                return

            # Comprueba la información del juego en txtfiles/juegos.txt
            game_name = None
            info_juego = ""
            with open('txtfiles/juegos.txt', 'r') as juegosPath:
                datos = []
                stock_juego = False

                for line in juegosPath:
                    if str(serial) in line:

                        stock_juego = True
                        info_juego = line.strip() 
                        dividir_linea = info_juego.split(", ")
                        game_name = str(dividir_linea[0])
                        stock = int(dividir_linea[3])

                        if stock > 0:
                            stock -= 1  
                            dividir_linea[
                                3] = str(stock)
                            if stock == 1:
                                print("Última existencia")
                            if stock == 0:
                                dividir_linea[2] = "Agotado" 

                            # Escribir el archivo compras.txt con los datos del juego   
                            with open('txtfiles/compras.txt', 'a') as comprasPath:
                                comprasPath.write(f"{dni}, {game_name}, {serial}\n")
                                print("Compra realizada con éxito")

                        else:
                            print("El juego está agotado.")
                        info_juego = ", ".join(dividir_linea) + "\n" 

                    datos.append(info_juego)

            if not stock_juego:
                print("Juego sin stock")
                return

            with open('txtfiles/juegos.txt', 'a+') as juegosPath:
                for line in datos:
                    juegosPath.write(line)

        except IOError:
            print("Error al leer o escribir el archivo.")
        except Exception as e:
            print(f"Error: {e}")

GestorCompras.mostrar_compra()