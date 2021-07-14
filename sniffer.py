# only ip 4 and tcp stream
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)# tcp stream and ip v4
while True:
	data = s.recv(65535)
	data = str(data,'hex')
	data = bytes.fromhex(data)
	print(data.decode('utf-8'))