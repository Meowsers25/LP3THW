# import argv from sys module
from sys import argv

# 2 arguments given by user in command line
script, filename = argv

# opens ex15_sample.txt and stores it in the txt variable
txt = open(filename)

print(f"Here's your file {filename}")

# .read() tells Python to read the file and we print it out
print(txt.read())

print("Type the filename again:")

# stores our input in the file_again variable. In this case we are 
# inputting ex15_sample.txt again.
file_again = input("> ")

# Once again, we open the ex15_sample.txt and store it in a variable.
# This time the variable is called txt_again.
txt_again = open(file_again)

# And here we tell Python to read ex15_sample.txt and print it out.
print(txt_again.read())

# close the files
txt.close()
txt_again.close()

