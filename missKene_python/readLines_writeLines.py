# Readlines accept a parameter of byte to return
file = open("profile.txt", "r")

print(file.readlines(100))


# writeLines allow to write several strings to a file
file = open("pythonLab.txt", "a")
file.writelines(["\n1.File Handling", "\n2.Exception Handling", "\n3.Regular Expression"])

file = open("pythonLab.txt", "r")
print(file.read())


file.close()