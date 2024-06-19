## 函数
- 定义函数，实参和形参
```python
def greet_user(username):
    print(f'hello {username}')

name = input('What is your name?\n')
greet_user(name)
```

- 位置实参 (基于实参的顺序进行关联)
```python
def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name}.")

describe_pet("dog", "lucky")
```
- 关键字实参 (无需考虑顺序)
```python
def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name}.")

describe_pet( pet_name="lucky",animal_type="dog")
```
- 默认值 (如果在调用函数中给形参提供了实参，Python 将使用指定的实参值；否则，将使用形参的默认值。)
```python
def describe_pet(animal_type, pet_name='xiao gou'):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name}.")

describe_pet( pet_name="lucky",animal_type="dog")
describe_pet( animal_type="dog")
```

### 返回值
- 返回简单的值

```python
def get_formatted_name(first_name, last_name):
    fullname = f'{first_name} {last_name}'
    return fullname.title()

formatted_name = get_formatted_name('janis', 'zhang')
print(formatted_name)
```

- 实参可选
```python
def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = f'{first_name} {last_name} {middle_name}'
    else:
        full_name = f'{first_name} {last_name}'
    return full_name.title()

formatted_name = get_formatted_name('janis', 'zhang','wang')
print(formatted_name)
formatted_name = get_formatted_name('janis', 'zhang')
print(formatted_name)
```
- 返回字典
```python
def build_person(first_name, last_name):
    person = {'first_name': first_name, 'last_name': last_name}
    return person

musician = build_person('John', 'Doe')
print(musician)
```
```python
def build_person(first_name, last_name, age=None):

    person = {'first_name': first_name, 'last_name': last_name}
    if age is not None:
        person['age'] = age
    return person
person = build_person('John', 'Smith')
print(person)
person = build_person('John', 'Smith', age=25)
print(person)
```
- 结合使用函数和while循环

#### 传递列表
```python
def greet_users(names):
    for name in names:
        print(f'Hello {name}')

greet_users(['John', 'Doe', 'Janis'])
```
- **禁止**函数修改列表
- 将列表的副本传递给函数,切片表示法[:]创建列表的副本。
```python
function_name(list_name[:])
```

#### 传递任意数量的实参
Python 允许函数从调用语句中收集任意数量的实参。  
```python
def make_pizza(*toppings):
    print('making a pizza with the following toppings:')
    for topping in toppings:
        print(topping)

make_pizza(1,2,3,4)
make_pizza('mushrooms', 'green peppers', 'extra cheese')
```
- 结合使用位置实参和任意数量的实参
```python
def make_pizza(size, *toppings):
    print('making a pizza with the following toppings:')
    print(f'The size is {size}')
    for topping in toppings:
        print(topping)

make_pizza(20,'mushrooms', 'green peppers', 'extra cheese')
```
- 使用任意数量的关键字实参
```python
def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein', location='San Francisco')
print(user_profile)
```

### 将函数存储在模块中
import语句可让你在当前运行的程序文件中使用模块的代码。
```python
import pizza

pizza.make_pizza(20,'pepperoni')
pizza.make_pizza(15,'mushrooms','green peppers')
```
- 导入特定的函数
```python
from pizza import make_pizza

make_pizza(20,'pepperoni')
make_pizza(15,'mushrooms','green peppers')
```
```python
from module_name import function_0, function_1, function_2
```
- 使用as给函数、模块指定别名
```python
from pizza import make_pizza as mp

mp(20,'pepperoni')
mp(15,'mushrooms','green peppers')
```
```python
import pizza as pzz

pzz.make_pizza(20,'pepperoni')
pzz.make_pizza(15,'mushrooms','green peppers')
```

- 导入模块中的所有函数 (不推荐)
```python
from pizza import *
```

## 类
- 在python中，首字母大写的名称指的是类。
- __init__()方法：
  - 开头和末尾各有两个下划线
  - 当创建类的新实例的时，都会自动运行它。
  - 形参self必不可少，且必须位于其他形参数前面。
  - 当 Python 调用这个方法来创建Dog实例时，将**自动**传入实参self。每个与实例相关联的方法调用都会自动传递实参self，该实参是一个指向实例本身的引用，让实例能够访问类中的属性和方法。

