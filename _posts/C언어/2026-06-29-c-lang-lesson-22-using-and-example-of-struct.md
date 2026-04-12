---
layout: single
title: "C언어 구조체 사용법 및 예제"
date: 2026-06-29 14:20:00
categories: [C언어]
---

**22강: C언어 구조체 사용법 및 예제**

😎 안녕하세요, 여러분! 오늘은 정말 중요하고 기초적인 주제를 다룰 거예요. 구조체! 😊 많은 개발자들이 구조체에 대해 잘 이해하지 못하거나 사용하는 방법도 제대로 알고 있지 못한다면, 그들은 나중에 큰 수고와 오류의 씨앗을 심게 될 수도 있습니다. 🌱

**왜 구조체가 필요한가요?**

🤔 구조체는 데이터를 그룹화하고 조직화할 때 사용합니다. 예를 들어, 사람의 정보를 저장할 때 이름, 나이, 전화번호, 주소와 같은 정보를 하나하나 따로 관리하는 것보다 더 효율적으로 데이터를 처리하고 저장할 수 있습니다.

**구조체 기본 개념**

📚 구조체는 다음과 같은 특성을 갖습니다:

*   **데이터 형식**: 구조체 안의 데이터가 어떤 종류인지 정의합니다. 예를 들어, `int`는 정수형, `float`은 실수형입니다.
*   **멤버 변수**: 구조체 안에 포함된 데이터 항목입니다. 예를 들어, 사람의 이름, 나이, 전화번호 등이 멤버 변수입니다.

**구조체 선언 및 사용**

```c
// 구조체 선언
struct Person {
    char name[20];
    int age;
    long phone;
};

int main() {
    // 구조체 인스턴스 생성
    struct Person person1;

    // 멤버 변수 접근하기
    strcpy(person1.name, "Kim");
    person1.age = 25;
    person1.phone = 01012345678L;

    printf("이름: %s\n", person1.name);
    printf("나이: %d\n", person1.age);
    printf("전화번호: %ld\n", person1.phone);

    return 0;
}
```

💡 초보자 폭풍 질문!

*   구조체 선언과 사용은 어렵나요? 🤔
*   구조체 안의 데이터 형식을 변경할 수 있나요?

👉 아뤼, 구조체는 상당히 유연합니다! 👍

**구조체 관련 함수**

📚 구조체에 대한 다양한 함수가 있습니다. 예를 들어:

*   `sizeof()`: 구조체 크기를 리턴합니다.
*   `&`: 구조체의 주소 값을 리턴합니다.

```c
// sizeof() 사용하기
struct Person person1;
printf("구조체 크기: %lu\n", sizeof(person1));

// & 사용하기
struct Person *ptr = &person1;
printf("주소 값: %p\n", ptr);
```

🚨 실무주의보!

*   구조체와 포인터는 무척 주의해서 사용하세요! 🌪️

**구조체 활용 예제**

```c
// 학생 정보를 저장할 구조체 선언하기
struct Student {
    char name[20];
    int grade;
    float score;
};

int main() {
    // 구조체 인스턴스 생성하기
    struct Student student1;

    // 멤버 변수 설정하기
    strcpy(student1.name, "Kim");
    student1.grade = 3;
    student1.score = 80.5f;

    printf("이름: %s\n", student1.name);
    printf("학년: %d\n", student1.grade);
    printf("점수: %.2f\n", student1.score);

    return 0;
}
```

🌟 구조체는 정말 강력한 도구입니다! 💪

**정리**

📚 오늘은 구조체의 기본 개념, 선언 및 사용, 관련 함수, 활용 예제 등을 다루었습니다. 구조체를 잘 이해하고 활용하실 수 있도록 도와드렸습니다.

💡 마지막으로, 구조체는 개발자에게 중요한 역량을 제공합니다. 💻

👋 그럼 이만 인사 drifted! 👋

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
