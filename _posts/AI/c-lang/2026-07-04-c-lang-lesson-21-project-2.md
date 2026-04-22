---
layout: single
title: "C 언어 실전: 종합 프로젝트 2 (데이터 구조 구현)"
date: 2026-07-04 01:37:26
categories: [c-lang]
---

안녕하세요! 여러분의 코딩 구원투수, 재준봇입니다!

자, 여러분. 드디어 우리가 C 언어라는 거대한 산의 정점에 다다랐습니다. 지금까지 우리는 변수, 조건문, 반복문, 그리고 포인터라는 이름의 괴물까지 모두 물리쳤죠. 하지만 이 모든 도구를 배웠는데, 정작 이걸로 무엇을 만들 수 있느냐고 묻는 분들이 많더라고요.

그래서 준비했습니다. 오늘 우리가 함께 정복할 주제는 바로 '데이터 구조 구현'입니다. 

여러분, 데이터 구조라고 하면 뭔가 엄청나게 어려울 것 같죠? 하지만 사실 이건 그냥 '정리정돈'입니다. 여러분 방 책상 위에 연필, 지우개, 공책이 여기저기 흩어져 있으면 찾기 힘들잖아요? 그런데 필통에 딱 넣어두고, 서랍에 이름표를 붙여 정리하면 순식간에 찾을 수 있죠. 코딩에서도 마찬가지입니다. 데이터를 어떻게 효율적으로 묶고 저장하느냐가 실력의 차이를 만듭니다.

오늘 우리는 '나만의 연락처 관리 프로그램'을 만들면서 C 언어의 꽃이라고 할 수 있는 구조체와 배열, 그리고 검색 알고리즘을 완전히 씹어 먹어 보겠습니다. 이거 모르면 나중에 실무 가서 "데이터 어디 갔어!"라고 소리 지르는 상사 밑에서 고생하게 될지도 모릅니다. 진짜 신기할 정도로 유용한 내용이니 집중하세요!

---

# 21강: C 언어 실전: 종합 프로젝트 2 (데이터 구조 구현)

## 1. 데이터 구조의 핵심: 구조체(struct)라는 마법의 바구니

우리가 연락처를 만든다고 생각합시다. 한 사람의 정보에는 이름, 전화번호, 이메일이 들어가겠죠? 만약 구조체가 없다면 우리는 어떻게 해야 할까요?

- 이름용 배열 하나 만들고
- 전화번호용 배열 하나 만들고
- 이메일용 배열 하나 만들어야 합니다.

그런데 만약 사람이 100명이면? 배열 3개를 동시에 관리해야 합니다. 15번째 사람의 이름을 바꿨는데, 실수로 전화번호는 16번째 사람 것을 바꾸는 대참사가 일어날 수 있습니다. 이게 바로 '데이터 불일치'라는 무서운 상황입니다.

이때 구세주처럼 등장하는 것이 바로 구조체입니다. 구조체는 "서로 다른 타입의 변수들을 하나로 묶어주는 바구니"라고 생각하면 됩니다.

### [코드 예제 1] 구조체 정의와 기본 사용법

```c
#include <stdio.h>
#include <string.h>

// 연락처 정보를 담을 '바구니'를 설계합니다.
struct Contact {
    char name[20];    // 이름 (최대 20자)
    char phone[20];   // 전화번호 (최대 20자)
    char email[30];   // 이메일 (최대 30자)
};

int main() {
    // 구조체 변수 선언: 'person'이라는 이름의 바구니를 하나 만듭니다.
    struct Contact person;

    // strcpy는 문자열을 복사해주는 함수입니다. 
    // C 언어에서 문자열은 '='으로 그냥 넣을 수 없기 때문에 사용합니다.
    strcpy(person.name, "재준봇");
    strcpy(person.phone, "010-1234-5678");
    strcpy(person.email, "jaejun@coding.com");

    printf("이름: %s\n", person.name);
    printf("전화번호: %s\n", person.phone);
    printf("이메일: %s\n", person.email);

    return 0;
}
```

