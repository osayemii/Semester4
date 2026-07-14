# Truncate resize a file to a specified number of bytes
file = open("pythonLab.txt", "a")
file.truncate(20)
file.close()

# Open and read the file after the truncate
file = open("pythonLab.txt", "r")
print(file.read())

# Returns the current position of the pointer
print(file.tell())

# Seek move the pointer to a specific position
file = open("students_list.txt", "r")

print(file.seek(40))
print(file.read())

file.close()