
# dictionary
about_me = {
    "name": "Sergio",
    "last": "Inzunza",
    "age": 35,
    "hobbies": [],
    "address": {
        "street": "42 evergreen",
        "city": "Springfield"
    }
}

print( about_me["name"] )

# using string formatting, print the full name (first last)
print(f"{about_me['name']} {about_me['last']}")

# street and city
address = about_me["address"]
print(address["street"])
print(address["city"])


# modify
about_me["age"] = 36

# create new key
about_me["phone"] = "123 3232 3444"

print(about_me)




# List
print("-" * 40)

names = []
names.append("Gary")
names.append("Oscar")
names.append("Angel")
names.append("Kvon")

print(names)

print(names[0])
print(names[1])
print(names[2])
print(names[3])

# for loop
print("using loops " * 4)
for name in names:
    print(name)


nums = [1,2,3,4,5,6,7,5,4,4,7,2,54,6,2,768,89,345,5467,908,2,4,78,678,123,435]

# exe 1: print all numbers
#    b) except 4
for num in nums:
    if num != 4:
        print(num)


# exe 2: count how many 4s there are in the list
# start a counter on 0
# travel the list and get each number inside
#   if the number is a 4, increase the counter
# print the counter
counter = 0
for num in nums:
    if num == 4:
        #counter = counter + 1
        counter += 1

print(counter)

# using list count
print(nums.count(4))




# exe 3: Sum all the nums
# start with a sum of 0
# travel the list and get each number inside
#   add the number to the running sum
# print the sum
my_sum = 0
for num in nums:
    #sum = sum + num
    my_sum += num

print(my_sum)

print(sum(nums))




students = [ 
    {
        "name": "Kvon",
        "age": 36
    },
    {
        "name": "Gary",
        "age": 37
    },
    {
        "name": "Oscar",
        "age": 33
    },
    {
        "name": "Angel",
        "age": 35
    },
]

# exe 4: Sum the ages  (141)
total = 0
for student in students:
    age = student["age"]
    total += age

print(total)







# Find the minimum algorithm

ages = [ 62,34,21,78,23,88,20, 65,32, 17, 94, 17, 16, 65,21,89]

min = ages[0]
for num in ages:
    if num < min:
        min = num

print(f"the youngest person's age is {min}")









# endpoint that will return a list of strings
# the list will contain the unique categories


# 2 - print each category from the products
# 3 - create a new list

# 6 - if the category does not exist inside the list
    # 4 - push category into the list

# 5 - print the list

from mock_data import catalog


def get_unique_categories():
    print("-" * 30)

    categories = []
    for prod in catalog:
        cat = prod["category"]
        if cat not in categories:
            categories.append(cat)
        
    print(categories)



get_unique_categories()


colors = ["red", "blue", "orange", "orange", "Blue", "Green", "Red", "blue", "Black", "gray", "GrAY", "oRanGE"]

# get the unique colors as a list
def get_unique_colors(): 
    print("*" * 30)
    
    result = []    
    for color in colors:
        if color.lower() not in result:
            result.append(color.lower())

    print(result)

get_unique_colors()