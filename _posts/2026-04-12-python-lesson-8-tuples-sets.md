---
layout: post
title: "파이썬 기초: 튜플(tuple)과 집합(set)"
date: 2026-04-12 05:54:04
categories: [파이썬 강의]
---

# 파이썬 기초: 튜플(tuple)과 집합(set)

안녕하세요! 이번 강좌에서는 파이썬의 두 가지 중요한 자료 구조인 튜플(tuple)과 집합(set)에 대해 알아보겠습니다. 이들은 리스트와 비슷하지만, 몇 가지 핵심적인 차이점이 있습니다.

## 1. 튜플 (Tuple)

튜플은 데이터를 순서대로 저장하는 시퀀스 자료 구조입니다. 튜플의 주요 특징은 다음과 같습니다:

- **변경 불가능**: 튜플의 요소를 추가, 삭제하거나 변경할 수 없습니다.
- **성능**: 리스트보다 더 빠르게 접근 가능합니다.
- **사용 목적**: 데이터가 변하지 않는 경우에 사용됩니다.

### 1.1 튜플 생성

튜플은 소괄호 `()` 또는 `tuple()` 함수를 사용하여 생성할 수 있습니다.

```python
# 소괄호를 이용한 튜플 생성
my_tuple = (1, 2, 3)
print(my_tuple)  # 출력: (1, 2, 3)

# tuple() 함수를 이용한 튜플 생성
another_tuple = tuple([4, 5, 6])
print(another_tuple)  # 출력: (4, 5, 6)
```

### 1.2 튜플 접근

튜플은 인덱싱과 슬라이싱을 통해 요소에 접근할 수 있습니다.

```python
# 튜플의 첫 번째 요소 접근
print(my_tuple[0])  # 출력: 1

# 튜플의 마지막 요소 접근
print(my_tuple[-1])  # 출력: 3

# 슬라이싱을 사용한 부분 튜플 생성
print(my_tuple[1:3])  # 출력: (2, 3)
```

### 1.3 튜플의 변경 불가능성

튜플은 변경 불가능하므로 요소를 추가하거나 수정할 수 없습니다.

```python
# 튜플에 새로운 요소 추가 시도
my_tuple.append(4)  # 에러 발생: AttributeError: 'tuple' object has no attribute 'append'

# 튜플의 요소 변경 시도
my_tuple[0] = 10     # 에러 발생: TypeError: 'tuple' object does not support item assignment
```

## 2. 집합 (Set)

집합은 중복된 데이터를 허용하지 않는 자료 구조입니다. 주요 특징은 다음과 같습니다:

- **중복 제거**: 집합 내에 같은 값이 여러 번 들어가면 하나만 저장됩니다.
- **순서 없음**: 집합은 요소의 순서를 보장하지 않습니다.
- **집합 연산 지원**: 교집합, 합집합, 차집합 등의 기본적인 수학적 연산을 쉽게 수행할 수 있습니다.

### 2.1 집합 생성

집합은 중괄호 `{}` 또는 `set()` 함수를 사용하여 생성할 수 있습니다.

```python
# 중괄호를 이용한 집합 생성
my_set = {1, 2, 3, 3}
print(my_set)  # 출력: {1, 2, 3}

# set() 함수를 이용한 집합 생성
another_set = set([4, 5, 6, 6])
print(another_set)  # 출력: {4, 5, 6}
```

### 2.2 요소 추가 및 삭제

집합에는 `add()` 메서드로 요소를 추가하고, `remove()` 또는 `discard()` 메서드로 요소를 삭제할 수 있습니다.

```python
# 요소 추가
my_set.add(4)
print(my_set)  # 출력: {1, 2, 3, 4}

# 요소 삭제 (존재하지 않는 요소를 삭제 시도시 에러 발생)
my_set.remove(5)  # KeyError: 5

# 안전한 요소 삭제 (존재하지 않는 요소를 삭제 시도해도 에러 미발생)
my_set.discard(5)
print(my_set)  # 출력: {1, 2, 3, 4}
```

### 2.3 집합 연산

집합에서는 다양한 수학적 연산을 수행할 수 있습니다.

```python
# 합집합
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2
print(union_set)  # 출력: {1, 2, 3, 4, 5}

# 교집합
intersection_set = set1 & set2
print(intersection_set)  # 출력: {3}

# 차집합 (set1에 있지만 set2에는 없는 요소들)
difference_set = set1 - set2
print(difference_set)  # 출력: {1, 2}
```

## 3. 튜플과 집합의 사용 사례

### 3.1 튜플의 활용 예시

- **데이터 보호**: 변경 불가능한 특성으로 데이터를 안전하게 저장하고 전달할 때 유용합니다.
- **함수 반환값**: 여러 개의 값을 동시에 반환할 때 사용됩니다.

```python
def get_user_info():
    name = "Alice"
    age = 30
    return (name, age)

user_info = get_user_info()
print(user_info)  # 출력: ('Alice', 30)
```

### 3.2 집합의 활용 예시

- **중복 제거**: 리스트에서 중복된 요소를 쉽게 제거할 때 사용됩니다.
- **빠른 조회 및 연산**: 고유한 데이터만을 다루는 작업에 유용합니다.

```python
# 중복된 아이디 목록에서 중복 제거
user_ids = [101, 102, 103, 101, 104]
unique_user_ids = set(user_ids)
print(unique_user_ids)  # 출력: {101, 102, 103, 104}

# 두 집합의 교집합 구하기
groupA = {101, 102, 105}
groupB = {102, 103, 106}
common_ids = groupA & groupB
print(common_ids)  # 출력: {102}
```

## 4. 정리

이번 강좌에서는 파이썬의 튜플(tuple)과 집합(set)에 대해 배웠습니다. 튜플은 변경 불가능한 순서된 시퀀스이며, 집합은 중복을 허용하지 않는 고유한 요소들의 모임입니다. 각각의 특성에 따라 적절한 상황에서 사용하면 매우 유용하게 활용할 수 있습니다.

다음 강좌에서는 파이썬의 딕셔너리(dictionary)와 관련된 내용을 다룰 예정입니다! 기대됩니다~

---

이 글은 초보자를 위한 튜플과 집합에 대한 이해를 돕기 위해 작성되었습니다. 문법 오류나 더 나은 설명이 있다면 언제든지 알려주세요!

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
