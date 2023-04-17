#!/usr/bin/env python3
import sys


def main():
    # get file to decode from args
    if len(sys.argv) < 2:
        print('Usage: python3 unlock-wg.py <file to decode>')
        sys.exit(1)

    decode_filename = sys.argv[1]

    # open file to decode in binary mode
    with open(decode_filename, 'rb') as input_file:
        # read file to decode
        in_header_mode = True
        output_filename = ''

        while in_header_mode:
            data = input_file.readline()

            if data.startswith(b'filename: '):
                output_filename = data[10:].decode('utf-8').strip()

            if data == b'----\n':
                in_header_mode = False

            if data == b'':
                print('Premature end of file')
                sys.exit(1)

        print(f'Decoding {decode_filename} to {output_filename}')
        with open(output_filename, 'wb') as output_file:
            data = input_file.read()

            for byte in data:
                output_file.write(bytes([byte ^ 42]))


if __name__ == '__main__':
    main()


