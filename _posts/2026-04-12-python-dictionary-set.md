---
layout: post
title: "딕셔너리(Dictionary)와 집합(Set)"
date: 2026-04-12 13:51:38
categories: [파이썬 강의]
---

**5강: 딕셔너리(Dictionary)와 집합(Set)**

안녕하세요, 여러분! 오늘은 파이썬의 두 가지 아주 중요한 자료형을 배울 것입니다. 그 중 첫 번째는 dictionary입니다. dictionary는 말 그대로 단어장 같은거에요. 키-값 쌍으로 구성된 데이터를 저장하고 조회할 수 있습니다.

**dictionary란?**

dictionary는 파이썬에서 사용하는 자료형 중 하나로, key-value 쌍을 저장하는 데 사용됩니다. 예를 들어, 이름과 나이를 dictionary의 key와 value로 저장한 후에 필요시에는 이름(key)으로 나이(value)를 바로 조회할 수 있습니다.

**dictionary 만들기**

dictionary는 `{}`으로 선언하며, `key : value` 형식으로 요소를 추가합니다.

```python
# 이름과 나이를 dictionary에 추가합니다.
people = {
    '홍길동' : 30,
    '김유신' : 35,
    '강감찬' : 40
}
```

dictionary의 key는 유일해야 하며, value는 중복될 수 있습니다.

**dictionary 요소 접근**

dictionary 요소를 접근할 때는 key를 사용합니다. 단순히 dictionary의 이름 뒤에 `[]`와 함께 key를 작성하면 됩니다.

```python
# '홍길동'의 나이를 출력합니다.
print(people['홍길동'])  # 30
```

dictionary의 key가 없을 때 오류가 나지 않도록 하려면 `.get()` 메서드를 사용할 수 있습니다. 이때, 두 번째 인수로 default value를 설정하여 key가 없는 경우 default value를 반환합니다.

```python
# '강감찬'이 없을 때 default value 0을 출력합니다.
print(people.get('강감찬', 0))  # 40
```

dictionary의 요소를 삭제할 때는 `del` 키워드를 사용하여 key를 지웁니다.

```python
# '김유신' 요소를 삭제합니다.
del people['김유신']
```

**집합(Set)**

집합(set)은 파이썬에서 사용하는 자료형 중 하나로, 순서가 없는 유일한 요소의 모음입니다. 집합은 `{}`으로 선언하며, 요소는 `,` 또는 `()`으로 구분합니다.

```python
# 정수 1, 2, 3, 4를 집합에 추가합니다.
numbers = {1, 2, 3, 4}
```

집합의 특징은 순서가 없고, 중복된 요소가 없습니다. 따라서, `1`을 두 번 더 추가하면 변경되지 않습니다.

```python
# 정수 1을 다시 집합에 추가합니다.
numbers.add(1)
print(numbers)  # {1, 2, 3, 4}
```

집합의 요소를 삭제할 때는 `remove()` 메서드를 사용하여 요소를 지웁니다. 만약, 삭제하려는 요소가 없을 경우 오류가 발생합니다.

```python
# 정수 5를 집합에서 삭제합니다.
numbers.remove(5)
print(numbers)  # {1, 2, 3, 4}
```

집합의 교집합, 합집합, 차집합을 구할 때는 `&`, `|`, `-` 연산자를 사용할 수 있습니다.

```python
# 정수 1, 2, 3, 5를 다른 집합에 추가합니다.
numbers2 = {1, 2, 3, 5}

# 교집합을 구합니다.
print(numbers & numbers2)  # {1, 2, 3}
# 합집합을 구합니다.
print(numbers | numbers2)  # {1, 2, 3, 4, 5}
# 차집합을 구합니다.
print(numbers - numbers2)  # {4}
```

**정리**

dictionary와 집합은 파이썬에서 사용하는 자료형 중 아주 중요한 두 가지입니다. dictionary는 key-value 쌍을 저장하고 조회할 수 있는 자료형으로, 집합은 순서가 없는 유일한 요소의 모음입니다. 이 둘을 잘 활용하면 코딩 문제를 해결하거나 데이터를 처리할 때 큰 도움이 될 것입니다.

💡 초보자 폭풍 질문!

* dictionary는 key-value 쌍이여야 하나, 반대도 가능한가요?
	+ 안됩니다. dictionary의 key는 유일해야 하며, value는 중복될 수 있습니다.
* 집합은 순서가 없으므로, 정렬이 필요할 때 사용하나요?
	+ 아니에요. 집합은 순서가 없습니다. 데이터를 정렬하고 싶을 때는 sorted() 함수를 사용하세요.

🚨 실무주의보

* dictionary와 집합은 파이썬의 built-in 자료형으로, 자주 사용하는 자료형입니다.
* dictionary와 집합을 잘 활용한다면 코딩 문제를 해결하거나 데이터를 처리할 때 큰 도움이 될 것입니다.

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
