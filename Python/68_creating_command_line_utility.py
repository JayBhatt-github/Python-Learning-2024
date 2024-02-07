# Arg Parse in Python

import argparse  

parser = argparse.ArgumentParser()  

# By default, it treats input number as string  
parser.add_argument("--num", type=int, help="Enter number to get square of it.")  
args = parser.parse_args()  
print(args.num**2)  # No need to convert the string to an integer before squaring

# To test this program, you can run it from the command line with the --num argument
# For example, if you want to find the square of 5, you can run the command:
# python 68_creating_command_line_utility.py --num 5
