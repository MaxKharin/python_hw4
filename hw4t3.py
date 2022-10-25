# Задайте последовательность чисел.
# Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.


import random
rndm_lst = []
for i in range(0,10):
    n = random.randint(1,9)
    rndm_lst.append(n)
print(rndm_lst)


def get_unique_numbers(numbers):
    list_of_unique_numbers = []
    unique_numbers = set(numbers)

    for number in unique_numbers:
        list_of_unique_numbers.append(number)

    return list_of_unique_numbers


print(get_unique_numbers(rndm_lst))
