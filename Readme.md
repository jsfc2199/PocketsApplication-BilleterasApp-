# Aplicación bolsillos (Base de datos)
Bolsillos que permitirán la gestión de ahorros para diferentes objetivos.

## Herramientas necesarias 
Se deberá tener Python3 instalado

## Cómo ejectutar el programa
Para ejecutar el programa principal se debe ejecutar el siguiente comando en el CMD dentro de la carpeta: python BolsillosVirtuales.py

## Generalidades
Note: The "HowItWorks.txt" file has the same information as the readme but in english.

En la barra de menú se encontrarán los campos de archivo, limpiar campos, CRUD, y ayuda.

Archivo: Contará con dos pestañas, "Conectar a la base de datos" y "Salir". La primera hará la conexión a la base de datos. Se recomienda, al usar por primera vez la aplicación, usar ésta función, luego no tendrá que volverse a hacer la conexión. La pestaña salir, como sunombre indica, saldrá de la aplicación.

Limpiar Campos: Borrará el contenido escrito en los campos de Nombre nueva billetera, saldo actual, valor a consignar, valor a retirar/transferir y saldo final.

CRUD: Tendrá las pestañas "Crear", "Leer", "Actualizar" y "Eliminar" que tendrás las mismas funciones de los botones que están al final de la aplicación. (Se explica más adelante)

Ayuda: Contiene las pestañas "¿Cómo funciona?", "Version", y "Acerca de...". La pestaña "¿Cómo funciona? sólo avisará que se lea el readme o el archivo txt "HowItWorks". "Versión" solo mostrará la versión, siendo ésta la 1.0, y "Acerca de..." menciona las características más generales de la aplicación.


## Interfaz y ¿Cómo funciona?
Se presentan dos combo box en los cuales se verán las billeteras ya sea que se tengan desde antes o se creen nuevas, esto último a partir del botón Crear.

Al presionar Crear habrá dos formas de hacerlo, con sólo el nombre de la billetera o el nombre junto con un valor a consignar, de lo contrario no se podrá crear. Luego de ellos se podrá usar el botón "Refrescar", que hará que se actualice la información de los combo box.

El botón leer permitirá leer únicamente el saldo actual de la billetera en el apartado "Billeteras" el cual podrá ser utilizado para lo siguiente:
	- Usando el botón "Calcular", que a su vez calculará el saldo final que se pretende tener en la billetera luego de consignarle y/o retirarle dinero
	- Luego de usar el botón anterior, se podrá utilizar el botón "Actualizar", en caso de que se quiera actualizar el saldo actual por el saldo final luego de hacer la operación. Los registros se guardarán en la base de datos, si sólo se consignó, si sólo se retiró, o se hizo ambas cosas quedará registrado en la base de datos junto con el nuevo saldo actual.

El botón eliminar, eliminará la billetera que se encuentre en el campo "Billeteras" y nuevamente se deberá usar el botón "Refrescar" para que se actualicen los combo box.

Luego, el botón "Descargar" permitirá retirar el dinero de la billetera seleccionada en el combo box "Billetera a descargar/transferir", pero sólo permitirá está acción si la billetera seleccionada en el combo box "Billeteras" es la denominada "CuentaPrincipal" es por esto que la billetera "CuentaPrincipal" se crea automáticamente al conectarse por primera vez con la base de datos.
Entonces, para usar este boton se tendrá que tener seleccionada "CuentaPrincipal". Siempre se descargará el total de la billetera seleccionada en el combo box "Billetera a descargar/transferir". Cabe mencionar que al presionar "Descargar" aparecerá un messagebox indicando si quieres realizar la operación, en caso de que se acepte, "CuentaPrincipal" tendrá el dinero que tenía más el montó que se descarga de la segunda billetera. Por lo tanto la segunda billetera quedará con un valor de 0.

Finalmente el botón "Transferir" permitirá transferir dinero entre las diferentes billeteras, se podrá realizar esto entre todas las billeteras, es decir, cualquier combinación de billeteras.
Al presionar este botón, el campo "Valor a consignar" reflejará el valor con el que quedará la billetera del apartado "Billeteras", mientras que en saldo final se verá el valor con el que quedará la billetera en el aparatado "Billetera a descargar/transferir". Nuevamente se pregunta si se queire hacer esta operación y si sí, se actualizará todo en la base de datos.

