#!/usr/bin/env python3

def main():

    s = [[i,j] for i in range(1,7) 
            for j in range (1,7) 
            if i + j == 5]
    #print(f"({tuple(s[0])},{},{tuple(s[1])})")
    #print(tuple(*s),sep="\n")
    print(tuple(s[0]),tuple(s[1]),tuple(s[2]),tuple(s[3]),sep="\n")


if __name__ == "__main__":
    main()
#  for i in range(1,6):
  #      for j in range(1,6):