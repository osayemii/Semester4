import pickle

student = {
    "name": "Aisha",
    "age": 20,
    "department": "Data Science"
}

# Serialization
with open("student.pk1", "wb") as file:
    pickle.dump(student, file)
    
# Deserialization
with open("student.pk1", "rb") as file:
    data = pickle.load(file)
    
print(data)