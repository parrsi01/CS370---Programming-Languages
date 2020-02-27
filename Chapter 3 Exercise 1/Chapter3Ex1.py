import disassembler
import sys
'''
Author: Simon Parris
'''
def main():
	print("Hello there!")
	print('Sample Code')

if len(sys.argv) == 1:
	main()
else:
	disassembler.disassemble(main)