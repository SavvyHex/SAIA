#!/usr/bin/python3

import wikipedia

def main():
    print(wikipedia.summary(input("Enter something to search for\n")))

if __name__ == "__main__":
    main()