---
layout: single
title: "그래프 자료 구조"
date: 2026-06-15 16:00:42
categories: [C언어]
---

## 🔥 36강: 그래프 자료구조, 연결된 세상을 만드는 마법! 🚀

**C언어 일타 강사로서 15년이라는 시간 동안 수많은 개발자들을 보내봤지만,** 이렇게 흥분되는 주제를 가르쳐주는 건 처음인 것 같아요! 🤩 그래프 자료구조, 들으니 뭔가 신비롭고 모험스럽지 않나요? 마치 판타지 소설 속 마법같죠. 🤔 오늘부터 우리도 그래프의 세계로 떠나서 **소통, 연결, 관계**를 나타내는 이 신기한 자료구조를 함께 알아보자!

### 🧙‍♂️ 첫걸음: 그래프란 무엇일까요?

그래프는 간단히 말하자면, **점과 선으로 구성된 그림**입니다. 점이라고 하는 노드는 데이터를 나타내고, 선은 두 노드 사이의 관계를 표현하는 엣지입니다.  🗺️ 마치 도시와 도로를 연결해서 지도를 그리는 것처럼요! 

예를 들어:

* **친구 네트워크**: 친구들을 점으로, 서로 친한 관계를 선으로 나타내면 친구들 사이의 관계가 눈에 드러나는 그래프가 만들어집니다. 
* **웹사이트 링크**: 웹사이트를 점으로, 연결된 링크를 선으로 표현하면 인터넷 네트워크 구조를 시각적으로 파악할 수 있습니다.

🤯 이처럼 다양한 분야에서 그래프는 데이터의 관계와 연결성을 효과적으로 보여주는 강력한 도구가 됩니다!


### 📚 그래프의 종류: 각자의 매력, 각자의 용도!


그래프는 그 구조에 따라 다양하게 분류될 수 있습니다. 가장 흔히 볼 수 있는 유형은 다음과 같습니다:

* **유향 그래프**: 모든 엣지가 방향이 있는 그래프입니다. 예를 들어, 뉴스 기사에서 링크하는 웹사이트처럼 A -> B 라는 특정 방향성을 가진 연결을 나타낼 때 사용됩니다.
  ```c
  // 아래 코드는 유향 그래프의 노드 구조를 나타냅니다.
  struct Node {
    int data; 
    struct Edge* next; // 다음 연결된 노드를 가리키는 포인터
  };

  struct Edge {
    int destination; // 연결되는 노드의 데이터
    struct Edge* next; // 다음 연결된 에지(선)를 가리키는 포인터
  };
  ```
* **비유향 그래프**: 엣지가 방향이 없는 그래프입니다. 친구 관계를 표현할 때 사용되는 경우가 많습니다. 서로 친한 상태라는 정보만 전달하고, 특정 방향은 없으므로 무방향의 연결을 나타냅니다.
  ```c
  // 아래 코드는 비유향 그래프 노드 구조를 나타냅니다. 
  struct Node {
    int data; 
    struct Edge* next; // 다음 연결된 노드를 가리키는 포인터
  };

  struct Edge {
    int destination; // 연결되는 노드의 데이터
    struct Edge* next; // 다음 연결된 에지(선)를 가리키는 포인터
  };
  ```
* **무향 그래프**: 엣지가 없거나, 모든 엣지는 방향이 없는 그래프입니다.


### 🔥 실제 코드 예제: 친구 네트워크 구현하기

친구 관계를 나타내는 비유향 그래프를 C언어로 구현해 볼까요? 😎
```c
#include <stdio.h>
#include <stdlib.h>

// 노드 구조
struct Node {
    int data;          // 친구의 ID 
    struct Node* next; // 다음 친구를 가리키는 포인터
};

// 노드 생성 함수
struct Node* createNode(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->next = NULL; 
    return newNode;
}

// 친구 관계 연결 함수
void addFriendship(struct Node** head, int friend1, int friend2) {
    struct Node* newNode1 = createNode(friend2); // 친구2를 노드로 추가
    struct Node* temp1 = *head; 

    while (temp1->data != friend1) { // 친구1을 찾기 위한 루프
        temp1 = temp1->next;
    }

    newNode1->next = temp1->next; // 친구2를 친구1의 다음 연결 노드로 추가
    temp1->next = newNode1; 
    
    struct Node* newNode2 = createNode(friend1); // 친구1을 노드로 추가
    struct Node* temp2 = *head;

    while (temp2->data != friend2) { // 친구2를 찾기 위한 루프
        temp2 = temp2->next;
    }
    newNode2->next = temp2->next; // 친구1을 친구2의 다음 연결 노드로 추가
    temp2->next = newNode2; 

}


// 친구 네트워크 출력 함수
void printNetwork(struct Node* head) {
    struct Node* current = head;
    while (current != NULL) {
        printf("%d: ", current->data); 
        struct Node* temp = current->next;
        while (temp != NULL) {
            printf("%d -> ", temp->data);
            temp = temp->next;
        }
        printf("\n"); 
        current = current->next;
    }
}

int main() {
    struct Node* head = createNode(1);  // 첫 번째 친구 (ID: 1) 추가
    addFriendship(&head, 1, 2);      // 친구 1과 2 연결
    addFriendship(&head, 1, 3);      // 친구 1과 3 연결

    printNetwork(head); 
    return 0;
}
```


###  💡 초보자 폭풍 질문!

* 그래프 자료구조를 사용하면 어떤 문제들을 해결할 수 있을까요? 🤔
* 친구 네트워크처럼 다른 실제 사례에서 그래프를 활용하는 예시가 있다면 어떻게 생각하시나요? 💡


### 🚀 핵심 알고리즘: 그래프 검색!

그래프 자료구조를 효율적으로 활용하기 위해서는 그래프 내에서 특정 노드나 경로를 찾는 알고리즘이 필수입니다. 🔥  
몇 가지 중요한 알고리즘들을 살펴보겠습니다:

* **Breadth-First Search (BFS)**: 🌲 가상의 나무처럼 층을 만들며 각 노드에서 시작하여 인접한 노드를 방문하는 알고리즘으로, 최단 경로 찾기가 효과적입니다.
* **Depth-First Search (DFS)**: 🌋 같은 깊이까지 갈 수록 모든 노드를 확인하며, 그래프의 복잡한 구조를 파악하기 좋습니다.

###  🚨 실무주의보: 시간복잡도에 주시!

그래프 알고리즘을 선택할 때는 **시간 복잡도**가 중요합니다. 🧐 어떤 알고리즘이 더 효율적으로 데이터 처리하는지 이해하는 것은 프로그램의 성능 향상에 큰 영향을 미칩니다.

### 🧙‍♂️ 그래프의 신비로운 세계, 계속해서 탐험하세요!

오늘은 그래프 자료구조의 기본 개념과 구현 방식을 살펴보았습니다. ✨  
그래프는 데이터 분석, 네트워크 설계, 인공지능 등 다양한 분야에서 활용되는 강력한 도구입니다. 앞으로 더욱 깊이 있게 그래프의 세계를 탐험하고, 실제 프로젝트에 적용하여 자신만의 프로그램을 만들어 보세요! 🚀




<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
