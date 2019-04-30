"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE

# f = open('foo.txt', 'r')
# print(f.read())
# f.close()

with open('foo.txt') as f:
    print(f.read())

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

# b = open('bar.txt', 'w')
# b.write("The etymology of 'foo' is obscure.\n")
# b.write("It's used in connection with 'bar'.\n")
# b.write("Not to be confused with the military slang 'FUBAR'.\n")
# b.close()

with open('bar.txt', 'w') as b:
    b.write("The etymology of 'foo' is obscure.\n")
    b.write("It's used in connection with 'bar'.\n")
    b.write("Not to be confused with the military slang 'FUBAR'.\n")
