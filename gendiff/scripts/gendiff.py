#!/usr/bin/python3


import argparse
parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
parser.add_argument('first_file', help='what about first file')
parser.add_argument('second_file', help='what about second file')
parser.add_argument("-f", "--format", help="set format of output")
args = parser.parse_args()
   
    

