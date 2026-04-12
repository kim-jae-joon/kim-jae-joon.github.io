---
layout: single
title: "알고리즘 및 데이터 구조 개요"
date: 2026-07-02 18:44:59
categories: [C언어]
---

## 🚀 19강: 알고리즘 & 데이터 구조 - 코딩 세계의 레고 마스터 되기!

안녕하세요, 코딩 영웅 여러분! 👋 오늘은 **알고리즘과 데이터 구조**라는 강력한 무기를 손에 쥐는 날입니다! 이거 모르면 코딩 세계에서 혼자 뒤처질 수 있으니, 꼭 따라 해보세요! "이거 모르면 큰일 납니다!" 😉

### 🧩 알고리즘이란 무엇인가요?

알고리즘이란 쉽게 말해 **문제 해결의 단계별 레시피**입니다. 마치 **요리책**처럼 정확한 순서와 방법을 따라가면 맛있는 요리(결과물)를 만들 수 있죠! 예를 들어, **"계란을 깨고 소금을 넣어 볶아서 프라이 완성!"**이 바로 알고리즘의 기본입니다.

#### 알고리즘 예시: 맛있는 코드 레시피

```c
#include <stdio.h>

// 함수: 맛있는 프라이 만드는 레시피
void makeFriedEgg() {
    // 1단계: 계란 깨기
    printf("계란을 깨세요.\n");
    
    // 2단계: 소금 넣기
    printf("소금을 조금 넣어주세요.\n");
    
    // 3단계: 프라이팬에 볶기
    printf("중불에서 볶아주세요.\n");
    
    // 4단계: 완성!
    printf("맛있는 프라이 완성!\n");
}

int main() {
    makeFriedEgg();  // 레시피 실행!
    return 0;
}
```

**코드 설명:**
- `makeFriedEgg()` 함수는 프라이를 만드는 단계별 지시사항을 포함합니다.
- `printf` 함수는 각 단계를 출력하는 역할을 합니다.
- `main()` 함수는 전체 레시피를 실행하는 시작점입니다.

### 🏗️ 데이터 구조: 정보의 효율적인 저장소

데이터 구조는 **정보를 효과적으로 저장하고 관리하는 방법**입니다. 마치 **창고 관리**처럼, 잘 정리된 창고는 필요한 물건을 빠르게 찾을 수 있죠!

#### 데이터 구조 예시: 정보의 효율적인 정리

1. **배열 (Array)**
   - **개념**: 연속된 메모리 공간에 동일한 타입의 데이터를 저장하는 방법입니다.
   - **예시 코드**: 학생들의 점수를 저장해보세요!

   ```c
   #include <stdio.h>

   int main() {
       int scores[5];  // 최대 5명의 학생 점수를 저장할 배열
       int i;

       // 점수 입력
       for (i = 0; i < 5; i++) {
           printf("학생 %d의 점수를 입력하세요: ", i + 1);
           scanf("%d", &scores[i]);
       }

       // 점수 출력
       printf("\n학생들의 점수:\n");
       for (i = 0; i < 5; i++) {
           printf("학생 %d: %d점\n", i + 1, scores[i]);
       }

       return 0;
   }
   ```

   **코드 설명:**
   - `scores[5]`는 크기가 5인 정수 배열입니다.
   - `for` 반복문을 사용해 점수를 입력받고, 다시 출력합니다.
   - 배열 인덱스는 `0`부터 시작하므로 주의하세요!

2. **연결 리스트 (Linked List)**
   - **개념**: 각 노드가 데이터와 다음 노드를 가리키는 포인터로 구성된 구조입니다. 마치 **연결된 퍼즐 조각** 같아요!
   - **예시 코드**: 간단한 노드 클래스 구현

   ```c
   #include <stdio.h>
   #include <stdlib.h>

   // 노드 구조체 정의
   typedef struct Node {
       int data;
       struct Node* next;
   } Node;

   // 함수: 노드 생성
   Node* createNode(int value) {
       Node* newNode = (Node*)malloc(sizeof(Node));
       newNode->data = value;
       newNode->next = NULL;
       return newNode;
   }

   // 함수: 연결 리스트 출력
   void printList(Node* head) {
       Node* current = head;
       while (current != NULL) {
           printf("%d -> ", current->data);
           current = current->next;
       }
       printf("NULL\n");
   }

   int main() {
       Node* head = createNode(10);
       Node* second = createNode(20);
       head->next = second;  // 연결

       printList(head);  // 출력: 10 -> 20 -> NULL
       free(head);       // 메모리 해제
       return 0;
   }
   ```

   **코드 설명:**
   - `Node` 구조체는 데이터와 포인터를 포함합니다.
   - `createNode` 함수로 새로운 노드를 생성하고, `next` 포인터로 연결합니다.
   - `printList` 함수는 리스트의 내용을 순서대로 출력합니다.

