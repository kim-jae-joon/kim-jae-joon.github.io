---
layout: single
title: "함수 포인터와 콜백 함수"
date: 2026-07-09 18:43:17
categories: [C언어]
---

# 12강: 함수 포인터와 콜백 함수 - 코딩의 마법사가 되어보자!

안녕하세요, 코딩의 마법을 함께 탐험하는 여러분! 오늘은 **함수 포인터와 콜백 함수**에 대해 이야기해볼게요. 이건 좀 복잡해 보일 수 있지만, 걱정 마세요! 초보자도 쉽게 이해할 수 있도록 단계별로 차근차근 설명해 드릴게요. 🤔

## 함수 포인터: 함수를 가리키는 마법의 지팡이

### 기본 개념
함수 포인터는 이름 그대로 **함수를 가리키는 포인터**예요. 이걸 사용하면 코드의 유연성이 훨씬 높아지고, 함수를 동적으로 호출할 수 있어요. 마치 마법 지팡이처럼 필요할 때마다 함수를 호출하는 거죠!

#### 예제 1: 기본 함수 포인터 사용
```c
#include <stdio.h>

// 기본 함수 선언
void sayHello() {
    printf("안녕하세요!\n");
}

void greetFunction(void (*funcPtr)()) {
    // 함수 포인터 호출
    funcPtr(); // 여기서 sayHello 함수가 호출됨
}

int main() {
    // 함수 포인터 선언
    void (*ptr)() = sayHello; // 함수 포인터에 함수 주소 할당
    
    // 함수 호출
    greetFunction(ptr); // sayHello 호출
    
    // 다른 함수 호출 예시
    void anotherFunction() {
        printf("다른 인사말!\n");
    }
    greetFunction(anotherFunction); // 다른 함수 호출
    
    return 0;
}
```
**코드 설명:**
1. `sayHello` 함수는 간단한 인사말을 출력합니다.
2. `greetFunction`은 함수 포인터 `funcPtr`을 매개변수로 받아 호출합니다.
3. `ptr` 변수는 `sayHello` 함수의 주소를 가리키게 됩니다.
4. `greetFunction`에서 `ptr`을 통해 `sayHello`를 호출하고, 필요에 따라 다른 함수 `anotherFunction`도 호출할 수 있습니다.

### 왜 필요한 걸까요?
함수 포인터는 다음과 같은 상황에서 유용해요:
- **다양한 동작의 선택**: 사용자 입력에 따라 다른 동작을 수행할 때.
- **코드 재사용성**: 동일한 구조에서 다양한 함수를 동적으로 실행할 때.

### 초보자 폭풍 질문! 🚨
**질문**: 함수 포인터를 사용하면 코드가 복잡해지지 않나요?
**답변**: 처음에는 복잡해 보일 수 있지만, 익숙해지면 코드의 유연성과 재사용성이 크게 향상되어 오히려 효율적인 코드 작성에 도움이 됩니다. 점진적으로 연습하면 자연스럽게 이해할 수 있을 거예요!

## 콜백 함수: 이벤트 핸들러의 마법사

### 기본 개념
콜백 함수는 **함수를 다른 함수의 인자로 전달**하는 기법입니다. 주로 이벤트 처리나 비동기 작업에서 많이 사용됩니다. 마치 마법사의 주문처럼 특정 이벤트가 발생했을 때 특정 동작을 수행하도록 만드는 거죠!

#### 예제 2: 콜백 함수 사용
```c
#include <stdio.h>
#include <stdlib.h>

// 기본 함수 선언
void simpleCallback(int value) {
    printf("콜백 함수 호출: 값은 %d\n", value);
}

// 콜백 함수를 매개변수로 받는 함수
void executeWithCallback(void (*callback)(int), int num) {
    // 콜백 함수 호출
    callback(num); // 특정 값을 전달하여 콜백 함수 호출
}

int main() {
    // 콜백 함수 호출 예시
    executeWithCallback(simpleCallback, 42); // 콜백 함수와 값 전달
    
    // 다른 콜백 함수 예시
    void anotherCallback(int val) {
        printf("다른 콜백 함수 호출: 값은 %d\n", val);
    }
    executeWithCallback(anotherCallback, 100); // 다른 콜백 함수 호출
    
    return 0;
}
```
**코드 설명:**
1. `simpleCallback` 함수는 주어진 값을 출력합니다.
2. `executeWithCallback` 함수는 콜백 함수와 정수 값을 매개변수로 받습니다.
3. `main` 함수에서는 `simpleCallback`과 `anotherCallback`을 각각 호출하며 동작을 다르게 수행합니다.

