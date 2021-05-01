import socket
import sys
import requests , urllib.request
import time
details = {
	"vendor":"cisco",
	"model":"isr-4xxx", # it will get printed after the router get's booted up
	"os":"ios", 
	"ram":"4gb",
}
print(f"Booting ...")
time.sleep(2.5)
for i in details:
	print(f"{i}:{details[i]}")

try:
	# here we will give the network setting of a router 
	network_setting = [{
		"interface":"g0/0/0",
		"ip":"10.0.0.2",
		"mask":"24",
		"mac":"FA:CE:B0:00:00:0C",
		"state":"down",
	},{
		"interface":"g0/0/1",
		"ip":"",
		"mask":"",
		"mac":"00:00:00:00:00:01",# mac address for the other interface
		"state":"down",
	}]
	port = 1235

except:
	print("Can'not start the router!!!")
	sys.exit(2)

neigh_ip = "10.0.0.1" # ip of the router1
BUFFER = 1024
try:
	sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	sock.connect(("127.0.0.1",port))
except  ConnectionRefusedError:
	sys.exit("\nServer is not UP ,(First Run the Router1)!!!")
msg = "Hello , Router1"
msgSend = msg.encode("utf-8")
sock.send(msgSend)

print(f"Getting Reply...")

recvData = sock.recv(BUFFER)
print(recvData.decode('utf-8'))