from collections import Counter
import random
import matplotlib.pyplot as plt

# settings
number_of_dices = 2
number_of_throws = 10000

# will contain dices throws' average values
data_average = []

temp = []

for throw in range(number_of_throws):

    temp.clear()

    for dice in range(number_of_dices):
        temp.append(random.randint(1, 6))
    
    temp_average = sum(temp)/len(temp)

    data_average.append(temp_average)

# average dice throws' unique values (e.g. 1, 1.3, 1.6 etc.)
unique_data = list(Counter(data_average).keys())

# count of every unique value
unique_count = list(Counter(data_average).values())

# ----- graph part -----
fig = plt.figure(figsize = (10, 5))

plt.bar(unique_data, unique_count, color='maroon', width=0.1)

plt.xlabel("Average dice throw value")
plt.title("Dice Normal Distribution")
plt.show()