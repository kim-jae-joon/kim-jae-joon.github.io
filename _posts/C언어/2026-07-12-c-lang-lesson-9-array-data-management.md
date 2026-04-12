---
layout: single
title: "배열: 한 번에 여러 변수 관리"
date: 2026-07-12 14:17:52
categories: [C언어]
---

**9강: 배열 - 한 번에 여러 변수 관리**

😎안녕하세요, 여러분! 오늘 우리는 C언어의 arrays라는 또 하나의 강력한 도구를学습합니다. arrays를 공부하는 것이 왜 중요할까요? 🤔그것은 단순히 변수 여러개를 관리하려는 간단한 문제였던 것일까? 😊아니요, 그보다는 훨씬 더 많은 용도로 사용됩니다.

예를들어, 한 학생이 수학 시험에서 받은 총점을 관리하려면, 그 학생의 이름, 성별, 국어, 영어, 수학 점수를 각각 변수로 선언하고, 각 점수에 해당하는 변수를 입력해야 합니다. 😩하지만, 만약 학생 수가 100명이라고 가정한다면? 🤯변수의 개수가 한 번에 100개가 증가하면, 관리하기 어려워지기 시작합니다.

이때 arrays라는 도구가 등장합니다! 👀배열은 한 번에 여러 변수를 관리할 수 있는 강력한 도구입니다. 💪

### arrays 기본 구조

```c
int scores[3]; // 3개의 정수형 변수 선언
```

위의 코드에서 `scores`라는 이름의 배열이 선언되었습니다. 이 때, `[3]`은 배열 안에 들어갈 변수의 개수를 의미합니다.

### array elements

배열을 구성하는 각 요소를 element라고 합니다. 📝각 요소는 별도로 저장되고, 접근할 수 있습니다.

```c
int scores[3];
scores[0] = 90; // 첫 번째 요소에 90 할당
scores[1] = 80;
scores[2] = 70;

printf("%d %d %d\n", scores[0], scores[1], scores[2]);
```

위의 코드에서, `scores[0]`, `scores[1]`과 같은 방식으로 각 요소에 접근하고, 할당합니다.

### array length

배열 안에 들어있는 실제 요소 개수를 얻으려면 어떻게 해야할까요? 🤔

```c
int scores[] = {90, 80, 70};
int len = sizeof(scores) / sizeof(scores[0]);
printf("array length: %d\n", len);
```

위의 코드에서 `sizeof` 연산자를 사용하여 배열 전체 길이와 각 요소 길이를 구하고, 배열 길이를 계산합니다.

### 실무 활용

실제 프로젝트에 arrays를 적용하면 다음과 같습니다.

```c
#include <stdio.h>

int main() {
    int scores[5];
    
    printf("Enter 5 scores: ");
    for(int i = 0; i < 5; i++) {
        scanf("%d", &scores[i]);
    }
    
    printf("\nScores:\n");
    for(int i = 0; i < 5; i++) {
        printf("%d\n", scores[i]);
    }
    
    return 0;
}
```

위의 코드에서, 사용자로부터 5개의 점수를 입력받아 저장하고, 저장된 점수들을 출력합니다.

👀이러한 arrays를 통해 한 번에 여러 변수를 관리할 수 있습니다. 💪배열은 다양한 용도로 사용될 수 있으며, 실무에서도 중요합니다. 🤔

### 초보자 폭풍 질문! 💡

*   arrays와 포인터는 어떤 차이가 있나요?
    *   arrays는 이름이 있는 변수 집합으로 생각할 수 있습니다. 반면에 포인터는 변수의 주소를 저장하는 변수입니다.
*   array elements를 접근하는 방법은 무엇인가요?
    *   square bracket `[]`을 사용하여 접근합니다.

### 실무주의보 🚨

*   arrays를 사용할 때, 잘못된 index 값을 사용하면 프로그램이 종료될 수 있으니 주의하세요! 😳
*   array length를 알고 싶을 때는 `sizeof` 연산자를 사용하세요!

이상으로 arrays라는 강력한 도구에 대해 공부했습니다. 💡 arrays를 잘 활용하여 다양한 문제를 해결할 수 있습니다! 🚀

### 참고 자료

*   C언어 공식 문서: [arrays](https://docs.microsoft.com/ko-kr/cpp/standard-library/arrays?view=msvc-170)
*   IBM Developer: [Arrays in C Programming Language](https://www.ibm.com/docs/en/zos/2.4.0?topic=elements-arrays-c-programming-language)

그럼 다음 강의에서 다시 뵙겠습니다! 😊

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
