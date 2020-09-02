#!/usr/bin/env python3

def extract_numbers(s):
    words = s.split()
    result = []

    for item in words:
        try:
            result.append(int(item))
            continue
        except ValueError:
            pass
        try:
            result.append(float(item))
            continue
        except ValueError:
            continue
       
    return result

def main():
    print(extract_numbers("abc 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()