3. **스택 (Stack)**
   - **개념**: **후입선출(LIFO, Last In First Out)** 방식으로 데이터를 관리하는 구조입니다. 마치 **접시 쌓아올리기**와 같아요!
   - **예시 코드**: 간단한 스택 구현

   ```c
   #include <stdio.h>
   #include <stdlib.h>

   #define MAX 100  // 스택의 최대 크기

   typedef struct Stack {
       int items[MAX];
       int top;
   } Stack;

   // 스택 생성 함수
   Stack* createStack() {
       Stack* stack = (Stack*)malloc(sizeof(Stack));
       stack->top = -1;  // 초기화
       return stack;
   }

   // 스택에 데이터 추가 (Push)
   void push(Stack* stack, int value) {
       if (stack->top >= MAX - 1) {
           printf("스택 오버플로우!\n");
           return;
       }
       stack->items[++stack->top] = value;
       printf("%d를 스택에 추가했습니다.\n", value);
   }

   // 스택에서 데이터 제거 (Pop)
   int pop(Stack* stack) {
       if (stack->top < 0) {
           printf("스택 언더플로우!\n");
           return -1;  // 오류 처리
       }
       return stack->items[stack->top--];
   }

   int main() {
       Stack* myStack = createStack();

       push(myStack, 10);
       push(myStack, 20);
       printf("가장 위의 요소는 %d입니다.\n", pop(myStack));  // 20
       printf("다음 요소는 %d입니다.\n", pop(myStack));       // 10

       free(myStack);  // 메모리 해제
       return 0;
   }
   ```

   **코드 설명:**
   - `Stack` 구조체는 정수 배열과 `top` 포인터를 가집니다.
   - `push` 함수는 데이터를 스택의 최상단에 추가합니다.
   - `pop` 함수는 최상단 데이터를 제거하고 반환합니다.
   - 스택의 크기 제한(`MAX`)을 고려해야 합니다.

### 💡 초보자 폭풍 질문! 🤔

**Q1:** 배열과 연결 리스트 중 어떤 상황에서 배열을, 어떤 상황에서 연결 리스트를 사용하는 것이 좋을까요?
- **A1:** 배열은 **연속적인 데이터**를 효율적으로 다룰 때 좋습니다. 예를 들어, 고정된 크기의 데이터 리스트를 다룰 때 적합합니다. 반면에 **동적 크기 조정**이 필요한 경우나 데이터 삽입/삭제가 빈번한 상황에서는 연결 리스트가 더 유용합니다. 연결 리스트는 메모리 할당과 해제가 자유롭기 때문이죠!

**Q2:** 스택과 큐는 어떻게 다른가요?
- **A2:** 스택과 큐는 모두 **데이터 구조**이지만, 동작 방식이 다릅니다. **스택**은 **LIFO (Last In First Out)** 방식으로 데이터를 관리합니다 (예: 접시 쌓기). **큐**는 **FIFO (First In First Out)** 방식으로 데이터를 관리합니다 (예: 줄 서기). 큐는 주로 대기열 관리에 사용되고, 스택은 함수 호출 스택이나 브라우저의 뒤로 가기 기능 등에 활용됩니다.

### 🚨 실무주의보 🛡️

실제 프로젝트에서는 다양한 데이터 구조를 적절히 혼합하여 사용하는 것이 중요합니다. 예를 들어, **캐싱** 기능을 구현할 때는 **해시 테이블**과 **연결 리스트**를 함께 활용하여 빠른 검색과 동적 크기 조정을 동시에 달성할 수 있습니다. **알고리즘의 효율성** 또한 성능 최적화에 큰 영향을 미치므로, 문제의 특성에 맞는 최적의 알고리즘을 선택하는 능력이 필요합니다.

### 📚 요약

오늘 배운 내용을 간단히 정리하면:
- **알고리즘**: 문제 해결의 단계별 레시피!
- **데이터 구조**: 정보를 효율적으로 저장하고 관리하는 방법들!
  - **배열**: 연속된 메모리 공간 활용
  - **연결 리스트**: 유연한 데이터 연결
  - **스택**: LIFO 방식으로 데이터 관리

이제 코딩 세계에서 정보를 효과적으로 다루는 레고 마스터가 되셨나요? 🤓 계속 연습하고 실험해보세요! 여러분의 코딩 여정이 빛나길 바랍니다! 🚀

---

이렇게 상세하고 친근한 스타일로 작성하면 초보자들도 이해하기 쉽고 재미있게 학습할 수 있을 거예요! 추가 질문이나 다른 요청이 있으시면 언제든지 말씀해 주세요!

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
