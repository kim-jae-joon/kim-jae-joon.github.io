---
layout: single
title: "C 언어 동적 메모리 할당 (malloc, free)"
date: 2026-07-08 19:07:06
categories: [Rust C 언어]
---

## 🚀 13강: C 언어의 마법 주문 - 동적 메모리 할당 (malloc, free) 🪄

안녕하세요, 코드의 마법사 여러분! 오늘은 C 언어에서 정말로 신기하고도 강력한 마법 주문을 배울 거예요. **동적 메모리 할당**이라는 주제인데요, 이 기술을 마스터하면 마치 컴퓨터 속의 마법사가 된 듯한 느낌이 드실 거예요! 🧙‍♂️✨

### 💡 개념 이해: 메모리 탐험대 출발!

**동적 메모리 할당**이란 프로그램이 실행되는 도중에 필요한 만큼의 메모리 공간을 자동으로 할당받아 사용하는 기술을 말합니다. 이 기술이 없었다면, 메모리 크기를 미리 고정해야 했을 텐데, 그건 마치 방을 이사 갈 때마다 미리 방 크기를 정해놓는 것과 같죠. 전혀 유연하지 않잖아요!

**malloc 함수**는 이 마법 주문의 핵심입니다. 이 함수는 `void* malloc(size_t size)` 형태로 작동해요. 간단히 말해, "크기 `size` 만큼의 메모리 공간을 할당해 줘"라고 컴퓨터에게 요청하는 마법 주문이죠.

### 🤯 왜 동적 메모리 할당이 필요한가요?

- **유연성**: 프로그램 실행 중에 필요한 데이터의 크기를 미리 알 수 없을 때 유용합니다. 예를 들어, 사용자가 입력하는 데이터의 크기가 달라질 수 있는 상황이죠.
- **효율성**: 필요한 만큼만 메모리를 사용하므로 메모리 낭비를 줄일 수 있습니다. 마치 옷장에서 필요한 옷만 꺼내 입는 것처럼요!

### 🛠️ 실전 예제: 동적 메모리 할당 정복하기

#### 예제 1: 간단한 숫자 배열 할당

```c
#include <stdio.h>
#include <stdlib.h>  // malloc 함수를 사용하기 위해 포함

int main() {
    int n;
    printf("배열의 크기를 입력하세요: ");
    scanf("%d", &n);  // 사용자로부터 배열 크기 입력 받기

    // 동적 메모리 할당
    int* numbers = (int*)malloc(n * sizeof(int));  // n 크기의 int 배열 할당

    // 메모리 할당 확인
    if (numbers == NULL) {
        printf("메모리 할당 실패!\n");
        return 1;  // 에러 처리
    }

    // 배열 초기화
    for (int i = 0; i < n; i++) {
        numbers[i] = i * 10;  // 배열 요소 초기화
    }

    // 결과 출력
    printf("할당된 배열: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", numbers[i]);
    }
    printf("\n");

    // 할당된 메모리 해제
    free(numbers);  // 메모리 해제

    return 0;
}
```
**코드 해설:**
- `malloc(n * sizeof(int))`: 사용자가 입력한 `n` 크기만큼의 정수 배열을 동적으로 할당합니다.
- `numbers == NULL`: 메모리 할당이 실패했는지 확인합니다. 실패 시 에러 메시지 출력 및 프로그램 종료.
- `for` 루프를 이용해 배열 초기화와 출력을 수행합니다.
- `free(numbers)`: 사용 후 메모리를 해제하여 메모리 누수를 방지합니다.

#### 예제 2: 구조체 동적 할당 - 복잡한 데이터 관리

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    char name[50];
    float salary;
} Employee;

int main() {
    int num_employees;
    printf("직원 수를 입력하세요: ");
    scanf("%d", &num_employees);

    // 동적 메모리 할당
    Employee* employees = (Employee*)malloc(num_employees * sizeof(Employee));

    if (employees == NULL) {
        printf("메모리 할당 실패!\n");
        return 1;
    }

    // 직원 데이터 입력 및 출력
    for (int i = 0; i < num_employees; i++) {
        printf("직원 %d 이름 입력: ", i + 1);
        scanf("%s", employees[i].name);
        printf("급여 입력: ");
        scanf("%f", &employees[i].salary);

        printf("이름: %s, 급여: %.2f\n", employees[i].name, employees[i].salary);
    }

    // 할당된 메모리 해제
    free(employees);

    return 0;
}
```
**코드 해설:**
- `typedef struct`: 구조체를 정의하여 직원의 이름과 급여를 한 번에 관리할 수 있게 합니다.
- `Employee* employees = (Employee*)malloc(...)`: 구조체 배열을 동적으로 할당합니다.
- 각 직원의 정보를 입력받고 출력합니다.
- 마지막으로 할당된 메모리를 해제합니다.

### 💡 초보자 폭풍 질문! 🧙‍♂️

**Q1:** `malloc`이 반환하는 값이 `NULL`이면 어떻게 해야 하나요?
- **A:** `malloc`이 메모리 할당에 실패하면 `NULL`을 반환합니다. 이 경우 프로그램은 에러 메시지를 출력하고 종료하거나 다른 방법으로 대체 메모리 할당을 시도해야 합니다. 위 예제에서 `if (numbers == NULL)` 부분을 참고하세요.

**Q2:** `free` 함수를 호출하지 않으면 메모리 누수가 발생하나요?
- **A:** 네, 그렇습니다! `free` 함수를 호출하지 않으면 할당된 메모리가 해제되지 않고 프로그램이 종료될 때까지 메모리가 점유됩니다. 이는 메모리 누수로 이어져 시스템 성능 저하를 초래할 수 있습니다. 항상 `free`를 적절히 사용해야 합니다.

### 🚨 실무주의보 ⚠️

**주의사항:**
- **메모리 누수 방지**: 모든 동적 할당은 반드시 해제해야 합니다. `free`를 빠뜨리지 마세요!
- **크기 계산 주의**: `sizeof`를 잘못 사용하면 예상치 못한 메모리 오류가 발생할 수 있으니 주의하세요.

### 마무리: 마법사의 비결

동적 메모리 할당은 마치 마법사의 지팡이처럼 유연하고 강력합니다. 이를 잘 활용하면 프로그램의 성능과 효율성을 극대화할 수 있어요. 오늘 배운 내용을 바탕으로, 여러분도 이제 더 유연하고 강력한 코드를 작성할 수 있을 거예요! 

**다음 강의에서는 더 복잡한 메모리 관리 기법을 다룰 예정이니, 지금까지 배운 내용을 잘 정리해 두세요!** 🧙‍♂️🔥

함께 코딩의 마법을 펼쳐나가요! 🎉

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