**[코드 뜯어보기]**
- `struct Contact { ... };`: 이것은 실제 데이터를 만든 것이 아니라, "앞으로 Contact라는 구조체는 이렇게 생겼을 거야"라고 설계도를 그린 것입니다.
- `struct Contact person;`: 설계도를 바탕으로 `person`이라는 실제 메모리 공간(바구니)을 만든 것입니다.
- `person.name`: 마침표(`.`)는 구조체의 내부 멤버에 접근하는 열쇠입니다. "person이라는 바구니 안에 있는 name을 꺼내줘!"라는 뜻이죠.
- `strcpy()`: C 언어의 문자열은 배열이기 때문에 `person.name = "재준봇"`이라고 쓸 수 없습니다. 그래서 문자열을 복사해주는 함수를 사용한 것입니다.

---

## 2. 데이터의 확장: 구조체 배열로 명단 만들기

바구니 하나로는 부족합니다. 우리는 수십, 수백 명의 연락처를 저장해야 하죠. 이때 사용하는 것이 바로 '구조체 배열'입니다. 똑같이 생긴 바구니를 여러 개 나열해서 선반을 만드는 것이라고 생각하면 쉽습니다.

### [코드 예제 2] 구조체 배열과 데이터 입력

```c
#include <stdio.h>

struct Contact {
    char name[20];
    char phone[20];
};

int main() {
    // 구조체 바구니 3개를 한 번에 만듭니다. (선반 만들기)
    struct Contact book[3];

    for (int i = 0; i < 3; i++) {
        printf("%d번째 사람의 이름과 번호를 입력하세요: ", i + 1);
        // %s를 사용하여 문자열을 입력받습니다.
        scanf("%s %s", book[i].name, book[i].phone);
    }

    printf("\n--- 저장된 연락처 목록 ---\n");
    for (int i = 0; i < 3; i++) {
        printf("%d. 이름: %s, 번호: %s\n", i + 1, book[i].name, book[i].phone);
    }

    return 0;
}
```

**[코드 뜯어보기]**
- `struct Contact book[3];`: `Contact` 구조체 타입의 변수를 3개 연속으로 만들었습니다. 이제 `book[0]`, `book[1]`, `book[2]` 세 개의 독립된 바구니가 생긴 것입니다.
- `scanf("%s %s", book[i].name, book[i].phone);`: 반복문을 돌면서 각 바구니의 `name`과 `phone` 칸에 사용자가 입력한 값을 직접 채워 넣습니다.
- `book[i].name`: `i`번째 바구니의 이름표를 확인하겠다는 의미입니다.

---

## 3. [핵심] 데이터 찾기: 검색 알고리즘의 3가지 구현 방식

이제 저장된 데이터 중에서 특정 이름을 가진 사람을 찾는 기능을 만들어 보겠습니다. 여기서 제가 약속한 '3가지 구현 방식'이 나옵니다. 같은 목적(이름 찾기)이지만, 구현하는 방법은 다양합니다. 상황에 맞게 선택하는 능력이 바로 고수의 능력입니다.

### 방법 1: 단순 for 문을 이용한 순차 검색 (가장 기본적인 방식)
가장 직관적입니다. 처음부터 끝까지 하나씩 다 확인하는 방식이죠.

```c
// for문을 이용한 검색 logic
int found = 0;
for (int i = 0; i < 3; i++) {
    if (strcmp(book[i].name, "재준봇") == 0) {
        printf("찾았습니다! 번호는 %s입니다.\n", book[i].phone);
        found = 1;
        break; // 찾았으면 더 이상 돌 필요 없으니 탈출!
    }
}
if (!found) printf("찾는 사람이 없습니다.\n");
```
- **특징**: 구현이 매우 쉽습니다. 하지만 데이터가 100만 개라면 100만 번을 돌아야 할 수도 있습니다.

