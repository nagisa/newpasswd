#!/usr/bin/env python
__version__ = "0.1"

import os
import argparse

# Python 2 compatibility
try:
    chr(256)
except ValueError:
    chr = unichr

# Arguments' parser
parser = argparse.ArgumentParser(description='Generate a brand new password.')
parser.add_argument('-l', '--length', metavar='LEN', type=int, default=32,
                    help='length of your password')
parser.add_argument('-n', '--count', metavar='N', type=int, default=1,
                    help='ammount of passwords to generate')
parser.add_argument('-r', '--random', action='store_true',
                    help='use /dev/random as source of randomity')
parser.add_argument('--extended', action='store_true',
                    help='use more latin characters when generating a '
                         'password')
parser.add_argument('--greek', action='store_true',
                    help='use greek characters when generating a password')
parser.add_argument('--cyrillic', action='store_true',
                    help='use cyrillic characters when generating a password')


def random_byte():
    if args.random and dev_random:
            return dev_random.read(1)
    else:
        return os.urandom(1)


def random_chr():
    return letters[ord(random_byte()) % len(letters)]


if __name__ == "__main__":
    args = parser.parse_args()

    letters = [chr(i) for i in range(0x21, 0x7F)]

    if args.extended:
        # Add Latin-1 Supplement, Extended-A and Extended-B to list of characters.
        letters.extend([chr(i) for i in range(0xA1, 0xAD)])
        letters.extend([chr(i) for i in range(0xAE, 0x250)])
        # Add Latin Extended Additional
        letters.extend([chr(i) for i in range(0x1E00, 0x1F00)])

    if args.greek:
        # Add Greek and Coptic to list of characters.
        # This table has some non-printable characters in the middle.
        excl = [0x378, 0x379, 0x37f, 0x380, 0x381, 0x382, 0x383, 0x38B, 0x38D,
                0x3A2]
        letters.extend([chr(i) for i in range(0x374, 0x400) if i not in excl])
        # Add Greek Extended Additional
        # This table has some non-printable characters in the middle.
        excl = [0x1F16, 0x1F17, 0x1F1E, 0x1F1F, 0x1F46, 0x1F47, 0x1F4E,
                0x1F4F, 0x1F58, 0x1F5A, 0x1F5C, 0x1F5E, 0x1F7E, 0x1F7F,
                0x1FB5, 0x1FC5, 0x1FD4, 0x1FD5, 0x1FDC, 0x1FF0, 0x1FF1,
                0x1FF5, 0x1FFF]
        letters.extend([chr(i) for i in range(0x1F00, 0x2000) if i not in excl])

    if args.cyrillic:
        # Add Cyrillic to list of characters...
        letters.extend([chr(i) for i in range(0x400, 0x528)])


    if args.random:
        # Try opening /dev/random
        try:
            dev_random = open('/dev/random', 'rb')
        except IOError:
            dev_random = None

    # Generate required ammount of passwords.
    for _ in range(args.count):
        print("".join(random_chr() for _ in range(args.length)))