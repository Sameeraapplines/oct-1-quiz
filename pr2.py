# password program
length = 0
lower = 0
upper = 0
digit = 0
special_character = 0
passwd = input("enter pwd\n")
if (len(passwd) >= 8):
	for i in passwd:
		if (i.islower()):
			lower+=1			
		if (i.isupper()):
			upper+=1			
		if (i.isdigit()):
			digit+=1			
		if(i=='@'or i=='$' or i=='_'):
			special_character+=1

if (len(passwd)>=8 and lower>=1 and upper>=1 and digit>=1 and special_character>=1):
	print("Valid Password")
elif (len(passwd)<8):
    print("Not a valid password. Password should have minimum 8 characters.")
elif (lower == 0):
    print("Not a valid password. Password should have atleast 1 lowercase character.")
elif (upper == 0):
    print("Not a valid password. Password should have atleast 1 uppercase character.")
elif (digit == 0):
    print("Not a valid password. Password should have atleast 1 number.")
elif (special_character == 0):
    print("Not a valid password. Password should have atleast 1 special character.")


