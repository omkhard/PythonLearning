import requests
import socket , sys , urllib.request
import time 

def networkSetting(NS,index):
	STR = ""
	for f in range(index+1):
		for j in NS[f]:
			STR = STR+NS[f][j]
			STR = STR+"\n"
	return STR


details = {
	"vendor":"cisco",  # details about the router 
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
		"ip":"10.0.0.1",
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
	port = 12345

except:
	print("Can'not start the router!!!")
	sys.exit(2)

INT = input("\nWhich interface you want to up!... (g0/0/0 or g0/0/1):")
if INT == "g0/0/0":
	i = 0
	network_setting[i]["state"] = "up"
	print(network_setting[0])
else:
	i =  1
	network_setting[i]["state"] = "up"
	print(network_setting[1])


neigh_ip = "10.0.0.2" # ip of router2
LOOPBACK = "127.0.0.1"
PORT = 1235
BUFFER = 1024
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(("127.0.0.1",PORT))
sock.listen()


while True:
	connect , address = sock.accept()
	recvdData = connect.recv(BUFFER)
	print(f"Neighboor  adjacencies Hello Packet:{recvdData.decode('utf-8')}")
	msg = "Hello , Router2".encode("utf-8")
	connect.send(msg)
	print(f"Connected...  to looopback 1 | address 127.0.0.1")
	DETAILS = str(input("Do you want to see the Router details (y/n):"))
	if DETAILS == "y" or DETAILS == "yes":
		print(f"\nDetails:\n{networkSetting(network_setting,i)}")

	else:
		break
	sock.close()
	break

