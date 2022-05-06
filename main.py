'''Example code for reading and writing files in Python
The files must be in the directory where your main.py file resides or you have
to enter the full path to the directory'''

'''The function open will open the given file in a specified mode ("r" for read, "w" for write
 and "a" for append) The simplest way is shown below. This is not recommended because you have
 to close your files manually!'''
f = open('text.txt', 'r')
text = f.readlines()
f.close()  # always close file after using!
print(text)

'''This is the recommended method:
Using the with keyword the file will be closed automatically after the execution
of the code block, keep in mind that every line will have a line termination at the end
that often must be taken into account when working with text from files

More information about line and file endings:
https://realpython.com/read-write-files-python/
https://docs.python.org/3/tutorial/inputoutput.html
'''
print("------Reading all lines and line terminations at once")
with open('text.txt', 'r') as reader:
    # returning all lines as list
    contents = reader.readlines()
print(contents)

print("------Reading file line by line")
with open('text.txt', 'r') as reader:
    # reading the contents line by line
    for line in reader:
        print(line, end="")
    print("")

print("------Appending to a file")
with open('text.txt', 'a') as writer:
    writer.write("Mona")

'''
Writing to a file will overwrite the content!
with open('text.txt', 'w') as writer:
    writer.write("Hello")
    

You can create new files of ever supported type by your OS:'''

print("------Making a new file")
with open('second_text.txt', 'w') as writer:
    writer.write("This is a new file\n")
    for line in contents:
        writer.write(line)


'''the reader object provides useful formatting functions
the code below reads a file where the names are written in a line and seprated by a whitespace.
the rsplit() function gets the names separated by the whitespace. You can pass other seperators to
the rsplit() function too like a e.g.: comma or underscore. Lookup other useful funtions'''

print("------Separating words by whitespace")
with open('names_inline.txt', 'r') as reader:
    contents = reader.readlines()
    print(contents[0])
    for line in contents:
        contents = line.rsplit()
    print(contents[0])
