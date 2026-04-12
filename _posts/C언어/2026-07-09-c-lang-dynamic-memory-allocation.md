---
layout: single
title: "C언어 응용: 동적 메모리 할당 (malloc, free)"
date: 2026-07-09 21:08:14
categories: [C언어]
---

## 🚀 12강: 메모리 마법사가 되어보자! 🪄 C언어 동적 메모리 할당 (malloc, free) 정복하기

**진짜 신기하죠?** 지금까지 우리는 컴퓨터가 미리 정해놓은 땅(정적 메모리) 위에서만 놀았어요. 하지만 때로는 땅을 계속 늘리거나 줄여가며 탐험해야 할 때가 있죠! 바로 이럴 때 필요한 게 바로 **동적 메모리 할당**이에요. 마치 **무한한 마법의 땅**을 얻는 것과 같아요! 오늘은 이 마법의 기술을 배워보면서 **malloc**과 **free**라는 두 마법사를 마스터해보겠습니다.

### 🧙‍♂️ 기본 개념: 메모리의 유동성

**정적 메모리 할당**은 컴파일할 때 메모리 크기가 고정되어 있어요. 마치 집을 지을 때 정해진 크기의 땅을 사는 것과 같죠. 반면 **동적 메모리 할당**은 프로그램 실행 중에 필요에 따라 메모리 공간을 늘리거나 줄여요. 마치 **도시를 건설하듯이** 필요에 따라 확장하고 축소하는 거예요!

#### 핵심 마법사들: `malloc`, `free`

- **`malloc`**: 메모리 마법사의 주문! 이 함수를 사용하면 프로그램 실행 중에 원하는 크기의 메모리 블록을 할당받을 수 있어요.
  
- **`free`**: 메모리 회수 마법사! 할당받은 메모리를 더 이상 사용하지 않을 때는 `free`로 메모리를 되돌려줘야 메모리 누수를 막을 수 있어요.

### 📝 코드로 배우는 마법

#### 1. `malloc`으로 메모리 할당하기

**상황**: 여러 개의 학생들 점수를 저장할 수 있는 배열을 동적으로 생성해보겠습니다. 점수 개수는 런타임에 결정됩니다.

```c
#include <stdio.h>
#include <stdlib.h> // malloc, free 함수를 사용하기 위해 포함

int main() {
    int numStudents;
    
    // 사용자로부터 학생 수 입력 받기
    printf("학생 수를 입력하세요: ");
    scanf("%d", &numStudents); // 사용자 입력 받기

    // 동적으로 점수 배열 생성
    int *scores = (int *)malloc(numStudents * sizeof(int)); // 마법의 주문!

    if (scores == NULL) {
        printf("메모리 할당 실패!");
        return 1; // 오류 처리
    }

    // 점수 입력 예시 (5명의 학생 점수)
    for (int i = 0; i < numStudents; i++) {
        printf("학생 %d의 점수를 입력하세요: ", i + 1);
        scanf("%d", &scores[i]);
    }

    // 점수 출력
    printf("각 학생의 점수:\n");
    for (int i = 0; i < numStudents; i++) {
        printf("학생 %d: %d점\n", i + 1, scores[i]);
    }

    // 메모리 해제
    free(scores); // 마법의 회수 주문!

    return 0;
}
```

**설명**:
- `malloc(numStudents * sizeof(int))`: `numStudents` 개수만큼 `int` 타입의 메모리 공간을 할당합니다. `sizeof(int)`는 `int` 타입의 크기를 반환합니다.
- `if (scores == NULL)`: 할당이 실패했는지 확인합니다. `NULL`이면 메모리 할당에 실패한 것입니다.

#### 2. 다양한 할당 방식: 반복문 활용

**상황**: 동일한 크기의 메모리 블록을 여러 번 할당해보겠습니다. 이때 반복문을 활용해보세요!

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int numBlocks;
    int *blockArray;

    printf("할당할 블록 수를 입력하세요: ");
    scanf("%d", &numBlocks);

    // 여러 블록 할당
    blockArray = (int *)malloc(numBlocks * sizeof(int *)); // 포인터 배열 할당
    if (blockArray == NULL) {
        printf("메모리 할당 실패!\n");
        return 1;
    }

    for (int i = 0; i < numBlocks; i++) {
        blockArray[i] = (int *)malloc(sizeof(int)); // 각 블록 할당
        if (blockArray[i] == NULL) {
            printf("블록 %d 할당 실패!\n", i + 1);
            return 1;
        }
        printf("블록 %d 크기: %zu 바이트\n", i + 1, sizeof(int));
    }

    // 메모리 해제
    for (int i = 0; i < numBlocks; i++) {
        free(blockArray[i]); // 각 블록 해제
    }
    free(blockArray); // 포인터 배열 해제

    return 0;
}
```

**설명**:
- `malloc(numBlocks * sizeof(int *))`: 각 블록을 가리키는 포인터 배열을 할당합니다.
- 중첩된 `malloc`을 사용해 각 블록을 동적으로 할당합니다.
- 반복문을 통해 각 블록을 개별적으로 해제합니다.

#### 3. `free`의 중요성: 메모리 누수 방지

**상황**: 메모리 누수를 막기 위해 `free`를 어떻게 사용해야 하는지 살펴보겠습니다.

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int *data = (int *)malloc(sizeof(int)); // 메모리 할당
    if (data == NULL) {
        printf("메모리 할당 실패!\n");
        return 1;
    }

    *data = 42; // 값 할당
    printf("할당된 메모리 값: %d\n", *data);

    // 메모리 해제 필수!
    free(data); // 메모리 회수

    // 다시 할당 후 사용 (주의: 이미 해제된 메모리는 사용 금지!)
    data = (int *)malloc(sizeof(int)); // 안전한 메모리 재할당
    if (data == NULL) {
        printf("메모리 재할당 실패!\n");
        return 1;
    }
    *data = 100; // 새로운 값 할당
    printf("재할당된 메모리 값: %d\n", *data);

    return 0;
}
```

**설명**:
- **메모리 해제 후 재할당 주의**: 메모리를 해제한 후에는 다시 할당해야 합니다. 이전에 해제된 메모리를 사용하면 **예기치 않은 오류**가 발생할 수 있습니다.

### 💡 초보자 폭풍 질문!

**Q**: `malloc`이 `NULL`을 반환하면 어떻게 해야 하나요?
**A**: `malloc`이 `NULL`을 반환하면 메모리 할당에 실패한 거예요. 이 경우 프로그램에서 오류 메시지를 출력하고 종료하는 것이 좋습니다. 안전한 코딩을 위해 항상 이 부분을 체크해야 합니다.

### 🚨 실무주의보

**주의사항**: `free`를 잘못 사용하면 **메모리 누수**가 발생할 수 있습니다. 특히 중첩된 할당 구조에서는 각 할당된 메모리를 정확히 해제해야 합니다. 실수로 메모리를 해제하지 않으면 프로그램이 점차적으로 메모리를 잃어 성능 저하를 초래할 수 있으니 주의하세요!

### 마무리

오늘 배운 동적 메모리 할당은 **프로그래밍의 마법**이에요! `malloc`으로 원하는 만큼의 메모리를 생성하고, `free`로 적절히 회수하면 프로그램의 유연성과 효율성이 크게 향상됩니다. 이제 당신도 **메모리의 마법사**가 되었어요! 계속 연습하고 다양한 상황에서 이 기술을 활용해보세요. 다음 강의에서는 이 기술을 활용한 더 복잡한 예제를 살펴볼 예정이니 기대해주세요! 🧙‍♂️✨

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
