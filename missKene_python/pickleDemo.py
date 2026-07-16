import pickle

student = {
    "name": "Aisha",
    "age": 20,
    "department": "Data Science"
}

# Serialization / Pickling
with open("student.pk", "wb") as file:
    pickle.dump(student, file)
    
# Deserialization / Unpickling
with open("student.pk", "rb") as file:
    data = pickle.load(file)
    
print(data)