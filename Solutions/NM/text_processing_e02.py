#!/usr/bin/env python3
'''
Contributor Name: NM
Resources Referred: *
'''
'''
From the following text, print only the lines that start with a word that has only uppercase characters:
hello - don't print me
HELLO - but I'm ok
Im a line that shouldn't be printed
BUT I'm a line that should
'''

#store the text in a variable
in_str ='''\
hello - don't print me
HELLO - but I'm ok
Im a line that shouldn't be printed
BUT I'm a line that should
'''

def main():
#break the text into lines, each line into words and verify the first word is upper and print the line if True
    for line in in_str.splitlines():
        if (line.split(" ")[0]).isupper():
            print (line)

if __name__ == "__main__":
    main()