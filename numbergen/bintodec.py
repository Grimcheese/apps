#! python 3

import random

def GenerateDecimal(min, max):
	return(random.randint(min, max))
	

def GenerateBinary(min, max):
	temp = GenerateDecimal(min, max)
	return(bin(temp))
	
def main():
	print("This program will randomly generate numbers between 0 and 511")
	random.seed()

	option = int(input("Binary or Decimal? (1/0): "))
	n = int(input("Number of numbers to generate: "))
	
	min = 0
	max = 511
	
	numList = []
	convertList = []
	for i in range(0, n):
		if option == 1:
			num = GenerateBinary(min, max)
			convertList.append(int(num, 2))
		elif option == 0:
			num = GenerateDecimal(min, max)
			convertList.append(bin(num))
			
		print(num)
		numList.append(num)
		wait = input("PRESS ENTER TO CONTINUE")
			
	for i in range(0, n):
		print(numList[i])
		print(convertList[i])
		
main()