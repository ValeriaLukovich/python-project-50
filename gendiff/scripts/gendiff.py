#!/usr/bin/python3


import argparse
from gendiff.diff import generate_diff


string = 'Compares two configuration files and shows a difference.'
parser = argparse.ArgumentParser(description=string)
parser.add_argument('first_file', help='what about first file')
parser.add_argument('second_file', help='what about second file')
parser.add_argument("-f", "--format", help="output format, default: 'stylish'")
args = parser.parse_args()


def main():
    if args.format == 'plain':
        print(generate_diff(args.first_file, args.second_file, form="plain"))
    elif args.format == 'json':
        print(generate_diff(args.first_file, args.second_file, form="json"))
    else:
        print(generate_diff(args.first_file, args.second_file, form="stylish"))


if __name__ == '__main__':
    main()
