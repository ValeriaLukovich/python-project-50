from gendiff.diff import generate_diff
from gendiff.function_package.stylish import stylish
from gendiff.function_package.plain import plain
from gendiff.function_package.json import json_f


__all__ = (
    "generate_diff",
    "stylish",
    "plain",
    "json_f",
    )


def main():
    print(stylish(generate_diff(args.first_file, args.second_file)))


if __name__ == '__main__':
    main()  
