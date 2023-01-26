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

# set contains only unique values
unique_data = list(Counter(data_average).keys())

unique_count = list(Counter(data_average).values())

print(unique_data)

print(unique_count)