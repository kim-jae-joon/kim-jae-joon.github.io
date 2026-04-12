---
layout: single
title: "정렬 알고리즘: 퀵 정렬, 계수 정렬"
date: 2026-06-26 14:20:24
categories: [C언어]
---

**25강: 정렬 알고리즘 - 퀵 정렬, 계수 정렬**

안녕하세요! 오늘은 여러분들과 함께 정렬 알고리즘의 세계로 여행을 떠납니다. 🚀 퀵 정렬과 계수 정렬이란 무엇이며, 각각 어떤 장점과 단점을 가지고 있는지 알아보겠습니다.

**퀵 정렬 (Quick Sort)**

퀵 정렬은 1960년 가우스에 의해 개발된 알고리즘입니다. 이름에서 알 수 있듯이 '빨리' 정렬하는 알고리즘입니다! 🔥 퀵 정렬의 기본 아이디어는 데이터를 피봇 값 하나로 나누고, 작은 부분을 다시 퀵 정렬으로 호출하는 것입니다.

### 퀵 정렬의 동작 과정

1.  **피봇 선택** : 데이터 중에서 임의의 값을 선택합니다.
2.  **데이터 분할** : 피봇 값보다 작거나 같은 데이터와 큰 데이터로 나눕니다.
3.  **재귀적 호출** : 작은 부분은 다시 퀵 정렬을 호출하여 정렬합니다.

### 예제: 퀵 정렬의 구현

```markdown
### 퀵 정렬 코드 (C언어)

```c
#include <stdio.h>

// 함수 prototype
void quick_sort(int arr[], int left, int right);

int main() {
    int arr[] = {64, 34, 25, 12, 22, 11, 90};
    int n = sizeof(arr) / sizeof(arr[0]);

    printf("정렬 전: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }

    quick_sort(arr, 0, n - 1);

    printf("\n정렬 후: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }

    return 0;
}

// 퀵 정렬 함수
void quick_sort(int arr[], int left, int right) {
    if (left < right) {
        int pivot = partition(arr, left, right);
        quick_sort(arr, left, pivot - 1);
        quick_sort(arr, pivot + 1, right);
    }
}

// 파티션 함수
int partition(int arr[], int low, int high) {
    int pivot = arr[high];
    int i = (low - 1);

    for (int j = low; j <= high - 1; j++) {
        if (arr[j] < pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }

    swap(arr[i + 1], arr[high]);
    return (i + 1);
}

// 데이터 교환 함수
void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}
```

### 퀵 정렬의 장단점

-   **장점** : 평균 시간복잡도가 O(n log n), 정렬 과정이 효율적입니다.
-   **단점** : 최악의 경우 (이상적인 상황에서 데이터가 이미 정렬되어 있는 경우) 시간 복잡도는 O(n^2)가 됩니다.

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
