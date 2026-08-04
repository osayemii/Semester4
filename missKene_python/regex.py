import re

# '.' matches any 
text = "cat cut cot cart"
print(re.findall(r"c.t", text))


# '\d' matches only digit singularly ('2', '0') AND '\d+' matches only digits wholely ('20')
text = "Python was realeased in 1991."
numbers = re.findall(r"\d", text)
print(numbers)

text2 = "Python was realeased in February 20 1991."
numbers = re.findall(r"\d+", text2)
print(numbers)


text = "CS101 Python2025"
print(re.findall(r"[0-9]", text))


text = "Python was released in 1991. java was released in 1995. PHP was created in 1994."
years = re.findall(r"\d+", text)
print("Years found:")
print(years)


text = "Java, C++, Python, and PHP are programming language."
result = re.search(r"Python", text)

if result:
    print("Word found:", result.group())
    print("Starts at:", result.start())
    print("Ends at:", result.end())
else:
    print("Word not found.")
    
# -----------------------------------------
    
emails = [
    "jo2hn@gmailcom",
    "mary@yahoo.com",
    "student.com"
]

pattern = r"^\w+@\w+\.\w+$"

for email in emails:
    if re.search(pattern, email):
        print(email, "Valid")
    else:
        print(email, "Invalid")
        
        
# ---------------------------------

str = "Java was first released in 1995" 

result = re.match(r"\w{4}", str)
print("Match object: ", result)

if result != None:
    print("Match word: ", result.group())
    
    
# ------------------------------------------

s = "Computer Languages"

vowelMatch = re.finditer(r"[aeiou]", s)

for vowel in vowelMatch:
    print(vowel)


# -------------------------------------------
strl2 = "debby@mail.co"
strl1 = "PHP is an open-source programming language created in 1990."

listOFWords = re.split(r"\s+", strl1)
listOFWords = re.split(r"@\w+.", strl2)

print(listOFWords)


# ---------------------------------------------
import re
str1 = "Java was first released in 1995.\n PHP is an open-source programming language created in 1990."
string_pattern = r"\d{4}"
regex_pattern = re.compile(string_pattern)
print(type(regex_pattern))
result = regex_pattern.findall(str1)
result = re.findall(r'\d{4}', str1)
print(result)