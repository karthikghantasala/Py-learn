#!/bin/python

"""
Write a script that prompts the user for:
A file_name where it should write the content.
The content that should go in the file. The script should keep accepting lines of text until the user enters an empty line.
After the user enters an empty line, write all of the lines to the file and end the script.
"""
file_name = raw_input("Please type in the name of the file to be created.... \n")
print "Enter/Paste your content. Ctrl-D or Ctrl-Z ( windows ) to save it."

contents = ''
while True:
    try:
        line = str(raw_input(""))
        if line == '':
            break
    except EOFError:
        break
    contents = contents + '\n' + line

print contents
heros1_file = open(file_name, 'w')
heros1_file.write(contents)
heros1_file.close()

####linux academy solution


def get_file_name(reprompt=False):
    if reprompt:
        print("Please enter a file name.")

    file_name = raw_input("Destination file name: ").strip()
    return file_name or get_file_name(True)

file_name = get_file_name()

print("Please enter your content. Entering an empty line will write the content to %s:\n" % file_name)

with open(file_name, 'w') as f:
    eof = False
    lines = []

    while not eof:
        line = raw_input()
        if line.strip():
            lines.append("%s\n" % line)
        else:
            eof = True

    f.writelines(lines)
    print("Lines written to %s" % file_name)