#Define Collatz function takes in an integer called num
def collatz(num):
	#If even, half by 2, if odd, time 3 + 1
	
	if num % 2 == 0: #Even
		num = num//2
	elif num % 2 == 1: #Odd
		num = 3 * num +1
	print(num)
	return num

#Ask for an integer from user
print('Enter number:', end = " ")

#Try the program
try:
	#User input stored as user_number converted to integer
	user_number = int(input())
	#While loop if the number is not 1, keep calling collatz()
	while user_number != 1:
		#Replace global variable with local variable from collatz
		user_number = collatz(user_number)
#Value Error exception
except ValueError:
		print('ERROR: Invalid Value!')
	