# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

num = int(input('Enter your number, please: '))

lst = []
i = 2
while i <= num:
    if num % i == 0:
        lst.append(i)
        num //= i
    else:
        i += 1
print(f"The prime factors of {num} are: {lst}")