import requests
import sys , re
import argparse
import socket



# function definition 
def Gather(*arguments):
	
	print(f"\033[32mStatus Code:{response.status_code}\033[37m")
	for i in response.headers:
		print(f"{i}:{response.headers[i]}")

	
	try:
		print(response.json())
	except:
		print(f"No JSON data extracted!!!")
		pass
	

# try block to ensure the requirements.py  
try:
	parser = argparse.ArgumentParser("***python3 practice.py <options>")
	parser.add_argument('-u','--url',help='tag used to gather from an URL')
	parser.add_argument('-p','--port',help='port number defualt(is 80)')
	parser.add_argument('-s',help='Use this for sub domain analysis',dest='sub',action='store_true')

except (ValueError):
	print(f"Requirements not installed properly!!!")
	sys.exit(1) 

args = parser.parse_args()

# Gather with http websites
if args.url and not args.sub:
	domain = sys.argv[sys.argv.index('-u')+1]
	
	if not args.port or sys.argv[sys.argv.index('-p')+1] == 80:
		site = "http://"
		url = f"{site}{domain}:{port}"
		response = requests.get(url) # Get request
		postreq = requests.post(url) # Post request
	elif args.port or sys.argv[sys.argv.index('-p')+1] == 443:
		port = 443
		site = "https://"
		url = f"{site}{domain}"
		response = requests.get(url)#Get request
	port = sys.argv[sys.argv.index('-p')+1]
	try:
		sock = socket.create_connection((domain,port),timeout=5)
	except :
		print("timeout!!!")
		sys.exit()
	Gather(domain,port,response)

if args.url and args.sub:
	domain = sys.argv[sys.argv.index('-u')+1]
	port = 443
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

