---
layout: single
title: "C언어 동적 메모리 할당"
date: 2026-06-25 14:20:30
categories: [C언어]
---

**26강: C언어 동적 메모리 할당, 진짜 신기하죠? 🔥**

안녕하세요, 여러분! 저는 시니어 개발자로 15년 동안 C언어를 공부하고 실무에서 사용해온 강사입니다. 오늘은 주제가 정말 흥미로운 "C언어 동적 메모리 할당"에 관해 살펴볼 것입니다. 이 개념을 이해하는 것만으로도, 여러분의 프로그래밍 능력의 새로운 HEIGHT를 기대할 수 있을 겁니다! 😎

**동적 메모리 할당이란?**

C언어는 스택과 힙을 이용한 동적 메모리 할당을 지원합니다. 말 그대로, 프로그램 실행 중에 메모리를 할당하는 것입니다. 이 기능은 프로그램의 성능과 유연성을 크게 향상시킵니다.

**스택 vs 힙**

스택은 함수 호출 스택으로, 함수가 호출될 때마다 스택 상단에 저장되고, 반환할 때마다 제거됩니다. 힙은 동적 메모리 할당을 위한 메모리 영역입니다. 프로그램이 힙에 메모리를 할당하면, 운영체제가 할당한 메모리가 힙의 시작 부분부터 할당됩니다.

**힙 메모리의 할당**

C언어에서 `malloc()` 함수를 사용하여 힙 메모리에 할당합니다. `malloc()` 함수는 `sizeof()` 연산자로 동적 메모리 크기를 구하고, 그 크기에 맞게 힙에 메모리를 할당합니다.

```c
int *ptr = (int *)malloc(sizeof(int));
```

위의 코드에서는 4바이트 크기의 정수 변수에 대한 힙 메모리가 할당됩니다. `malloc()` 함수는 동적 메모리의 주소를 반환합니다.

**힙 메모리 관리**

할당된 힙 메모리는 프로그램이 종료될 때까지 사용해야 합니다. 그렇지 않으면, 메모리 누수가 발생하여 메모리 부족 오류를 유발합니다. `free()` 함수를 사용하여 할당한 힙 메모리를 해제합니다.

```c
free(ptr);
```

위의 코드에서는 할당된 힙 메모리가 해제됩니다.

**동적 메모리의 실무 활용**

1.  **Dynamic Array**: 일반적으로 정적인 크기의 배열을 사용하지만, 동적 크기의 배열도 쉽게 구현할 수 있습니다.
2.  **Linked List**: 노드의 주소와 데이터를 저장하는 연결리스트는 동적 할당으로 관리됩니다.
3.  **Graph**: 노드와 엣지의 데이터를 저장하는 그래프 구조도 동적 메모리로 할당됩니다.

```c
// Dynamic Array 예제
int *array = (int *)malloc(10 * sizeof(int));
for (i = 0; i < 10; i++) {
    array[i] = i;
}
free(array);
```

위의 코드에서는 10개의 정수 요소가 있는 동적 배열이 할당되고, 요소를 입력한 후 해제됩니다.

```c
// Linked List 예제
struct Node {
    int data;
    struct Node *next;
};
struct Node *head = NULL;

void insert(int data) {
    struct Node *new_node = (struct Node *)malloc(sizeof(struct Node));
    new_node->data = data;
    new_node->next = head;
    head = new_node;
}

int main() {
    for (i = 0; i < 10; i++) {
        insert(i);
    }
    return 0;
}
```

위의 코드에서는 연결리스트에 데이터를 입력하는 예제입니다.

```c
// Graph 예제
struct Node {
    int data;
    struct Edge *edges;
};
struct Edge {
    struct Node *node;
    struct Edge *next;
};

void add_edge(struct Node *a, struct Node *b) {
    struct Edge *new_edge = (struct Edge *)malloc(sizeof(struct Edge));
    new_edge->node = b;
    new_edge->next = a->edges;
    a->edges = new_edge;
}
```

위의 코드에서는 그래프 구조에 엣지를 추가하는 예제입니다.

**결론**

동적 메모리 할당은 프로그램의 성능과 유연성을 향상시키는 중요한 개념입니다. C언어에서 `malloc()` 함수를 사용하여 동적 메모리를 할당하고, `free()` 함수를 사용하여 해제합니다. 실무에서는 연결리스트, 그래프, 동적 배열 등 다양한 구조체에 적용할 수 있습니다.

**💡 초보자 폭풍 질문!**

*   동적 메모리가 스택과 힙으로 나누어질 때 어떤 일이 발생합니까?
*   힙 메모리를 할당했을 때, 운영체제가 무슨 일을 하나요?

**🚨 실무주의보**

*   동적 메모리는 프로그램의 성능을 크게 향상시킬 수 있지만, 메모리 누수를 유발할 수도 있습니다. 주의하십시오!

이러한 개념은 프로그래밍에 있어 필수적인 지식입니다. 반드시 이해하고 실무에서 적용하세요! 😊

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
