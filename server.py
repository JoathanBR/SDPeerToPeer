import socket

s = socket.socket()
host = socket.gethostname()  #pegar o endereço do host
port = 8080
s.bind((host, port))
s.listen(1)  #escutar 1 computador
print(host)
print("Esperando por alguma conexão...")

conn, addr = s.accept()
print(addr, "Tem conexão com a rede")

filename = input(str("Por favor, coloque o nome do Arquivo: "))
file = open(filename, 'rb')
filedata = file.read(1024)
print(filedata)
conn.send(filedata)
print("Arquivo foi mandado com sucesso")