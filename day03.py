# day3 6/5/2026
# chapter 6
# 创建字典
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# exercise 6-1
person = {
    'first_name': 'zhang',
    'last_name': 'san',
    'age': 30,
    'city': 'beijing'
}
print(person)

# exercise 6-2
favorite_numbers = {
    'zhangsan': 7,
    'lisi': 3,
    'wangwu': 9,
    'zhaoliu': 5,
    'tianqi': 1
}
print(favorite_numbers)

# exercise 6-3
glossary = {
    'string': 'a series of characters',
    'list': 'a collection of items in a particular order',
    'dictionary': 'a collection of key-value pairs',
    'tuple': 'an immutable ordered list of items',
    'set': 'an unordered collection of unique items'
}
for term, definition in glossary.items():
    print(f"{term}: {definition}")

# exercise 6-5
rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china'
}
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

# exercise 6-6
favorite_languages = {
    'jen': 'python',
    'exo': 'java',
    'edward': 'ruby',
    'phil': 'python',
}
friends = ['jen', 'edward']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}!")
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

# 嵌套
# 列表中的元素是字典
print("#"*40)
aline_0 = {"color": "green", "points": 5}
aline_1 = {"color": "yellow", "points": 10}
aliens = [aline_0, aline_1]
for aline in aliens:
    print(aline)

alines = []
# 创建30个绿色的外星人
for alines_number in range(30):
    new_aline = {"color": "green", "points": 5, "speed": "slow"}
    alines.append(new_aline)
# 显示前5个外星人
for aline in alines[: 5]:
    print(aline)
print(f"\n total number of alines:{len(alines)}")

# exercise 6-7
people = [
    {"name": "Alice", "age": 17},
    {"name": "Rechard", "age": 23}
]
for person in people:
    print(f"The person's name is {person["name"]} and they are {person["age"]} years old.")

# exercis 6-8
pets = [
    {"type": "dog", "owner": "Alice"},
    {"type": "cat", "owner": "Bob"},
    {"type": "hamster", "owner": "Charlie"}
]

for pet in pets:
    print(f"The {pet['type']} is owned by {pet['owner']}.")

# exercise 6-9
favorite_places = {
    'Alice': ['beijing', 'shanghai'],
    'Bob': ['guangzhou', 'shenzhen'],
    'Charlie': ['hangzhou', 'nanjing']
}
for name, places in favorite_places.items():
    print(f"{name}'s favorite places are: {', '.join(places)}")

# exercise 6-10
favorite_numbers = {
    'Alice': [3, 7],
    'Bob': [5, 9],
    'Charlie': [1, 4]
}
for name, numbers in favorite_numbers.items():
    print(f"{name}'s favorite numbers are: {', '.join(str(num) for num in numbers)}")

# exercise 6-11
cities = {
    'beijing': {
        'country': 'china',
        'population': 21540000,
        'fact': 'the capital of china'
    },
    'shanghai': {
        'country': 'china',
        'population': 24280000,
        'fact': 'the largest city in china'
    }
}
for city, info in cities.items():
    print(f"{city.title()}:")
    for key, value in info.items():
        print(f"  {key}: {value}")


#chapter 7 用户输入和while循环
print("#"*80)
# input函数，会将输入转化为字符串
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

# exercise 7-1
requests = input("what kind of rental car do you want? ")
print(f"Let me see if I can find you a {requests}.")

