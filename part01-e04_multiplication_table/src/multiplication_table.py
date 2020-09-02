#!/usr/bin/env python3


def main():
    for i in range(10):
        for j in range(10):
            print(f"{(j+1)*(i+1):<4d}", end="")
        print("")


if __name__ == "__main__":
    main()
