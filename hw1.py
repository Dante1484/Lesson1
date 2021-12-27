# 1

# age1 = input('age1: ')
# age2 = input('age2: ')
# a = int(age1)
# b = int(age2)
# print(a + b)
#
# phones = input('phones: ')
# print(phones)

# 2

# x = '0'
# n = 9
# time = int(input('sec: '))
# s = time % 60
# if s > 9:
#     s = s
# else: s = (x + str(s))
#
# m = (time // 60) % 60
# if m > 9:
#     m = m
# else: m = (x + str(m))
#
# h = time // 3600
# if h > 9:
#     h = h
# else: h = (x + str(h))
#
# print(h, ':', m, ':', s)

# 3

# n = input('n: ')
# print(int(n) + int(n + n) + int (n + n + n))

# 4

# n = int(input('Целое положительное число: '))
# n = 123454321
# while n > 0:
#     last = n % 10
#     n = n // 10
#     last1 = n % 10
#     last2 = max(last, last1)
# print(last2)

# 5

rev = int(input('revenue: '))
costs = int(input('costs: '))
if rev > costs:
    print('Прибыль')
    profit = ((rev - costs) / rev)
    print(profit)
    num = int(input('Людские ресурсы: '))
    ppu = (rev - costs) / num
    print(ppu)
else: print('Убыток')
