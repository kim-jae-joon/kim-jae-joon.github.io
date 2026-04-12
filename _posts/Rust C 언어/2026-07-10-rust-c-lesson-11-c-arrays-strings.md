---
layout: single
title: "C 언어 배열 및 문자열 처리"
date: 2026-07-10 19:06:38
categories: [Rust C 언어]
---

### 11강: C 언어 배열 및 문자열 처리 - 코딩의 마법 세상으로 초대합니다!

안녕하세요, 코딩의 마법사들! 오늘은 **C 언어 배열**과 **문자열 처리**에 대해 깊이 파고들어 보려 합니다. 이 두 주제는 프로그래밍의 기초이자 튼튼한 기반이 될 거예요. 준비되셨나요? 함께 떠나볼까요!

#### 📚 배열이란 무엇인가요? - 마법의 주문을 배우다

**배열**은 마치 마법사의 마법 상자 같아요. 각각의 슬롯에 특별한 주문(값)을 넣어 두고 필요할 때마다 꺼내 쓰는 거죠. C 언어에서 배열은 동일한 타입의 데이터를 연속된 메모리 공간에 저장합니다.

**예제 1: 기본 배열 사용**

```c
#include <stdio.h>

int main() {
    // 마법 상자(배열)를 5개의 정수로 준비합니다.
    int magicBox[5] = {10, 20, 30, 40, 50}; // 초기값 설정

    // 각각의 주문을 마법 상자에서 꺼내기
    for (int i = 0; i < 5; i++) {
        printf("마법 상자의 %d번째 주문: %d\n", i + 1, magicBox[i]);
    }

    // 또는 직접 인덱스를 통해 접근
    printf("마법 상자의 2번째 주문: %d\n", magicBox[1]); // 출력: 마법 상자의 2번째 주문: 20

    return 0;
}
```

**코드 설명:**
1. `int magicBox[5]` : 크기가 5인 정수 배열을 선언합니다.
2. `{10, 20, 30, 40, 50}` : 배열의 초기값을 설정합니다.
3. `for` 루프를 사용해 배열의 각 요소를 출력합니다. `i`는 인덱스를 나타내며, `i + 1`을 사용해 사용자 친화적인 출력을 만듭니다.
4. `magicBox[1]` : 특정 인덱스에 접근하여 값을 출력합니다.

#### 🧙‍♂️ 배열 조작의 다양한 마법 - 여러 가지 방법으로 접근하기

##### 반복문으로 배열 탐색하기

**반복문 예제: `for`, `while`, `do-while`**

```c
// 1. for 문으로 배열 탐색
for (int i = 0; i < 5; i++) {
    printf("for 문으로 본 주문: %d\n", magicBox[i]);
}

// 2. while 문으로 배열 탐색
int j = 0;
while (j < 5) {
    printf("while 문으로 본 주문: %d\n", magicBox[j]);
    j++;
}

// 3. do-while 문으로 배열 탐색
int k = 0;
do {
    printf("do-while 문으로 본 주문: %d\n", magicBox[k]);
    k++;
} while (k < 5);
```

**코드 설명:**
- **`for` 문**: 간단하고 직관적인 반복 구조입니다. 초기값, 조건, 증감식이 한 줄에 정리되어 있어요.
- **`while` 문**: 조건이 참일 때까지 계속 실행되는 구조로, 유연성이 뛰어납니다.
- **`do-while` 문**: 최소 한 번은 실행되어야 하는 상황에 적합합니다. 이 예제에서는 배열의 끝까지 탐색하는 데 유용해요.

##### 배열의 크기 조절 - 마법 상자 확장하기

**예제 2: 동적 배열 생성**

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int *enchantedSpells = NULL; // 마법 주문 배열 초기화
    int numSpells = 5; // 주문 개수 설정

    // 메모리 동적 할당
    enchantedSpells = (int *)malloc(numSpells * sizeof(int));

    // 초기값 설정
    for (int i = 0; i < numSpells; i++) {
        enchantedSpells[i] = i * 10; // 0부터 시작해 10씩 증가하는 주문들
    }

    // 주문 출력
    for (int i = 0; i < numSpells; i++) {
        printf("마법 상자 %d번째 주문: %d\n", i + 1, enchantedSpells[i]);
    }

    // 메모리 해제 (마법 주문 해제)
    free(enchantedSpells);
    enchantedSpells = NULL; // 중요! 메모리 누수 방지

    return 0;
}
```

**코드 설명:**
1. `malloc`을 사용해 동적으로 메모리를 할당합니다. `sizeof(int)`는 각 요소의 크기를 계산합니다.
2. 초기값을 설정하고 배열 요소를 출력합니다.
3. **메모리 해제**: `free`를 통해 할당된 메모리를 해제하여 메모리 누수를 방지합니다. `enchantedSpells = NULL;`로 안전하게 초기화합니다.

#### ⚙️ 문자열 처리 - 마법의 텍스트 마법

문자열은 마치 마법사의 비밀서적 같아요. 각 글자가 마법의 단어로 구성되어 있어요!

**예제 3: 문자열 다루기**

```c
#include <stdio.h>
#include <string.h>

int main() {
    char magicScript[] = "마법의 주문을 부르세요!"; // 마법의 문장 선언
    int len = strlen(magicScript); // 문자열 길이 구하기

    printf("마법의 문장: %s\n", magicScript);
    printf("마법 문장의 길이: %d\n", len);

    // 문자열 조작 예시: 대문자로 변환
    for (int i = 0; i < len; i++) {
        if (magicScript[i] >= 'a' && magicScript[i] <= 'z') {
            magicScript[i] = magicScript[i] - 'a' + 'A'; // 소문자를 대문자로 변환
        }
    }

    printf("대문자로 변환된 마법 문장: %s\n", magicScript);

    return 0;
}
```

**코드 설명:**
1. `strlen` 함수를 사용해 문자열의 길이를 구합니다.
2. 문자열 내 각 문자를 순회하며 소문자를 대문자로 변환합니다. `ASCII 코드`의 특성을 활용해요!

#### 🚨 실무주의보 🚨
- **메모리 관리**: 동적 할당한 메모리는 반드시 `free`로 해제해야 합니다. 그렇지 않으면 메모리 누수가 발생할 수 있어요!
- **문자열 안전성**: `strlen`과 같은 함수를 사용할 때, 버퍼 오버플로우를 주의하세요. 특히 사용자 입력을 처리할 때는 더욱 신경 써야 합니다.

#### 💡 초보자 폭풍 질문! 💡
1. **Q: 배열의 크기를 동적으로 조절하는 방법은 무엇인가요?**
   - **A:** 동적 할당(`malloc`)을 사용하여 필요에 따라 배열 크기를 늘릴 수 있습니다. 하지만 주의해야 할 점은 메모리 해제(`free`)를 잊지 않는 것입니다.

2. **Q: 문자열에서 특정 글자를 찾는 방법은 무엇인가요?**
   - **A:** `strchr` 함수를 사용하면 쉽게 특정 문자를 찾을 수 있습니다. 예를 들어, `char *pos = strchr(magicScript, 'o');`로 'o'를 찾을 수 있습니다.

이제 여러분도 배열과 문자열 처리의 마법을 어느 정도 이해하셨을 거예요! 실습을 통해 더욱 자신감을 가지게 될 거예요. 코딩은 마법 같아요 – 계속 연습하고 실험하면서 자신만의 마법을 완성해보세요!

다음 강의에서는 더 흥미로운 주제로 만나요! 🌟

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
