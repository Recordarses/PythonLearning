# 2026/06/03
# 修改、添加和删除元素
# exercise 3-4
print("----------------------this is exercise 3-4------------------")
guests = ['liu', 'z', 'lily']
print(f"have dinner with me, {guests[0]}")
print(f"have dinner with me, {guests[1]}")
print(f"have dinner with me, {guests[2]}")

# exercise 3-5
print("----------------------this is exercise 3-5------------------")
print(f"{guests[1]} can not come with us.")
guests[1] = 'coco'
print(f"have dinner with me, {guests[0]}")
print(f"have dinner with me, {guests[1]}")
print(f"have dinner with me, {guests[2]}")

# exercise 3-6
print("----------------------this is exercise 3-6------------------")
print(" i find a larger table.")
guests.insert(0, 'rio')
guests.insert(2,'mitty')
guests.append('nino')
for i in guests:
    print(f"have dinner with me, {i}")

# exercise 3-7
print("----------------------this is exercise 3-7------------------")
print("I can only invite 2 guests")
people1 = guests.pop()
print(f"sorry, I can not invite you, {people1}")
people2 = guests.pop()
print(f"sorry, I can not invite you, {people2}")
people3 = guests.pop()
print(f"sorry, I can not invite you, {people3}")
for i in guests:
    print(f"{i}, you are still in the list. ")
del guests[:]
print(guests)

# exercise 3.8
print("----------------------this is exercise 3-8------------------")
lst = ['dubai', 'dream', 'canada', 'austrin']
print(sorted(lst))
print(lst)
print(sorted(lst, reverse=True))
print(lst)
lst.reverse()
print(lst)
lst.reverse()
print(lst)
lst.sort()
print(lst)
lst.sort(reverse=True)
print(lst)

# exercise 3-9
print("----------------------this is exercise 3-9------------------")
print(f"I invite {len(lst)} guests")

# exercise 3-10
print("----------------------this is exercise 3-10------------------")
# anyway you do

# exercise 4-1
print("----------------------this is exercise 4-1------------------")
pizzas = ['beef', 'chicken', 'seafood']
for i in pizzas:
    print(f"I like {i} pizza.")
print("I really love pizza!")

# exercise 4-2
print("----------------------this is exercise 4-2------------------")
animals = ['dog', 'cat', 'rabbit']
for i in animals:
    print(f"A {i} would make a great pet.")
print("Any of these animals would make a great pet!")

# exercise 4-3
print("----------------------this is exercise 4-3------------------")
for i in range(1, 21):
    print(i)

# exercise 4-4
#lst = list(range(1, 1000001))
#for i in lst:
    print(i)

#print(min(lst))
#print(max(lst))
#print(sum(lst))

# exercise 4-6
for i in range(1, 21, 2):
    print(i)

# exercise 4-7
for i in range(3, 30, 3):
    print(i)

# exercise 4-8
lst = [value**3 for value in range(1, 11)]
for i in lst:
    print(i)

# exercise 4-9
lst = [value**3 for value in range(1, 11)]

# exercise 4-10
print("The first three items in the list are:")
print(lst[:3])
print("Three items from the middle of the list are:")
print(lst[3:6])
print("The last three items in the list are:")
print(lst[-3:])

# exercise 4-11
my_pizzas = ['beef', 'chicken', 'seafood']
friend_pizzas = my_pizzas[:]
my_pizzas.append('veggie')
friend_pizzas.append('fruit')
print("My favorite pizzas are:")
for i in my_pizzas:
    print(i)
print("My friend's favorite pizzas are:")
for i in friend_pizzas:
    print(i)

# exercise 4-13
my_foods = ('beef', 'chicken', 'seafood', 'veggie', 'fruit')
for food in my_foods:
    print(food)
# my_foods[0] = 'pork' # tuple不支持修改元素

my_foods = ('pork', 'chicken', 'seafood', 'veggie', 'fruit')
for food in my_foods:
    print(food)

# 第五章
print('#'*40)

# exercise 5-1
print("----------------------this is exercise 5-3------------------")
alien_color = 'green'
if alien_color == 'green':
    print("you get 5 points")
if alien_color != 'green':
    print("you get 10 points")

# exercise 5-4
alien_color = "green"
if alien_color == 'green':
    print("you get 5 points")
else:
    print("you get 10 points")

# exercise 5-7
favorite_fruits = ['apple', 'banana', 'orange']
if 'apple' in favorite_fruits:
    print("you really like apple!")
if 'orange' in favorite_fruits:
    print("you really like orange!")
if 'pear' in favorite_fruits:
    print("you really like pear!")

# exercise 5-8
users = ['admin', 'alice', 'bob', 'coco', 'david']
for user in users:
    if user == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {user}, thank you for logging in again.")

# exercise 5-9
for user in users:
    if not users:
        print("we need to find some users!")
    elif user == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {user}, thank you for logging in again.")

# exercise 5-10
current_users = ['admin', 'alice', 'bob', 'coco', 'david']
current_users_lower = [user.lower() for user in current_users]
new_users = ['admin', 'alice', 'bob', 'coco', 'david', 'nino']
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"{new_user} has been used, please enter a new username.")
    else:
        print(f"{new_user} is available.")

# exercise 5-11
lst = list(range(1, 10))
for i in lst:
    if i == 1:
        print(f"{i}st")
    if i == 2:
        print(f"{i}nd")
    if i != 1 and i != 2:
        print(f"{i}th")


