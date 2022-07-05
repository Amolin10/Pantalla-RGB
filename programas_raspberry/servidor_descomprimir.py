# server.py
from zipfile import ZipFile
import socket
import struct
import os
import time

# Esta función se asegura de que se reciban los bytes
# que indican el tamaño del archivo que será enviado,
# que es codificado por el cliente vía struct.pack(),
# función la cual genera una secuencia de bytes que
# representan el tamaño del archivo.
def receive_file_size(sck: socket.socket):
    fmt = "<Q"
    expected_bytes = struct.calcsize(fmt)
    received_bytes = 0
    stream = bytes()
    while received_bytes < expected_bytes:
        chunk = sck.recv(expected_bytes - received_bytes)
        stream += chunk
        received_bytes += len(chunk)
    filesize = struct.unpack(fmt, stream)[0]
    return filesize


# Leer primero del socket la cantidad de 
# bytes que se recibirán del archivo.
def receive_file(sck: socket.socket, filename):
    filesize = receive_file_size(sck)
    # Abrir un nuevo archivo en donde guardar
    # los datos recibidos.
    with open(filename, "wb") as f:
        received_bytes = 0
        # Recibir los datos del archivo en bloques de
        # 1024 bytes hasta llegar a la cantidad de
        # bytes total informada por el cliente.
        while received_bytes < filesize:
            chunk = sck.recv(1024)
            if chunk:
                f.write(chunk)
                received_bytes += len(chunk)

#Tiempo de espera para que se inicie el programa al encender la Raspberry
time.sleep(22)

#Ruta donde se va a guardar la configuración recibida 
ruta = '/var/www/html/UploadServer/upload/'
#Nombre del archivo recibido
file_name = 'config.zip'

#Dirección y puerto en donde se levanta el socket
with socket.create_server(("192.168.1.110", 6190)) as server:
    print("Esperando al cliente...")
    #El servidor se encontrará en espera hasta recibir una petición de conexión
    conn, address = server.accept()
    print(f"{address[0]}:{address[1]} conectado.")
    print("Recibiendo archivo...")
    #Guardar el archivo recibido mediante la conexión en la ruta establecida 
    receive_file(conn, ruta + file_name)
    print("Archivo recibido.")

    #Descomprime el archivo recibido
    with ZipFile(ruta + file_name, 'r') as zip:
        zip.printdir()
        zip.extractall(path=ruta) 


print("Conexión cerrada.")

#Al recibir un archivo se reinicia la Raspberry
os.system('reboot')