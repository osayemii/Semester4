studentScores = {
    "Daniel": 90,
    "Prince": 89,
    "jemimmah": 70,
    "Tumi": 85,
    "Basir": 75
}

total_score = 0
for value in studentScores.values():
    total_score += value

average = total_score / len(studentScores)

file = open("student_score.txt", "w")

for key, value in studentScores.items():
    file.write(f"{key}: {value}\n")
    
file.write(f"\nAverage: {average}")
file.close()


file = open("student_score.txt", "r")
print(file.read())
file.close()