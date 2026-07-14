# Read and display all contents of students_list.txt
file = open("students_list.txt", "r")
contents = file.read()
print(contents)
file.close()