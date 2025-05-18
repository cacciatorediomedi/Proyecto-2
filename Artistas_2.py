def menu():
    while True:
        print("\nMenú de Opciones")
        print("1. Agregar un nuevo artista")
        print("2. Modificar un artista")
        print("3. Mostrar todos los artistas")
        print("4. Eliminar un artista")
        print("5. Buscar un artista")
        print("6. Salir")

        opcion = input("Ingrese la opción deseada: ")

        match opcion:
            case "1":
                # Agregar un nuevo artista
                pass
            case "2":
                # Modificar un artista
                pass
            case "3":
                # Mostrar todos los artistas
                pass
            case "4":
                # Eliminar un artista
                pass
            case "5":
                # Buscar un artista
                pass
            case "6":
                print("Saliendo del programa")
                break
            case _:
                print("Opción inválida. Por favor, intente nuevamente.")

menu()

import sqlite3

# Función para conectar a la base de datos
def conectar_db():
    return sqlite3.connect('artistas.db')

# Función para agregar un artista
def agregar_artista():
    conn = conectar_db()
    nombre = input("Ingrese nombre: ")
    edad = int(input("Ingrese edad: "))
    cantidad_albumes = int(input("Ingrese cantidad de álbumes: "))
    genero_musical = input("Ingrese género musical: ")
    sql = '''INSERT INTO artistas (nombre, edad, cantidad_albumes, genero_musical)
             VALUES (?, ?, ?, ?)'''
    conn.execute(sql, (nombre, edad, cantidad_albumes, genero_musical))
    conn.commit()
    conn.close()

# Función para modificar un artista
def modificar_artista():
    conn = conectar_db()
    nombre = input("Ingrese nombre del artista a modificar: ")
    edad = int(input("Ingrese nueva edad: "))
    cantidad_albumes = int(input("Ingrese nueva cantidad de álbumes: "))
    genero_musical = input("Ingrese nuevo género musical: ")
    sql = '''UPDATE artistas SET edad = ?, cantidad_albumes = ?, genero_musical = ?
             WHERE nombre = ?'''
    conn.execute(sql, (edad, cantidad_albumes, genero_musical, nombre))
    conn.commit()
    conn.close()

# Función para mostrar todos los artistas
def mostrar_artistas():
    conn = conectar_db()
    sql = '''SELECT * FROM artistas'''
    cursor = conn.execute(sql)
    for row in cursor:
        print(f"Nombre: {row[0]}, Edad: {row[1]}, Cantidad de álbumes: {row[2]}, Género musical: {row[3]}")
    conn.close()

# Función para eliminar un artista
def eliminar_artista():
    conn = conectar_db()
    nombre = input("Ingrese nombre del artista a eliminar: ")
    sql = '''DELETE FROM artistas WHERE nombre = ?'''
    conn.execute(sql, (nombre,))
    conn.commit()
    conn.close()

# Función para buscar un artista
def buscar_artista():
    conn = conectar_db()
    nombre = input("Ingrese nombre del artista a buscar: ")
    sql = '''SELECT * FROM artistas WHERE nombre = ?'''
    cursor = conn.execute(sql, (nombre,))
    row = cursor.fetchone()
    if row:
        print(f"Nombre: {row[0]}, Edad: {row[1]}, Cantidad de álbumes: {row[2]}, Género musical: {row[3]}")
    else:
        print("Artista no encontrado")
    conn.close()s