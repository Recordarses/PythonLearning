# day5,6/8-2026
# Chapter 8 函数
def greet_uesr():
    """显示简单的问候语"""
    print("hello!")

greet_uesr()

# exercise 8-1
def display_message():
    """本章学的是什么"""
    print("本章学的是函数")

display_message()

# exercise 8-2
def favorite_book(title):
    """打印最喜欢的书"""
    print(f"One of my favorite books is {title}")

favorite_book("Alice in Wonderland")

# exercise 8-3
def make_shirt(size, text):
    """T恤定制"""
    print(f"The size of the shirt is {size}, and the text on the shirt is '{text}'.")
make_shirt("L", "I love Python")
make_shirt(size="M", text="Python is great!")
make_shirt(text="Python is awesome!", size="S")

# exercise 8-4
def make_shirt(size, text="I love Python"):
    """T恤定制，默认文本"""
    print(f"The size of the shirt is {size}, and the text on the shirt is '{text}'.")   
make_shirt("L")
make_shirt("M", "Python is great!")
make_shirt(text="Python is awesome!", size="S")

# exercise 8-5
def describe_city(city, country="China"):
    """描述城市"""
    print(f"{city} is in {country}.")   
describe_city("Beijing")
describe_city("Shanghai")
describe_city("New York", "USA")

# 8.3 返回值 return，函数可以返回一个值，调用函数的代码可以使用这个值。
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name("jimi", "hendrix") # 赋值
print(musician)

# 让实参成为可选的
def get_formatted_name(first_name, last_name, middle_name = ""):
    """返回整洁的姓名"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name("jimi", "hendrix")
print(musician)

# 8.3.3 返回字典
def build_person(first_name, last_name, age=None):
    """返回一个字典，包含一个人的信息"""
    person = {"first": first_name, "last": last_name}
    if age:
        person["age"] = age
    return person

musician = build_person("jimi", "hendrix")
print(musician)

# 结合使用函数和while循环
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\n please tell me your name:")
    print("(enter 'q' to quit)")
    first_name = input("First name: ")
    if first_name == 'q':
        break
    last_name = input("Last name: ")
    if last_name == 'q':
        break

    formatted_name = get_formatted_name(first_name, last_name)
    print(f"Hello, {formatted_name}!")

# exercise 8-6
def city_country(city, country):
    """返回一个格式为City, Country的字符串"""
    return f"{city}, {country}"

print(city_country("Beijing", "China"))
print(city_country("Shanghai", "China"))
print(city_country("New York", "USA"))

# exercise 8-7
def make_album(artist_name, album_title, tracks=None):
    """返回一个字典，包含专辑的信息"""
    album = {"artist": artist_name, "title": album_title}
    if tracks:
        album["tracks"] = tracks
    return album
print(make_album("Taylor Swift", "1989"))

# exercise 8-8
while True:
    print("\nPlease enter the artist and album name:")
    print("(enter 'q' to quit)")
    artist_name = input("Artist name: ")
    if artist_name == 'q':
        break
    album_title = input("Album title: ")
    if album_title == 'q':
        break

    album = make_album(artist_name, album_title)
    print(album)

# 8.4 传递列表给函数
def greet_users(names):
    """向列表中的每位用户都发出简单的问候"""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

# 8.4.2 在函数中修改列表
def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计，知道没有未打印的设计为止
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"print model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """显示打印好的所有模型"""
    print("\n The following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# 8.4.3 禁止函数修改列表
# 向函数传递列表的副本，而不是原件，这样函数就无法修改原来的列表。
# function_name(list_name[:]) # 传递列表的副本
# 但是一般来说，如果函数需要修改列表，就让它修改列表，不要试图禁止它修改列表。这是因为为了让函数使用现成的列表，传递列表的副本会占用额外的内存空间。

# exercise 8-9
def show_magicians(magicians):
    """打印魔术师的名字"""
    for magician in magicians:
        print(magician)

magicians = ['alice', 'david', 'carolina']
show_magicians(magicians)

# exercise 8-10
def send_messages(messages, sent_messages):
    """打印每条消息，并将其移到已发送消息列表中"""
    while messages:
        current_message = messages.pop(0)
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

messages = ["Hello, Alice!", "Hi, David!", "Hey, Carolina!"]
sent_messages = []
send_messages(messages, sent_messages)

# exercise 8-11
def send_messages(messages, sent_messages):
    """打印每条消息，并将其移到已发送消息列表中"""
    while messages:
        current_message = messages.pop(0)
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

messages = ["Hello, Alice!", "Hi, David!", "Hey, Carolina!"]
sent_messages = []
send_messages(messages[:], sent_messages) # 传递列表的副本
print("Original messages:", messages) # 原列表未修改