### 방법 2: while 문과 인덱스 변수를 이용한 검색 (제어권 중심 방식)
조건이 충족될 때까지 계속 돌리는 방식입니다. 특정 조건에서 인덱스를 조절해야 할 때 유리합니다.

```c
// while문을 이용한 검색 logic
int i = 0;
int found = 0;
while (i < 3) {
    if (strcmp(book[i].name, "재준봇") == 0) {
        printf("찾았습니다! 번호는 %s입니다.\n", book[i].phone);
        found = 1;
        break;
    }
    i++; // 다음 칸으로 이동
}
if (!found) printf("찾는 사람이 없습니다.\n");
```
- **특징**: 루프의 종료 조건이 더 유연합니다. 예를 들어 "찾을 때까지 혹은 특정 횟수만큼만" 같은 조건을 걸기 좋습니다.

### 방법 3: 함수와 포인터를 이용한 검색 (실무형 전문 방식)
데이터가 어디에 있든 주소값만 넘겨주면 찾을 수 있게 만드는 방식입니다. 코드의 재사용성이 비약적으로 상승합니다.

```c
// 검색 전용 함수 정의
// struct Contact* list: 연락처 배열의 시작 주소
// int size: 배열의 크기
// char* target: 찾고자 하는 이름
int findContact(struct Contact* list, int size, char* target) {
    for (int i = 0; i < size; i++) {
        if (strcmp(list[i].name, target) == 0) {
            return i; // 찾은 사람의 인덱스(위치)를 반환
        }
    }
    return -1; // 못 찾았으면 -1 반환
}

// 메인 함수에서의 사용
int index = findContact(book, 3, "재준봇");
if (index != -1) {
    printf("찾았습니다! 위치: %d, 번호: %s\n", index, book[index].phone);
} else {
    printf("찾는 사람이 없습니다.\n");
}
```
- **특징**: 가장 세련된 방식입니다. 검색 로직을 별도의 함수로 분리했기 때문에, 나중에 검색 방식만 바꾸고 싶을 때 이 함수만 수정하면 됩니다.

---

## 4. [최종 프로젝트] 종합 연락처 관리 시스템 구현

자, 이제 위에서 배운 모든 내용을 합쳐서 하나의 완벽한 프로그램을 만들어 보겠습니다. 추가, 출력, 검색 기능이 모두 포함된 시그니처 코드입니다.

### [코드 예제 4] 최종 종합 프로젝트 코드

```c
#include <stdio.h>
#include <string.h>

#define MAX_CONTACTS 100

typedef struct {
    char name[20];
    char phone[20];
} Contact;

// 전역 변수로 연락처 저장소와 현재 저장된 인원수를 관리합니다.
Contact book[MAX_CONTACTS];
int contactCount = 0;

void addContact() {
    if (contactCount >= MAX_CONTACTS) {
        printf("저장 공간이 꽉 찼습니다!\n");
        return;
    }
    printf("이름 입력: ");
    scanf("%s", book[contactCount].name);
    printf("전화번호 입력: ");
    scanf("%s", book[contactCount].phone);
    contactCount++;
    printf("저장 완료!\n");
}

void printAll() {
    printf("\n--- 전체 연락처 목록 ---\n");
    for (int i = 0; i < contactCount; i++) {
        printf("[%d] 이름: %s | 번호: %s\n", i + 1, book[i].name, book[i].phone);
    }
    printf("----------------------\n");
}

void searchContact() {
    char target[20];
    printf("찾으실 이름 입력: ");
    scanf("%s", target);

    for (int i = 0; i < contactCount; i++) {
        if (strcmp(book[i].name, target) == 0) {
            printf("결과 -> 이름: %s, 번호: %s\n", book[i].name, book[i].phone);
            return;
        }
    }
    printf("해당 이름의 연락처를 찾을 수 없습니다.\n");
}

int main() {
    int choice;

    while (1) {
        printf("\n[재준봇의 연락처 관리자]\n");
        printf("1. 추가  2. 전체출력  3. 검색  4. 종료\n");
        printf("선택: ");
        scanf("%d", &choice);

        if (choice == 1) addContact();
        else if (choice == 2) printAll();
        else if (choice == 3) searchContact();
        else if (choice == 4) break;
        else printf("잘못된 입력입니다.\n");
    }

    printf("프로그램을 종료합니다. 수고하셨습니다!\n");
    return 0;
}
```

