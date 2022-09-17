# # how we read keyboard input
# keyboard_input = input("lets read your input?")
# input("This is what we read from our user keyboard ---", keyboard_input)
#
# username = input("enter your username: ")
# password = input("Enter your password: ")
# print("Hey %s, your password is %s" % (username, password))
#
#
#
# # execptions errors
#
# try:
#     print( 'x' / 2 )
#     f = open("file.txt" )
# except(TypeError, FileNotFoundError):
#     print( "An exception was raised" )
#
# print( 'Continued with rest of the program')


# import time
#
# x = 0
# def x_loop ():
#     global x
#     try:
#         while True:
#             time.sleep( 1 )
#             print(  'printing ...%d' % x  )
#             x+= 1
#
#
#     except KeyboardInterrupt:
#         print("nah")
#         x_loop()
#
# x_loop()

filename = input( 'what\'s the filename? ')
try:
    open( filename, 'r' )
    print( " file found ... reading it. ")
except FileNotFoundError:
    print( "File not found ... creating it")
    open( filename, 'w' )



    



import sys
print(sys.argv)

val = int(sys.argv[1])
for _ in range(int(sys.argv[2])):
    val += int(sys.argv[2])
    print("value is ", val)
    input("press ENTER to continue.\n")
print(val)




# tuplesin python
african_countries = ('nigeria', 'ghana', 'kanya','egypt',
                     'zimbabwe', 'eswatini', 'togo')
print(african_countries)
print(african_countries[0])
print(african_countries[1:4])
print(african_countries.index('ghana'))
print(african_countries.count('kenya'))
print(len(african_countries))
print(min(african_countries))

print(max(african_countries))

# set
countries_in_africa = "ghana"
human ={"name":"lola grey", "gender": "f","age":19,"age": 37, 7: "numbers of days in the week", countries_in_africa: "countries in africa", True: "has some" }

print(human)
print(human['name'])
print(human[7])
print(human[True])
print(human[african_countries])
print(human.keys())
print(human.values())
print(human.items())
print(human.get('name'))
print(human.popitem())
print(human.fromkeys('name'))
print(dict().fromkeys(['name','age'],True))
dictionary = {
    "laptop": "a computer that sits on the lap",
    "desktop": "a computer that sits on the desk",
    "palmtop": "a computer that stays on the palm"
}

even_number_in_the_range_of_1_300 = [i for i in range(1, 300) if i % 2 == 0]
print(even_number_in_the_range_of_1_300)

set










your_name = "lolo"
age = 16
string = "your name is %s, and your age is %s " \
        %(your_name.title(),str(age))

print(string)

# names = ['eli', 'presh' ,'tola', 'james' , 'dami']
# print(names)
#
# years = ('12', '13', '14','15', '16')
# print(years)
# conversion = list(years)
# print(conversion)
#
#
# # datatypes
#
# # list
# names = ['eli', 'presh' ,'tola', 'james' , 'dami']
# # tuple
# years = ('12', '13', '14','15', '16')
# # numbers
# n = 18
# # sets
# s = {"apple", "bannana" ,"cherry"}
# # dictionary
# print(names,years,n,s)
#
#
# converts = list(range(30))
# print(converts)
#
#
# cars = [ 'lambo', 'ferrari', 'bugatti','benz']
# print(cars)
# cars[2] = 'toyota'
# print(cars)
# del cars[3]
# print(cars)
# # types of basic list operators
# # *,+,in,not in,
# numbers = [1,2,3] + [4,5,6]
# print(numbers)
# numbers = numbers * 3
# print(numbers)
#
# days = [[1,2,3], [4,5,6], [7,8,9]]
# print(days)
# print(days[2][1])
# # list
#
# text = ["i go up"]
# numbs = []
# # print(text.split())
# # print(days.count(4))
# # print(text.capitalize())
# text.append("now")
# print(text)
#
#
# items = [ 'items 1' ,'items 2']
# items.extend('items3')
# print(items)

