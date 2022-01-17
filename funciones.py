from tkinter import messagebox
from tkinter import *
from tkinter import ttk
import sqlite3
import CRUD

#Sale de la aplicación
def salirApp(root):
    salida = messagebox.askokcancel("Salir","¿Deseas salir de la aplicación?")
    if salida == True:
       root.destroy()

#Muestra la versión de la aplicación
def version():
    messagebox.showinfo("Version", "Programa de ahorros en bolsillos Ver. 1.0")

#Muestra información muy general de la aplicación
def acerdaDe():
    messagebox.showinfo("Acerda de", 
                        "Programa de bolsillos virtuales los cuales guardarán la información en una base de datos.\n \n" + 
                        "Podrá transferir dinero desde la cuenta principal a los bolsillos, retirar y consignar dinero a la cuenta "+
                        "principal y a las billeteras calculando previamente el monto que tendrá" + 
                        ", así como descargar todo el dinero de los mismos. También se podrán realizar las operaciones de un CRUD")

#Muestra un mensaje que recomienda leer el readme o el archivo HowItWorks
def comoFunciona():
    messagebox.showinfo("¿Cómo Funciona?","Leer 'readme' o el archivo txt 'HowItWorks'")

#Limpia los campos de escritura y lectura    
def limpiarCampos(nombreBilletera,saldoActual,consignarTransferir,retirar,saldoFinal):
    nombreBilletera.set("")
    saldoActual.set("")
    consignarTransferir.set("")
    retirar.set("")
    saldoFinal.set("")

#Define los valores que tendrá el combo box
def comboBoxBilleteras():
    try:
        conexionBaseDatos=sqlite3.connect("Bolsillos")
        puntero=conexionBaseDatos.cursor()
        puntero.execute("SELECT NOMBRE_BILLETERA FROM BOLSILLOS_AHORROS")
        nombresBilleteras = puntero.fetchall()
        return nombresBilleteras
    except:
        return False

#Refresca los valores que hay en ambos combo box
def refrescar(comboBilleteras, comboBilleterasTransferir):
    try:
        conexionBaseDatos=sqlite3.connect("Bolsillos")
        puntero=conexionBaseDatos.cursor()
        puntero.execute("SELECT NOMBRE_BILLETERA FROM BOLSILLOS_AHORROS")
        nombresBilleteras = puntero.fetchall()
        comboBilleteras['values']=nombresBilleteras
        comboBilleterasTransferir['values']=nombresBilleteras
        messagebox.showinfo("Billeteras", "Billeteras actualizadas con exito.")
    except:
        return False
    
#Solo permite escribir numeros en los campos numeros 
def soloNumeros(texto):
    return texto.isdigit()

#Solo permite escribir letras sin espacios en los campos de escritura
def textoSinEspacios(texto):
    return texto.isalpha()

#Calcula el saldo final que tendrá la billetera inicial seleccionada en función del saldo actual, consignación y retiro
def calcular(comboNombreBilleteras, saldoActual, saldoFinal, valorConsignacion, valorRetiro):
    conexionBaseDatos=sqlite3.connect("Bolsillos")
    puntero=conexionBaseDatos.cursor()
    puntero.execute("SELECT * FROM BOLSILLOS_AHORROS WHERE NOMBRE_BILLETERA=?" , (comboNombreBilleteras.get(),))
    informacion = puntero.fetchall()
    
    for i in informacion:        
        saldoActual.set(i[2])
        
    if valorConsignacion.get()=="" and valorRetiro.get()=="":
        messagebox.showinfo("Saldo final","Se requiere que el campo consignar o retirar tengan valor, o ambos tengan un valor")
        
    elif valorConsignacion.get()!="" and valorRetiro.get()!="":
        saldoFinal.set(i[2]+(int(valorConsignacion.get()))-(int(valorRetiro.get())))   
        
    elif valorConsignacion.get()=="" and valorRetiro.get()!="":
        saldoFinal.set(i[2]-(int(valorRetiro.get())))   
    
    elif valorConsignacion.get()!="" and valorRetiro.get()=="":
        saldoFinal.set(i[2]+(int(valorConsignacion.get())))
 
    else:    
        messagebox.showerror("Error","No se pudo realizar el cálculo del saldo final.")

