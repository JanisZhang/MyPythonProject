## Python 从入门到实践
### 变量的命名和使用
- 变量名只能包含数字、字母和下划线，不能以数字开头。

## 字符串
- 引号可以是单引号，也可以是双引号。
#### 使用字符串的方式
- title()
- upper()
- lower()

#### 字符串中使用变量
- f字符串：python通过花括号内的变量替换为其值
```python
firstname = 'janis'
lastname = 'zhang'
fullname = f'{firstname} {lastname}'
print(fullname)
greeting = f'Hello,Miss {lastname.title()}'
print(greeting)
```

#### 使用制表符/换行符
```python
print('\tHello \nWorld!')
```

#### 删除空白
- rstrip 删除左端空白
- lstrip删除右端空白
- strip删除空白

#### 删除前缀
```python
nostarch_url = 'https://nostarch.com'
print(nostarch_url.removeprefix('https://'))
print(nostarch_url.removesuffix('.com'))
message = 'python_notes.txt'
print(message.removesuffix('.txt'))
```

## 数
#### 浮点数
- 结果包含的小数位数可能是不确定的
```python
print(0.2+0.1)
print(0.2+0.2)
---
0.300000000000004
0.4
```
#### 整数和浮点数
- 将任意两个数相除，结果总是浮点数，即便这两个数都是整数且能整除
```python
print(4/2) >>> 2.0
```
- 在其他任何运算中，如果一个操作数是整数，另一个操作数是浮点数，结果也总是浮点数
```python
print(1+2.0) >>> 3.0
print(2*3.0) >>> 6.0
```
- 数字中的下划线
```python
universe_age = 14_000_000_000_000
print(universe_age)  >>> 14000000000000
```
- 同时给多个变量赋值
```python
x,y,z = 34,11,33
print(x) >>> 34
```
- 常量 (使用全大写字母)
```python
MAX_CONNECTIONS = 5000
```

## 列表
#### 访问列表元素
- 索引从0开始
- ython 为访问最后一个列表元素提供了一种特殊语法。通过将索引指定为-1，可让 Python 返回最后一个列表元素。
```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[-1])
print(len(bicycles))
print(bicycles[0:2])
print(bicycles[2:4])
print(bicycles[2:])
print(bicycles[::2])
print(bicycles[::-1])
print(bicycles[0].title())
```
```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(f'My first bicycle was a {bicycles[0].title()}')
```
#### 操作列表元素
- 修改列表元素
```python
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
```
- del、pop()、remove()
```python
motorcycles = []
motorcycles.append('ducati')
motorcycles.append('honda')
motorcycles.append('jackal')
print(motorcycles)

motorcycles.insert(1, 'suzuki')
print(motorcycles)

del motorcycles[0]
print(motorcycles)
motorcycles.pop()
# motorcycles.pop(1)
print(motorcycles)
motorcycles.remove('honda')
print(motorcycles)
```
### 管理列表
- sort() 进行永久排序
```python
cars = ['bmw', 'toyota', 'audi', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
```
- sorted() 临时排序, reverse()
```python
cars = ['bmw', 'toyota', 'audi', 'subaru']
print(sorted(cars))
print(cars)
print(sorted(cars, reverse=True))
---
cars = ['bmw', 'toyota', 'audi', 'subaru']
cars.reverse()
print(cars)
```

### 操作列表
#### 创建数值列表
- range，差一行为
```python
for value in range(1,5):
    print(value)  >> 1,2,3,4
```
- list将range结果直接转换成列表
```python
numbers = list(range(1,11))
print(numbers)
numbers = list (range(2,11,2))
print(numbers)
```
```python
squares = []
for number in range(1, 11):
    square = number ** 2
    squares.append(square)
print(squares)
print(min(squares))
print(max(squares))
print(sum(squares))
```
- 列表推导式
```python
squares = [value**2 for value in range(1,11)]
print(squares)
```

### 切片
- 遍历
```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
# 输出名单上最后三名队员的名字
print(players[-3:])
for player in players[:3]:
    print(player.title())
```
- 复制列表
```python
my_food = ['apple', 'banana', 'cherry']
friend_foods = my_food[:]
print(friend_foods)
friend_foods = my_food[-2:]
friend_foods.append('carrot')
print(friend_foods)
```

## 元组
- 定义元组，使用圆括号
- 元组不能修改元素，但是可以重新定义整个元组
```python
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
---
# 遍历
for value in dimensions:
    print(value)
---
dimensions = (60, 550)
```

