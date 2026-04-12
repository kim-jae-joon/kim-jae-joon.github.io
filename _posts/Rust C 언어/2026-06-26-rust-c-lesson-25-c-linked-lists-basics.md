---
layout: single
title: "C 언어 링크드 리스트 기초 구현"
date: 2026-06-26 19:09:49
categories: [Rust C 언어]
---

## 💡 25강: C 언어 링크드 리스트 기초 구현 - 연결의 마법을 익혀보자!

안녕하세요, 코드 마법사 여러분! 💫 오늘은 우리가 마법의 책에서 한 장을 꺼내는 것처럼 **링크드 리스트(Linked List)**에 대해 알아보는 시간을 가져볼게요. 초보자 여러분, 걱정 마세요! 저는 당신의 손을 잡고 이 신비로운 세계로 이끌어 줄 친절한 가이드가 될게요.

### ✨ 링크드 리스트: 연결의 예술

**링크드 리스트**는 각각의 데이터 노드(Node)가 **다음 노드를 가리키는 포인터(Pointer)**를 가진 데이터 구조예요. 마치 학교에서 학생들이 서로의 연락처를 가지고 있어서 원하는 정보를 빠르게 찾아볼 수 있는 것처럼, 링크드 리스트도 데이터를 연결해서 효율적으로 관리할 수 있게 해줍니다.

#### 🎯 목표 설정
- 노드 구조 이해하기
- 기본적인 링크드 리스트 생성 및 조작하기
- 실제 예제를 통해 실무 감각 익히기

### 🤔 기본 개념 파헤치기

#### 노드(Node)란 무엇인가요?
링크드 리스트의 핵심 구성 요소인 **노드**는 데이터와 그 다음 노드를 가리키는 포인터로 이루어져 있어요. 쉽게 말해, **"이 데이터 다음에는 무엇이 있을까?"** 라는 질문에 답하는 존재라고 생각하면 됩니다.

**예제 코드: 노드 구조 정의**
```c
#include <stdio.h>
#include <stdlib.h>

// 노드 구조체 정의
typedef struct Node {
    int data;           // 노드에 저장될 데이터
    struct Node* next;  // 다음 노드를 가리키는 포인터
} Node;

// 노드 생성 함수 예시
Node* createNode(int value) {
    Node* newNode = (Node*) malloc(sizeof(Node));  // 메모리 할당
    newNode->data = value;                         // 데이터 설정
    newNode->next = NULL;                          // 초기 포인터는 NULL
    return newNode;                                // 생성된 노드 반환
}

int main() {
    // 노드 생성 예시
    Node* head = createNode(10);  // 첫 번째 노드 생성
    head->next = createNode(20);  // 두 번째 노드 연결
    head->next->next = createNode(30);  // 세 번째 노드 연결

    // 노드 데이터 출력 예시
    Node* current = head;
    while (current != NULL) {
        printf("노드 데이터: %d\n", current->data);
        current = current->next;  // 다음 노드로 이동
    }
    free(head);  // 메모리 해제
    return 0;
}
```

**코드 설명:**
1. **구조체 정의 (`struct Node`)**: 데이터(`data`)와 다음 노드를 가리키는 포인터(`next`)를 포함합니다.
2. **노드 생성 함수 (`createNode`)**: 새로운 노드를 동적으로 생성하고 데이터를 설정합니다. 포인터는 처음에는 `NULL`로 설정됩니다.
3. **메인 함수**: 노드를 생성하고 연결한 후, 각 노드의 데이터를 출력합니다. 마지막으로 메모리를 해제하여 누수를 방지합니다.

### 🔄 노드 연결 방법 다양하게 살펴보기

링크드 리스트에서 노드를 연결하는 방법은 여러 가지가 있어요. 다양한 상황에 따라 적절한 방법을 선택하면 더 유연하게 다룰 수 있답니다.

#### 1. **단순 연결 리스트 (Singly Linked List)**
가장 기본적인 형태로, 각 노드는 오직 **다음 노드만**을 가리킵니다. 마치 일렬로 줄지어 서 있는 친구들 같아요!

**예제 코드: 노드 추가**
```c
// 노드 추가 함수 예시 (단순 연결 리스트)
void appendNode(Node** head, int value) {
    Node* newNode = createNode(value);  // 새로운 노드 생성
    if (*head == NULL) {
        *head = newNode;  // 리스트가 비어있으면 헤드 설정
        return;
    }
    Node* temp = *head;
    while (temp->next != NULL) {
        temp = temp->next;  // 마지막 노드까지 이동
    }
    temp->next = newNode;  // 마지막 노드에 새 노드 연결
}

int main() {
    Node* head = NULL;
    appendNode(&head, 10);
    appendNode(&head, 20);
    appendNode(&head, 30);

    // 노드 출력
    Node* current = *head;
    while (current != NULL) {
        printf("노드 데이터: %d\n", current->data);
        current = current->next;
    }
    return 0;
}
```