nums = [1,3,4,8,8,9,6,5]
# nums.insert(2,5)
# print(nums)
# # nums.clear()
# # print(nums)
# nums.pop(1)
# print(nums)
# nums.pop(0)
# print(nums)

# nums.remove(1)
# print(nums)

# print(nums.index(4))

fruits = [ "mango", "grape", " guava ", "melon"]
print(fruits.index("grape"))
fruits.reverse()
print(fruits)

digits = [2,1,4,3,7,5,9,7,0]
digits.sort()
print(digits)
digits.reverse()
print(digits)




# import math
#
# x = 5
# y = 2
#
# print(math.pow(x,y))
# print(math.sqrt(4))
# print(math.sin(45))
# print(math.tan(45))
# print(math.cos(45))
# print(math.floor(4.8))
# print(math.ceil(4.8))
# print(math.radians(60))
# print(math.factorial(4))
# print(math.log(100,10))
#

from random import randint, randrange, shuffle, choice, choices, random
# for _ in range(10):
#     print(randint(2,10))
#
# print(randrange(10, 30, 5))
#
numbers = [1,2,3,4,5,6,7,8,9,10]
# print(numbers, "before shuffling")
# shuffle(numbers)
# print(numbers, 'after submiting')

# for _ in range(5):
#     print(choice(numbers))
# print(choices(numbers, k=3))
print(random())




# strings
import functions


numbers = "numbers are meant to be used"
# indexing

print(numbers[-1])
# slicing
print(numbers[-3:-1])
print(numbers[-1])
print(numbers[:])
print(numbers[1:])
print(len(numbers))

# updating strings
numbers = "figures" + numbers[7: ]
print(numbers)

# statement
statement = "he said , \"i won\'t plus i cant\' said sule"
print(statement)
statement = "he said , \"i won\'t plus i cant\' said sule"

comment =  "x\t there and there:\ngood work!"

comment = r"x\t there and there:\ngood work!"
print(comment)





