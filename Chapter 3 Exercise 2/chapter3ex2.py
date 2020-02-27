import disassembler
import sys
'''
Author: Simon Parris
'''
def main():
	num = int(input("Enter a number: "))
	numlist = []
	
	try:
		num = int(num)
	except ValueError:
		print("Value is not an integer!")
	else:
		for i in range(num+1):
			if i % 2 == 0: 
				numlist.append(i)
		print(numlist)
			
	

if len(sys.argv) == 1:
	main()
else:
	disassembler.disassemble(main)