**코드 설명:**
- `appendNode` 함수는 리스트의 마지막 노드를 찾아 새로운 노드를 연결합니다.
- 리스트가 비어있으면 새 노드가 헤드가 됩니다.

#### 2. **이중 연결 리스트 (Doubly Linked List)**
이중 연결 리스트는 각 노드가 **이전 노드와 다음 노드**를 가리킵니다. 마치 양방향으로 연결된 자전거 도로 같아요!

**예제 코드: 이중 연결 리스트 노드 구조 및 추가**
```c
// 이중 연결 리스트 노드 구조체 정의
typedef struct DoubledNode {
    int data;           // 데이터
    struct DoubledNode* prev;  // 이전 노드 포인터
    struct DoubledNode* next;  // 다음 노드 포인터
} DoubledNode;

// 이중 연결 리스트 노드 생성 함수
DoubledNode* createDoubledNode(int value) {
    DoubledNode* newNode = (DoubledNode*) malloc(sizeof(DoubledNode));
    newNode->data = value;
    newNode->prev = NULL;
    newNode->next = NULL;
    return newNode;
}

// 이중 연결 리스트 노드 추가 함수
void appendDoubledNode(DoubledNode** head, DoubledNode* newNode) {
    if (*head == NULL) {
        *head = newNode;
        return;
    }
    DoubledNode* temp = *head;
    while (temp->next != NULL) {
        temp = temp->next;
    }
    temp->next = newNode;
    newNode->prev = temp;
}

int main() {
    DoubledNode* head = NULL;
    DoubledNode* node1 = createDoubledNode(10);
    DoubledNode* node2 = createDoubledNode(20);

    appendDoubledNode(&head, node1);
    appendDoubledNode(&head, node2);

    DoubledNode* current = *head;
    while (current != NULL) {
        printf("노드 데이터: %d\n", current->data);
        current = current->next;
    }
    return 0;
}
```

**코드 설명:**
- 이중 연결 리스트는 이전 노드 포인터(`prev`)를 추가로 포함하여 양방향 연결을 지원합니다.
- `appendDoubledNode` 함수는 마지막 노드를 찾아 새로운 노드를 연결합니다.

### 💡 초보자 폭풍 질문! 🚨
**질문 1:** 링크드 리스트에서 메모리 관리는 어떻게 해야 하나요?
- **답변:** 링크드 리스트에서 메모리 할당은 동적 할당을 사용합니다 (`malloc`, `free`). 각 노드를 생성할 때 메모리를 할당하고, 리스트에서 노드를 제거하거나 프로그램이 종료될 때마다 해당 메모리를 `free` 함수로 해제해야 메모리 누수를 방지할 수 있어요.

**질문 2:** 단순 연결 리스트와 이중 연결 리스트 중 어떤 상황에서 어떤 것을 사용해야 하나요?
- **답변:** 
  - **단순 연결 리스트**: 데이터를 순차적으로 처리하거나 추가/삭제가 주로 일어나는 경우에 적합합니다. 예를 들어, 스택(Stack) 구현이나 큐(Queue) 구현에 좋습니다.
  - **이중 연결 리스트**: 양방향 탐색이 필요한 경우나 데이터의 이전 상태를 쉽게 참조해야 할 때 유용합니다. 예를 들어, 브라우저의 뒤로 가기 기능이나 편집기에서의 되돌리기 기능 구현에 적합합니다.

### 🏆 실무주의보
링크드 리스트를 활용할 때 주의할 점이 몇 가지 있어요:
- **성능 고려**: 노드를 삽입하거나 삭제할 때는 특히 이전 노드를 찾아야 하는 경우 시간 복잡도가 증가할 수 있어요 (O(n)). 따라서, 성능 최적화를 위해 적절한 알고리즘 선택이 중요합니다.
- **메모리 관리**: 항상 메모리 누수를 주의해야 합니다. 노드를 제거하거나 프로그램이 종료될 때 메모리를 정확히 해제해야 합니다.

### 🎓 마무리
오늘은 링크드 리스트의 기초를 탄탄히 다졌어요! 이 지식을 바탕으로 더 복잡한 데이터 구조와 알고리즘을 이해하는 데 큰 도움이 될 거예요. 실습을 통해 계속 연습하고 다양한 상황에 적용해보세요. 여러분의 코딩 스킬이 한층 업그레이드될 거예요!

**다음 강의에서는 스택(Stack)과 큐(Queue) 구현에 대해 다룰 예정이니, 그 전까지 링크드 리스트의 마법을 만끽해보세요!** 🌟

---

이 강의가 여러분의 코딩 여정에 빛나는 길잡이가 되길 바랍니다. 궁금한 점이 있으면 언제든지 질문해주세요! 😊

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
