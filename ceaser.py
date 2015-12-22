import sys 

def encrypt(k):
	plaintext = raw_input('Enter plain text message: ')
	cipher = ''

	for each in plaintext:
		c = (ord(each)+k) % 126
		
		if c < 32: 
			c+=31
			
		cipher += chr(c)
		
	print 'Your encrypted message is: ' + cipher

def decrypt(k):
	cipher = raw_input('Enter encrypted message: ')
	plaintext = ''
	
	for each in cipher:
		p = (ord(each)-k) % 126
	
		if p < 32:
			p+=95
						
		plaintext += chr(p)
		
	print 'Your plain text message is: ' + plaintext

def main():
	choice = raw_input("For Encript 'e' \nFor Decript 'd': ")

	if (choice != 'e') & (choice != 'd'):
		sys.exit('your choice should be e or d')

	key = raw_input("Enter the key: ")
	try:
   		val = int(key)
	except ValueError:
		sys.exit('That s not an int! key should be int')
   		

	if choice == 'e':
		encrypt(int (key))
	elif choice == 'd':	
		decrypt(int(key))

if __name__ == "__main__":
	main()
