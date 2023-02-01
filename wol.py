import socket

def isWol(dati):
	correct = False
	correct = dati[0:12] == 'ffffffffffff'
	mac = dati[12:24] * 16
	correct = correct and mac == dati[12:]
	return correct
	
#ip = "192.168.1.23" #Natalino
ip = "192.168.1.16"	#PC grande Giamma
port = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = (ip, port)
s.bind(server_address)
print("Ctrl+c per chiudere il server")
print("Server in ascolto")
while True:
	data, address = s.recvfrom(4096)
	isW = isWol(data.hex())
	if isW:
		print("WOL")
		s.sendto(data, ("192.168.1.255", 9))
		
