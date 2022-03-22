import sqlite3
from sqlite3 import Error

try:
    con = sqlite3.connect('mislang507.db')

    print("Conexion exitosa")
except Error:
    print("Conexion fallida")

try:
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS slang(id integer PRIMARY KEY, palabra text, definicion text)")
    print("Creacion exitosa")
except Error:
    print("Error en creacion")

print("DICCIONARIO DE SLANG 507")
print("SELECCIONE UNA DE LAS SIGUIENTES OPCIONES:")
print("1: Agregar")
print("2: Editar")
print("3: Eliminar")
print("4: Ver listado")
print("5: Buscar significado")
seleccion = int(input(""))

if seleccion == 1:

    id = int(input("ID: "))
    palabra = input("Slang: ")
    definicion = input("definicion: ")

    try:
        cur = con.cursor()
        cur.execute('''INSERT INTO slang VALUES(?, ?, ? )''', (id, palabra, definicion))
        con.commit()
        print("Insercion exitosa")
    except Error:
        print("Error en insercion")

elif seleccion == 2:

    try:
        editar_palabra = input("Palabra a editar: ")
        editar_definicion = input("Nueva definicion: ")
        cur = con.cursor()
        cur.execute('UPDATE slang SET definicion = ? WHERE palabra = ?',  (editar_definicion, editar_palabra,))
        con.commit()
        print("Actualizacion exitosa")
    except Error:
        print("Error al actualizar datos")

elif seleccion == 3:

    try:

        remover = input("Eliminar: ")
        cur = con.cursor()
        cur.execute('DELETE FROM slang WHERE palabra = ?', (remover,))
        con.commit()
        print("Registro Eliminado")
    except Error:
        print("Error al eliminar")

elif seleccion == 4:
    try:

        cur = con.cursor()
        cur.execute('SELECT id, palabra, definicion FROM slang ')
        p = cur.fetchall()

        for i in p:
            print(i)


    except:
        print("Error al traer datos")

elif seleccion == 5:
    try:
        peticion = input("Buscar: ")
        cur = con.cursor()
        cur.execute('SELECT definicion FROM slang WHERE palabra = ?', (peticion,))
        # con.commit()
        print(cur.fetchall())
        # for slang in peticion:

    except Error:
        print("Error al traer datos")

con.close()
