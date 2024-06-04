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





