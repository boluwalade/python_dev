import random

animal_list = list(range(1,10))

for i in range(10):
    n = [random.randint(1,20)]
    animal_list = animal_list + n
animal_list.append(1)
print(animal_list)

# for i in enumerate(animal_list):
#     print(i[1])