# demoAutoHost
Demo de cómo usar la librería py3270 para interactuar con un Host MVS para poder realizar automatizaciones

---

## Descripción

Para ejecutar este programa/Notebook se necesitan básicamente 2 cosas:

1. La librería [py3270](https://github.com/py3270/py3270). Una vez tengas un workspace para este proyecto, yo me hago un entorno virtual para cada proyecto, puedes instalar esta librería con “pip install py3270”, como se haría con cualquier librería Python.

2. El emulador [x3270](http://x3270.bgp.nu/). Del emulador x3270 ha varias versiones que son variantes del mismo según para que se usan, pero todas están en la misma web, unas son para usar como emulador normal, otra es la versión Windows. La wc3270 es la versión que necesita la librería [py3270](https://github.com/py3270/py3270) en windows. El fichero wc3270.exe hay que copiarlo en la raíz del workspace, donde están los ficheros .py o .ipynb. 

Otra cosa necesaria es un host contra el que conectarse. Para esta demo he instalado un Hercules. En concreto para tener ya un sistema funcionando he usado esta versión de [TK4](https://wotho.ethz.ch/tk4-/) que ya trae todo lo necesario. Prácticamente solo hay que descargar/descomprimir el fichero [tk4-_v1.00_current.zip](https://wotho.ethz.ch/tk4-/tk4-_v1.00_current.zip) y ejecutar el comando mvs.bat.


---

## Preparar entorno en local

1. Instalar Python 3.8+ desde [python.org](https://www.python.org/downloads/)

2. crear directorio:

	`cd c:\Dev\Python\workspace`
	
	`mkdir demoAutoHost`
	
	`cd demoAutoHost`
	
3. crear entorno virtual
	
	`pip install virtualenv`
	
	`virtualenv env`
	
4. Activar el entorno virtual
	desde C:\Dev\Python\workspace\demoAutoHost ejecutar:
	
	`c:/Dev/Python/workspace/demoAutoHost/env/Scripts/activate.ps1`
	
5. Copiar codigo de demoAutoHost en C:\Dev\Python\workspace\demoAutoHost

6. instalar librerias

    `pip install py3270`
    o
	`pip install -r .\requirements.txt` (Aquí pueden haber más porque el VSCode y Jupyter han instalado las que necesitan para ejecutar el notebook )
	
7. Ejecutar aplicacion

	`c:/Dev/Python/workspace/demoAutoHost/env/Scripts/python.exe c:/Dev/Python/workspace/demoAutoHost/demoAutoHost.py`

