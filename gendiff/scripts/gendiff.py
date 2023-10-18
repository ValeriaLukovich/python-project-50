#!/usr/bin/python3


import argparse
from gendiff.diff import generate_diff
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
        print(plain(generate_diff(args.first_file, args.second_file)))
    elif args.format == 'json':
        print(json_f(generate_diff(args.first_file, args.second_file)))
    else:
        print(stylish(generate_diff(args.first_file, args.second_file)))


if __name__ == '__main__':
    main()
