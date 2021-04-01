"""
	Class Table 
	0-127
	128-191
	192-223
"""
Str = str(input("Choose your class [A , B or C ]:"))
num = int(input("No. of devices you want as hosts:"))

if Str == "A":
	num1 = 0 
	num2 = 0
	num3 = 0
	BIN = str(f"{num:032b}")
	num1 = int(BIN[-8:len(BIN)],2)
	num2 = int(BIN[-16:-8],2)
	# num3 = int(BIN[-32:-16],2)
	# 2^24 hosts can rely 
	if len(BIN) < 16:
		num3 = 0
		if len(BIN) < 8:
			num2 = 0 
			num3 = 0
	else:
		num3 = int(BIN[-32:-16],2)
	ip = int(input("Choose the ip from range [0-127]:"))
	print(f"Your network address is: {ip}.0.0.0")
	print(f"Your last host  address is:/{ip}.{num3}.{num2}.{num1}")