---
layout: post
title: "파이썬 함수와 모듈"
date: 2026-04-12 05:54:04
categories: [파이썬 강의]
---

# 6강: 파이썬 함수와 모듈

안녕하세요! 이번 강의에서는 파이썬에서 매우 중요한 두 가지 개념인 '함수'와 '모듈'에 대해 자세히 알아보겠습니다. 함수는 코드를 재사용하고 조직하는 데 도움이 되며, 모듈은 함수와 변수를 그룹화하여 프로그램을 더욱 구조적으로 만들어 줍니다.

## 1. 함수 소개

함수는 특정 작업을 수행하는 코드의 묶음입니다. 이를 통해 코드의 중복을 줄이고 재사용성을 높일 수 있습니다.

### 기본 문법
```python
def 함수명(매개변수):
    # 함수 본문
    return 반환값
```

#### 예제: 간단한 더하기 함수
```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # 출력: 8
```

## 2. 매개변수와 인자

함수를 정의할 때 사용하는 변수를 **매개변수**라고 합니다. 함수를 호출할 때 전달하는 값은 **인자**라고 합니다.

#### 예제: 이름을 인사하는 함수
```python
def greet(name):
    return f"Hello, {name}!"

message = greet("Alice")
print(message)  # 출력: Hello, Alice!
```

## 3. 반환값

함수는 작업이 완료되면 결과를 **반환**할 수 있습니다. `return` 키워드를 사용하여 값을 반환합니다.

#### 예제: 정수의 제곱을 계산하는 함수
```python
def square(number):
    return number * number

result = square(4)
print(result)  # 출력: 16
```

## 4. 모듈 소개

모듈은 관련된 변수와 함수를 그룹화한 것입니다. 다른 파일에서 가져와서 사용할 수 있습니다.

### 기본 문법
```python
# mymodule.py
def greet():
    return "Hello from module!"

# main.py
import mymodule

print(mymodule.greet())  # 출력: Hello from module!
```

## 5. 내장 모듈 활용

파이썬에는 다양한 내장 모듈이 제공되어 있습니다. 예를 들어, `math` 모듈은 수학 연산을 위한 함수와 상수를 포함하고 있습니다.

#### 예제: math 모듈 사용
```python
import math

# 원의 둘레 계산
radius = 5
circumference = 2 * math.pi * radius
print(circumference)  # 출력: 31.41592653589793
```

## 6. 모듈 설치

외부 모듈을 사용하려면 `pip`를 통해 설치할 수 있습니다.

#### 예제: requests 모듈 설치와 사용
```bash
# 터미널에서 실행
pip install requests
```
```python
import requests

response = requests.get("https://api.github.com")
print(response.status_code)  # 출력: 200
```

## 정리

- **함수**는 재사용 가능한 코드의 묶음입니다.
- **매개변수**와 **인자**를 사용하여 함수에 데이터를 전달합니다.
- **반환값**은 함수가 완료된 후 반환할 수 있습니다.
- **모듈**은 관련된 변수와 함수를 그룹화한 것입니다.
- 다양한 내장 모듈과 외부 모듈을 활용하여 프로그램을 더욱 효율적으로 작성할 수 있습니다.

이제 여러분이 파이썬에서 함수와 모듈을 효과적으로 사용할 수 있을 거예요! 다음 강의에서는 클래스와 객체 지향 프로그래밍에 대해 알아보겠습니다.

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
