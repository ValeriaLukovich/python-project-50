#!/usr/bin/python3


import argparse
from gendiff.generate_diff import generate_diff
from gendiff.function_package.stylish import stylish
from gendiff.function_package.plain import plain
from gendiff.function_package.json import json_f


string = 'Compares two configuration files and shows a difference.'
parser = argparse.ArgumentParser(description=string)
parser.add_argument('first_file', help='what about first file')
parser.add_argument('second_file', help='what about second file')
parser.add_argument("-f", "--format", help="output format, default: 'stylish'")
args = parser.parse_args()


def main():
    if args.format == 'plain':
        print(generate_diff(args.first_file, args.second_file, format=plain))
    elif args.format == 'json':
        print(generate_diff(args.first_file, args.second_file, format=json_f))
    else:
        print(generate_diff(args.first_file, args.second_file, format=stylish))


if __name__ == '__main__':
    main()
