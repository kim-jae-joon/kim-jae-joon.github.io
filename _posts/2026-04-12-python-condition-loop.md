---
layout: post
title: " 条件문과 반복문"
date: 2026-04-12 13:51:38
categories: [파이썬 강의]
---

**6강: CONDITIONS AND LOOPS**

😊 안녕하세요! 파이썬 초보자 여러분! 이번 강의에서는 정말 핵심적인 concept입니다. 조건문과 반복문을 이해한다면, 파이썬을 정말이지 능숙하게 다루실 수 있을 거예요!

**CONDITIONS**

조건문은 "if"라고도 부릅니다. 우리가 흔히 사용하는 "만약 A라면 B가 되라!"라는 의미입니다.

```python
x = 5

if x > 10:
    print("x는 10보다 크다!")
else:
    print("x는 10보다 작거나 같다.")
```

위 코드는 x의 값이 10보다 큰지 작은지에 따라 다르게 출력합니다. "if" 뒤에는 조건문이 오고, ":"를 사용하여 block을 구분합니다.

```python
# if-else 문 예제: age가 19세 이상인지 확인한다.
age = 20

if age >= 19:
    print("성인입니다.")
else:
    print("미성년자입니다.")

# 조건문으로 if를 더 깊게 사용하는 방법: elif, in
fruits = ["사과", "배", "딸기"]

if "사과" in fruits:
    print("사과가 있습니다!")
elif "바나나" in fruits:
    print("바나나가 있습니다!")
else:
    print("해당 과일이 없습니다.")
```

조건문은 여러개를 연결할 수 있고, 조건문 안에 조건문을 넣을 수도 있습니다.

```python
# 조건문과 if-elif-else를 사용하여 중복된 코드를 줄이는 방법
score = 90

if score >= 80:
    grade = "A"
elif score >= 70:
    grade = "B"
elif score >= 60:
    grade = "C"

print(grade)
```

**LOOPS**

반복문은 "while"과 "for"라는 두 가지 방법이 있습니다. "while"은 while loop, "for"는 for each loop라고도 부릅니다.

```python
# while loop 예제: i가 10보다 작을 때까지 더해간다.
i = 0

while i < 10:
    print(i)
    i += 1
```

위 코드는 0부터 9까지의 숫자를 출력합니다. "while"은 계속해서 반복할 조건이 있어야 하고, "for"도 마찬가지입니다.

```python
# for each loop 예제: fruits 리스트에 있는 과일 이름을 모두 출력한다.
fruits = ["사과", "배", "딸기"]

for fruit in fruits:
    print(fruit)
```

위 코드는 fruits 리스트에 있는 모든 과일 이름을 출력합니다. "for"는 반복 변수와 iterable(object, tuple, list)을 사용합니다.

```python
# for each loop 예제: index와 value를 함께 사용하여 dictionary를 순회한다.
person = {"이름": "길동", "나이": 20}

for key, value in person.items():
    print(f"{key}: {value}")
```

위 코드는 dictionary에 있는 모든 키와 값을 출력합니다.

```python
# for each loop 예제: range 함수를 사용하여 숫자를 반복한다.
for i in range(1, 11):
    print(i)
```

위 코드는 1부터 10까지의 숫자를 출력합니다.

**REAL-WORLD EXAMPLES**

조건문과 반복문을 실무에서 사용하는 예제입니다. 이 예제를 보시고, 위에 나온 예제와 어떻게 연결되는지 확인해 보세요!

```python
# 실무 예제 1: 회원 가입 시, 나이를 확인한다.
age = int(input("나이를 입력하세요: "))

if age >= 19:
    print("성인입니다.")
else:
    print("미성년자입니다.")

# 실무 예제 2: 상품 가격을 할인한다. (10% OFF)
price = float(input("가격을 입력하세요: "))

discount = price * 0.1

print(f"할인 가격: {price - discount}")
```

위 코드는 회원 가입 시 나이를 확인하고, 상품 가격을 할인합니다.

```python
# 실무 예제 3: 학생 이름과 점수를 출력한다.
name = input("이름을 입력하세요: ")
score = float(input("점수를 입력하세요: "))

if score >= 80:
    grade = "A"
elif score >= 70:
    grade = "B"
elif score >= 60:
    grade = "C"

print(f"{name}: {grade}")
```

위 코드는 학생 이름과 점수를 출력합니다.

**CONCLUSION**

조건문과 반복문은 파이썬의 기본 문법입니다. 조건문을 사용하여 프로그램을 제어하고, 반복문을 사용하여 반복적인 작업을 자동화할 수 있습니다. 위 예제를 보시고, 실무에서 어떻게 사용하는지 확인해 보세요! 💪💻

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
