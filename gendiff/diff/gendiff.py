import argparse

from gendiff import generate_diff


USAGE = 'usage: gendiff [options] <filepath1> <filepath2>'
DESCRIPTION = 'Compares two configuration files and shows a difference.'


def parser():
    parser = argparse.ArgumentParser(DESCRIPTION, USAGE)
    parser.add_argument('file_1')
    parser.add_argument('file_2')
    parser.add_argument('-f', '--format', default='stylish',
                        help='output format (default: "stylish")')
    args = parser.parse_args()
    return generate_diff(args.file_1, args.file_2, args.format)
