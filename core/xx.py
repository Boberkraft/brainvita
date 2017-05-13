# from enum import IntEnum
#
# class Difficulty(IntEnum):
#     Normal, Hard, Hardcore = range(3)
#
# a = Difficulty.Hard
# print(a)
# print(a == 1)
# print(dir(a))
# print(a.name)
# print(xxx)

a = list(range(20))
print(id(a))
for _ in range(len(a)):
    del a[-1]
print(id(a))
a.append(123)