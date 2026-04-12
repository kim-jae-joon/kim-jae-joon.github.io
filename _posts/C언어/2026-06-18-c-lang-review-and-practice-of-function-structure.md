---
layout: single
title: "함수 및 구조체: 종합 이해와 실습"
date: 2026-06-18 14:30:37
categories: [C언어]
---

**33강: 함수 및 구조체 - 종합 이해와 실습 🤯**

안녕하세요, 프로그래밍을 처음 배우는 분들을 위한 시그니처 블로그 강의입니다! 👋 오늘은 매우 중요한 주제, **함수와 구조체**에 대해 배울 것입니다. 🔥

**함수란 무엇인가? 🤔**

함수는 프로그램을 작고 단순하게 유지하는 데 도움을주는 가장 강력한 도구 중 하나입니다. 함수는 반복적인 코드를 한 번에 작성하고, 필요할 때 쉽게 호출하여 사용할 수 있습니다.

**구조체란 무엇인가? 🌐**

구조체는 관련된 데이터를 묶어 저장하는 자료형입니다. 구조체 내부의 데이터에 접근하기 위해 선언된 변수나 함수에 이름을 붙여 주어 소스코드 내에서 쉽게 사용할 수 있도록 해줍니다.

**함수 정의 📝**

함수를 정의하려면, 다음 형식으로 function 키워드를 사용합니다.
```c
return-type function_name(인자1, 인자2, ..., 인자N) {
    함수 body;
}
```
*   `return-type` : 함수가 반환하는 자료형입니다. void는 값을 반환하지 않습니다.
*   `function_name` : 함수 이름입니다. 대문자를 사용하면 안됩니다.
*   `인자1`, `인자2`, ..., `인자N` : 함수에 입력할 인수(매개변수)입니다.

**함수 호출 📞**

함수를 호출하려면, 다음 형식을 사용합니다.
```c
return-value = function_name(인자1, 인자2, ..., 인자N);
```
*   `return-value` : 함수가 반환하는 값을 저장할 변수입니다.
*   `function_name` : 호출할 함수 이름입니다.

**구조체 정의 📄**

구조체를 정의하려면, typedef 키워드를 사용합니다. 구조체 내부에 있는 각 데이터 항목은 struct-keyword로 시작하고, 끝에는 세미콜론이 붙습니다.
```c
typedef struct {
    자료형 변수1;
    자료형 변수2;
    ...
} 구조체 이름;
```
*   `자료형` : 변수의 자료형입니다. 예를 들어, int나 float와 같은 기본자료형 또는 char나 string과 같은 구조체입니다.
*   `변수1`, `변수2`, ... : 구조체 내부에 있는 데이터 항목입니다.

**구조체 사용 📊**

구조체를 사용하려면, typedef 키워드가 붙은 구조체 이름을 사용합니다. 예를 들어,
```c
typedef struct {
    int x;
    int y;
} Point;

int main() {
    Point p1; // Point 구조체 변수 p1 선언
    p1.x = 10;
    p1.y = 20;
    printf("p1의 x값: %d, p1의 y값: %d\n", p1.x, p1.y); // p1의 값을 출력
}
```
**함수와 구조체를 함께 사용 🤝**

함수와 구조체를 함께 사용하면 매우 효율적인 프로그래밍이 가능합니다. 예를 들어,
```c
typedef struct {
    int x;
    int y;
} Point;

int calculate_distance(Point p1, Point p2) {
    return sqrt((p2.x - p1.x) * (p2.x - p1.x) + (p2.y - p1.y) * (p2.y - p1.y));
}

int main() {
    Point p1;
    p1.x = 10;
    p1.y = 20;

    Point p2;
    p2.x = 30;
    p2.y = 40;

    printf("두 점 사이의 거리: %d\n", calculate_distance(p1, p2));
}
```
이러한 예제를 통해 함수와 구조체가 어떻게 함께 사용할 수 있는지 보았습니다. 💡

**실습 🔍**

함수와 구조체를 실무에서 활용하는 방법을 알기 위해 다음 과제를 수행하십시오.

1.  `Person` 구조체를 정의하고, 이름, 나이, 주소 정보가 저장되는 `print_person_info` 함수를 작성합니다.
2.  `Person` 구조체에 저장된 정보를 이용하여, 해당 사람의 평균 연령을 계산하는 `calculate_average_age` 함수를 작성합니다.

**해결책 🔑**

1.  `Person` 구조체와 관련된 코드는 다음과 같습니다.

    ```c
typedef struct {
    char name[50];
    int age;
    char address[200];
} Person;

void print_person_info(Person p) {
    printf("이름: %s, 나이: %d, 주소: %s\n", p.name, p.age, p.address);
}

int main() {
    Person p1;
    strcpy(p1.name, "홍길동");
    p1.age = 30;
    strcpy(p1.address, "서울시 영등포구");

    print_person_info(p1);

    return 0;
}
```

2.  `calculate_average_age` 함수는 다음과 같습니다.

    ```c
int calculate_average_age(Person p1, Person p2) {
    int sum = p1.age + p2.age;
    return (sum / 2);
}

int main() {
    Person p1;
    strcpy(p1.name, "홍길동");
    p1.age = 30;

    Person p2;
    strcpy(p2.name, "이순신");
    p2.age = 40;

    printf("두 사람의 평균 연령: %d\n", calculate_average_age(p1, p2));

    return 0;
}
```

**요약 📚**

함수와 구조체는 프로그래밍에서 매우 중요한 개념입니다. 함수를 사용하면 반복적인 코드를 한 번에 작성하고, 필요할 때 쉽게 호출하여 사용할 수 있습니다. 구조체는 관련된 데이터를 묶어 저장하는 자료형으로, 소스코드 내부의 데이터에 접근하기 위해 선언된 변수나 함수에 이름을 붙여 주어 쉽게 사용할 수 있도록 해줍니다.

이러한 개념은 프로그램의 유지보수성과 효율성을 크게 향상시키므로, 프로그래밍 언어를 배울 때 이러한 중요한 개념을 숙지하는 것이 중요합니다. 💡

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
