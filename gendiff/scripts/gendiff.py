import argparse

from gendiff import generate_diff


def main():
    parser = argparse.ArgumentParser(prog='gendiff', usage='usage: gendiff [-h] first_file second_file', 
                                 description='Compares two configuration files and shows a difference.')
    parser.add_argument('file_1')
    parser.add_argument('file_2')
    args = parser.parse_args()
    print(generate_diff(args.file_1, args.file_2))
#parser.add_argument('-f', '--format', help='set format of output')
    #parser.print_help()





if __name__ == '__main__':
    main()
