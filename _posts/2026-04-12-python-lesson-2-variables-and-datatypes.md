---
layout: post
title: "파이썬 기초: 변수와 자료형"
date: 2026-04-12 05:54:04
categories: [파이썬 강의]
---

# 2강: 파이썬 기초 - 변수와 자료형

안녕하세요! 이번 강의에서는 파이썬에서 가장 기본적인 개념 중 하나인 '변수와 자료형'에 대해 알아보겠습니다. 이는 프로그래밍을 시작하는 모든 초보자에게 필수적인 지식입니다. 변수는 데이터를 저장할 수 있는 공간이고, 자료형은 그 데이터가 어떤 종류의 값인지 결정합니다. 이제부터 각각에 대해详细介绍해보도록 하겠습니다.

## 1. 변수란?

변수(variable)는 프로그래밍에서 가장 기본적인 개념 중 하나입니다. 변수는 데이터를 저장할 수 있는 공간을 의미하며, 이는 나중에 사용될 때 그 안에 저장된 값을 참조하는 이름으로 불립니다. 간단히 말해, 변수는 데이터의 이름표 역할을 합니다.

### 예제 코드
```python
# 변수 선언 및 할당
name = "Alice"
age = 30
height = 5.7

print(name)   # Alice 출력
print(age)    # 30 출력
print(height) # 5.7 출력
```

## 2. 자료형이란?

자료형(data type)은 변수가 저장할 수 있는 데이터의 종류를 나타냅니다. 파이썬에서는 여러 가지 기본적인 자료형을 제공하며, 이들을 통해 다양한 유형의 데이터를 다룰 수 있습니다.

### 주요 자료형

1. **정수(int)**: 정수 값을 저장하는 자료형입니다.
2. **실수(float)**: 소수점이 있는 숫자를 저장하는 자료형입니다.
3. **문자열(str)**: 텍스트 데이터를 저장하는 자료형입니다.
4. **불리언(bool)**: 참(True) 또는 거짓(False) 값을 저장하는 자료형입니다.

### 예제 코드
```python
# 정수(int)
age = 25

# 실수(float)
height = 5.9

# 문자열(str)
name = "Bob"

# 불리언(bool)
is_student = True

print(type(age))      # <class 'int'>
print(type(height))   # <class 'float'>
print(type(name))     # <class 'str'>
print(type(is_student)) # <class 'bool'>
```

## 3. 변수 선언 및 할당

변수를 선언하고 값을 할당하는 방법은 간단합니다. 변수 이름을 지정한 후 등호(`=`)를 사용하여 값을 할당하면 됩니다.

### 예제 코드
```python
# 정수 할당
num = 10

# 실수 할당
price = 3.99

# 문자열 할당
greeting = "Hello, World!"

# 불리언 할당
is_valid = False

print(num)      # 10 출력
print(price)    # 3.99 출력
print(greeting) # Hello, World! 출력
print(is_valid) # False 출력
```

## 4. 변수 이름 규칙

변수 이름을 지정할 때는 다음과 같은 규칙을 따라야 합니다:

- **영문자**, **숫자**, **언더바(_)**만 사용 가능합니다.
- 숫자로 시작할 수 없습니다.
- 공백은 사용할 수 없습니다.
- 파이썬의 예약어(예: `if`, `else`, `for` 등)는 변수 이름으로 사용할 수 없습니다.

### 예제 코드
```python
# 올바른 변수 이름 예시
valid_name = "Alice"
age_2023 = 30
is_student = True

# 잘못된 변수 이름 예시
1variable = "Invalid" # 숫자로 시작 불가능
invalid-name = "Invalid" # 공백 사용 불가능
if = "Reserved keyword" # 파이썬 예약어 사용 불가능
```

## 5. 변수의 타입 변경

파이썬은 동적타이핑(dynamically typed) 언어로, 변수의 타입을 명시적으로 선언하지 않아도 자동으로 추론합니다. 따라서 변수에 저장된 데이터의 타입은 자유롭게 변경할 수 있습니다.

### 예제 코드
```python
# 초기 타입: 정수(int)
num = 10

print(type(num)) # <class 'int'>

# 타입 변경: 실수(float)
num = 3.14

print(type(num)) # <class 'float'>

# 타입 변경: 문자열(str)
num = "Pi"

print(type(num)) # <class 'str'>
```

## 6. 여러 변수 선언 및 할당

한 번에 여러 개의 변수를 동시에 선언하고 할당할 수도 있습니다.

### 예제 코드
```python
# 여러 변수 선언 및 할당
name, age, height = "Charlie", 35, 6.1

print(name)   # Charlie 출력
print(age)    # 35 출력
print(height) # 6.1 출력

# 같은 값으로 여러 개의 변수 할당
a = b = c = 0

print(a, b, c) # 0 0 0 출력
```

## 7. 주석(Comments)

코드를 작성할 때는 이해하기 쉽게 주석을 추가하는 것이 좋습니다. 파이썬에서 주석은 `#` 기호로 시작합니다.

### 예제 코드
```python
# 이 코드는 사용자 이름과 나이를 출력합니다.
name = "David"
age = 40

print("Name:", name) # Name: David 출력
print("Age:", age)   # Age: 40 출력
```

## 정리

이번 강의에서는 파이썬에서 변수와 자료형에 대해 배웠습니다. 변수는 데이터를 저장하는 공간을 의미하며, 자료형은 그 데이터의 종류를 나타냅니다. 정수, 실수, 문자열, 불리언 등의 기본적인 자료형을 이해하고 사용할 수 있도록 했습니다. 또한 변수 선언 및 할당 방법과 규칙, 타입 변경, 여러 변수 선언, 주석 등에 대해 살펴보았습니다.

다음 강의에서는 조건문과 반복문 등 제어 구조에 대해 알아보도록 하겠습니다. 파이썬을 이용한 프로그래밍 세계를 더 깊게 이해해 나가세요!

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
