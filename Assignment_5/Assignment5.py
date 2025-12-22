"""Task 1: Create a Dictionary of Student Marks

Problem Statement: Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.
"""
students= {
    "Alice":85,
    "Bob":90,
    "Charlie":80,
    "Mary Joe":77
}
student_name = input("Enter student name: ").strip().title()
if student_name in students:
    print(f"{student_name}\'s marks: {students[student_name]}")
else:
    print("Student not found.")

"""Task 2: Demonstrate List Slicing 
Problem Statement: Write a Python program that:
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list
"""
list1=[]
for i in range(1,11):
    list1.append(i)
print("Original list: ",list1)
elements =list1[:5]
print("Extracted first five elements: ",elements)
print("Reversed extracted elements: ",elements[::-1])