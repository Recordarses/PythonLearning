# 2.变量和简单数据类型
# 2.1 变量
message  = "Hello Python Crash Course Reader"
print(message)

# exercise 1-1
a = "we eat apple today!"
print(a)

a = "what do we eat?"
print(a)

# 2.3 字符串
# 2.3.1 方法
name = "alice Brown"
print(name.title())
print(name.upper())
print(name.lower())

# 2.3.2 在字符串中使用变量
# f 字符串
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name}{last_name}"
print(full_name)
print(f"Hello, {full_name.title()}")

message = f"Hello, {full_name.title()}"
print(message)

# 2.3.3 添加空白，读取更容易
# 添加制表符\t
print("Python")
print("\tPython")

# 换行符\n
print("langues:\nPython\nC\nJavaScript")

# 同时包含制表符和换行符
print("Language:\n\tPython\n\tC\n\tJavaScript")

# 2.3.4 删除空白
favorite_language = "python "
print(favorite_language)
print(favorite_language.rstrip())
print(favorite_language)
# 要想永久删除，需要关联到变量
favorite_language = favorite_language.rstrip()
print(favorite_language)

# 去掉左侧空白
favorite_language = " python"
favorite_language = favorite_language.lstrip()
print(favorite_language)

# 去掉左右两侧空白
favorite_language = " python "
favorite_language = favorite_language.strip()
print(favorite_language)

# exercise 2-5
slogan = "Albert Eistein once said, \"A person who never made a mistake never\ntried anything new. \""

# exercise 2-6
famous_person = "Albert Eistein"
message = f"{famous_person} once said, \"A person who never made a mistake never\ntried anything\""
print(message)

# 2-7
name = '\tAlice\n Brown\t'
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())

# 2.4 数
4/2 # 两个整数相除，结果总是浮点
1+2.0 # 如果一个操作数是整数，另一个操作数是浮点数，结果也总是浮点数
university = 14_000_000_000

x, y, z = 1, 2, 3# 多变量同时赋值

MAX_CONNECTIONS = 5000 # 常量，全部大写

# exercise 2-8
print(2+6)
print(1*8)
print(16/2)
print(10-8)

# exercise 2-9
num = 7
message = f"my favorite number is {num}"
print(message)

import this

# 第三章 列表
print('------------------this is chapter 3------------------')
# exercise 3-1
names = ["Alice", "Bob", "Charlie"]
print(names[0])
print(names[1])
print(names[2])

# exercise 3-2
print(f"{names[0]} God bless you!")
print(f"{names[1]} God bless you!")
print(f"{names[2]} God bless you!")

# exercise 3-3
transportations = ['bike', 'car', 'ship']
for i in transportations:
    message = f"I would like to commute by {i}"
    print(message)

