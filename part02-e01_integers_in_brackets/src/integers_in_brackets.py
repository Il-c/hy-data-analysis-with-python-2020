#!/usr/bin/env python3
import re

def integers_in_brackets(s):
 
    raakalista = re.findall(r'\[[\s]*[+-]?\d+[\s]*\]',s)
    intlista = [item.strip("[]\s") for item in raakalista]

    return list(map(int,intlista))

def main():
    print(integers_in_brackets("afd [128+] [47 ] [a34]  [ +-43 ]tt [+12]xxx"))
    print(integers_in_brackets("afd [asd] [12 ] [a34]  [        -43 ]tt [+12]xxx"))
if __name__ == "__main__":
    main()
