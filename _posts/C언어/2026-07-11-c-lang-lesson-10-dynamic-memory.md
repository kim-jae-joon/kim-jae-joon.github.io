---
layout: single
title: "동적 메모리 할당 (malloc, free)"
date: 2026-07-11 18:42:50
categories: [C언어]
---

# 🚀 10강: 동적 메모리 할당의 마법 - `malloc`, `free` 마스터하기

안녕하세요, 코딩 초보자 여러분! 오늘은 코드 세계에서 정말 멋진 마법사 같은 기능, 바로 **동적 메모리 할당**에 대해 배워볼게요. 특히 `malloc`과 `free` 함수에 집중해 보면서, 여러분의 코드가 훨씬 유연하고 효율적으로 변신하는 과정을 함께 살펴보도록 하죠! 🌟

## 🧙‍♂️ 동적 메모리 할당이란?

**"진짜 신기하죠? 컴퓨터 메모리는 마치 우리 집의 방처럼, 미리 정해진 크기로만 사용할 수 있다고 생각했는데, 동적 메모리 할당이 있으니 이제는 필요에 따라 방을 만들고 없애는 것 같아요!"**

동적 메모리 할당은 프로그램 실행 중에 필요한 만큼 메모리를 할당하고 해제하는 기술입니다. 이는 특히 큰 데이터 구조나 알 수 없는 크기의 데이터를 다룰 때 매우 유용해요. 마치 레스토랑에서 손님이 올 때마다 테이블을 추가하거나 없애는 것과 비슷하죠!

### 핵심 개념 이해하기

1. **`malloc()` 함수**:
   - **목적**: 필요한 크기만큼의 메모리 공간을 할당받아 주소를 반환합니다.
   - **사용법**: `void *malloc(size_t size);`
   - **예시 코드**:
     ```c
     #include <stdio.h>
     #include <stdlib.h>

     int main() {
         // 100바이트 크기의 메모리 할당
         int *dynamicArray = (int *)malloc(100 * sizeof(int));
         
         if (dynamicArray == NULL) {
             // 메모리 할당 실패 시 처리
             printf("메모리 할당 실패!\n");
             return 1;
         }
         
         // 할당된 메모리에 값 할당
         for (int i = 0; i < 100; i++) {
             dynamicArray[i] = i * 10; // 각 요소에 값 할당
         }
         
         // 결과 출력
         for (int i = 0; i < 100; i++) {
             printf("dynamicArray[%d] = %d\n", i, dynamicArray[i]);
         }
         
         // 할당된 메모리 해제
         free(dynamicArray);
         
         return 0;
     }
     ```
     - **코드 해설**:
       - `malloc(100 * sizeof(int))`: 100개의 정수를 저장할 수 있는 메모리 공간을 할당합니다.
       - `dynamicArray` 포인터가 할당된 메모리 주소를 가리킵니다.
       - 할당 실패 시 `NULL`을 반환하므로 체크가 필수입니다.
       - 메모리에 값을 할당하고 출력합니다.
       - 마지막으로 `free(dynamicArray)`로 메모리를 해제하여 메모리 누수를 방지합니다.

2. **`free()` 함수**:
   - **목적**: 할당된 메모리를 해제하여 메모리 누수를 방지합니다.
   - **사용법**: `void free(void *ptr);`
   - **예시 코드**: 위의 `malloc` 예제에서 마지막 줄 `free(dynamicArray);`를 통해 메모리를 해제합니다.

### 다양한 할당 방법 살펴보기

#### 반복문 활용 예제
- **for 루프**: 반복적으로 메모리 할당과 해제를 처리할 때 유용합니다.
  ```c
  for (int i = 0; i < 5; i++) {
      int *ptr = (int *)malloc(sizeof(int));
      if (ptr == NULL) {
          printf("할당 실패!\n");
          return 1;
      }
      *ptr = i * 10;
      printf("%d\n", *ptr);
      free(ptr); // 각 반복마다 메모리 해제
  }
  ```
  - **해설**: 각 반복마다 새로운 메모리를 할당하고 즉시 사용 후 해제합니다.

- **while 루프**: 사용자 입력에 따라 동적으로 할당할 때 적합합니다.
  ```c
  int more;
  do {
      printf("더 할당할까요? (1: 예, 0: 아니요) ");
      scanf("%d", &more);
      if (more == 1) {
          int *ptr = (int *)malloc(sizeof(int));
          if (ptr == NULL) {
              printf("할당 실패!\n");
              break;
          }
          *ptr = 42; // 임의의 값 할당
          printf("할당된 값: %d\n", *ptr);
          free(ptr); // 사용 후 메모리 해제
      }
  } while (more == 1);
  ```
  - **해설**: 사용자 입력에 따라 메모리 할당 여부를 결정합니다.

#### 조건문 활용 예제
- **if-else 문**: 특정 조건에 따라 메모리 할당 여부를 결정합니다.
  ```c
  int dataSize = 200;
  if (dataSize > 0) {
      int *data = (int *)malloc(dataSize * sizeof(int));
      if (data == NULL) {
          printf("메모리 할당 실패!\n");
          return 1;
      }
      // 데이터 처리 코드
      free(data); // 작업 후 메모리 해제
  } else {
      printf("데이터 크기가 유효하지 않습니다.\n");
  }
  ```
  - **해설**: 데이터 크기에 따라 메모리 할당을 동적으로 결정하고 처리합니다.

### 💡 초보자 폭풍 질문!
- **Q**: 메모리 할당이 실패하면 어떻게 해야 하나요?
  - **A**: `malloc()`이 `NULL`을 반환하면 메모리 할당이 실패한 것입니다. 이 경우 에러 메시지를 출력하거나 대체 동작을 수행해야 합니다. 예를 들어:
    ```c
    if (ptr == NULL) {
        printf("메모리 할당 실패!\n");
        return 1; // 프로그램 종료 또는 대체 동작
    }
    ```

### 🚨 실무주의보
- **메모리 누수 주의**: `free()`를 빠뜨리면 메모리 누수가 발생할 수 있어요! 항상 할당과 해제를 짝지어 처리하는 습관을 들이세요.

## 🔥 마무리

동적 메모리 할당은 코드의 유연성과 효율성을 극대화하는 강력한 도구입니다. `malloc`과 `free`를 적절히 사용하면 프로그램이 더욱 지능적이고 대응력 있게 변모할 수 있어요. 이제 여러분도 메모리 마법사가 되어, 코드를 더욱 풍성하게 만들어보세요! 🧙‍♀️💪

이번 강의가 도움이 되었기를 바라며, 다음 강의에서도 계속해서 함께 성장해 나가요! 👋

---

이렇게 상세하고 재미있게 동적 메모리 할당에 대해 설명해 보았습니다. 궁금한 점이 있으면 언제든지 질문해주세요! 🚀📚

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