### 继承
- 在括号内指定父类名称
- 给子类定义属性和方法
- 重写父类中的方法
```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()

    def read_odometer(self):
        print(f'This car has {self.odometer_reading} miles on it.')

    def update_odometer(self, mileage):
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can't roll back an odometer")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gas_tank(self):
        print('filllllll')

class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 40

    def describe_battery_size(self):
        print("This car has a battery size of {}".format(self.battery_size))

    def fill_gas_tank(self):
        print("this car doesn't have a gas tank!")

my_tesla = ElectricCar('Tesla', 'model3', 2024)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery_size()
my_tesla.fill_gas_tank()
```

- 将实例用做属性
```python
class Battery:
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery_size(self):
        print("This car has a battery size of {}".format(self.battery_size))

class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

my_tesla = ElectricCar('Tesla', 'model3', 2024)
my_tesla.battery.describe_battery_size()
```

- 导入类
```python
from car import car
```
- 从一个模块中导入多个类
```python
from car import car, electric_car
```
- 导入整个模块
```python
import car
```
- 导入模块的所有类
```python
from module_name import *
```
- 使用别名
```python
from electric_car import ElectricCar as EC
my_leaf = EC('nissan', 'leaf', 2024)
```

## python 标准库
python标准库是一组模块，在安装python时已经包含在内。  

- random模块的函数，randint()和choice
```python
from random import randint

print(randint(1,6))

from random import choice

players = ['carles','michael','florence','eli']
first = choice(players)
second = choice(players)
print(first)
print(second)
```
- 类名应采用驼峰命名法，并且不使用下划线
- 实例名和模块名都次啊用全小写格式，并在单词之间加上下划线

## 文件和异常
- 读取文件全部内容
- pathlib模块处理文件和目录
```python
from pathlib import Path

path = Path('resources/pi_digits.txt')
content = path.read_text()
print(content)
```
#### 相对路径和绝对路径
- 绝对路径通常比相对路径⻓，因为它们以系统的根文件夹为起点

### 访问文件中的各行
```python
path = Path('resources/pi_digits.txt')
content = path.read_text()
lines = content.splitlines()

for line in lines:
    if '323846' in line:
        print(line)

pi_string = ''

for line in lines:
    pi_string += line.lstrip()

print(pi_string)
print(len(pi_string))
```

- 包含100万位的大型文件：在可处理的数据量方面，Python没有任何限制。只要系统的内存足够大，想处理多少数据就可以处理多少数据。

### 写入文件
```python
path = Path('resources/pi_digits.txt')
content = 'hello world.\n'
content += 'This is the first line.\n'
content += 'This is the second line.\n'
path.write_text( content)
```

### 异常
异常试是使用try-except代码块处理的
```python
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
    
```
- else 代码块
```python
print("Give me two numbers, and I'll divide them.\n")
print("Enter 'q' to exit\n")
while True:
    first_number = input("first_number:")
    second_number = input("second_number:")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)
```
- 处理FileNotFoundError异常 (same as above)
- 静默失败
```python
except ZeroDivisionError:
  pass
```
- 计算一个文件大致包含多少单词
```python
from pathlib import Path

def count_words(filepath):
    path = Path(filepath)
    content = path.read_text()
    return len(content.split())

print(count_words('resources/pi_digits.txt'))
```

### 存储数据
- 使用模块json来存储数据
- 使用json.dumps()和json.loads()
```python
from pathlib import Path
import json

numbers = [2,3,5,7,9,11,13,15,17,19,23]
contents = json.dumps(numbers)
path = Path('resources/numbers.json')
path.write_text(contents)

path = Path('resources/numbers.json')
contents = path.read_text()
print(json.loads(contents))
```

### 测试
- pytest
```python
def test_formatted_name():
    formatted_name = get_formatted_name('janis', 'joplin')
    assert formatted_name == 'Janis Joplin'
```
- 测试中常用的断言
```python
assert a == b
assert a != b
assert a
assert not a
assert element in list
assert element not in list
```