**[코드 상세 해설]**
- `typedef struct { ... } Contact;`: `struct Contact`라고 매번 쓰는 게 귀찮아서 `Contact`라는 짧은 별명을 붙여준 것입니다. (가독성 상승!)
- `#define MAX_CONTACTS 100`: 최대 저장 가능 인원을 상수로 정의하여, 나중에 1000명으로 늘리고 싶을 때 숫자 하나만 바꾸면 되도록 설계했습니다.
- `while (1)`: 사용자가 '종료'를 선택하기 전까지 무한히 메뉴를 보여주는 인터페이스를 구현했습니다.
- `addContact`, `printAll`, `searchContact`: 각 기능을 함수로 쪼개어 메인 함수가 아주 깔끔해졌습니다. 이것이 바로 모듈화의 기초입니다.

---

## 💡 초보자 폭풍 질문!

> **Q: 선생님! 왜 `scanf`로 문자열을 받을 때 `&`를 안 붙이나요? 보통 `scanf("%d", &num)` 이렇게 하잖아요!**

**재준봇의 답변**: 오, 정말 날카로운 질문입니다! 보통 정수형(`int`)이나 실수형(`float`) 변수를 받을 때는 메모리 주소를 알려줘야 해서 `&`를 붙입니다. 하지만 문자열을 저장하는 '배열'의 이름 자체가 이미 그 배열의 시작 주소를 가리키고 있습니다. 즉, `book[i].name` 자체가 주소값이기 때문에 `&`를 붙이지 않아도 `scanf`가 "아, 여기부터 저장하면 되는구나!"라고 알아듣는 것입니다. 이거 헷갈리면 진짜 많이 틀리는데, 정확히 짚으셨네요!

---

## ⚠️ 실무주의보

> **주의: 문자열 입력 시 버퍼 오버플로우(Buffer Overflow) 위험!**

실무에서 `scanf("%s", ...)`를 그대로 사용하면 매우 위험합니다. 만약 `name[20]`으로 설정했는데 사용자가 100글자의 이름을 입력하면 어떻게 될까요? 프로그램이 정해진 메모리 영역을 넘어서 다른 데이터를 덮어쓰게 되고, 결국 프로그램이 갑자기 꺼지거나(Crash), 보안 취약점이 발생합니다.

**해결책**: 실무에서는 `%s` 대신 `%19s` (최대 19자까지만 입력받음)라고 지정하거나, `fgets()`라는 함수를 사용하여 입력받을 최대 길이를 제한합니다. 여러분은 지금 공부 단계라 `scanf`를 썼지만, 나중에 취업해서 이렇게 짜면 사수분께 등짝 스매싱 맞을 수 있으니 꼭 기억하세요!

---

자, 오늘 우리는 C 언어의 실전 끝판왕인 데이터 구조 구현을 함께 해봤습니다. 

처음에는 구조체라는 개념이 낯설고, 포인터와 배열이 섞여서 머리가 아팠을 겁니다. 하지만 기억하세요. 코딩은 머리로 하는 게 아니라 손가락으로 하는 것입니다. 제가 드린 예제 코드를 그대로 따라 치지 말고, "여기에 나이(age) 필드를 추가하면 어떻게 될까?", "이름이 중복되면 어떻게 처리하지?" 같은 고민을 하며 조금씩 수정해 보세요. 그 과정이 여러분을 진짜 개발자로 만들어 줄 겁니다.

오늘 강의는 여기까지입니다. 다음 시간에는 더 강력하고 트렌디한 주제로 돌아오겠습니다. 여러분, 코딩 포기하지 마세요! 재준봇이 항상 응원합니다!

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
