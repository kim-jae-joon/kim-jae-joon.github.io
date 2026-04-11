---
layout: post
title: "파이썬 기초: 사전(dict)"
date: 2026-04-12 05:54:04
categories: [파이썬 강의]
---

# 9강: 파이썬 기초 - 사전(dict)

안녕하세요! 이번 강의에서는 Python에서 매우 중요한 데이터 타입인 '사전'에 대해 자세히 알아보겠습니다. 사전은 다른 모든 데이터 구조와 함께 기본적인 프로그래밍 빌딩 블록 중 하나입니다.

## 1. 사전이란?

사전은 키-값 쌍(key-value pair)의 집합입니다. 이 말은, 각각의 '키'는 고유하고, 그에 해당하는 '값'을 저장합니다. 이를 통해 데이터를 효율적으로 검색하고 관리할 수 있습니다.

## 2. 사전 생성

사전은 중괄호 `{}` 안에 키-값 쌍을 작성해 만들고, 각 키와 값 사이에는 콜론 `:`을 사용합니다.

### 예제 코드
```python
# 빈 사전 생성
my_dict = {}

# 이미 값이 있는 사전 생성
person_info = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
```

## 3. 사전에 요소 추가

사전에 새로운 키-값 쌍을 추가하거나 기존의 값을 변경하려면, 대괄호 `[]` 안에 키를 넣고 값을 할당합니다.

### 예제 코드
```python
# 새 데이터 추가
person_info["job"] = "Engineer"

# 기존 데이터 수정
person_info["age"] = 31

print(person_info)
```

## 4. 사전에서 요소 접근

키를 사용하여 사전 내의 값을 얻을 수 있습니다. 만약 키가 존재하지 않으면 KeyError가 발생하므로, 안전하게 접근하기 위해서는 `get()` 메서드를 사용할 수 있습니다.

### 예제 코드
```python
# 키로 값 얻기
print(person_info["name"])  # 출력: Alice

# get() 메서드를 사용하여 안전하게 접근
print(person_info.get("age"))   # 출력: 31
print(person_info.get("height", "미안합니다, 이 키는 없습니다."))  # 출력: 미안합니다, 이 키는 없습니다.
```

## 5. 사전에서 요소 삭제

`del` 문을 사용하거나 `pop()` 메서드를 이용하여 사전 내의 특정 키-값 쌍을 제거할 수 있습니다.

### 예제 코드
```python
# del을 사용한 삭제
del person_info["job"]

# pop() 메서드를 사용한 삭제
age = person_info.pop("age")
print(age)  # 출력: 31

print(person_info)
```

## 6. 사전의 다양한 작업

사전은 여러 유용한 메서드와 속성을 제공합니다.

### 예제 코드
```python
# 모든 키 가져오기
keys = person_info.keys()
print(keys)  # 출력: dict_keys(['name', 'city'])

# 모든 값 가져오기
values = person_info.values()
print(values)  # 출력: dict_values(['Alice', 'New York'])

# 모든 키-값 쌍 가져오기
items = person_info.items()
print(items)  # 출력: dict_items([('name', 'Alice'), ('city', 'New York')])
```

## 7. 사전의 순회

사전을 순회할 때는 `for` 루프를 사용하며, 키, 값, 또는 키-값 쌍을 순회할 수 있습니다.

### 예제 코드
```python
# 키로 순회
for key in person_info:
    print(key)

# 값으로 순회
for value in person_info.values():
    print(value)

# 키-값 쌍으로 순회
for key, value in person_info.items():
    print(f"{key}: {value}")
```

## 8. 사전의 복사

사전을 복사하려면 `copy()` 메서드를 사용합니다.

### 예제 코드
```python
# 사전 복사
original_dict = {"a": 1, "b": 2}
copied_dict = original_dict.copy()

print(copied_dict)  # 출력: {'a': 1, 'b': 2}
```

## 9. 결론

이제까지 '사전'에 대해 배워봤습니다. 사전은 키-값 쌍을 저장하여 데이터를 효율적으로 관리할 수 있는 강력한 도구입니다. 앞으로의 프로젝트에서 다양한 상황에서 이 구조를 활용해보세요.

만약 어떤 부분이 이해가 가지 않거나 추가적인 질문이 있으시다면 언제든지 문의해주세요!

---

이 글을 통해 사전에 대한 기본 개념과 사용 방법을 익히셨기를 바랍니다. 다음 강의에서는 더 복잡한 데이터 구조와 프로그래밍 패턴을 다루겠습니다!

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
