# Backdoor Server (Víctima)

Este es el código del servidor que actúa como la "víctima" en un entorno de prueba controlado. El servidor escucha conexiones entrantes, recibe comandos, los ejecuta y devuelve los resultados al cliente (atacante).

---

## Requisitos

1. **Python 3.x**: Asegúrate de tener Python instalado.
2. **Librerías necesarias**:
   - `cryptography`

Instala las dependencias ejecutando:

```bash
pip install cryptography

Cómo Usar
Clonar el repositorio (opcional):

bash
Copy
git clone https://github.com/tuusuario/turepositorio.git
cd turepositorio
Ejecutar el servidor:

Guarda el código en un archivo, por ejemplo, server.py.

Ejecuta el servidor:

bash
Copy
python server.py
El servidor escuchará en todas las interfaces (0.0.0.0) en el puerto 4444.

Funcionalidades del Servidor:

Ejecutar comandos: El servidor ejecuta comandos enviados por el cliente y devuelve la salida.

Descargar archivos: Si el cliente envía el comando download <ruta>, el servidor envía el archivo especificado.

Persistencia: El comando persist agrega el servidor al inicio del sistema (Windows).

Ocultación: El comando hide simula la ocultación del proceso.

Detener el servidor:

Presiona Ctrl + C en la terminal donde se está ejecutando el servidor.

Entorno de Prueba
Máquina Virtual: Usa una máquina virtual (por ejemplo, VirtualBox) para ejecutar el servidor en un entorno aislado.

Firewall: Asegúrate de que el puerto 4444 esté abierto en el firewall de la máquina víctima.



--------------------------------------------------------------------------------------------------------------
---

### **README.md para el Cliente (Atacante)**

```markdown
# Backdoor Client (Atacante)

Este es el código del cliente que actúa como el "atacante" en un entorno de prueba controlado. El cliente se conecta al servidor (víctima), envía comandos y recibe los resultados.

---

## Requisitos

1. **Python 3.x**: Asegúrate de tener Python instalado.
2. **Librerías necesarias**:
   - `cryptography`

Instala las dependencias ejecutando:

```bash
pip install cryptography
Cómo Usar
Clonar el repositorio (opcional):

bash
Copy
git clone https://github.com/tuusuario/turepositorio.git
cd turepositorio
Ejecutar el cliente:

Guarda el código en un archivo, por ejemplo, client.py.

Ejecuta el cliente:

bash
Copy
python client.py
El cliente intentará conectarse al servidor en la dirección IP y puerto especificados.

Funcionalidades del Cliente:

Ejecutar comandos: Envía comandos al servidor y recibe la salida.

bash
Copy
shell> whoami
shell> ipconfig
Descargar archivos: Usa el comando download <ruta> para descargar un archivo desde la víctima.

bash
Copy
shell> download C:/secret.txt
Agregar persistencia: Usa el comando persist para agregar el backdoor al inicio del sistema de la víctima.

bash
Copy
shell> persist
Ocultar proceso: Usa el comando hide para simular la ocultación del proceso en la víctima.

bash
Copy
shell> hide
Salir del cliente:

Escribe exit o quit para cerrar la conexión.

Entorno de Prueba
Máquina Virtual: Usa una máquina virtual (por ejemplo, VirtualBox) para ejecutar el cliente en un entorno aislado.

Dirección IP: Asegúrate de conocer la dirección IP de la máquina víctima.
