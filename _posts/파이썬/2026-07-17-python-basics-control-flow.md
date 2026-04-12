---
layout: single
title: "하는 엘소 : 입력치세요 (종머울북호야물할)"
date: 2026-07-17 14:44:18
categories: [파이썬]
---

🎉 **4강: 하는 엘소 - 입력치세요 (종머울북호야물할)** 🔥

 안녕하세요, 모두들! 오늘은 파이썬 프로그래밍의 강력한 친구인 `입력`에 대해 배우게 됩니다. 💪 혹시 아직도 "입력" 이라는 단어를 못 알아먹는 사람 있나요? 😂 걱정하지 마세요! 나는 당신에게 "입력을 이해하라!" 를 보여드리겠습니다.

## 4강 - 입력을 시작합니다!

이제까지 우리가 배운 내용으로부터, **함수**와 **리스트**, **딕셔너리**를 사용하여 데이터를 처리하는 방법에 대해 배웠습니다. 하지만, 프로그램은 단지 데이터를 처리하기만 하는 것이 아닙니다! 😎 실제로, 사용자에게 정보를 입력 받거나, 파일에서 데이터를 읽어오는 경우도 있습니다.

이제부터 **입력**이라는 개념을 배워보겠습니다!

## 입력이란?

입력을 생각할 때, 사용자가 키보드로 누르는 키에 따라 다른 종류의 출력이 나온다고 생각하시면 됩니다. 예를 들어, "Hello" 라는 글자를 입력하면, 프로그램은 해당 문자를 출력합니다.

이러한 **입력**과 **출력**을 이해하기 위해서는 **스트림(stream)** 이라는 개념을 알아야 합니다!

### 스트림(Stream) چیست?

스트림은 데이터가 순서대로 흐르는 것이라고 생각하시면 됩니다. 예를 들어, 키보드로 입력 받은 문자는 스트림에 먼저 들어가게 되고, 프로그램이 해당 스트림에서 문자를 읽어와서 출력합니다.

스트림에는 여러 종류가 있습니다!

#### 1. **키보드 스트림**

*   사용자가 키보드를 눌러서 입력한 값을 받아오는 스트림입니다.
*   `sys.stdin` 모듈을 사용하여 생성할 수 있습니다.

```python
import sys

stream = sys.stdin
```

#### 2. **파일 스트림**

*   파일에서 데이터를 읽어오는 스트림입니다.
*   `open()` 함수를 사용하여 생성할 수 있습니다.

```python
with open("example.txt", "r") as file:
    stream = file
```

#### 3. **네트워크 스트림**

*   네트워크에서 데이터를 읽어오는 스트림입니다.
*   `socket` 모듈을 사용하여 생성할 수 있습니다.

```python
import socket

stream = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
stream.connect(("www.example.com", 80))
```

### 입력받기

입력을 받는 방법은 여러 가지가 있습니다!

#### 1. **`input()`** 함수

*   사용자가 키보드로 입력한 값을 받아옵니다.
*   `input()` 함수를 사용하여 호출할 수 있습니다.

```python
user_input = input("Enter your name: ")
print(user_input)
```

#### 2. **`readline()`** 메서드

*   파일에서 한 줄씩 읽어옵니다.
*   `stream.readline()` 메서드를 사용하여 호출할 수 있습니다.

```python
with open("example.txt", "r") as file:
    stream = file
    user_input = stream.readline()
print(user_input)
```

#### 3. **`readlines()`** 메서드

*   파일에서 모든 라인 읽어옵니다.
*   `stream.readlines()` 메서드를 사용하여 호출할 수 있습니다.

```python
with open("example.txt", "r") as file:
    stream = file
    user_input = stream.readlines()
print(user_input)
```

## 실습해 보세요!

실습을 통해 배우는 것이 가장 효과적입니다! 😎

*   **입력을 받고, 출력** 하세요!
*   **파일에서 데이터를 읽어와서 출력**하세요!
*   **네트워크에서 데이터를 읽어와서 출력**하세요!

## 마무리

이제까지 우리는 **입력을 이해**하고, 다양한 방법으로 입력을 받는 법에 대해 배웠습니다! 😎

이전 강의에서 배운 것들을 이번 강의 내용과 조합하여, 프로그램을 작성해 보세요!

💪 실습을 통해 배우는 것이 가장 효과적입니다! 🚀

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
