from collections import Counter
import random

number_of_dices = 3
number_of_throws = 10000

data_average = []

temp = []

for throw in range(number_of_throws):

    temp.clear()

    for dice in range(number_of_dices):
        temp.append(random.randint(1, 6))
    
    temp_average = sum(temp)/len(temp)

    data_average.append(temp_average)

data_average.sort()


# set contains only unique values
unique_data = list(Counter(data_average).keys())

unique_count = list(Counter(data_average).values())

num_of_elements = len(unique_count)

data = []

# merge lists into one
for i in range(num_of_elements):
    data.append([])
    data[i].append(unique_data[i])
    data[i].append(unique_count[i])

print(unique_data)

print(unique_count)

print(data)