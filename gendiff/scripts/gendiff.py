#!/usr/bin/python3


import argparse
parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
parser.add_argument('first_file', help='what about first file')
parser.add_argument('second_file', help='what about second file')

args = parser.parse_args()
print(args.first_file)
    
    

