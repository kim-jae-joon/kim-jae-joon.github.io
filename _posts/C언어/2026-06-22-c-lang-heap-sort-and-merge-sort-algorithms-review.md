---
layout: single
title: "정렬 알고리즘: 힙 정렬 및 mergesort"
date: 2026-06-22 14:20:56
categories: [C언어]
---

😎 안녕하세요, 여러분! 오늘은 29강으로 시작합니다. '정렬 알고리즘: 힙 정렬 및 mergesort'라는 주제로 여러분들의 심장을 뛰게 할 것 같습니다! 🔥

**🚨 실무주의보**

정렬이란? 그저 데이터를 오름차순이나 내림차순으로 정렬하는 것일 뿐이라고 생각하실 수도 있지만, 실제로 정렬은 매우 복잡한 문제입니다. 🤯 정렬 알고리즘의 종류는 수십 가지가 넘고, 각각의 특징과 효율성도 다릅니다.

오늘은 두 가지 대표적인 정렬 알고리즘인 힙 정렬(Hey Sort)와 mergesort에 대해서 알아볼 것입니다. 💡

**힙 정렬(Hey Sort)**

힙 정렬은 1964년에 Robert W. Floyd가 처음으로 제안한 정렬 알고리즘입니다. 이 알고리즘의 이름이 힙과 관련이 있으므로, 먼저 힙이란 무엇인지부터 알아보겠습니다.

**🤔 힙이란?**

힙은 특정한 조건을 만족하는 트리结构입니다. 힙에서는 부모 노드가 자식 노드보다 작은지 확인하여 트리를 구성합니다. 예를 들어, 

```markdown
       4
     /   \
    2     6
   / \   / \
  1   3 5   7
```

이런 형태의 트리가 힙입니다.

**👨‍💻 힙 정렬 알고리즘**

힙 정렬은 다음과 같은 단계를 거칩니다.

1.  데이터를 힙 트리에 삽입합니다.
2.  힙이 비어 있는 경우, 루트 노드가 제일 큰 값인 경우, 그 값을 마지막 위치로 옮깁니다.
3.  자식 노드를 하나씩 비교하여 큰 값을 상위 노드로 옮김으로써, 트리가 다시 힙으로 변환합니다.

```markdown
import heapq

# 힙 정렬 함수
def heap_sort(arr):
    # 힙을 초기화합니다.
    heap = []
    
    # 데이터를 힙에 삽입합니다.
    for num in arr:
        heapq.heappush(heap, num)
        
    # 힙에서 데이터를 하나씩 꺼내어 정렬된 배열로 만듭니다.
    sorted_arr = []
    while heap:
        sorted_arr.append(heapq.heappop(heap))
        
    return sorted_arr

# 예시
arr = [4, 2, 6, 1, 3, 5, 7]
print(heap_sort(arr))  # [1, 2, 3, 4, 5, 6, 7]
```

힙 정렬은 시간 복잡도가 O(n log n)입니다.

**🔥 mergesort**

마지막으로 introduces 할 알고리즘은 mergesort입니다. 이 알고리즘의 이름이 merge와 sort에서 따온 것입니다. 🔍

margesort는 다음과 같은 단계를 거칩니다.

1.  데이터를 2개의 부분집합으로 나누어 재귀적으로 정렬합니다.
2.  두 개의 부분집합을 하나로 합쳐서 정렬된 결과를 얻습니다.

```markdown
import random

# mergesort 함수
def merge_sort(arr):
    # 데이터가 한 개 이하일 경우, 이미 정렬된 것으로 간주합니다.
    if len(arr) <= 1:
        return arr
    
    # 데이터를 절반으로 나누어 재귀적으로 정렬합니다.
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    # 두 개의 부분집합을 하나로 합쳐서 정렬된 결과를 얻습니다.
    return merge(left_half, right_half)

# 병합 함수
def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
    
    # 두 개의 부분집합에서 가장 작은 값을 선택합니다.
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
            
    # 남은 부분집합을 병합합니다.
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1
        
    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1
        
    return merged

# 예시
arr = [random.randint(1, 100) for _ in range(10)]
print(merge_sort(arr))
```

margesort는 시간 복잡도가 O(n log n)입니다.

**🎉 정리**

힙 정렬과 mergesort은 정렬 알고리즘의 대표적인 예입니다. 힙 정렬은 기본적으로 힙 트리를 이용한 알고리즘이며, 데이터를 한 번에 삽입하여 효율적으로 정렬합니다. 반면, mergesort는 재귀적이면서 부분집합을 병합하는 알고리즘입니다.

실제로, 이러한 알고리즘은 각각의 특징과 장단점이 있으므로 상황에 맞게 선택하여 사용해야 합니다. 💡

이러한 내용을 마치며, 정렬 알고리즘이야말로 코딩 세계의 심장인 것 같습니다! 🙌

**💬 초보자 폭풍 질문!**

*   힙 정렬은 언제 사용해야 하나요?
*   mergesort는 왜 재귀적으로 작동하는 걸까요?

그럼, 여러분들의 반응을 기다리겠습니다! 😄

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
