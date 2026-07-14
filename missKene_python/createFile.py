# Create and write into a file
file = open("students_list.txt", "w")

file.write("Deborah\n")
file.write("Tumi\n")
file.write("Daniel\n")
file.write("Adams\n")
file.write("Prince\n")

file.close()

print("Students saved successfully.")