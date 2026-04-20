#3.1 Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case.

fname = input('Enter file name: ')
fhand = open(fname)
for line in fhand:
    stripped_file = line.rstrip()
    lines = stripped_file.upper()
    print(lines)