# # # # # x = 15
# # # # # y = 12
# # # # #
# # # # # if y > x:
# # # # #     print("15 is greater than 12")
# # # # # else:
# # # # #     print("15 is not greater than 12")
# # # # #
# # # # #
# # # # # fruits = ['cashew','mango', 'apple', 'grape', 'date', 'orange', 'cherry']
# # # # # for fruit in fruits:
# # # # #     if fruit == 'cashew':
# # # # #         print("ill pass on cashew")
# # # # #     elif fruit == 'apple':
# # # # #         print('yeah,its apple')
# # # # #     elif fruit == 'grape':
# # # # #         print("yes i love grapes")
# # # # #     elif fruit == 'date':
# # # # #         print("no i don't give a fuck about date")
# # # # #     elif fruit == 'orange':
# # # # #         print("sometimes i take oranges" )
# # # # #     elif fruit == 'cherry':
# # # # #         print("i love cherries")
# # # # #     else:
# # # # #         print('not my best friuts')
# # # #
# # # # student = {
# # # #     "name": "michael",
# # # #     "gender": "male",
# # # #     "is_senior": True,
# # # #     "uniform": None,
# # # #     "skirt_dot_write": True
# # # #
# # # # }
# # # # if student['gender'] == 'male':
# # # #     if student['is_senior']:
# # # #         student['uniform'] = 'trouser'
# # # #
# # # #     else:
# # # #         student["uniform"] = 'kneaker'
# # # # elif student['gender'] == 'female':
# # # #     if student['is_senior']:
# # # #         student['uniform'] = 'skirt'
# # # #     else:
# # # #         student['uniform'] = 'gown'
# # # # else:
# # # #     print("we don't want ny other")
# # # #     if student['skirt_dot_write']:
# # # #         student['uniform'] = 'short kneaker'
# # # #
# # # # print(student)
# # # #
# # # # x = 5
# # # # y = 10 if x == 5 else 20
# # # # print(y)
# # # #
# # # # # loops
# # # #
# # # # # number_datatype = 20
# # # # # string_datatype = 'lots of them '
# # # # # for char in str
# # # # #         print(i)
# # # #
# # # # number_datatype = 20
# # # # string_datatype = 'lots of them '
# # # # fruits = ['cashew','mango', 'apple', 'grape', 'date', 'orange', 'cherry']
# # # # for fruit in fruits:
# # # #      print(fruits)
# # # #
# # # # student = {
# # # #     "name": "michael",
# # # #     "gender": "male",
# # # #     "is_senior": True,
# # # #     "uniform": None,
# # # #     "skirt_dot_write": True
# # # # }
# # # #
# # # # for fruit in fruits:
# # # #     print(fruit)
# # # #     for letter in fruit:
# # # #         print(letter)
# # # # for prop in student:
# # # #     print(student)
# # # #
# # # #
# # # # number_datatype = 20
# # # # for num in range(5, number_datatype, 5):
# # # #     print(num)
# # # #
# # # #
# # # #
# # #
# # #
# # # # numbers = [1 , 2 ,3 , 4 , 5 , 6 ]
# # # # for number in number:
# # # #     if number % 2:
# # # # #         print(number)
# # #
# # # # whileloop
# # # # count = 0
# # # # while count < 10:
# # # #     print(count)
# # # #     count += 1
# # # #
# # # # print('Done.')
# # # #
# # # # while True:
# # # #     print("Till the end of time. yaay!!")
# # # #
# # # # print('Done')
# # #
# # #
# # # # break statement, continue statement
# # #
# # # fruits = ['cashew','mango', 'apple', 'grape', 'date', 'orange', 'cherry']
# # # favourite_fruit = None
# # # not_favourite_fruit = ['cashew', 'cherry']
# # #
# # # for fruit in fruits:
# # #     if fruit in not_favourite_fruit:
# # # continue
# # #
# # #     print("Wash it")
# # #     print("Peel it")
# # #     print("Eating it")
# # #     print("More.")
# # #     print()
# # #
# # # #     if fruit == 'apple':
# # # #         favourite_fruit = fruit
# # # #         break
# # # #
# # # # print(not_favourite_fruit)
# # #
# #
# # # functions
# #
# # # def eat(edible, code="at coding"):
# # #     print("Micheal %s is great %s." %( edible, code))
# # #
# # # # positional argument
# # # # eat("literally", "at coding")
# # # # keyword argument
# # #
# # # eat("literally")
# #
# # # argument destructuring
# #
# # # def fruit_salad(*fruits):
# # #     print(fruits)
# # #
# # # fruit_salad('pinnapple' , 'bannana' , 'apple' , 'watermelon')
# #
# #
# # # def fruit_salad():
# # #     fruit_salad('pinnapple' , 'bannana' , 'apple' , 'watermelon')
# # #     for fruit in fruit_salad():
# # #         print("adding %s to the salad" % fruit_salad())
# # #         fruit = []
# # #         print("Fruits left in function", fruit_salad())
# # #
# # #         print("done")
# # #
# # #     fruit_salad()
# # #     print("fruits left", fruit_salad())
# #
# # def fruits_salad
#
#
#
#
#
#
# def square(number):
#     s_number = number * number
#     return s_number
#
# squared_num = square(2)
# print(squared_num)
# print(square (4))
#

# make a function that counts the number of time a given item appears in a list

numerals = [1,2,3,4,5,2,3,2,1,1,4,5,2]
x = numerals.count(2)
print("the number 2 occurs " + str(x) + " times")




 # basic operators
 # x=5 # print(x + 3)
# # print(x - 3)
# # print(x / 3)
# # print(x * 3)
# # print(x % 3)
# # print(x // 3)
# # print(x ** 3)

