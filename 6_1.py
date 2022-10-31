# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N
N = input()
factorial = lambda x: 1 if x == 0 else x * factorial(x - 1)

print([factorial(i) for i in range(1,int(N)+1)])
