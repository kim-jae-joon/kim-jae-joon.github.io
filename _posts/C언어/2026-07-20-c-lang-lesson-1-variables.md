---
layout: single
title: "C언어 기초: 변수와 자료형"
date: 2026-07-20 14:16:36
categories: [C언어]
---

**1강: C언어 기초 - 변수와 자료형**

안녕하세요! 여러분, 오늘부터 여러분의 코딩 여정을 함께할 최강의 C언어 일타 강사입니다. 🚀👋 저는 15년 차 시니어 개발자로, C언어를 완벽하게 마스터한 천재적인 개발자가 되겠습니다. 😎

**변수와 자료형: 간단하지만 아슬아슬한 개념**

variable (변수)과 data type (자료형)은 코딩의 가장 기본적인 개념입니다. 하지만 많은 사람들에게 혼란을 주는 부분이기도 합니다.💡 오늘은 이러한 개념을 쉽고 재미있게 알려드리겠습니다.

### 변수 (Variable)

변수는 데이터를 저장하기 위한 메모리 공간을 나타냅니다. 📚 예를 들어, 이름, 나이, 주소와 같은 정보를 저장할 수 있습니다. 변수를 선언하는 방법은 다음과 같습니다.
```c
int name; // 정수형 변수 선언
```
위의 코드는 `name`이라는 변수를 정수형으로 선언한 것입니다. `int`가 자료형입니다.

### 자료형 (Data Type)

자료형은 변수에 저장되는 데이터의 타입을 나타냅니다. 🤔 예를 들어, `int`, `char`, `float`, `double` 등이 있습니다.
```c
// 정수형
int a = 10;

// 문자형
char b = 'A';

// 실수형
float c = 3.14;
```
위의 코드는 각각 `a`, `b`, `c`라는 변수를 정수형, 문자형, 실수형으로 선언한 것입니다.

### 자료형의 종류

자료형은 여러 가지 종류가 있습니다.
#### 1. 정수형 (Integer)
* `int`: 4바이트
* `short int`: 2바이트
* `long int`: 8바이트
```c
int a = 10; // 4바이트
```
#### 2. 문자형 (Character)
* `char`: 1바이트
```c
char b = 'A'; // 1바이트
```
#### 3. 실수형 (Float)
* `float`: 4바이트
* `double`: 8바이트
```c
float c = 3.14; // 4바이트
```
#### 4. 논리형 (Boolean)
* `_Bool`: 1바이트
```c
_Bool d = 0; // 1바이트
```
### 자료형의 크기

자료형의 크기는 바이트 단위로 나타냅니다.
```c
#include <stdio.h>

int main() {
    int a;
    printf("%lu\n", sizeof(a)); // 출력: 4
    return 0;
}
```
위의 코드는 `a`라는 정수형 변수가 4바이트 크기를 갖는 것을 출력합니다.

### 자료형의 연산

자료형은 연산을 할 때도 다양한 특징이 있습니다. 예를 들어, 정수형과 실수형의 경우 자동 캐스팅이 발생할 수 있습니다.
```c
int a = 10;
float b = 3.14;

printf("%f\n", a + b); // 출력: 13.140000
```
위의 코드는 `a`와 `b`를 더하는 연산에서 정수형 `a`가 실수형 `b`로 자동 캐스팅된 것을 보여줍니다.

### 자료형의 활용

자료형은 프로그램을 작성할 때 매우 중요합니다. 예를 들어, 데이터베이스를 설계할 때 데이터 타입을 결정해야 합니다.
```c
#include <sqlite3.h>

int main() {
    sqlite3 *db;
    sqlite3_open("example.db", &db);

    // 테이블 생성
    char *sql = "CREATE TABLE example (id INTEGER, name TEXT)";
    sqlite3_exec(db, sql, NULL, NULL, NULL);

    return 0;
}
```
위의 코드는 SQLite를 사용한 데이터베이스 설계 예시입니다. `INTEGER`과 `TEXT`가 자료형으로 사용된 것을 볼 수 있습니다.

### 결론

변수와 자료형은 코딩의 가장 기본적인 개념입니다. 이 두 가지에 대한 이해는 프로그램을 작성할 때 매우 중요합니다. 💡이 포스트에서는 변수와 자료형에 대한 기초적인 내용을 설명했습니다. 실무에서 사용하는 다양한 예제를 살펴보시면 더 많은 것을 배울 수 있을 것입니다.

👉 **질문 있으시다면 COMMENT로 남겨주세요!** 🤔

### 추가자료

* [C언어 기본문법](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Basic_syntax)
* [자료형의 종류](https://www.w3schools.com/cpp/cpp_data_types.asp)

🚨 **실무주의보**

* 자료형을 잘못 선언하면 프로그램이 비정상적으로 동작할 수 있습니다. 💡
* 데이터베이스를 설계할 때 자료형을 적절하게 선택해야 합니다. 🔹

### 마무리

변수와 자료형에 대한 이해는 코딩의 가장 기본적인 부분입니다. 이 두 가지에 대해 공부하고实전을 반복하면 더 많은 것을 배우고 실무에서 더 많이 도움이 될 것입니다. 💪

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
