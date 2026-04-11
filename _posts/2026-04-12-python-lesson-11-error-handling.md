---
layout: post
title: "파이썬 예외 처리"
date: 2026-04-12 05:54:04
categories: [파이썬 강의]
---

# 11강: 파이썬 예외 처리

안녕하세요! 오늘은 파이썬에서 중요하게 다루는 '예외 처리'라는 주제에 대해 알아보도록 하겠습니다. 이 강의를 통해 여러분은 프로그램에서 발생할 수 있는 다양한 오류들을 어떻게 처리하고, 정상적인 흐름을 유지할 수 있는지를 배워 보게 될 것입니다.

## 1. 예외란 무엇인가요?

예외는 프로그램 실행 중에 비정상적으로 동작하여 프로그램이 종료되는 것을 방지하기 위해 사용하는 메커니즘입니다. 예를 들어, 파일을 열 때 해당 파일이 존재하지 않거나, 숫자를 0으로 나누려고 할 때와 같은 상황에서 발생할 수 있습니다.

## 2. 기본적인 예외 처리 구조

파이썬에서는 `try`, `except`, `else`, `finally` 블록을 사용하여 예외를 처리합니다. 기본적인 구조는 다음과 같습니다:

```python
try:
    # 예외가 발생할 가능성이 있는 코드
    pass
except SomeException as e:
    # 특정 예외가 발생했을 때 실행되는 코드
    print(f"오류 발생: {e}")
else:
    # 예외가 발생하지 않았을 때 실행되는 코드
    print("예외 없이 정상적으로 실행됨")
finally:
    # 무조건 실행되는 코드
    print("무조건 실행")
```

## 3. `try`와 `except` 사용하기

`try` 블록 안에 예외가 발생할 수 있는 코드를 작성하고, `except` 블록에는 그 예외를 처리하는 코드를 작성합니다.

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"오류 발생: {e}")
```

## 4. 여러 예외 처리하기

하나의 `except` 블록에서 여러 가지 예외를 처리할 수도 있습니다:

```python
try:
    file = open("nonexistentfile.txt")
except (FileNotFoundError, IOError) as e:
    print(f"오류 발생: {e}")
```

## 5. 모든 예외를 캡처하기

모든 종류의 예외를 한 곳에서 처리하고자 할 때는 `Exception` 클래스를 사용합니다:

```python
try:
    result = "10" + 20
except Exception as e:
    print(f"오류 발생: {e}")
```

## 6. `else`와 `finally` 블록

- **`else` 블록**: 예외가 발생하지 않았을 때 실행됩니다.
- **`finally` 블록**: 어떤 일이 발생하더라도 무조건적으로 실행됩니다.

```python
try:
    result = 10 / 2
except ZeroDivisionError as e:
    print(f"오류 발생: {e}")
else:
    print("예외 없이 정상적으로 계산됨")
finally:
    print("계산 작업 완료")
```

## 7. 사용자 정의 예외 만들기

필요에 따라 자신만의 예외 클래스를 만들어 사용할 수 있습니다:

```python
class MyCustomError(Exception):
    pass

try:
    raise MyCustomError("사용자 정의 오류 발생!")
except MyCustomError as e:
    print(f"오류 발생: {e}")
```

## 8. 실전 예제: 파일 읽기

예외 처리를 사용하여 파일을 안전하게 읽는 방법을 알아보겠습니다:

```python
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("파일이 존재하지 않습니다.")
    except IOError:
        print("파일 읽기 오류 발생.")
    else:
        print("파일을 성공적으로 읽었습니다.")

read_file("example.txt")
```

## 9. 요약

오늘은 파이썬에서 예외 처리에 대해 배웠습니다. `try`, `except`, `else`, `finally` 블록을 사용하여 프로그램에서 발생할 수 있는 다양한 오류를 안전하게 처리하고, 정상적인 흐름을 유지할 수 있습니다. 또한, 사용자 정의 예외 클래스를 만들어 좀 더 세밀한 오류 관리를 할 수도 있습니다.

다음 강좌에서는 파이썬에서의 모듈과 패키지에 대해 알아보도록 하겠습니다. 준비되었나요?

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