#Descarga la billetera seleccionada en el segundo combo box moviendo ese dinero a la billetera en el combo box 1
def descargar(comboNombreBilleteras, comboNombreBilleteraDescargar, saldoFinal):
    conexionBaseDatos=sqlite3.connect("Bolsillos")
    puntero=conexionBaseDatos.cursor()
    if comboNombreBilleteras.get()!="CuentaPrincipal":
        messagebox.showerror("Descarga","Por favor, seleccione en el apartado 'Billeteras' la billetera 'CuentaPrincipal', si la eliminó por favor, crearla.")
    if comboNombreBilleteraDescargar.get()=="":
        messagebox.showerror("Descarga","Por favor, seleccione la billetera que será descargada.")
    try:    
        puntero.execute("SELECT * FROM BOLSILLOS_AHORROS WHERE NOMBRE_BILLETERA=?" , (comboNombreBilleteraDescargar.get(),))
        saldoActualBilleteraDescargar=puntero.fetchall()
        
        puntero.execute("SELECT * FROM BOLSILLOS_AHORROS WHERE NOMBRE_BILLETERA=?" , (comboNombreBilleteras.get(),))
        saldoActualCuentaPrincipal=puntero.fetchall()
        
        saldoFinal.set(saldoActualBilleteraDescargar[0][2]+saldoActualCuentaPrincipal[0][2])
        actualizar = messagebox.askokcancel("Descarga","En saldo final, se verá reflejado el valor con el que contará la cuenta principal luego de descargar la billetera a descargar.\nPresione 'Ok' si desea que se realice la descarga completamente y la actualización de los datos.")
       
        if actualizar == True:
            datosCuentaDescargar=0,0,0,comboNombreBilleteraDescargar.get()
            datosCuentaPrincipal = saldoFinal.get(), 0, 0, comboNombreBilleteras.get()
            
            puntero.execute("UPDATE BOLSILLOS_AHORROS SET SALDO_ACTUAL=?, CONSIGNACIONES=?,RETIROS_TRANSFERENCIAS=? WHERE NOMBRE_BILLETERA=?", (datosCuentaDescargar))
            puntero.execute("UPDATE BOLSILLOS_AHORROS SET SALDO_ACTUAL=?, CONSIGNACIONES=?,RETIROS_TRANSFERENCIAS=? WHERE NOMBRE_BILLETERA=?", (datosCuentaPrincipal))
            
            conexionBaseDatos.commit()            
            messagebox.showinfo("Base de datos","Billetera descargada con éxito.\nRegistro actualizado con éxito")
    
    except:
        False

#Permite transferir dinero entre las diferentes billeteras y hace el calculo respectivo con el que contará cada una de las mismas
def transferir(comboNombreBilleteras, comboNombreBilleteraTransferir, transferir, consignar, saldoFinal, saldoActual):
    conexionBaseDatos=sqlite3.connect("Bolsillos")
    puntero=conexionBaseDatos.cursor()
    
    if consignar.get()!="":
        messagebox.showerror("Transferir","Por favor, limpie el campo de consignar para realizar la transferencia")
    try:
        
        puntero.execute("SELECT * FROM BOLSILLOS_AHORROS WHERE NOMBRE_BILLETERA=?" , (comboNombreBilleteras.get(),))
        saldoActualBilletera=puntero.fetchall()
        
        puntero.execute("SELECT * FROM BOLSILLOS_AHORROS WHERE NOMBRE_BILLETERA=?" , (comboNombreBilleteraTransferir.get(),))
        saldoActualBilleteraTransferir=puntero.fetchall()
        
        saldoFinal.set(int(transferir.get())+saldoActualBilleteraTransferir[0][2])
        saldoActual.set(abs(int(transferir.get())-saldoActualBilletera[0][2]))
        
        actualizar = messagebox.askokcancel("Descarga","En saldo final, se verá reflejado el valor con el que contará la billetera que recibira el dinero luego de hacer la transferencia.\nEn valor a consignar se verá reflejado el saldo con el que quedará la billetera inicial. Presione 'Ok' si desea que se realice la descarga completamente y la actualización de los datos.")
        
        if actualizar == True:
            
            datosCuentaBilletera=saldoActual.get(),0,transferir.get(),comboNombreBilleteras.get()
            datosCuentaTransferir = saldoFinal.get(),transferir.get(),0,comboNombreBilleteraTransferir.get()
            
            puntero.execute("UPDATE BOLSILLOS_AHORROS SET SALDO_ACTUAL=?, CONSIGNACIONES=?,RETIROS_TRANSFERENCIAS=? WHERE NOMBRE_BILLETERA=?", (datosCuentaBilletera))
            puntero.execute("UPDATE BOLSILLOS_AHORROS SET SALDO_ACTUAL=?, CONSIGNACIONES=?,RETIROS_TRANSFERENCIAS=? WHERE NOMBRE_BILLETERA=?", (datosCuentaTransferir))
            
            conexionBaseDatos.commit()            
            messagebox.showinfo("Base de datos","Billeteras actualizadas con éxito.")
            
    except:
        False