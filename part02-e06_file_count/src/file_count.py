#!/usr/bin/env python3

import sys

def file_count(filename):
    file_lines = 0
    words = 0
    chars = 0
    with open(filename, "r") as f:
        for line in f.readlines():
            chars = chars + len(line)
            words = words + len(line.split())
            file_lines += 1

    return (file_lines, words, chars)

def main():
    for file in sys.argv[1:]:
        lines, words, chars = file_count(file)
        print(f"{lines}\t{words}\t{chars}\t{file}")

if __name__ == "__main__":
    main()
