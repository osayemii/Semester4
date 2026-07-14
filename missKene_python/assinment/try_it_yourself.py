from random import shuffle

# Number 1
print("\nNumber 1")
list1 = [5, 8, -3, 6, -1, -5, 9, 11, -19]
positive = lambda num : num>0
negative = lambda num : num<0

print(f"Positive list: {sorted(filter(positive, list1))}")
print(f"Negative list: {sorted(filter(negative, list1))}")


# Number 2
print("\nNumber 2")
num2_dict = [
    {
        'flower': 'Rose',
        'color': 'Red'
    },
    {
        'flower': 'Lily',
        'color': 'White'
    },
    {
        'flower': 'Rose',
        'color': 'Red'
    },
    {
        'flower': 'Daisy',
        'color': 'Blue'
    }
]

colors = lambda color : color['color']

print(f"Sorted by Colors: {sorted(num2_dict, key=colors)}")


# Number 3
print("\nNumber 3")

num_list1 = [5, 7.8, 9, 11, 10.5]
num_list2 = [3, 8, 4.5, 7, 11]

multiply = lambda x,y : x*y

print(f"{num_list1} multiplied by {num_list2} = {list(map(multiply, num_list1, num_list2))}")


# Number 4
print("\nNumber 4")

occ_list = [1, 2, 4, 2, 6, 1, 4, 7, 2, 8, 3, 9, 1, 3, 6, 2, 3, 2]
count_twos = lambda numList: sum(1 for x in numList if x == 2)
print(f"Total number of 2s: {count_twos(occ_list)}")


# Number 5
print("\nNumber 5")

num_list = [1, 3, 5, 9]
word_list = ['rose', 'lily', 'jasmine', 'daisy']

shuffle(num_list)
shuffle(word_list)

print(f"Shuffled numbers: {num_list}")
print(f"Shuffled words: {word_list}")