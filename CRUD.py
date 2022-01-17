from tkinter import messagebox
import sqlite3

#Realiza la conexión a la base de datos y crea la billetera CuentaPrincipal
def conexionBBDD():
    conexionBaseDatos=sqlite3.connect("Bolsillos")
    puntero=conexionBaseDatos.cursor()
    try:
        puntero.execute('''
                         CREATE TABLE BOLSILLOS_AHORROS(
                             ID INTEGER PRIMARY KEY AUTOINCREMENT,
                             NOMBRE_BILLETERA VARCHAR(50),
                             SALDO_ACTUAL INTEGER,
                             CONSIGNACIONES INTEGER,
                             RETIROS_TRANSFERENCIAS INTEGER
                             )
                         ''')
               
        puntero.execute("INSERT INTO BOLSILLOS_AHORROS VALUES(NULL,'CuentaPrincipal',0,0,0)",)
        conexionBaseDatos.commit()
        
        messagebox.showinfo("Base de datos","Base de datos creada con éxito")
        messagebox.showinfo("Base de datos","Se ha insertado el registro: 'CuentaPrincipal'")
        
        
    except:
        messagebox.showwarning("Base de datos","La base de datos que se quiere crear ya existe")

#Actualiza la información de acuerdo a los campos saldo actual, consignaciones y retiros 
def actualizar(comboNombreBilleteras,saldoFinal, consignacion, retiro):
    conexionBaseDatos=sqlite3.connect("Bolsillos")
    puntero=conexionBaseDatos.cursor()    
    
    datos = saldoFinal.get(), consignacion.get(), retiro.get(), comboNombreBilleteras.get()
    
    puntero.execute("UPDATE BOLSILLOS_AHORROS SET SALDO_ACTUAL=?, CONSIGNACIONES=?,RETIROS_TRANSFERENCIAS=? WHERE NOMBRE_BILLETERA=?", (datos))
    conexionBaseDatos.commit()
    messagebox.showinfo("Base de datos","Registro actualizado con éxito")
    
#Elimina la billetera seleccionada del primer combo box
def eliminar(comboNombreBilleteras):
    conexionBaseDatos=sqlite3.connect("Bolsillos")
    puntero=conexionBaseDatos.cursor()    
    puntero.execute("DELETE FROM BOLSILLOS_AHORROS WHERE NOMBRE_BILLETERA=?" , (comboNombreBilleteras.get(),))
    conexionBaseDatos.commit()
    
    messagebox.showinfo("Base de datos","Registro eliminado con éxito")    

#lee la información de saldo actual que se encuentre en la billetera seleccionada en el primer combo box
def leer(comboNombreBilleteras, saldoActual):
    conexionBaseDatos=sqlite3.connect("Bolsillos")
    puntero=conexionBaseDatos.cursor()
    
    puntero.execute("SELECT * FROM BOLSILLOS_AHORROS WHERE NOMBRE_BILLETERA=?" , (comboNombreBilleteras.get(),))
    informacion = puntero.fetchall()
    for i in informacion:
        saldoActual.set(i[2])
    conexionBaseDatos.commit()

#Crea una nueva billetera solo usando el nombre o usando el nombre y un valor a consignar    
def crear(nombreBilletra, saldoActual, consignar, retirarTransferir):
    conexionBaseDatos=sqlite3.connect("Bolsillos")
    puntero=conexionBaseDatos.cursor()
    
    if verificarRegistro(nombreBilletra.get())==True: 
        messagebox.showwarning("Registro","Se ha encontrado una billetera virtual con el mismo nombre." + 
                               "\n \nPor favor intente realizar un registro nuevo o solicitar información de las billeteras actuales")
    else:
        datos=nombreBilletra.get(), saldoActual.get(), consignar.get(), retirarTransferir.get()
        
        if nombreBilletra.get()=="":
            messagebox.showinfo("Crear","No se puede crear el bolsillo sin un nombre")
            
        elif nombreBilletra.get()!="" and (saldoActual.get()=="" and consignar.get()=="" and retirarTransferir.get()==""):
            datos = nombreBilletra.get(), 0, 0, 0    
            puntero.execute("INSERT INTO BOLSILLOS_AHORROS VALUES(NULL,?,?,?,?)",(datos))    
            conexionBaseDatos.commit()
            messagebox.showinfo("Crear","Registro insertado con éxito")
            
        elif nombreBilletra.get()!="" and consignar.get()!="" and retirarTransferir.get()=="":
            datos = nombreBilletra.get(), consignar.get(), consignar.get(), 0
            puntero.execute("INSERT INTO BOLSILLOS_AHORROS VALUES(NULL,?,?,?,?)",(datos))    
            conexionBaseDatos.commit()
            messagebox.showinfo("Crear","Registro insertado con éxito")
        else:
            messagebox.showwarning("Crear","No se pudo realizar el registro. Intente crear la billetera sólo con el nombre o el nombre y un valor a consignarle")

#verifica si la billetera ya existe en la BD
def verificarRegistro(nombreBilletera):
    conexionBaseDatos=sqlite3.connect("Bolsillos")
    puntero=conexionBaseDatos.cursor()
    puntero.execute("SELECT * FROM BOLSILLOS_AHORROS WHERE NOMBRE_BILLETERA ='{}'".format(nombreBilletera))
    registro = puntero.fetchall()
    if registro:
        return True
    else:
        return False