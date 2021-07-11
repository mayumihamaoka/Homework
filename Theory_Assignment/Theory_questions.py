# print('BANANA'.isupper())
# # True
# print('banana'.isupper())
# # False
# print('baNana'.isupper())
# # False
# print('  '.isupper())
# # False
#
# name = str(input("What's your name? ")).lower()
# print(name)
#
# name = str(input("What's your name? ")).capitalize()
# print(name)
#
# 'ab c\n\nde fg\rkl\r\n'.splitlines()

# print('1,2,3'.split(','))
#
# txt = ",,,,,rrttgg.....banana....rrr"
# x = txt.strip(",.grt")
# print(x)
#
# txt = "Hello UnIvERSE"
# x = txt.swapcase()
# print(x)

# tuple = (1, 7, 5, 4, 8, 5)
# x = tuple.count(5)
# print(x)
#
# # indextuple = (1, 7, 7, 5, 4, 6, 8)
# # x = indextuple.index(8)
# # print(x)
#
# fruits = ['orange', 'kiwi', 'apple', 'banana']
# # print(fruits.count('apple'))
# # print(fruits.index('banana',4))
# # fruits.reverse()
# # print(fruits)
# # fruits.append('grape')
# # print(fruits)
# # fruits.sort()
# # print(fruits)
# # fruits.pop()
# # # print(fruits)
# # fruits.clear()
# # print(fruits)
# berries = ['strawberry','blueberry','grape']
# # fruits.extend(berries)
# # print(fruits)
# #
# # berries.remove('strawberry')
# # print(berries)
#
# berries.insert(0,"cherry")
# print(berries)

# classroom = { }
# print(classroom.copy())
#
# fruitsp = ["apple", "banana", "cherry"]
# print(fruitsp.copy())

flowers_set = {'dandelion', 'rose', 'daisy'}
flowers_set.add('lilies')
# flowers_set.clear()
print(flowers_set)
print()

flowers_set.copy()
print(flowers_set)
print()

#flowers_set = {'dandelion', 'rose', 'daisy','lilies'}
flowers_set.remove('dandelion')
print(flowers_set)
print()

flower_set = {'lilies', 'rose', 'daisy'}
herbs_set = {'mint','rosemary','basil','rose'}
distinct = herbs_set.difference(flowers_set)
print(distinct)
print()

similar = herbs_set.intersection(flowers_set)
print(similar)
print()

plants_set = flowers_set.issubset(herbs_set)
print(plants_set)
print()

plants_set = flowers_set.issuperset(herbs_set)
print(plants_set)
print()

herbs_set.pop()
print(herbs_set)
print()

#symetric_difference
print('Example symetric_difference')
flower_set = {'lilies', 'rose', 'daisy'}
herbs_set = {'mint','rosemary','basil','rose'}
plants_set = flowers_set.symmetric_difference(herbs_set)
print(plants_set)
print()

#union
print('Example Union')
flower_set = {'lilies', 'rose', 'daisy'}
herbs_set = {'mint','rosemary','basil','rose'}
plants_set = flowers_set.union(herbs_set)
print(plants_set)
print()

#update
print('Example update')
flower_set = {'lilies', 'rose', 'daisy'}
herbs_set = {'mint','rosemary','basil','rose'}
flowers_set.update(herbs_set)
print(flowers_set)
print()