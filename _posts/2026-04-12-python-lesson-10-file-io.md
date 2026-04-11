---
layout: post
title: "파이썬 파일 입출력"
date: 2026-04-12 05:54:04
categories: [파이썬 강의]
---

# 파이썬 파일 입출력 10강: 초보자를 위한 단계별 가이드

안녕하세요! 이번에는 파이썬의 파일 입출력에 대해 자세히 알려드리겠습니다. 이 강의를 통해 여러분은 파일을 읽고 쓸 수 있는 기본적인 방법부터 고급 기능까지 배울 수 있습니다.

## 1. 파일 열기와 닫기

파일 입출력을 하기 위해서는 먼저 파일을 열어야 합니다. 파이썬에서는 `open()` 함수를 사용하여 파일을 엽니다. 예제 코드로 살펴보겠습니다.

```python
# 파일 열기
file = open('example.txt', 'r')
print(file)

# 파일 닫기
file.close()
```

위 코드에서 `'example.txt'`는 파일의 이름이며, `'r'`은 파일을 읽기 모드로 열겠다는 의미입니다. 파일 사용이 끝나면 반드시 `close()` 함수를 호출하여 파일을 닫아줍니다.

## 2. `with` 문을 사용한 안전한 파일 관리

파일을 항상 닫지 않는 것은 문제가 될 수 있습니다. 이를 방지하기 위해 `with` 문을 사용할 수 있습니다. 이 문법은 자동으로 파일을 열고, 블록이 종료되면 파일을 자동으로 닫아줍니다.

```python
# with문을 사용한 파일 열기와 닫기
with open('example.txt', 'r') as file:
    print(file)
```

위 코드에서 `with` 문 내부의 코드가 실행된 후, 자동으로 파일이 닫히게 됩니다. 이는 예외 상황에서도 파일을 제대로 닫아주는 역할도 합니다.

## 3. 파일 읽기

파일을 열었으면 이제 파일을 읽어보겠습니다. 가장 기본적인 방법은 `read()` 메서드를 사용하는 것입니다.

```python
# 파일 전체 내용 읽기
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
```

위 코드에서는 파일의 모든 내용을 한 번에 읽어옵니다. 만약 파일이 매우 크다면 메모리를 많이 사용할 수 있으므로, 작은 단위로 읽는 방법도 있습니다.

```python
# 파일을 줄 단위로 읽기
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())
```

위 코드에서는 파일의 각 줄을 한 번에 읽어옵니다. `strip()` 메서드를 사용하여 줄 끝의 줄 바꿈 문자를 제거합니다.

## 4. 파일 쓰기

이제는 파일에 내용을 써보겠습니다. 쓰기는 `'w'` 모드를 사용하여 파일을 열면 됩니다.

```python
# 파일 쓰기
with open('example_write.txt', 'w') as file:
    file.write('Hello, World!\n')
    file.write('This is a new line.')
```

위 코드에서는 `write()` 메서드를 사용하여 문자열을 파일에 씁니다. 여러 줄을 쓰고 싶다면 `\n`을 사용하여 줄 바꿈을 할 수 있습니다.

## 5. 리스트로 파일 읽기와 쓰기

파일의 내용을 리스트로 다루는 것도 편리합니다. `readlines()` 메서드를 사용하면 파일의 모든 줄을 리스트로 반환할 수 있습니다.

```python
# 파일을 리스트로 읽기
with open('example.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())
```

반대로, 리스트에 있는 내용을 파일에 쓸 때는 `writelines()` 메서드를 사용할 수 있습니다.

```python
# 리스트로 파일 쓰기
lines = ['Hello, World!\n', 'This is a new line.']
with open('example_write.txt', 'w') as file:
    file.writelines(lines)
```

위 코드에서는 `writelines()` 메서드를 사용하여 리스트의 내용을 파일에 한 번에 씁니다.

## 6. 추가 모드로 파일 열기

