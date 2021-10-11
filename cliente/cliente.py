import socket

s = socket.socket()
host = input(str("Por favor, entre com o endereço do host: "))
port = 8080

s.connect((host, port))
print("conectado...")

filename = input(str("Por favor, coloque o nome do Arquivo: "))
file = open(filename, 'wb')
file_data = s.recv(1024)
file.write(file_data)
file.close()
print("Arquivo foi recebido com sucesso")
