---
layout: post
title: "파이썬 기초: 반복문"
date: 2026-04-12 05:54:04
categories: [파이썬 강의]
---

# 5강: 파이썬 기초 - 반복문

안녕하세요! 오늘은 파이썬의 기초 중 하나인 '반복문'에 대해 알아보도록 하겠습니다. 반복문을 이용하면 코드를 여러 번 실행할 수 있어 프로그래밍에서 매우 중요한 역할을 합니다.

## 1. 반복문이란?

반복문은 특정한 작업을 계속해서 반복적으로 수행하는 것을 말합니다. 파이썬에서는 `for` 루프와 `while` 루프这两种 주요 반복문을 사용할 수 있습니다.

## 2. for 루프

`for` 루프는 시퀀스(리스트, 튜플, 문자열 등)를 순회하며 각 요소에 대해 작업을 수행합니다.

### 예제 코드
```python
fruits = ['사과', '바나나', '체리']

for fruit in fruits:
    print(fruit)
```

실행 결과는 다음과 같습니다.
```
사과
바나나
체리
```

## 3. while 루프

`while` 루프는 주어진 조건이 참일 때 계속해서 코드를 실행합니다.

### 예제 코드
```python
count = 0
while count < 5:
    print(count)
    count += 1
```

실행 결과는 다음과 같습니다.
```
0
1
2
3
4
```

## 4. break 문

`break` 문은 반복문을 즉시 종료합니다.

### 예제 코드
```python
fruits = ['사과', '바나나', '체리', '포도']

for fruit in fruits:
    if fruit == '체리':
        break
    print(fruit)
```

실행 결과는 다음과 같습니다.
```
사과
바나나
```

## 5. continue 문

`continue` 문은 현재 반복을 건너뛰고 다음 반복으로 넘어갑니다.

### 예제 코드
```python
for number in range(1, 6):
    if number % 2 == 0:
        continue
    print(number)
```

실행 결과는 다음과 같습니다.
```
1
3
5
```

## 6. 중첩된 반복문

반복문을 여러 개 중첩해서 사용할 수도 있습니다.

### 예제 코드
```python
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} * {j} = {i*j}")
```

실행 결과는 다음과 같습니다.
```
1 * 1 = 1
1 * 2 = 2
1 * 3 = 3
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
3 * 1 = 3
3 * 2 = 6
3 * 3 = 9
```

## 7. 리스트 컴프리헨션

리스트 컴프리헨션은 간결하게 리스트를 생성할 수 있는 방법입니다.

### 예제 코드
```python
squares = [x**2 for x in range(1, 6)]
print(squares)
```

실행 결과는 다음과 같습니다.
```
[1, 4, 9, 16, 25]
```

## 8. 실습

이제 직접 코드를 작성해보세요!

1. 1부터 10까지의 숫자 중 짝수만 출력하세요.
    
    ```python
    for number in range(1, 11):
        if number % 2 == 0:
            print(number)
    ```
    
2. 이름 리스트에서 '나라'를 포함하는 이름만 출력하세요.

    ```python
    names = ['민수', '나라', '정우', '나라산']
    for name in names:
        if '나라' in name:
            print(name)
    ```

3. 2부터 10까지의 숫자 중 소수를 출력하세요.

    ```python
    primes = []
    for num in range(2, 11):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    print(primes)
    ```

## 결론

이번에는 파이썬의 반복문에 대해 알아보았습니다. `for` 루프와 `while` 루프를 사용해 코드를 여러 번 실행하고, `break`와 `continue` 문을 통해 반복문의 흐름을 제어할 수 있습니다. 또한 리스트 컴프리헨션은 간결한 리스트 생성을 위해 유용합니다.

다음 강에서는 함수에 대해 알아보도록 하겠습니다! 많은 도움이 되었기를 바랍니다.

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
