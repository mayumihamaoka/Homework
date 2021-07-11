#capitalize
print('Example capitalize')
name = str('MAYUmI').capitalize()
print(name)
print()

#casefold
print('Example casefold')
motivational = ('ALL study AND eFfort will pay off')
motivational_casefold = motivational.casefold()
print(motivational_casefold)
print()

#center
print('Example center')
header = str('Availability').center(50)
print(header)
print()

#count
print('Example count')
instructions = ('Include 3 liters of water and 2 liters of concentrate orange juice')
liters = instructions.count('liters')
print(liters)
print()

#endswith
print('Example endswith')
name = ('My name is Mayumi.')
sentence = name.endswith(".")
print(sentence)
print()

#find
print('Example find')
name = ('My name is Mayumi.')
sentence = name.find("is")
print(sentence)
print()

#format
print('Example format')
name = ('Disney')
sentence = ('My name is {}').format(name)
print(sentence)
print()

#index
print('Example index')
name = ('My name is Mayumi.')
sentence = name.index("name")
print(sentence)
print()

#isalnum
print('Example isalnum')
instructions = ('Include 3 liters of water and 2 liters of concentrate orange juice')
liters = instructions.isalnum()
print(liters)
print()

#isalpha
print('Example isalpha')
price = 'Price'.isalpha()
print(price)
print()

#isdigit
print('Example isdigit')
price = '50.60'
price_value = price.isdigit()
print(price_value)
print()

#islower
print('Example islower')
price = 'price is 50.60'.islower()
print(price)
print()

#isnumeric
print('Example isnumeric')
price = '5060²'
price_value = price.isnumeric()
print(price_value)
print()

#isspace
print('Example isspace')
name = ('  ')
sentence = name.isspace()
print(sentence)
print()

#istitle
print('Example istitle')
name = ('My Name Is Mayumi.')
sentence = name.istitle()
print(sentence)
print()

#isupper
print('Example isupper')
deadline = str('SUNDAY')
deadline_upper = deadline.isupper()
print(deadline_upper)
print()

#join
print('Example join')
classroom = ("Mary","Bella","Josh")
classroom_csv = ", ".join(classroom)
print(classroom_csv)
print()

#lower
print('Example lower')
name = str('MAYUmI').lower()
print(name)
print()

#lstrip
print('Example lstrip')
ingredients = '     3 liters of water'
instructions = ingredients.lstrip()
print("Include", instructions, "in the bowl.")
print()

#replace
print('Example replace')
ingredients = '3 liters of water'
instructions = ingredients.replace("water","orange juice")
print("Include", instructions, "in the bowl.")
print()

#rsplit
print('Example rsplit')
classroom = ("John; Mary; Bella; Josh")
classroom_list = classroom.rsplit(';')
print(classroom_list)
print()

#rstrip
print('Example rstrip')
ingredients = '3 liters of water,.,.,.,'
instructions = ingredients.rstrip(',.')
print("Include", instructions, "in the bowl.")
print()

#split
print('Example split')
classroom = ("Mary Bella Josh")
classroom_list = classroom.split()
print(classroom_list)
print()

#splitlines
print('Example splitlines')
instructions = ('Include 3 liters of water \n 2 liters of concentrate orange juice')
instructions_lines = instructions.splitlines()
print(instructions_lines)
print()

#startswith
print('Example startswith')
name = ('My Name Is Mayumi.')
sentence = name.startswith('Name')
print(sentence)
print()

#strip
print('Example strip')
ingredients = '     3 liters of water     '
instructions = ingredients.strip()
print("Include", instructions, "in the bowl.")
print()

#swapcase
print('Example swapcase')
name = str('My Name IS MAYumi').swapcase()
print(name)
print()

#title
print('Example title')
name = str('My Name IS MAYumi').title()
print(name)
print()

#upper
print('Example upper')
name = str('My Name IS MAYumi').upper()
print(name)
print()


