"""
Task 1: Read a File and Handle Errors
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.
"""
filename = "sample.txt"
try:
    f1 = open(filename, "rt")
    content = f1.readlines()
    f1.close()
    print("Reading file content:")
    i = 1
    for line in content:
        print(f"Line {i}: {line.strip()}")
        i += 1
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")


"""
Task 2: Write and Append Data to a File
Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.
"""
data = input("Enter text to write in the file: ")
with open("output.txt", "w") as file:
    file.write(data+"\n")
    print("Data successfully inserted to output.txt")
data1= input("Enter additional text to append: ")
with open("output.txt", "a") as file:
    file.write(data1+"\n")
    print("Data successfully appended")
file.close()
print("File content of output.txt")
with open("output.txt", "r") as file:
    content = file.read()
    print(content)