## if语句
```python
cars = ['bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
---
age = 12
if age < 4:
    print("You are a child")
elif age < 18:
    print("You are a teenager")
else:
    print("You are cold")
```
- 比较 (and、or)
```python
car = 'audi'
print(car == 'Audi')
print(car.upper() == 'Audi'.upper())
---
age_0 = 22
age_1 = 8
print( age_0 > 10 and age_0 < 20)
---
age = 12
if age < 4:
    price = 0
elif age < 18:
   price = 100
else:
    price = 200
print(price)
```
- 检查特定的值在不在列表中
```python
requested_toppings = ['mushrooms', 'extra cheese', 'onions']
print('test' in requested_toppings)
print('test' not in requested_toppings)
---
requested_toppings = ['mushrooms', 'extra cheese', 'onions']
print('mushrooms' in requested_toppings)
```
- 布尔表达式
```python
can_edit = False
print(can_edit)
```
- 检查特殊元素
```python
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for item in requested_toppings:
    if item == 'green peppers':
        print("sorry,we don't have green peppers")
    else:
        print(f"adding {item}")
```
- 在for循环前确定列表非空
```python
requested_toppings = []

if requested_toppings:
    for item in requested_toppings:
        if item == 'green peppers':
            print("sorry,we don't have green peppers")
else:
    print("plain pizza")
```

## 字典
- 字典是一系列键值对
```python
alien_0 = {'color': 'blue', 'weight': 100}
print(alien_0['color'])
print(alien_0['weight'])
```
- 添加键值对
```python
alien_0 = {}
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
---
{'x_position': 0, 'y_position': 25}
```
- 修改字典中的值
```python
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")
```
- 删除字典中的值
```python
del alien_0['x_position']
print(alien_0)
```
- 使用get来访问值。（如果指定的键可能不存在，应考虑使用get方法）
```python
alien_0 = {'color': 'green', 'speed': 'slow'}
print(alien_0['point'])
---
print(alien_0.get('point', 'No this value'))
```
- 遍历字典
- 遍历所有键值对 - items()
```
user_0 = {
    'username':'efermi',
    'first':'enrico',
    'last':'fermi'
}

for key,value in user_0.items():
    print(f'key is {key}')
    print(f'value is {value}')
```

- 遍历字典中的所有key - keys()
```
for key in user_0.keys():
    print(key.title())
```
```
favorite_language = {
    'Test1':'Japanese',
    'Test2':'Chinese',
    'phil':'English'
}
friends = ['phil', 'sarah']

for name in favorite_language.keys():
    print(f'Hi {name.title()}')

    if name in friends:
        language = favorite_language[name].title()
        print(f'Nice to meet you, {name}!, I see you love {language}')

    if name not in friends:
        print(f'{name} not my friends.')
```

- 按特定的顺序遍历字典中的所有键 - sorted()
```
favorite_language = {
    'jen':'python',
    'sarah':'c',
    'edward':'rust',
    'phil':'pyhton'
}

for name in sorted(favorite_language.keys()):
    print(f'{name.title()}, thank you for taking the poll.')
```

- 遍历字典中的所有value - values()
```
for value in sorted(favorite_language.values()):
    print(f'value')
```

- 去除重复项 - set()
```
for language in set(favorite_language.values()):
    print(language.title())
```

- 使用花括号创建集合
```
sara_favorite_language = {'java','rust','c'}
favorite_language = {
    'jen':'python',
    'sara':sara_favorite_language,
    'edward':'rust',
    'phil':'python',
    'sarah':'c',
}

# find sara's favorite language
for name in favorite_language.keys():
    if name == 'sara':
        print(favorite_language[name])
```

### 嵌套
```
aliens = []

for alien_number in range(30):
    new_ailen = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_ailen)

for alien in aliens[:5]:
    print(alien)

print(f'Total number of ailens: {len(aliens)}')
```
- 修改外星人
```
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'fast'
        alien['points'] = 10

for alien in aliens[:5]:
    print(alien)
```

- 在字典中存储列表/字典
```
pizza = {
    'crust':'thick',
    'toppings':['mushrooms','extra cheese']
}

print(f"You ordered a {pizza['crust']} -crust pizza")

for topping in pizza['toppings']:
    print(f'\t{topping}')

```
```
favorite_language = {
    'jen':['python','rust'],
    'sara':['rust','go'],
    'phil':['python','haskell'],
    'sarah':['c'],
}


for name,languages in favorite_language.items():
    if len(languages) >1:
        print(f"{name.title()}'s favorite languages are:")
    else:
        print(f"{name.title()}'s favorite languages is:")

    for language in languages:
        print(f'\t{language.title()}')
```


## 用户输入和while循环
- input()函数
```
message = input("tell me something, i'll print it\n")
print(message)

prompt = "What's your name?\n"
message = input(prompt)
print(f'Hello, {message}')
```
- int()函数
```
prompt = "What's your age?\n"
age = input(prompt)

if int(age) > 18:
    print('teenager')
else: 
    print('child')
```
- 求模运算符（%）- 计算余数

- while循环
```
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number+=1
```

### 使用while循环处理列表和字典
- 在列表之间移动元素
```
unconfirmed_users = ['alice','brian','candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

```

- 删除为特定值的所有列表元素
```
pets = ["cat", "dog", "mouse", "rabbit", "cat"]
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)
```









