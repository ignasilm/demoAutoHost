# %% [markdown]
# ## Notebook Jupyter Demo de automatización de interacción con HOST/MVS
# ---
# 
# Esta demo es para mostrar que posibilidades hay para interactuar con un sistema HOST MVS con un código python. Para ello se utiliza la librería [py3270](https://github.com/py3270/py3270) y el emulador [x3270](http://x3270.bgp.nu/)
# 

# %% [markdown]
# Lo primero será importar la libreria py3270

# %%
import time, sys
from py3270 import Emulator


# %% [markdown]
# Iniciamos un objeto Emulador y conectamos al servidor. Al crear el objeto se puede indicar si queremos que sea visible la pantalla del emulador o que funcione sin mostrarla.

# %%
myhost = '127.0.0.1:3270'

my3270 = Emulator(visible=False)
my3270.connect(myhost)
print('Conexion establecida')

# %% [markdown]
# Realizamos el login. 
# 1. Para ello nos aseguramos que la pantalla se ha cargado completamente
# 2. Comprobamos que estamos en la pantalla de 'Logon'
# 3. Informamos el usuario y enviamos enter
# 

# %%
delayt = 1    # segundos de espera para asegurarnos que la pantalla se carga correctamente
mylogin = 'HERC01'
mypass = 'CUL8TR'

my3270.wait_for_field()
my3270.exec_command(b"Clear")
my3270.wait_for_field()
time.sleep(delayt)
if not my3270.string_found(23, 1, 'Logon ===>'):
	sys.exit('Error: print(my3270.string_get(23,1,20))')
my3270.send_string(mylogin)
my3270.send_enter()

# %% [markdown]
# A continuacion, informamos el password y mandamos enter

# %%
my3270.wait_for_field()
time.sleep(delayt)
if not my3270.string_found(1, 2, 'ENTER CURRENT'):
	sys.exit('Error: print(my3270.string_get(1, 2,20))')
my3270.send_string(mypass)
my3270.send_enter()
my3270.wait_for_field()
time.sleep(delayt)
print('Ya nos hemos logado')

# %% [markdown]
# Mandamos varios enter para saltar las siguientes pantallas hasta llegar al menu de aplicaciones

# %%
for i in range(3):
    my3270.send_enter()
    my3270.wait_for_field()
    time.sleep(delayt)

# %% [markdown]
# Seleccionamos la opción del menu para modificar un fichero

# %%
# 2 - EDIT
my3270.send_string("2")
my3270.send_enter()
my3270.wait_for_field()
time.sleep(delayt)

# %% [markdown]
# Informamos el formulario de busqueda de ficheros con los datos del fichero que queremos actualizar 

# %%
my3270.fill_field(6,18,'HERC01', 8)
my3270.fill_field(7,18,'AUTOM', 8)
my3270.fill_field(8,18,'DEMO', 8)
my3270.move_to(12,24)
my3270.delete_field()

# %% [markdown]
# Ejecutamos la busqueda del fichero

# %%
my3270.send_enter()
my3270.wait_for_field()
time.sleep(delayt)
print('Buscamos el fichero a editar')

# %% [markdown]
# Editamos el primer fichero de la lista

# %%
my3270.exec_command(b"TAB")
my3270.exec_command(b"TAB")
my3270.send_string("E")
my3270.send_enter()
my3270.wait_for_field()
time.sleep(delayt)

# %% [markdown]
# Borramos todo el contenido...

# %%
my3270.send_string("TOP")
my3270.send_enter()
my3270.wait_for_field()
time.sleep(delayt)
my3270.exec_command(b"TAB")
my3270.exec_command(b"TAB")
my3270.exec_command(b"TAB")
my3270.send_string("D999")
my3270.send_enter()
my3270.wait_for_field()
time.sleep(delayt)
print('Borramos el contenido')

# %% [markdown]
# ...e insertamos las nuevas lineas

# %%
my3270.exec_command(b"TAB")
my3270.exec_command(b"TAB")
my3270.send_string('i')
my3270.send_enter()
my3270.wait_for_field()
time.sleep(delayt)

for i in range(50):
    my3270.send_string('Contenido antiguo que hay que borrar antes de insertar ')
    my3270.send_string(str(i))
    my3270.send_enter()
    my3270.wait_for_field()
    #time.sleep(delayt)
print('Hemos insertado el nuevo texto en el fichero')
my3270.save_screen('./data/pantalla_demo.html')

# %% [markdown]
# Salimos al menú principal pulsando PF3 varias veces

# %%
for i in range(3):
    my3270.send_pf3()
    my3270.wait_for_field()
    time.sleep(delayt)
print('Salimos al menú para la ultima prueba')

# %% [markdown]
# Como demostración de que es posible leer directamente de pantalla y esperar a que se actualize algún dato, como la ejecucion correcta de algun proceso, vamos a recuperar la hora de pantalla y esperamos a que pase 1 minuto refrescando cada 10 segundos.

# %%
hora_inicial = my3270.string_get(12,70,5)
hora_actual = hora_inicial
intentos = 1
print('La hora inicial es', hora_inicial)
while hora_actual == hora_inicial and intentos <= 6:
    time.sleep(10)
    my3270.send_enter()
    my3270.wait_for_field()
    time.sleep(delayt)
    hora_actual = my3270.string_get(12,70,5)
    print('En el intento', intentos, 'la hora actual es', hora_actual, 'y la hora inicial era', hora_inicial)
    intentos = intentos + 1



# %% [markdown]
# Finalmente, terminamos la sesion y cerramos la conexion.

# %%
my3270.send_pf3()
my3270.wait_for_field()
time.sleep(delayt)
if not my3270.string_found(5, 2, 'READY'):
    my3270.send_pf3()
    my3270.wait_for_field()
    time.sleep(delayt)
    if not my3270.string_found(5, 2, 'READY'):
        my3270.send_pf3()
        my3270.wait_for_field()
        time.sleep(delayt)

my3270.send_string('LOGOFF')
my3270.send_enter()
my3270.wait_for_field()
time.sleep(delayt)
# Desconectamos y cerramos el emulador
my3270.terminate()

print('Hemos terminado')

