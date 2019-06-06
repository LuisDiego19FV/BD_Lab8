# lab8.py
# Por: Luis Diego Fernandez 16344
import os
import psycopg2

# Connection and Cursor
con = psycopg2.connect("dbname=lab8db user=postgres password=diego1234")
cur = con.cursor()

# print all information from last Query
def printQuery():
    row = cur.fetchone()

    if row is None:
        print("No se encontro la opcion buscada")
        return 0
    print("Resultado:")
    while row is not None:
        print(row)
        row = cur.fetchone()

    return 0

# show data of a Query
def showAllTable(table):
    cur.execute("SELECT * FROM "+ str(table))
    printQuery()

    return 0

# ej1
def ejercicioA(velocidad, ram):
    try:
        cur.execute("SELECT modelo, precio FROM pc WHERE velocidad = " + \
            str(velocidad) + " and ram = " + str(ram))
        printQuery()
    except psycopg2.DatabaseError as error:
        print("")
        return -1

    return 0

# ej2
def ejercicioB(modelo):
    try:
        cur.execute("DELETE FROM producto WHERE modelo = '" + str(modelo)+ "'")
        cur.execute("DELETE FROM pc WHERE modelo = '" + str(modelo) + "'")
    except psycopg2.DatabaseError as error:
        con.rollback()
        print("Modelo no existe")
        return -1
    con.commit()
    return 0

# ej3
def ejercicioC(modelo):
    try:
        cur.execute("UPDATE pc SET precio = precio-100 WHERE modelo = '" + str(modelo) + "'")
    except psycopg2.DatabaseError as error:
        con.rollback()
        print("Modelo no existe")
        return -1
    con.commit()
    return 0

# ej4
def ejercicioD(fabricante, modelo, velocidad, ram, disco, precio):
    try:
        cur.execute("INSERT INTO pc VALUES ('" + str(modelo) + \
            "', " +  str(velocidad) + ", " + str(ram) + ", " + str(disco) \
             + ", " + str(precio) +")")
        cur.execute("INSERT INTO producto VALUES ('" + str(fabricante) \
        + "', '" + str(modelo) + "', 'PC')")
    except psycopg2.DatabaseError as error:
        con.rollback()
        print("La tupla ya existe")
        return -1
    print("Nueva tupla insertada")
    con.commit()
    return 0

# MENU

end = False

os.system('cls' if os.name=='nt' else 'clear')

while not end:
    print("Opciones")
    print("1. Ejercicio A")
    print("2. Ejercicio B")
    print("3. Ejercicio C")
    print("4. Ejercicio D")
    print("5. Mostrar tabla")
    print("6. Salir")

    try:
        opcion = int(input("\nIngrese una de las opciones anteriores: "))
    except ValueError as error:
        print("Ingrese unicamente el numero de opcion requerida")

    if opcion < 1 or opcion > 6:
        print("Ingrese unicamente el numero de opcion requerida")

    if opcion == 1:
        os.system('cls' if os.name=='nt' else 'clear')
        print("Se localiza las PCs con una cierta velocidad y RAM.")
        try:
            velocidad = float(input("Ingrese velocida (float): "))
            ram = int(input("Ingrese ram (int): "))
            ejercicioA(velocidad,ram)
        except ValueError as error:
            print("Ingrese unicamente integers")

    if opcion == 2:
        os.system('cls' if os.name=='nt' else 'clear')
        print("Eliminar la tupla segun modelo.")
        try:
            modelo = input("Ingrese modelo: ")
            ejercicioB(modelo)
        except ValueError as error:
            print("Ingrese un modelo")

    if opcion == 3:
        os.system('cls' if os.name=='nt' else 'clear')
        print("Decrecer el precio 100 dolares de un modelo.")
        try:
            modelo = input("Ingrese modelo: ")
            ejercicioC(modelo)
        except ValueError as error:
            print("Ingrese un modelo")

    if opcion == 4:
        os.system('cls' if os.name=='nt' else 'clear')
        print("Ingrese una nueva tupla.")
        try:
            fabricante = input("Ingrese fabricante: ")
            modelo = input("Ingrese modelo: ")
            velocidad = float(input("Ingrese velocidad (float): "))
            ram = int(input("Ingrese RAM (int): "))
            disco = int(input("Ingrese disco (int): "))
            precio = float(input("Ingrese precio (float): "))
            ejercicioD(fabricante, modelo, velocidad, ram, disco, precio)
        except ValueError as error:
            print("Error en los valores ingresados")

    if opcion == 5:
        os.system('cls' if os.name=='nt' else 'clear')
        print("Elija una de las tablas a mostrar: ")
        print("1. producto")
        print("2. pc")
        try:
            opcion = int(input("Ingrese modelo: "))
        except ValueError as error:
            print("Ingrese una de las opciones")
            break

        if opcion == 1:
            showAllTable('producto')
        elif opcion == 2:
            showAllTable('pc')
        else:
            print("Ingrese unicamente una de las opciones")

    if opcion == 6:
        end = True
    else:
        input("\nPresione ENTER para continuar")
        os.system('cls' if os.name=='nt' else 'clear')



# Close shit
cur.close()
con.close()
