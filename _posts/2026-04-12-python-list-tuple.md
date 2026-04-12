---
layout: post
title: "리스트(List)와 튜플(Tuple)"
date: 2026-04-12 13:51:38
categories: [파이썬 강의]
---

**4강: 리스트(List)와 튜플(Tuple)**

안녕하세요, 여러분! 파이썬 세계의 아름다움을 탐험하는 여러분 환영합니다! 🚀 이번 강의에서는 두 가지 핵심 자료형, `리스트` 와 `튜플` 을 소개할 것입니다. 이들은 함께 작업하고 데이터를 다루는 데 도움이 될 것입니다.

### 리스트(List)

**리스트란 무엇입니까?**
리스트는 파이썬에서 가장 일반적으로 사용되는 자료형입니다. 리스트는 여러 개의 값을 포함하며, 값을 추가, 제거, 수정할 수 있습니다. 리스트는 대괄호 `[]` 안에 값들을 입력하여 정의합니다.

```markdown
# 예제 1: 리스트 생성
my_list = [1, 2, 3, 4, 5]
print(my_list)  # [1, 2, 3, 4, 5]
```

**리스트 특징**
리스트는 다음과 같은 특징을 가지고 있습니다.

*   **인덱싱**: 리스트의 각 요소는 인덱스(0부터 시작)로 참조할 수 있습니다.
*   **슬라이싱**: 리스트의 일부를 슬라이스(대괄호 안에 colon과 index)를 사용하여 추출할 수 있습니다.
*   **배열 연산**: 리스트의 모든 요소를 반복적으로 처리하기 위해 `for` 루프를 사용할 수 있습니다.

```markdown
# 예제 2: 인덱싱, 슬라이싱, 배열 연산
my_list = [1, 2, 3, 4, 5]

# 인덱싱
print(my_list[0])  # 1

# 슬라이싱
print(my_list[:3])  # [1, 2, 3]

# 반복
for item in my_list:
    print(item)  # 1, 2, 3, 4, 5
```

**리스트 메서드**
리스트는 다음과 같은 메서드를 제공합니다.

*   `append()`: 리스트에 요소를 추가합니다.
*   `extend()`: 리스트에 여러 요소를 추가합니다.
*   `insert()`: 특정 위치에 요소를 삽입합니다.
*   `remove()`: 지정된 요소를 제거합니다.
*   `sort()`: 리스트를 정렬합니다.

```markdown
# 예제 3: 메서드 사용
my_list = [1, 2, 3]

# append()
my_list.append(4)
print(my_list)  # [1, 2, 3, 4]

# extend()
my_list.extend([5, 6])
print(my_list)  # [1, 2, 3, 4, 5, 6]
```

### 튜플(Tuple)

**튜플란 무엇입니까?**
튜플은 불변의 자료형으로 여러 개의 값을 포함합니다. 튜플은 값들을 괄호 `()` 안에 입력하여 정의합니다.

```markdown
# 예제 4: 튜플 생성
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)  # (1, 2, 3, 4, 5)
```

**튜플 특징**
튜플은 다음과 같은 특징을 가지고 있습니다.

*   **불변**: 튜플의 내용을 수정할 수 없습니다.
*   **인덱싱**: 튜플의 각 요소는 인덱스(0부터 시작)로 참조할 수 있습니다.
*   **슬라이싱**: 튜플의 일부를 슬라이스(대괄호 안에 colon과 index)를 사용하여 추출할 수 있습니다.

```markdown
# 예제 5: 인덱싱, 슬라이싱
my_tuple = (1, 2, 3, 4, 5)

# 인덱싱
print(my_tuple[0])  # 1

# 슬라이싱
print(my_tuple[:3])  # (1, 2, 3)
```

**튜플 메서드**
튜플은 다음과 같은 메서드를 제공합니다.

*   `index()`: 튜플에서 지정된 요소를 찾습니다.
*   `count()`: 튜플에서 지정된 요소의 카운트를 반환합니다.

```markdown
# 예제 6: 메서드 사용
my_tuple = (1, 2, 3)

# index()
print(my_tuple.index(2))  # 1

# count()
print(my_tuple.count(1))  # 1
```

### 실무 활용

리스트와 튜플은 파이썬에서 다양한 상황에 사용할 수 있습니다. 예를 들어, 데이터를 처리하거나 저장할 때 리스트를 사용할 수 있으며, 데이터의 불변성을 유지해야 하는 경우에는 튜플을 사용할 수 있습니다.

```markdown
# 예제 7: 실무 활용
student_list = [
    {"name": "John", "age": 20},
    {"name": "Alice", "age": 22}
]

print(student_list)  # [{"name": "John", "age": 20}, {"name": "Alice", "age": 22}]

# 튜플을 사용하여 학생의 정보를 불변으로 유지합니다.
student_tuple = (
    ("John", 20),
    ("Alice", 22)
)

print(student_tuple)  # (("John", 20), ("Alice", 22))
```

### 초보자 폭풍 질문!

리스트와 튜플에 대한 궁금증이 많은가요? 이 곳에서 물어볼 수 있습니다. 💬

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
