fname = "C:\\Users\\mayum\\Documents\\Trainings\\NANODEGREE\\1.Python lessons 1-6\\Session 5 (21-06-21)\\5.3_example_one.txt"

count = 0

with open(fname, "r") as text:
    for animals in text:
        animals = animals.strip()
        print(animals)

letters = list(animals)
print(letters)

        if letters == upper()

        words = animals.split() # turn into a list of words
        print(words)

#
# S = "Apple"
# print(S[::-1])
#
#
# S = "ABDEFGHI"
# print(S[2:5])
# print(S[:5])
# print(S[6:])
# print(S[-2:])
# # print(S[::-1])
#
# list = ["cat","horse","elephant","dog"]
# longest_word = max(list, key=len)
# print(longest_word)
#
# print()
#
# a_list = ["a_string", "the_longest_string", "string"]
# longest_string = max(a_list, key=len)
# print(longest_string)

print("Please select operation - \n"
      "1. Add\n"
      "2.Subtract\n"
      "3.Multiply\n"
      "4.Divide\n"
      )

select=int(input("Select operations form 1,2,3,4:"))
number_1=int(input("Enter first number:"))
number_2=int(input("Enter first number:"))

if select == 1:
    print(number_1 + number_2)
elif select == 2:
    print(number_1 - number_2)
elif select == 3:
    print(number_1 * number_2)
elif select == 4:
    print(number_1 / number_2)
else:
    print("Please insert 1,2,3 or 4 as operations")

age = 48
discount = True if age >= 65 else False
print(discount)
