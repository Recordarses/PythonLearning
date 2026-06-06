# day4, 6/6/2026
# 7.2 while 循环
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

print("#"*40)

cuurent_number = 0
while cuurent_number < 10:
    cuurent_number += 1
    if cuurent_number % 2 == 0:
        continue
    print(cuurent_number)

# exercise 7-4
while True:
    message = input("请输入一系列披萨配料：")
    if message == "quit":
        break
    print(f"我们会在披萨中添加{message}")

# exercise 7-5
while True:
    message = int(input("请问你的年龄是？"))
    if message < 3:
        print("free!")
        break
    elif 3 <= message <= 12:
        print("ticket price is $10.")
        break
    else:
        print("ticket price is $15.")
        break

# 7.3 使用while循环处理列表和字典
unconfirmed_users = ["alice", "bob", "charlie"]
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# 删除包含特定值的所有列表元素
pets = ["dog", "cat", "dog", "hamster", "dog"]

while "dog" in pets:
    pets.remove("dog")

print(pets)

# exercise 7-8
sandwich_orders = ["pastrami", "tuna", "pastrami", "ham", "pastrami"]
finished_sandwiches = []
for sandwich in sandwich_orders:
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)
print("\nThe following sandwiches have been made:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)

# exercise 7-9
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
print("Sorry, we are out of pastrami sandwiches.")

# exercise 7-10
dream_vacation = input("If you could visit one place in the world, where would you go? "
)
print(f"I'd like to go to {dream_vacation.title()}.")
