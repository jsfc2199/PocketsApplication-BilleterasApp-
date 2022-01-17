from tkinter import messagebox
import sqlite3

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
   
def actualizar(comboNombreBilleteras,saldoFinal, consignacion, retiro):
    conexionBaseDatos=sqlite3.connect("Bolsillos")
    puntero=conexionBaseDatos.cursor()    
    
    datos = saldoFinal.get(), consignacion.get(), retiro.get(), comboNombreBilleteras.get()
    
    puntero.execute("UPDATE BOLSILLOS_AHORROS SET SALDO_ACTUAL=?, CONSIGNACIONES=?,RETIROS_TRANSFERENCIAS=? WHERE NOMBRE_BILLETERA=?", (datos))
    conexionBaseDatos.commit()
    messagebox.showinfo("Base de datos","Registro actualizado con éxito")
    

def eliminar(comboNombreBilleteras):
    conexionBaseDatos=sqlite3.connect("Bolsillos")
    puntero=conexionBaseDatos.cursor()    
    puntero.execute("DELETE FROM BOLSILLOS_AHORROS WHERE NOMBRE_BILLETERA=?" , (comboNombreBilleteras.get(),))
    conexionBaseDatos.commit()
    
    messagebox.showinfo("Base de datos","Registro eliminado con éxito")    

def leer(comboNombreBilleteras, saldoActual):
    conexionBaseDatos=sqlite3.connect("Bolsillos")
    puntero=conexionBaseDatos.cursor()
    
    puntero.execute("SELECT * FROM BOLSILLOS_AHORROS WHERE NOMBRE_BILLETERA=?" , (comboNombreBilleteras.get(),))
    informacion = puntero.fetchall()
    for i in informacion:
        saldoActual.set(i[2])
    conexionBaseDatos.commit()

    
def crear(a,b,c,d):#a=nombreBilletra, b = saldoActual, c = consignar, d = retirarTransferir
    conexionBaseDatos=sqlite3.connect("Bolsillos")
    puntero=conexionBaseDatos.cursor()
    
    if verificarRegistro(a.get())==True: 
        messagebox.showwarning("Registro","Se ha encontrado una billetera virtual con el mismo nombre." + 
                               "\n \nPor favor intente realizar un registro nuevo o solicitar información de las billeteras actuales")
    else:
        datos=a.get(), b.get(), c.get(), d.get()
        
        if a.get()=="":#si no hay nombre de billetera no crea el registro
            messagebox.showinfo("Crear","No se puede crear el bolsillo sin un nombre")
            
        elif a.get()!="" and (b.get()=="" and c.get()=="" and d.get()==""):  #INSERTA EL REGISTRO CON SOLO EL NOMBRE
            datos = a.get(), 0, 0, 0    
            puntero.execute("INSERT INTO BOLSILLOS_AHORROS VALUES(NULL,?,?,?,?)",(datos))    
            conexionBaseDatos.commit()
            messagebox.showinfo("Crear","Registro insertado con éxito")
            
        elif a.get()!="" and c.get()!="" and d.get()=="": #insertar registro con consignacion
            datos = a.get(), c.get(), c.get(), 0
            puntero.execute("INSERT INTO BOLSILLOS_AHORROS VALUES(NULL,?,?,?,?)",(datos))    
            conexionBaseDatos.commit()
            messagebox.showinfo("Crear","Registro insertado con éxito")
        else:
            messagebox.showwarning("Crear","No se pudo realizar el registro. Intente crear la billetera sólo con el nombre o el nombre y un valor a consignarle")

def verificarRegistro(nombreBilletera): #verifica si la billetera ya existe en la BD
    conexionBaseDatos=sqlite3.connect("Bolsillos")
    puntero=conexionBaseDatos.cursor()
    puntero.execute("SELECT * FROM BOLSILLOS_AHORROS WHERE NOMBRE_BILLETERA ='{}'".format(nombreBilletera))
    registro = puntero.fetchall()
    if registro:
        return True
    else:
        return False

        
    