### 콜백 함수의 활용 사례
- **이벤트 핸들러**: 마우스 클릭이나 키보드 입력 시 특정 동작 수행.
- **비동기 작업**: 작업 완료 시 콜백 함수를 통해 결과 전달.

### 초보자 폭풍 질문! 🚨
**질문**: 콜백 함수를 어떻게 실제 프로젝트에 적용할 수 있을까요?
**답변**: 예를 들어, 웹 애플리케이션에서 AJAX 요청 후 완료 시 결과를 처리하는 데 사용할 수 있어요. 사용자 인터페이스가 비동기적으로 데이터를 가져오고, 콜백 함수를 통해 데이터가 도착했을 때의 동작을 정의할 수 있습니다.

## 다양한 활용 예시: 함수 포인터와 콜백의 힘을 보여주기

### 반복과 조건문 활용
함수 포인터와 콜백은 다양한 제어 구조와 함께 사용됩니다. 예를 들어, 반복문이나 조건문에서 동적으로 동작을 바꿀 수 있어요.

#### 예제 3: 반복문과 콜백 함수
```c
#include <stdio.h>
#include <stdbool.h>

bool shouldContinue = true;

void processItem(const char* item) {
    printf("처리 중인 아이템: %s\n", item);
    if (strcmp(item, "종료") == 0) {
        shouldContinue = false; // 종료 조건 설정
    }
}

void controlLoop(void (*processFunc)(const char*), bool *continueFlag) {
    while (*continueFlag) {
        // 사용자 입력 예시
        const char* userInput = "계속"; // 실제 프로그램에서는 사용자 입력을 받을 수 있음
        
        if (strcmp(userInput, "종료") == 0) {
            *continueFlag = false; // 종료 조건 처리
        } else {
            processFunc(userInput); // 콜백 함수 호출
        }
    }
}

int main() {
    bool continueFlag = true;
    controlLoop(processItem, &continueFlag);
    
    return 0;
}
```
**코드 설명:**
1. `processItem` 함수는 문자열을 처리하고 종료 조건을 설정합니다.
2. `controlLoop` 함수는 콜백 함수 `processFunc`를 사용하여 반복적으로 아이템을 처리합니다.
3. `continueFlag`를 통해 반복문을 제어하며, 사용자 입력에 따라 동작을 변경할 수 있습니다.

### 실무 주의보 🚨
**주의사항**: 함수 포인터와 콜백 함수를 잘못 사용하면 메모리 누수나 예기치 않은 동작이 발생할 수 있습니다. 특히 콜백 함수가 정의되지 않은 상태에서 호출되거나, 함수 포인터가 제대로 초기화되지 않았을 때 문제가 생길 수 있으니 주의하세요!

## 마무리: 코딩의 마법사로 성장하기

함수 포인터와 콜백 함수는 코딩의 마법을 한층 더 풍성하게 만들어 줍니다. 처음에는 헷갈릴 수 있지만, 꾸준히 연습하고 다양한 예제를 통해 익혀나가면 코딩의 유연성과 효율성을 크게 향상시킬 수 있어요.

**💡 초보자 폭풍 질문!** 🤔
**질문**: 함수 포인터와 콜백 함수를 공부하면서 어려운 점이 있다면 무엇인가요?
**답변**: 주로 초기 이해와 메모리 관리 부분에서 어려움을 느끼는 경우가 많아요. 꾸준히 예제를 돌려보고, 직접 함수를 정의해보며 연습하면 점점 익숙해질 거예요!

이제 여러분도 코딩의 마법사가 되어보세요! 다음 강의에서도 더욱 흥미로운 주제로 돌아올게요. 함께 성장해 나가요! 🌟

---

이렇게 상세하고 친근하게 작성하면 초보자들이 함수 포인터와 콜백 함수에 대해 좀 더 쉽게 이해하고 실무에 적용할 수 있을 거예요. 추가 질문이나 더 자세한 설명이 필요하면 언제든지 말씀해 주세요!

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
