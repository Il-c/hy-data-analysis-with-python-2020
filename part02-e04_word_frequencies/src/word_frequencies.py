#!/usr/bin/env python3

def word_frequencies(filename):

    d ={}
    with open(filename, "r") as f:
        for line in f:
            lista = line.split()
            
            for word in lista:
                word = word.strip("""!"#$%&'()*,-./:;?@[]_""")
                if d.get(word):
                    d[word]=d[word]+1
                else:
                    d[word]=1
    return d

def main():
    for i, j in word_frequencies("alice.txt").items():
        print(f"{i}\t{j}")

if __name__ == "__main__":
    main()
