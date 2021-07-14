import socket

domain = 'hackerone.com'
port  = 443

try:
	sock = socket.create_connection((domain,port))
	subdomain  = open('subs.txt').read().splitlines()
	for i in subdomain:
		url = f"{i}.{domain}"
		try:
			s = sock.connect_ex((url,port))
			print(url)
		except:
			pass

		
				
except socket.gaierror:
	print("Server not available!!!")
