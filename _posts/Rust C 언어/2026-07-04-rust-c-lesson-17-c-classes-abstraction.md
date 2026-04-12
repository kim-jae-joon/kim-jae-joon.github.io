---
layout: single
title: "C 언어 클래스 개념 소개 (추상화)"
date: 2026-07-04 19:08:01
categories: [Rust C 언어]
---

## 🚀 17강: C 언어 클래스 개념, 너의 코드 세계를 넓혀줄 마법의 열쇠! (추상화 마스터하기)

안녕하세요, 코드 모험가 여러분! 💪 오늘은 **C 언어의 신비로운 세계, 추상화**에 대해 깊이 있게 탐험해 보려 합니다. 혹시 "추상화?"라는 단어를 듣고 머리가 복잡해지는 듯한 느낌이 드나요? 걱정 마세요! 진짜 신기하죠? 추상화는 마치 복잡한 도시 속에서 깔끔한 지도를 얻는 것과 같답니다. 

**"왜 추상화가 필요할까?"**

상상해 보세요. 처음 프로그래밍을 배울 때, 모든 변수, 함수, 포인터가 복잡하게 얽혀 있던 경험이 있으시죠? 마치 광활한 컴퓨터 속 던전을 혼자 탐험하는 것 같았을 겁니다! 😵 이때 추상화는 우리에게 **'핵심 기능'만 간결하게 보여주는 마법의 렌즈** 역할을 합니다. 복잡한 코드 뒤에 숨겨진 핵심 원리를 이해하도록 도와주는 거죠!

### 🧩 추상화, 핵심만 챙기는 마법사

추상화는 **세부적인 구현 세부 사항을 숨기고 핵심 개념만 드러내는 기술**입니다. 마치 자동차 엔진의 복잡한 작동 원리를 이해하지 못해도 **"엑셀을 밟으면 앞으로 나간다"**는 기본 원리만 알면 충분히 운전할 수 있는 것과 같죠!

#### 예제 1: `struct`를 활용한 클래스 모방

C 언어에는 **`struct`**라는 강력한 도구를 통해 간단한 추상화를 구현할 수 있습니다. 예를 들어, `사람`이라는 개념을 추상화해 보겠습니다.

```c
#include <stdio.h>

// 1. '사람'이라는 추상적인 개념 정의 (struct)
struct Person {
    char name[50];  // 이름 저장 (이름이 길 수도 있으니 충분한 공간 할당)
    int age;        // 나이 저장
    
    // 함수 포인터를 통해 동작 추가 가능 (예시: 미래 확장성)
    void (*greet)(struct Person*); // 인사 메소드 추상화
};

// 2. 구조체에 맞는 데이터 초기화 함수
void initializePerson(struct Person* person, const char* name, int age) {
    strcpy(person->name, name); // 이름 복사
    person->age = age;          // 나이 설정
    person->greet = &sayHello;  // 인사 메소드 설정
}

// 3. 인사 메소드 구현 (추상화된 동작)
void sayHello(struct Person* person) {
    printf("안녕하세요, 제 이름은 %s이고 나이는 %d살입니다!\n", person->name, person->age);
}

int main() {
    struct Person john; // '사람' 추상체 생성
    initializePerson(&john, "존", 30); // 초기화
    john.greet(&john); // 추상화된 메소드 호출

    return 0;
}
```

**코드 해부:**

- **`struct Person`**: '사람'이라는 추상적인 개념을 정의합니다. 이름과 나이라는 데이터와, `greet`라는 **함수 포인터**를 통해 인사 동작을 추상화합니다.
- **`initializePerson`**: 구조체 데이터를 초기화하고, 추상화된 인사 메소드를 연결합니다. 마치 '사람' 객체를 실제로 만드는 마법사 같죠!
- **`sayHello`**: 실제 인사 동작을 구현합니다. 추상화된 개념(`greet`)을 통해 다양한 동작을 쉽게 적용할 수 있게 합니다.

**💡 초보자 폭풍 질문!**  
Q: 왜 `struct`를 사용해 클래스처럼 만드는 건가요?  
A: C 언어는 순수 객체 지향 언어가 아니지만, `struct`를 통해 데이터와 관련 동작을 하나로 묶어 추상화할 수 있습니다. 이는 코드의 가독성과 유지보수성을 크게 향상시키죠!

### 💡 실전 적용: 다양한 추상화 기법

추상화는 한 가지 형태로만 존재하는 게 아닙니다. 여러 방법으로 구현할 수 있어요!

#### 예제 2: 함수 추상화 - 반복 작업 단순화

```c
#include <stdio.h>

// 1. 복잡한 반복 작업을 단순화하는 함수 추상화
void printNumbers(int start, int end) {
    for (int i = start; i <= end; i++) { // 반복문 사용 (for문 예시)
        printf("%d ", i);
    }
    printf("\n");
}

int main() {
    printNumbers(1, 5); // 1부터 5까지 출력
    return 0;
}
```

**코드 해부:**

- **`printNumbers` 함수**: 숫자 출력이라는 복잡한 반복 작업을 **단일 함수 호출**로 단순화합니다. 이는 `for` 문을 직접 쓰는 것보다 코드가 훨씬 간결해집니다.

#### 예제 3: 조건문 추상화 - 다양한 시나리오 처리

```c
#include <stdio.h>

// 1. 조건에 따른 동작 추상화 (if-else 예시)
int checkAge(int age) {
    if (age >= 18) {
        printf("성인입니다!\n"); // 특정 조건 만족 시 동작
        return 1;
    } else {
        printf("미성년자입니다.\n"); // 다른 조건 시 동작
        return 0;
    }
}

int main() {
    checkAge(20); // 성인 확인
    checkAge(15); // 미성년자 확인
    return 0;
}
```

**코드 해부:**

- **`checkAge` 함수**: 나이에 따른 다양한 동작을 **하나의 함수**로 추상화하여 재사용성을 높입니다. 만약 나이 조건이 더 복잡해지면 `if-else` 문을 확장하거나 `switch` 문으로 전환할 수도 있습니다.

#### 예제 4: `switch` 문을 통한 선택지 추상화

```c
#include <stdio.h>

// 1. 여러 선택지를 간결하게 처리하는 switch 문 추상화
void menuSelector(int choice) {
    switch (choice) {
        case 1:
            printf("메뉴 1 선택!\n");
            break; // 각 선택지 종료
        case 2:
            printf("메뉴 2 선택!\n");
            break;
        default:
            printf("잘못된 선택입니다.\n");
    }
}

int main() {
    menuSelector(1); // 메뉴 선택 예시
    return 0;
}
```

**코드 해부:**

- **`menuSelector` 함수**: 사용자 입력에 따른 다양한 동작을 **`switch` 문**을 통해 간결하게 처리합니다. 이는 코드의 가독성을 크게 향상시키고 유지보수를 용이하게 합니다.

### 🚨 실무주의보

**주의사항**: 추상화는 강력하지만, 과도한 추상화는 오히려 코드 이해를 어렵게 만들 수 있습니다. 핵심은 **명확한 목표 설정**과 **적절한 수준의 추상화**를 유지하는 것입니다. 초보자 여러분, 꾸준히 코드를 작성하며 다양한 추상화 기법을 실험해 보세요! 실수도 성장의 기회니까요! 😊

---

오늘 배운 추상화의 마법을 통해 복잡한 코드 세계를 더욱 쉽게 탐험할 수 있을 거예요! 다음 강의에서는 더 흥미로운 주제로 찾아뵙겠습니다. 그럼, 코딩 모험 계속해서 즐기세요! 🎉💻

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
