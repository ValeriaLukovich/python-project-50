#!/usr/bin/python3


import argparse
from gendiff.generate_diff import generate_diff


parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
parser.add_argument('first_file', help='what about first file')
parser.add_argument('second_file', help='what about second file')
parser.add_argument("-f", "--format", help="set format of output")
args = parser.parse_args()
   
   
def main():
    print(generate_diff(args.first_file, args.second_file))
    
    
if __name__ == '__main__':
    main()    
   

  

    