파일에 새로운 내용을 추가하고 싶다면 `'a'` 모드를 사용하면 됩니다.

```python
# 파일에 내용 추가하기
with open('example_write.txt', 'a') as file:
    file.write('\nThis is an additional line.')
```

위 코드에서는 `append` 모드로 파일을 열어 새로운 줄을 추가합니다. 원래의 파일 내용은 유지되고, 새로운 내용이 뒤에 추가됩니다.

## 7. 바이너리 파일 다루기

텍스트 파일 외에도 바이너리 파일도 처리할 수 있습니다. 예를 들어 이미지 파일 등을 다룰 때 유용합니다.

```python
# 바이너리 파일 읽기
with open('example.jpg', 'rb') as file:
    content = file.read()
    print(content)
```

위 코드에서는 `'rb'` 모드로 파일을 열어 바이너리 데이터를 읽습니다. `read()` 메서드는 바이너리 데이터도 문자열처럼 처리할 수 있습니다.

```python
# 바이너리 파일 쓰기
with open('example_copy.jpg', 'wb') as file:
    file.write(content)
```

위 코드에서는 `'wb'` 모드로 파일을 열어 바이너리 데이터를 씁니다. 원래의 이미지 파일을 복사하는 예시입니다.

## 8. CSV 파일 다루기

CSV(Comma-Separated Values)는 텍스트 기반의 표준 파일 형식으로, 데이터 분석과 같은 작업에 자주 사용됩니다. 파이썬에서는 `csv` 모듈을 통해 CSV 파일을 쉽게 다룰 수 있습니다.

```python
# CSV 파일 읽기
import csv

with open('example.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

위 코드에서는 `csv.reader()` 함수를 사용하여 CSV 파일을 읽습니다. 각 행은 리스트 형태로 반환됩니다.

```python
# CSV 파일 쓰기
import csv

data = [
    ['Name', 'Age', 'City'],
    ['Alice', 30, 'New York'],
    ['Bob', 25, 'Los Angeles']
]

with open('example_write.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for row in data:
        writer.writerow(row)
```

위 코드에서는 `csv.writer()` 함수를 사용하여 CSV 파일을 씁니다. `writerow()` 메서드로 각 행을 추가할 수 있습니다.

## 9. JSON 파일 다루기

JSON(JavaScript Object Notation)은 데이터 저장과 교환에 널리 사용되는 형식입니다. 파이썬에서는 `json` 모듈을 통해 JSON 파일을 쉽게 다룰 수 있습니다.

```python
# JSON 파일 읽기
import json

with open('example.json', 'r') as file:
    data = json.load(file)
    print(data)
```

위 코드에서는 `json.load()` 함수를 사용하여 JSON 파일을 읽습니다. 데이터는 파이썬 딕셔너리나 리스트 형태로 반환됩니다.

```python
# JSON 파일 쓰기
import json

data = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}

with open('example_write.json', 'w') as file:
    json.dump(data, file)
```

위 코드에서는 `json.dump()` 함수를 사용하여 JSON 파일을 씁니다. 파이썬의 딕셔너리나 리스트를 JSON 형식으로 저장할 수 있습니다.

## 10. 예외 처리

파일 입출력 작업은 종종 오류가 발생할 수 있습니다. 예를 들어, 파일이 존재하지 않거나 권한 문제 등이 있을 수 있습니다. 이를 대비하여 예외 처리를 해주는 것이 좋습니다.

```python
# 예외 처리로 파일 열기
try:
    with open('nonexistent.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")
```

위 코드에서는 `try-except` 문을 사용하여 파일이 존재하지 않을 때 에러 메시지를 출력합니다. 다양한 예외 타입에 대해 핸들링할 수도 있습니다.

## 마무리

이렇게 파이썬에서 파일 입출력을 다루는 기본적인 방법들을 알아보았습니다. 실습해 보면서 익숙해지는 것이 좋겠습니다. 추가적으로 궁금한 점이 있으면 언제든지 질문해 주세요!

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
