import socket
import time

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
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
server_address = (ip, port)

time.sleep(5)

while True:
	try:
		s.bind(server_address)
		break
	except:
		time.sleep(5)

print("Ctrl+c per chiudere il server")
print("Server in ascolto")
while True:
	data, address = s.recvfrom(4096)
	isW = isWol(data.hex())
	if isW:
		# print("WOL") solo per debug
		s.sendto(data, ("192.168.1.255", 9))
		
