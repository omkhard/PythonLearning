"""
	Class Table 
	------------
	0-127
	128-191
	192-223
"""
def binary(a,b,bin1,bin2):#decimal to binary again to decimal converting function
	return int(b[bin1:bin2],2)



print("""\n'This Python tool was intended to made for better Subneting Calculations'\n""")

Str = str(input("Choose your class [A , B or C ]:"))
num = int(input("No. of devices you want as hosts:"))

if Str == "A":
	num1 = 0 
	num2 = 0
	num3 = 0
	BIN = str(f"{num:024b}")# for class A IP there could be 24 mask in subnet (24 , 1's)
	#num1 = int(BIN[-8:len(BIN)],2) # performing the same technique using function 
	#num2 = int(BIN[-16:-8],2)
	#num3 = int(BIN[-24:-16],2) OR
	num1 = binary(num1,BIN,-8,len(BIN))
	num2 = binary(num2,BIN,-16,-8)
	num3 = binary(num3,BIN,-24,-16)
	#  in class A 2^24 hosts can rely so 
	if len(BIN) < 16:
		num3 = 0
		if len(BIN) < 8:
			num2 = 0 
			num3 = 0
	else:
		num3 = int(BIN[-32:-16],2)
	try:
		ip = int(input("Choose the ip from range [0-127]:"))
		if ip > 127:
			exit("IP is in other class")
	except ValueError:
		exit("No IP given!")
	print(f"Your network address is: {ip}.0.0.0")
	print(f"Your last host address is:/{ip}.{num3}.{num2}.{num1}")# calling the subnets mask values as last addressOfnetwork
