# Fun with I/O

# when using hte open command, you need to not only provide the path
# (first argument), but also the mode in which you want to open the file
# (r = read, w = write)
jabber = open("sample.txt", 'r')

for line in jabber:
    # will only print the lines with the word 'jabberwock'
    if "jabberwock" in line.lower():
        print(line, end='')

# you must use this command when writing to a file, or the file may
# become corrupted
jabber.close()

print("=" * 40)

# with file: automatically closes the file once the object is no longer
# needed, so the close() command is not necessary
with open("sample.txt", 'r') as jabber:
    for line in jabber:
        if "JAB" in line.upper():
            print(line, end='')

print("=" * 40)

# readline() displays an entire line; the end='' does not print an empty
# space following the line
with open("sample.txt", 'r') as jabber:
    line = jabber.readline()
    while line:
        print(line, end='')
        line = jabber.readline()

print()
print("=" * 40)

# readlines() parses all lines of a .txt file, and converts them into a
# a list of strings
with open("sample.txt", 'r') as jabber:
    lines = jabber.readlines()
    print(lines)

# you can parse the created list, like any other
for line in lines:
    print(line, end='')

print()
print("=" * 40)

# Same as above, but using a slice to remove the \n
with open("sample.txt", 'r') as jabber:
    lines = jabber.readlines()
    print(lines)

for line in lines[::-1]:
    print(line, end='')

# you can have fun and completely change the direction of the text, with
# the read command and a similar loop to the one above
with open("sample.txt", 'r') as jabber:
    lines = jabber.read()

for line in lines[::-1]:
    print(line, end='')