try:
    with open("result56.txt", "r") as file:
        print(file.read)
except FileNotFoundError:
    print("File not Found.")