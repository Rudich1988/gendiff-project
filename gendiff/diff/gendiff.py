import argparse


def parser():
    parser = argparse.ArgumentParser(description=("Compares two configuration "
                                                  "files and shows "
                                                  "a difference."))
    parser.add_argument('file_1')
    parser.add_argument('file_2')
    parser.add_argument('-f', '--format', default='stylish',
                        help='output format (default: "stylish")')
    args = parser.parse_args()
    return (args.file_1, args.file_2, args.format)
