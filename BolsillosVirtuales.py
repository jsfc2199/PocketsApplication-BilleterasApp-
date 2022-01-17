from tkinter import *
from tkinter import ttk
import funciones
import CRUD

root = Tk()
root.title("Billeteras Virtuales")

root.iconbitmap("imagen.ico")

#--------------------------------Menu Superior---------------------------------
barraMenu = Menu()
root.config(menu=barraMenu, width=300,height=300)


bbddMenu=Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar a base de datos", command=lambda:CRUD.conexionBBDD())
bbddMenu.add_command(label="Salir", command=lambda: funciones.salirApp(root))

limpiarMenu=Menu(barraMenu, tearoff=0)
limpiarMenu.add_command(label="Limpiar", 
                        command=lambda:funciones.limpiarCampos(nombreNuevaBilleteraString, saldoActualDouble,
                                                               valorConsignarDouble,valorRetirarDouble,
                                                               saldoFinalDouble))

crudMenu=Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Crear", command=lambda: CRUD.crear(nombreNuevaBilleteraString, saldoActualDouble, valorConsignarDouble, valorRetirarDouble))
crudMenu.add_command(label="Leer", command=lambda: CRUD.leer(billeteras, saldoActualDouble))
crudMenu.add_command(label="Actualizar", command= lambda: CRUD.actualizar(billeteras, saldoFinalDouble, valorConsignarDouble, valorRetirarDouble))
crudMenu.add_command(label="Eliminar", command=lambda: CRUD.eliminar(billeteras))

ayudaMenu=Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="¿Cómo funciona?", command=lambda:funciones.comoFunciona()) #debe tener un command , explica como funciona el programa
ayudaMenu.add_command(label="Version", command=lambda: funciones.version())
ayudaMenu.add_command(label="Acerca de...", command = lambda:funciones.acerdaDe())

barraMenu.add_cascade(label="Archivo",menu=bbddMenu)
barraMenu.add_cascade(label="Limpiar campos",menu=limpiarMenu)
barraMenu.add_cascade(label="CRUD",menu=crudMenu)
barraMenu.add_cascade(label="Ayuda",menu=ayudaMenu)

#--------------------------------Labels frame----------------------------------
frameSuperior=Frame(root)
frameSuperior.pack()

billeteraDisponible=Label(frameSuperior, text="Billeteras: ")
billeteraDisponible.grid(row=0,column=0,pady=10,padx=10,sticky="w")

billeteraTransferir=Label(frameSuperior, text="Billetera a descargar/transferir: ")
billeteraTransferir.grid(row=1,column=0,pady=10,padx=10,sticky="w")

nuevaBilletera=Label(frameSuperior,text="Nombre nueva billetera: ")
nuevaBilletera.grid(row=2,column=0,pady=10,padx=10,sticky="w")

saldoActual=Label(frameSuperior, text="Saldo actual $:")
saldoActual.grid(row=3,column=0,pady=10,padx=10,sticky="w")

valorConsignar=Label(frameSuperior, text="Valor a consignar $: ")
valorConsignar.grid(row=4,column=0,pady=10,padx=10,sticky="w")

valorRetirar=Label(frameSuperior, text="Valor a retirar/transferir $: ")
valorRetirar.grid(row=5,column=0,pady=10,padx=10,sticky="w")

saldoFinal=Label(frameSuperior, text="Saldo final $: ")
saldoFinal.grid(row=6,column=0,pady=10,padx=10,sticky="w")

#--------------------------------Entrys frame----------------------------------
nombreNuevaBilleteraString=StringVar()
saldoActualDouble=StringVar()
valorConsignarDouble=StringVar()
valorRetirarDouble=StringVar()
saldoFinalDouble=StringVar()


cuadroNombre=Entry(frameSuperior, textvariable=nombreNuevaBilleteraString,width=30, validate = 'key', validatecommand=(root.register(funciones.textoSinEspacios),'%S'))
cuadroNombre.grid(row=2,column=1, padx=10, pady=10)

cuadroSaldoActual=Entry(frameSuperior, textvariable=saldoActualDouble,width=30)
cuadroSaldoActual.grid(row=3,column=1, padx=10, pady=10)
cuadroSaldoActual.configure(state="readonly")

