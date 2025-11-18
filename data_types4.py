import math
#Data_types.py unit 3
# Strings data type

# literal assignment
import math
first = "ibukun"
last = "show" 

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

#constructor function
# pizza = str("pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# concatenation
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

# casting a number to a string
decade =str(1980)
print(type(decade))
print(decade)

statement = "i love rock music from the " + decade + "s."
print(statement)

# multiple lines
multiline ='''
hey, how are you?                 

i was just thinking about you.    
                            all good?

'''
print(multiline)

# escaping special characters
sentence = 'i\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
print(sentence)

# string methods
print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("good", "ok"))
print(multiline)

print(len(multiline))
multiline += "                                                              "
multiline = "                                           " + multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

print("")

#build a menu 
title = "menu".upper()
print(title.center(20, "="))
print("coffee".ljust(16, ".")+ "$1".rjust(4))
print("muffin".ljust(16, ".")+ "$2".rjust(4))
print("cheesecake".ljust(16, ".")+ "$5".rjust(4))

print("")

#string index values
print(first[1])
print(first[-1])
print(first[1:-1])
print(first[1:])

# some methods return boolean data
print(first.startswith("i"))
print(first.endswith("j"))

# boolean data type

my_value =True
X = bool(False)
print(type(X))
print(isinstance(my_value, bool))

#numeric data types

#integer types
price= 100
best_price= int(80)
print(type(price))
print(isinstance(best_price, int))

# float types
gpa= 3.28
y= float(1.14)
print(type(gpa))

# complex types
comp_value= 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# built-in functions for numbers

print(abs(gpa))
print(abs(gpa * -1))
print(round(gpa))
print(round(gpa, 1))



print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

# casting a string to a number
zipcode = "10001"
zip_value = int(zipcode)
print(type(zipcode))

# error if you attempt to cast incorrect data