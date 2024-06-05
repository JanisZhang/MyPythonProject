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

