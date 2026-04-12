---
layout: single
title: "함수와 포인터: 개념 및 활용"
date: 2026-06-23 14:20:48
categories: [C언어]
---

**28강: 함수와 포인터 - 개념 및 활용**

안녕하세요, 여러분! 제 이름은 최상혁입니다. 저는 15년 차 시니어 개발자로, C언어의 진수사장이라고 일러주기도 하죠. 😊 오늘은 함수와 포인터라는 중요 концеп트를 다뤄볼 거에요.

**함수: 재사용 가능한 코드 블록**

함수는 재사용 가능한 코드 블록입니다. 어떤 작성을 해도, 다시 반복적으로 사용해야 하는 코드가 있나요? 그 때에는 함수를 만들어 보세요! 💡

```c
#include <stdio.h>

// 함수 정의
void sayHello() {
    printf("Hello, World!\n");
}

int main() {
    // 함수 호출
    sayHello();
    return 0;
}
```

위 코드에서 `sayHello()` 함수를 호출할 때마다 "Hello, World!"가 출력되는데요. 이렇게 함수는 여러 번 호출하여 반복적으로 사용할 수 있습니다.

**포인터: 데이터 주소**

포인터란 변수의 주소를 기억하고 있는 변수입니다. 🔑

```c
#include <stdio.h>

int main() {
    int x = 10;
    int* px; // 포인터 선언
    px = &x; // 주소 저장
    
    printf("변수 x의 값: %d\n", x);
    printf("변수 x의 주소: %p\n", (void*)&x); // 주소 출력
    return 0;
}
```

위 코드에서 `px`라는 포인터 변수를 선언한 뒤, 변수 `x`의 주소를 저장하였습니다. `&x`는 변수의 주소를 취합니다.

**함수와 포인터: 함께 사용하기**

함수와 포인터를 함께 사용하면 매우 유용하게 써 볼 수 있습니다. 😎

```c
#include <stdio.h>

// 함수 정의
void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main() {
    int x = 10;
    int y = 20;
    
    printf("변수 x: %d\n", x);
    printf("변수 y: %d\n", y);
    
    swap(&x, &y); // 함수 호출
    
    printf("변수 x: %d\n", x);
    printf("변수 y: %d\n", y);
    
    return 0;
}
```

위 코드에서 `swap()` 함수를 사용하였습니다. 이 함수는 두 변수의 값을 교환하는 역할을 합니다.

**함수와 포인터: 실무 활용**

함수와 포인터를 잘 이해하고 사용하면, 많은 문제들을 해결할 수 있습니다. 🚀

```c
#include <stdio.h>
#include <stdlib.h>

// 함수 정의
void* malloc(int size) {
    // 메모리 할당 코드
}

int main() {
    int* px = (int*)malloc(sizeof(int)); // 동적 메모리 할당
    
    if(px == NULL) { // 에러 처리
        printf("메모리 할당 실패\n");
        return 1;
    }
    
    *px = 10; // 값 저장
    
    printf("변수 x: %d\n", *px);
    
    free(px); // 메모리 해제
    
    return 0;
}
```

위 코드에서 `malloc()` 함수를 사용하였습니다. 이 함수는 동적 메모리를 할당해 주는 역할을 합니다.

**요약**

함수와 포인터는 코딩을 할 때 매우 중요합니다. 함수는 재사용 가능한 코드 블록, 포인터는 데이터 주소를 기억하고 있는 변수입니다. 함께 사용하면, 많은 문제들을 해결할 수 있습니다. 🔥

이번 강의에서는 함수와 포인터에 대한 개념과 활용을 다루었고, 실무 예시를 통해 어떻게 사용할 수 있는지 보았습니다. 💡

**실습**

* 함수와 포인터의 차이를 이해하고, 각자 알아본 코드를 작성해 보세요.
* 함수로 동적 메모리 할당 및 해제를 구현해 보세요.

함수와 포인터는 코딩을 할 때 반드시 알고 있어야 하는 개념입니다. 💪

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
