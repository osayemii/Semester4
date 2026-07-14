# Cpoy all contents from the students_list to a new file created as backup_students.txt
with open("students_list.txt", "r") as original:
    data = original.read()
    
with open("backup_student.txt", "w") as backup:
    backup.write(data)
    
# Using 'with' guarantees both files close automatically
print("Students copied successfully")