# str1= 'name'
# str2= 'phone'
# print(str1 > str2)
# print(str1 >= str2)
# print(str1 != str2)
# print(str1  is str2)
#
# print("\nList comparison:")
# List1=['name','phone']
# List2=['age','class']
#
# print(List1 > List2)
# print(List1 >= List2)
# print(List1 != List2)
# print(List1  is List2)
# # true is =1 and False =0  BY  default
# # Assignment operator  "="
# #bitwise operators   << and  >>
# print(16 << 4)
#logical operators  we have the , AND , NOR , OR
# print(True  and False or  not True)
# text ='name'
# items=[1,2,3]
# print('a' in text)
# print('a' not in text)
# new_items= items
#
# print(1 in items)
# print(5 in items)
# print( items is new_items)
print(ord("A"))
print(chr(65))

for i in range(256):
    print("ordinal number %d is %s"%(i,chr(i)))

print(ord('#'))
string =input("text what you need to covert no byte")
byte_string=""

for char in string:
    ord_num= ord(char)
    # convert ordinary number to binary
    ord_num= bin(ord_num)
    # trimming our OB() FUNCTION
    ord_num=ord_num[2:]
    #  calculate  length og zero to padding
    len_to_padd =8 - len(ord_num)
    # multiply"0" by length of zero to pad
    padded_zeros= "0"* len_to_padd
    # add padded zeros to  back ordinary number
    ord_num = padded_zeros + ord_num
    # concatenate byte to byte string
    byte_string += ord_num
print(byte_string)



string_number = "101"
print(string_number + '5')
print(int(string_number) + 5)
print(int(string_number) * 2)

digit = 10
print(digit * 3)
print(str(digit) * 3)

fruits = ['mango', 'pineapple', 'orange', 'grape']
my_fav_fruits_forever = tuple(fruits)

print(fruits)
print(my_fav_fruits_forever)

fruits[0] = 'cherry'
# fruits.append("cashew")
# print(fruits)
# print(my_fav_fruits_forever)
#
# person = {"name": 'jeo ken', "age": 35, "gender": 'M'}
# print(person)
# print(list(person))
# print(tuple(person))



person = [  { "name": 'jeo ken', "age": 35, "gender": 'M' , "id": 1},
            { "name": 'michael', "age": 34, "gender": 'M', "id": 2} ,
            { "name": 'tola', "age": 12, "gender": 'F', "id": 3} ,
            { "name": 'bola', "age": 21, "gender": 'F', "id": 4} ,
            { "name": 'samuel peters', "age": 12, "gender": 'M', "id": 5} ,
         ]



name_input = input("Name of person to find: ")
while not name_input:
    print("No name, type something.")
    name_input = input("name of person to find: ")

print()
age_input = input("how old is " + name_input + "?")
while not age_input.isdigit():
    print("invalid age input.")
    age_input = input("how old is " + name_input.title() + "?")
age_input = int(age_input)

query = { "name": name_input, "age": age_input }
result = None
for person in person:
    all_match = True
    for property in list(query):
        if person[property] != query[property]:
            all_match = False
    if all_match:
        result = person
        break


print(result)



numerator = 11
denominator = 3
print(11/3)
print(11//3)
print(11 % 3)
print(11**3)

print([1,2] > [2,3])
fan = 5 and 0
print([5] and [0])


x = ("apple", "banana", "cherry")
print(x)


variable_name= 5
print(variable_name)
variable_name="string"
print(variable_name)
names=["jeo","ken"]
print(names)

# multiple assignment
a,b,c,d,e = 1,2,3,4,5
print(a)
print(b)
print(c)
print(d)
print(e)


string = 'text data'
items = []
immutable_items = ()
person = {"name":"ken jeo", "age":35,"nationalities":["nigeria","ghana"],"male_genderism": True}
person["language"] =("english")
person["age"] = 37
person["age"] +=5
print(person)
print("Hi", person['name'],"\n you are",person['age'],"years old")



items = [1,2,3,4]
print(items)
print(items[2])
items[2] = 12
print(items)

del items[2]
print(items)

#tuples

immutable_items = ("do", "re","mi")
# print(immutable_items)

immutable_items[1] = 'fa'
print(immutable_items)