cuadroConsignar=Entry(frameSuperior, textvariable=valorConsignarDouble,width=30, validate = "key", validatecommand=(root.register(funciones.soloNumeros), '%S'))
cuadroConsignar.grid(row=4,column=1, padx=10, pady=10)

cuadroRetirarTransferir=Entry(frameSuperior, textvariable=valorRetirarDouble,width=30,validate = "key", validatecommand=(root.register(funciones.soloNumeros), '%S'))
cuadroRetirarTransferir.grid(row=5,column=1, padx=10, pady=10)

cuadroSaldoFinal=Entry(frameSuperior, textvariable=saldoFinalDouble,width=30)
cuadroSaldoFinal.grid(row=6,column=1)
cuadroSaldoFinal.configure(state="readonly")



#--------------------------------ComboBox frame--------------------------------
nombresBilleterasActuales = StringVar()
nombreBilleteraTransferir = StringVar()

billeteras = ttk.Combobox(frameSuperior, textvariable=nombresBilleterasActuales, state="readonly",width=27)
billeteras['values'] = funciones.comboBoxBilleteras()
billeteras.grid(row=0,column=1, padx=10,pady=10)


billeteraTransferir = ttk.Combobox(frameSuperior, textvariable=nombreBilleteraTransferir, state="readonly",width=27)
billeteraTransferir['values'] = funciones.comboBoxBilleteras()
billeteraTransferir.grid(row=1,column=1, padx=10,pady=10)

#--------------------boton calcular-----------------------------------------------
frameIntermedio = Frame(root)
frameIntermedio.pack()

botonCalcular = Button(frameIntermedio, text="Calcular",width=12, command=lambda:funciones.calcular(billeteras, saldoActualDouble, saldoFinalDouble, valorConsignarDouble, valorRetirarDouble))
botonCalcular.grid(row=1,column=0,padx=10,pady=10)

botonDescargar= Button(frameIntermedio, text="Descargar",width=12, command=lambda: funciones.descargar(billeteras, billeteraTransferir, saldoFinalDouble))
botonDescargar.grid(row=1,column=1,padx=10,pady=10)

botonTransferir= Button(frameIntermedio, text="Transferir",width=12, command=lambda: funciones.transferir(billeteras, billeteraTransferir, valorRetirarDouble, valorConsignarDouble, saldoFinalDouble, valorConsignarDouble)) 
botonTransferir.grid(row=1,column=2,padx=10,pady=10)

botonBorrarCampos= Button(frameIntermedio, text="Limpiar campos",width=12,
                          command=lambda:funciones.limpiarCampos(nombreNuevaBilleteraString, saldoActualDouble,
                                                               valorConsignarDouble,valorRetirarDouble,
                                                               saldoFinalDouble))
botonBorrarCampos.grid(row=1,column=3,padx=10,pady=10)

actualizarComboBox = Button(frameSuperior, text="Refrescar",height=4, command=lambda:funciones.refrescar(billeteras,billeteraTransferir))
actualizarComboBox.grid(row=0,column=3,padx=10,pady=10,rowspan=2)


#--------------------botonesCRUD-----------------------------------------------
frameInferior = Frame(root)
frameInferior.pack()

botonCrear=Button(frameInferior, text="Crear",width=12, command=lambda: CRUD.crear(nombreNuevaBilleteraString, saldoActualDouble, valorConsignarDouble, valorRetirarDouble))
botonCrear.grid(row=1,column=0,sticky="w",padx=10,pady=10)

botonLeer=Button(frameInferior, text="Leer",width=12, command=lambda: CRUD.leer(billeteras, saldoActualDouble))
botonLeer.grid(row=1,column=1,sticky="w",padx=10,pady=10)

botonActualizar=Button(frameInferior, text="Actualizar",width=12, command= lambda: CRUD.actualizar(billeteras, saldoFinalDouble, valorConsignarDouble, valorRetirarDouble)) 
botonActualizar.grid(row=1,column=2,sticky="w",padx=10,pady=10)

botonEliminar=Button(frameInferior, text="Eliminar",width=12, command=lambda: CRUD.eliminar(billeteras))
botonEliminar.grid(row=1,column=3,sticky="w",padx=10,pady=10)



#--------------------Mainloop--------------------------------------------------
root.mainloop()