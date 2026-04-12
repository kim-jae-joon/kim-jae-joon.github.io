---
layout: single
title: "조건문: if, else, switch 문"
date: 2026-07-15 18:41:48
categories: [C언어]
---

# 6강: 조건문: if, else, switch 문 - 코딩의 마법 같은 스위치 켜기!

안녕하세요, 코딩의 마법사 여러분! C언어의 세계에서 오늘은 마법 같은 조건문에 대해 함께 모험을 떠나보겠습니다. 만약 **만약에 날씨가 갑자기 폭풍우로 바뀌었다면 어떻게 할 거예요?** 🌪️  정답은 바로 **조건문**이죠! 오늘 배울 **if, else, switch 문**은 코딩에서 가장 중요한 마법 주문 중 하나입니다. 초보자 여러분도 걱정하지 마세요, 함께 하면 쉽게 이해할 수 있을 거예요!

## if 문: 마법의 문을 열다

**if 문**은 가장 기본적인 조건문으로, 특정 조건이 참일 때만 코드 블록을 실행시킵니다. 마치 마법의 문을 열고 닫히는 것처럼 작동해요!

### 기본 구조
```c
if (조건식) {
    // 조건식이 참이면 이 코드 실행
    printf("폭풍우가 시작됩니다!\n");
} else {
    // 조건식이 거짓이면 이 코드 실행
    printf("평화로운 날씨입니다.\n");
}
```

#### 코드 해부
1. **if (조건식)**: 괄호 안에 넣는 조건식이 참이면 코드 블록이 실행됩니다. 예를 들어, `온도 > 30` 이라면 "폭풍우 시작" 메시지가 출력됩니다.
2. **{}**: 코드 블록을 묶어주는 중괄호입니다. 여기에 여러 줄의 코드를 넣을 수 있어요.
3. **else**: 만약 조건식이 거짓이면 `else` 블록의 코드가 실행됩니다. 평화로운 날씨 메시지가 출력되는 거죠!

### 예제 1: 온도 기반 날씨 예보
```c
int currentTemp = 35; // 현재 온도 설정
if (currentTemp > 30) {
    printf("폭풍우 경보! 온도가 %d도입니다.\n", currentTemp);
} else {
    printf("평범한 날씨입니다. 온도는 %d도.\n", currentTemp);
}
```
**해설**: 온도가 30도를 넘으면 폭풍우 경보 메시지를 출력합니다.

### 예제 2: 숫자 맞추기 게임
```c
#include <stdio.h>
int main() {
    int guess = 7; // 사용자의 추측값
    int correctNumber = 7; // 정답

    if (guess == correctNumber) {
        printf("정답이에요! 축하합니다.\n");
    } else {
        printf("틀렸어요! 다시 시도해보세요.\n");
    }
    return 0;
}
```
**해설**: 사용자의 추측값과 정답을 비교하여 피드백을 줍니다.

## else if 문: 마법의 추가 문

`if`만으로는 조금 부족할 때가 있죠? 그럴 때 **else if**를 사용하면 여러 조건을 순차적으로 확인할 수 있어요!

### 구조
```c
if (조건1) {
    // 조건1 참이면 실행
} else if (조건2) {
    // 조건2 참이면 실행
} else {
    // 모든 조건이 거짓이면 실행
}
```

### 예제 3: 다양한 날씨 상태 판별
```c
int weatherCode = 2; // 날씨 상태 코드 (1: 맑음, 2: 구름, 3: 비)
if (weatherCode == 1) {
    printf("맑은 날씨입니다.\n");
} else if (weatherCode == 2) {
    printf("구름이 많은 날이네요.\n");
} else if (weatherCode == 3) {
    printf("비가 오는 날입니다.\n");
} else {
    printf("알 수 없는 날씨 상태입니다.\n");
}
```
**해설**: 날씨 코드에 따라 다양한 날씨 상태를 출력합니다.

## switch 문: 마법의 다중 선택기

`switch` 문은 `if-else`보다 간결하게 여러 조건을 처리할 때 유용해요. 마치 마법의 다중 선택기 같죠!

### 기본 구조
```c
switch (표현식) {
    case 값1:
        // 값1과 일치하면 이 코드 실행
        break;
    case 값2:
        // 값2와 일치하면 이 코드 실행
        break;
    default:
        // 모든 케이스가 일치하지 않으면 이 코드 실행
}
```

#### 코드 해부
1. **switch (표현식)**: `switch` 문은 주어진 표현식의 값을 기준으로 코드를 실행합니다.
2. **case 값**: 각각의 케이스는 특정 값에 대응합니다.
3. **break**: 중요해요! `break` 문이 없으면 다음 케이스로 넘어가는 ** fall-through ** 현상이 발생할 수 있어요.
4. **default**: 모든 케이스가 일치하지 않을 때 실행되는 기본 코드 블록입니다.

### 예제 4: 메뉴 선택 시스템
```c
#include <stdio.h>
int main() {
    int choice = 3; // 사용자 선택 번호

    switch (choice) {
        case 1:
            printf("메뉴 1 선택: 식사 주문 완료!\n");
            break;
        case 2:
            printf("메뉴 2 선택: 디저트 주문 완료!\n");
            break;
        case 3:
            printf("메뉴 3 선택: 음료 주문 완료!\n");
            break;
        default:
            printf("잘못된 선택입니다. 다시 선택해주세요.\n");
    }
    return 0;
}
```
**해설**: 사용자의 선택에 따라 다양한 메뉴 주문을 처리합니다.

### 예제 5: 학점 등급 판별
```c
#include <stdio.h>
int main() {
    float score = 85.5; // 학생의 점수

    switch ((int)(score / 10)) { // 점수를 10단위로 나눔
        case 9:
            printf("A+ 등급!\n");
            break;
        case 8:
            printf("A 등급!\n");
            break;
        case 7:
            printf("B+ 등급!\n");
            break;
        case 6:
            printf("B 등급!\n");
            break;
        default:
            printf("C 등급 이하.\n");
    }
    return 0;
}
```
**해설**: 점수를 기준으로 학점 등급을 판별합니다.

## 초보자 폭풍 질문! 🚨
**Q**: `if`와 `switch` 문을 언제 사용해야 하나요?
**A**: `if` 문은 다양한 조건을 순차적으로 확인할 때 유용합니다. 반면에 `switch` 문은 **정수 값**이나 **특정 열거형**에 대해 빠르고 간결하게 처리해야 할 때 적합합니다. 예를 들어, 메뉴 선택이나 학점 등급 판별 같은 경우 `switch`가 더 효율적입니다.

## 실무주의보
**🚨 실무에서의 주의사항**:
- **중복 `break`**: `switch` 문에서 각 케이스마다 `break`를 생략하면 **fall-through** 현상이 발생할 수 있으므로 주의해야 합니다.
- **복잡한 조건**: 너무 복잡한 `if-else` 연쇄는 코드 가독성을 저하시키므로 가능한 간결하게 유지하세요.

오늘 배운 조건문으로 여러분의 코드는 훨씬 더 똑똑해졌을 거예요! 아직 헷갈리는 부분이 있다면 언제든지 물어보세요. 함께 성장해 나가는 게 중요하니까요! 다음 강의에서 또 만나요! 🌟

---

이 강의가 여러분의 코딩 여정에 작은 마법처럼 작용하길 바라요! 💪🎓

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
