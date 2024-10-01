# First ensure file exists via os
file = open("example1.txt", "r")
print("File opened in read mode.")
file.close()

# file = open("example2.txt", "w")
# print("File opened in write mode.")
# file.close()

# file = open("example3.txt", "a")
# print("File opened in append mode.")
# file.close()

# file = open("example1.txt", "r")
# content = file.read()
# print("File content:\n", content)
# file.close()

# file = open("example1.txt", "r")
# for line in file:
# print("Line:", line.strip())
# file.close()

# file = open("example1.txt", "r")
# content = file.read(10) # Read the first 10 characters
# print("First 10 characters:", content)
# file.close()

# file = open("example2.txt", "w")
# file.write("Hello, Python!\n")

# file.write("Writing to a file.\n")
# file.close()

# file = open("example3.txt", "a")
# file.write("Appending new data.\n")
# file.close()

# file = open("example2.txt", "w")
# file.write("This will overwrite the previous content.\n")
# file.close()

# file = open("example1.txt", "r")
# content = file.read()
# file.close()
# print("File closed after reading.")

# file = open("example2.txt", "w")
# file.write("Closing the file after writing.\n")
# file.close()
# print("File closed after writing.")

# with open("example1.txt", "r") as file:
# content = file.read()
# print("File automatically closed after exiting the block.")

# try:
# file = open("nonexistent.txt", "r")
# except FileNotFoundError:
# print("The file does not exist.")

# try:
# file = open("/root/protected.txt", "r")
# except PermissionError:
# print("You do not have permission to access this file.")

# try:
# file = open("example1.txt", "r")
# content = file.read()
# file.close()
# except Exception as e:
# print(f"An error occurred: {e}")

