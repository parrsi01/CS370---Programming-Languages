#Author Simon Parris
'''
Complete exercise 35 in the text. First, write a Python program that computes a value like you are being asked to do in this assignment. For instance, 

print(5 * (6 + int(input("Please enter an number:"))))

After you disassemble this program, you will have the outline for the code that needs to be generated to complete this program. Then, you modify the code given in figure 5.26 to write code to a file instead of evaluating the expression. For instance, the 
'''
import sys
import disassembler
def main():
    value = 0
    value = int(input("Please Enter a number:"))
    print(value + value)

if len(sys.argv) == 1:
	main()
else:
	disassembler.disassemble(main)