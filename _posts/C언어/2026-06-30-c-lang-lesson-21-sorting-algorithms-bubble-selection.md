---
layout: single
title: "정렬 알고리즘: 버블 정렬, 선택 정렬"
date: 2026-06-30 14:19:47
categories: [C언어]
---

**21강: 정렬 알고리즘 - 버블 정렬, 선택 정렬**

안녕하세요, 여러분! 오늘 우리는 **정렬 알고리즘**에 대해 배울 것입니다. 이 강의는 제가 가장 좋아하는 주제 중 하나입니다. 왜냐하면, 여러분이 코딩을 시작했을 때, 자바스크립트, 파이썬, C언어 등 다양한 언어를 사용할 수록, 데이터 정렬에 대한 개념은 항상 중요성이 büy어나갑니다. 

정렬이라는 키워드는 누구나 알고 있지만, 정말 중요한 점은 여러분이 이론을 공부한 후, 실무에서 어떻게 적용되는지 알아야 합니다. 그래서 오늘 우리는 **버블 정렬(Bubble Sort)**과 **선택 정렬(Selection Sort)**을 함께 공부할 것입니다.

### 왜 정렬 알고리즘을 이해해야 하나요?

정렬이라는 개념은 여러분이 데이터를 관리하고 분석할 때 매우 중요합니다. 예를 들어, 학생의 이름과 점수를 정렬하여 1등부터 10등까지 출력하거나, 상품의 가격 순으로 목록을 정렬하는 등의 상황에서 정렬 알고리즘을 사용하게 됩니다.

하지만, 정렬 알고림즘은 단순히 데이터를 정렬하는 것만이 아닙니다. 왜냐하면, 데이터의 크기가 큰 경우라면, 데이터를 정렬할 때 시간과 메모리가 많이 소비될 수 있기 때문입니다. 

이러한 이유로 우리는 효율적인 정렬 알고리즘을 선택하고 사용하여야 합니다. 오늘은 이와 관련된 두 가지 대표적인 정렬 알고리즘인 **버블 정렬(Bubble Sort)**과 **선택 정렬(Selection Sort)**에 대해 배울 것입니다.

### 버블 정렬 (Bubble Sort)

버블 정렬은 가장 단순한 정렬 알고리즘 중 하나입니다. 이는 데이터를 한번에 하나씩 정렬하여, 데이터의 위치를 바꿔나가는 방식으로 동작합니다.

#### 버블 정렬 예제
```c
#include <stdio.h>

void bubble_sort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                // Swap
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

int main() {
    int arr[] = {5, 2, 8, 12, 3};
    int n = sizeof(arr) / sizeof(arr[0]);

    printf("Original array: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    bubble_sort(arr, n);

    printf("Sorted array: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}
```

#### 버블 정렬의 동작 방식

1.  가장 왼쪽부터 데이터를 하나씩 비교하여, 큰 데이터가 오른쪽으로 이동하는 것을 반복합니다.
2.  이 과정을 n-1 번 반복하여, 데이터가 최종적으로 정렬됩니다.

### 선택 정렬 (Selection Sort)

선택 정렬은 데이터의 각 위치에 대해, 가장 작은(또는 가장 큰) 값을 찾아서 그 위치로 옮기는 방식으로 동작합니다.

#### 선택 정렬 예제
```c
#include <stdio.h>

void selection_sort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        // Find the minimum element in the unsorted part of the array
        int min_idx = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[min_idx]) {
                min_idx = j;
            }
        }

        // Swap the found minimum element with the first element of the unsorted part
        int temp = arr[i];
        arr[i] = arr[min_idx];
        arr[min_idx] = temp;
    }
}

int main() {
    int arr[] = {5, 2, 8, 12, 3};
    int n = sizeof(arr) / sizeof(arr[0]);

    printf("Original array: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    selection_sort(arr, n);

    printf("Sorted array: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}
```

#### 선택 정렬의 동작 방식

1.  데이터의 각 위치에 대해, 가장 작은(또는 가장 큰) 값을 찾습니다.
2.  해당 위치와 발견된 값이 있는 위치를 swap합니다.

### 실무에서는 어떻게 사용할까요?

오늘 배운 버블 정렬과 선택 정렬은 모두 O(n^2)의 시간 복잡도를 가지고 있습니다. 하지만, 데이터의 크기가 작거나, 특정한 조건이 적용되는 경우에는 효과적일 수도 있습니다.

하지만, 데이터가 많아지면 시간복잡도가 비효율적으로 증가할 수 있기 때문에, 효율적인 정렬 알고리즘인 **퀵 소트(Quick Sort)**나 **머지소트(Merge Sort)**를 사용하는 것을 권장합니다.

### 결론

정렬 알고리즘은 코딩에서 매우 중요한 개념입니다. 오늘 우리는 버블 정렬과 선택 정렬에 대해 배웠습니다. 이들은 효율적이지는 않지만, 이해하기 쉬운 두 가지 대표적인 정렬 알고리즘입니다.

오늘의 실습으로 여러분이 데이터를 효과적으로 정렬하는 능력을 발휘할 수 있도록 도와주었으면 좋겠습니다. 

[🚨실무주의보] **정렬 알고리즘은 어떤 경우에 사용해야 하나요?**

정렬 알고리즘은 데이터가 많을 때, 또는 데이터의 크기가 작을 때 효과적으로 사용될 수 있습니다. 하지만, 데이터가 너무 많거나, 시간 복잡도가 O(n^2)일 때는 다른 효율적인 정렬 알고리즘을 사용하는 것을 권장합니다.

[💡 초보자 폭풍 질문!] **버블 정렬과 선택 정렬의 차이는 무엇인가요?**

버블 정렬은 데이터를 하나씩 비교하여, 큰 데이터가 오른쪽으로 이동하는 방식입니다. 반면에 선택 정렬은 각 위치에서 가장 작은(또는 가장 큰) 값을 찾고, 해당 위치로 옮기는 방식입니다.

이러한 차이로 인해 버블 정렬의 시간 복잡도는 선택 정렬보다 더 높습니다.

[👍 끝마치기]

오늘의 강의를 통해 여러분이 정렬 알고리즘에 대한 이해를 더深게 하고, 실무에서 어떻게 적용하는지 알아볼 수 있었을 것 같습니다. 

정렬 알고리즘은 코딩에서 매우 중요한 개념인 것을 다시한번 반복하고 싶습니다. 오랜 시간 공부하시느라 감사드리며, 다음 강의에서도 더 많은 것을 배워보실 수 있도록 도와드릴게요! 👋

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
