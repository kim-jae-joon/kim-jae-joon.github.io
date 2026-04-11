---
layout: post
title: "함수와 구조체: 모듈화와 복합 데이터"
date: 2026-04-12 05:11:14
categories: [C 언어 Programming]
---

안녕하세요, 여러분! C 언어 정복의 길을 함께 걷고 있는 여러분의 일타 강사, **쭈니**입니다! 🥳

벌써 5강에 오신 걸 진심으로 환영합니다! 지난 1강부터 4강까지 변수, 연산자, 조건문, 반복문 등 C 언어의 기본 골격을 차근차근 다져왔는데요. 이제 코드가 조금씩 길어지고 복잡해지기 시작할 거예요.

혹시 이런 고민 해보신 적 있으신가요?
"코드가 너무 길어져서 어디서부터 손대야 할지 모르겠어요..." 😥
"비슷한 코드를 계속 반복해서 쓰고 있는 것 같아요..." 😒
"학생 정보를 저장하려는데, 이름은 `char name[50]`, 학번은 `int student_id`, 학점은 `double grade`... 이렇게 변수를 따로따로 관리하니까 너무 헷갈려요!" 🤯

네, 맞아요! 이런 문제들은 코드가 성장하면서 자연스럽게 마주하게 되는 벽입니다. 하지만 걱정 마세요! 오늘 제가 준비한 **'함수'** 와 **'구조체'** 가 바로 이 문제들을 해결해 줄 C 언어의 강력한 무기들이랍니다!

이번 5강에서는 코드를 깔끔하게 정리하고 재사용 가능하게 만들어주는 **'함수'** 에 대해 배우고, 여러 종류의 데이터를 하나로 묶어 관리하는 **'구조체'** 에 대해 완벽하게 마스터할 겁니다. 이 두 가지 개념만 제대로 익혀도 여러분의 코딩 실력은 한 단계 아니, 두 단계 아니, 열 단계는 점프업 할 거예요! 기대되시죠? 자, 그럼 저 쭈니와 함께 신나는 C 언어의 세계로 떠나볼까요?! 출발~! 🚀

---

## 🚀 5강: 함수와 구조체: 모듈화와 복합 데이터

---

### 1. 코드를 깔끔하게 정리하는 마법! '함수(Function)'

**"함수(Function)"** 란 특정 작업을 수행하는 코드들의 묶음입니다. 우리가 매일 사용하는 프로그램들은 수십만, 수백만 줄의 코드로 이루어져 있는데요, 이 모든 코드를 한 덩어리로 관리한다면 상상만 해도 끔찍하겠죠? 😨

함수는 이 거대한 코드를 작은 단위의 작업들로 쪼개어 관리할 수 있게 해줍니다. 마치 레고 블록처럼, 각 블록(함수)은 특정 기능을 수행하고, 이 블록들을 조립해서 더 크고 복잡한 프로그램을 만드는 거죠!

**왜 함수를 써야 할까요? 🤔**

1.  **모듈화 (Modularity):** 프로그램을 여러 개의 작은 조각(모듈)으로 나눌 수 있어, 코드 관리가 훨씬 쉬워집니다.
2.  **코드 재사용 (Code Reusability):** 한번 만들어둔 함수는 필요할 때마다 몇 번이고 다시 호출해서 사용할 수 있습니다. 똑같은 코드를 여러 번 쓸 필요가 없어져요!
3.  **코드 가독성 (Readability):** 각 함수가 어떤 역할을 하는지 이름을 통해 명확히 알 수 있어, 다른 사람이 코드를 읽거나 나중에 내가 다시 코드를 볼 때 이해하기 쉽습니다.
4.  **오류 수정 용이 (Easier Debugging):** 문제가 발생했을 때, 어느 함수에서 문제가 생겼는지 빠르게 파악하고 수정할 수 있습니다.

#### 1.1. 함수의 기본 구조: 선언, 정의, 호출

함수를 사용하려면 크게 세 단계가 필요합니다.

*   **선언 (Declaration) / 프로토타입 (Prototype):** "이런 이름의 함수가 있고, 어떤 값을 받고 어떤 값을 돌려줄 거야!" 라고 컴파일러에게 미리 알려주는 과정입니다. (일종의 예고편!)
*   **정의 (Definition):** "자, 이 함수가 실제로 어떤 작업을 하는지 보여줄게!" 라고 코드를 작성하는 과정입니다. (본편!)
*   **호출 (Call):** "이 함수야, 너 이제 이 작업을 수행해!" 라고 함수를 실행시키는 과정입니다. (실행 버튼!)

```c
#include <stdio.h>

// 1. 함수의 선언 (프로토타입)
// 반환값 타입    함수이름 (매개변수 타입1 매개변수이름1, ...);
void print_hello(); // "안녕"을 출력하는 함수가 있다고 미리 알려줍니다.
int add_numbers(int a, int b); // 두 정수를 받아서 합계를 반환하는 함수가 있다고 알려줍니다.

int main() {
    printf("--- main 함수 시작 ---\n");

    // 3. 함수 호출
    print_hello(); // print_hello 함수를 실행해!

    int num1 = 10;
    int num2 = 20;
    int sum = add_numbers(num1, num2); // add_numbers 함수를 실행하고, 반환값을 sum 변수에 저장해!
    printf("두 수의 합: %d\n", sum);

    printf("--- main 함수 종료 ---\n");
    return 0; // main 함수도 하나의 함수이므로, 값을 반환합니다.
}

// 2. 함수의 정의
void print_hello() { // 선언과 동일한 형태의 함수 헤더
    printf("안녕하세요! 함수 호출 성공!\n"); // 이 함수가 실제로 하는 일
}

int add_numbers(int a, int b) { // 선언과 동일한 형태의 함수 헤더
    int result = a + b; // 매개변수 a와 b를 받아서 덧셈을 수행
    return result; // 계산 결과를 반환
}
```

**코드 설명:**

*   `void` 는 "반환할 값이 없다"는 의미입니다. `print_hello` 함수는 단순히 메시지를 출력하고 끝내기 때문에 `void`를 사용합니다.
*   `int add_numbers(int a, int b)`: 이 함수는 두 개의 `int`형 정수 `a`와 `b`를 **매개변수(parameter)** 로 받아서, `int`형 정수 값을 **반환(return)** 합니다.
*   `return result;`: `add_numbers` 함수가 `result` 변수에 담긴 값을 호출한 곳(`main` 함수)으로 돌려줍니다.

#### 1.2. 함수를 이용한 예제: 사각형 넓이 계산기

자, 그럼 함수를 사용해서 사각형의 넓이를 계산하는 프로그램을 만들어볼까요?

```c
#include <stdio.h>

// 사각형의 넓이를 계산하여 반환하는 함수
// 매개변수: 가로 (width), 세로 (height)
// 반환값: 넓이 (int)
int calculate_rectangle_area(int width, int height) {
    if (width <= 0 || height <= 0) {
        printf("경고: 가로와 세로는 양수여야 합니다. 0을 반환합니다.\n");
        return 0; // 잘못된 입력일 경우 0 반환
    }
    int area = width * height;
    return area; // 계산된 넓이 반환
}

// 메인 함수
int main() {
    int rect1_width = 5;
    int rect1_height = 8;
    int rect1_area;

    // 첫 번째 사각형의 넓이 계산 및 출력
    rect1_area = calculate_rectangle_area(rect1_width, rect1_height);
    printf("첫 번째 사각형의 가로: %d, 세로: %d\n", rect1_width, rect1_height);
    printf("첫 번째 사각형의 넓이: %d\n", rect1_area);
    printf("---------------------------\n");

    int rect2_width = 10;
    int rect2_height = 3;
    int rect2_area;

    // 두 번째 사각형의 넓이 계산 및 출력
    rect2_area = calculate_rectangle_area(rect2_width, rect2_height);
    printf("두 번째 사각형의 가로: %d, 세로: %d\n", rect2_width, rect2_height);
    printf("두 번째 사각형의 넓이: %d\n", rect2_area);
    printf("---------------------------\n");

    // 잘못된 입력 테스트
    int invalid_area = calculate_rectangle_area(-2, 7);
    printf("잘못된 입력으로 계산된 넓이: %d\n", invalid_area);

    return 0;
}
```

**쭈니's Tip! 💡**
`main` 함수 위에 `calculate_rectangle_area` 함수를 정의했기 때문에 따로 선언(프로토타입)을 해주지 않아도 컴파일러가 알아서 인식합니다. 하지만 일반적으로 코드를 더 깔끔하게 관리하기 위해 모든 함수를 `main` 함수 *위에* 선언하고, `main` 함수 *아래에* 정의하는 방식을 많이 사용합니다.

---

### 2. 나만의 데이터 타입을 만들자! '구조체(Struct)'

여러분, 우리가 학생 정보를 관리하는 프로그램을 만든다고 상상해 보세요. 학생 한 명당 이름, 학번, 학점, 전공 등 여러 정보가 필요하겠죠?

이 정보를 각각의 변수로 저장한다면 어떻게 될까요?
`char name1[50]; int student_id1; double grade1; char major1[50];`
`char name2[50]; int student_id2; double grade2; char major2[50];`
...

휴, 벌써부터 머리가 지끈거리죠? 이렇게 관련된 정보들을 따로따로 관리하면 코드가 복잡해지고 실수하기도 쉽습니다.

이럴 때 필요한 것이 바로 **"구조체(Struct)"** 입니다! 구조체는 여러 종류의 변수(데이터)들을 하나로 묶어 '나만의 새로운 데이터 타입'을 만드는 문법입니다. 마치 여러 부품을 조립해서 '자동차'라는 하나의 새로운 제품을 만드는 것과 같아요! 🚗

#### 2.1. 구조체의 선언과 사용

구조체를 사용하려면 먼저 구조체의 '형태'를 정의(선언)해야 합니다.

```c
#include <stdio.h>
#include <string.h> // 문자열 복사를 위해 필요

// 1. 구조체 선언 (정의)
// struct 키워드, 구조체 이름, 중괄호 안에 멤버 변수들
struct Student {
    char name[50];      // 이름 (문자열)
    int student_id;     // 학번 (정수)
    double grade;       // 학점 (실수)
    char major[50];     // 전공 (문자열)
}; // 세미콜론(;) 잊지 마세요!

int main() {
    // 2. 구조체 변수 선언
    struct Student student1; // Student 타입의 student1 이라는 변수를 만듭니다.

    // 3. 구조체 멤버 접근 및 값 할당
    // . (점) 연산자를 사용하여 구조체 변수의 각 멤버에 접근합니다.
    strcpy(student1.name, "김철수"); // 문자열은 strcpy 함수로 복사합니다.
    student1.student_id = 20230001;
    student1.grade = 4.2;
    strcpy(student1.major, "컴퓨터공학과");

    // 4. 구조체 멤버 값 출력
    printf("--- 학생 정보 ---\n");
    printf("이름: %s\n", student1.name);
    printf("학번: %d\n", student1.student_id);
    printf("학점: %.2f\n", student1.grade);
    printf("전공: %s\n", student1.major);

    // 또 다른 학생 정보 (초기화와 동시에 값 할당)
    struct Student student2 = {"이영희", 20230002, 3.8, "전자공학과"};
    printf("\n--- 다른 학생 정보 ---\n");
    printf("이름: %s\n", student2.name);
    printf("학번: %d\n", student2.student_id);
    printf("학점: %.2f\n", student2.grade);
    printf("전공: %s\n", student2.major);

    return 0;
}
```

**코드 설명:**

*   `struct Student { ... };`: `Student`라는 이름의 새로운 구조체 타입을 정의했습니다. 이 구조체는 `name`, `student_id`, `grade`, `major` 네 가지 멤버를 가집니다.
*   `struct Student student1;`: `Student` 타입의 `student1`이라는 구조체 변수를 선언합니다. 이제 `student1` 하나만으로 김철수 학생의 모든 정보를 관리할 수 있게 됩니다!
*   `student1.name`: `.` (점) 연산자를 사용해서 `student1` 구조체 변수 안에 있는 `name`이라는 멤버에 접근합니다.
*   `strcpy(student1.name, "김철수");`: 문자열은 `name = "김철수";` 처럼 직접 대입할 수 없고, 반드시 `strcpy` 함수(string copy)를 사용해서 복사해야 합니다. (`#include <string.h>` 필요!)
*   `struct Student student2 = {"이영희", 20230002, 3.8, "전자공학과"};`: 구조체 변수를 선언과 동시에 초기화할 수도 있습니다. 중괄호 `{}` 안에 멤버 순서대로 값을 넣어주면 됩니다.

#### 2.2. 구조체 배열: 여러 개의 구조체 관리

학생 한 명의 정보를 구조체로 관리하는 건 이제 쉽죠? 그럼 학생이 여러 명이라면 어떻게 할까요? 배열을 사용하면 됩니다!

```c
#include <stdio.h>
#include <string.h>

struct Student {
    char name[50];
    int student_id;
    double grade;
    char major[50];
};

int main() {
    // Student 구조체 3개를 저장할 수 있는 배열 선언 및 초기화
    struct Student students[3] = {
        {"김철수", 20230001, 4.2, "컴퓨터공학과"},
        {"이영희", 20230002, 3.8, "전자공학과"},
        {"박민수", 20230003, 3.5, "기계공학과"}
    };

    printf("--- 전체 학생 정보 ---\n");
    // 반복문을 사용하여 배열의 각 구조체에 접근
    for (int i = 0; i < 3; i++) {
        printf("학생 #%d\n", i + 1);
        printf("  이름: %s\n", students[i].name);
        printf("  학번: %d\n", students[i].student_id);
        printf("  학점: %.2f\n", students[i].grade);
        printf("  전공: %s\n", students[i].major);
        printf("--------------------\n");
    }

    // 특정 학생의 정보 수정
    strcpy(students[1].name, "이수정"); // 이영희 -> 이수정
    students[1].grade = 4.0;          // 학점 수정

    printf("\n--- 정보 수정 후 ---\n");
    printf("수정된 학생 #2의 정보:\n");
    printf("  이름: %s\n", students[1].name);
    printf("  학번: %d\n", students[1].student_id);
    printf("  학점: %.2f\n", students[1].grade);
    printf("  전공: %s\n", students[1].major);

    return 0;
}
```
이제 `students` 배열 하나로 여러 학생의 정보를 체계적으로 관리할 수 있게 되었습니다! 👍

---

### 3. 함수와 구조체의 시너지: 모듈화된 복합 데이터 관리!

자, 이제 함수와 구조체를 따로따로 배웠으니, 이 둘을 함께 사용하면 얼마나 강력해지는지 보여드릴 차례입니다! 함수를 통해 코드를 모듈화하고, 구조체를 통해 데이터를 복합적으로 관리하면, 훨씬 더 체계적이고 효율적인 프로그램을 만들 수 있습니다.

**예제: 학생 정보를 출력하는 함수**

앞서 만든 `Student` 구조체를 매개변수로 받아 학생 정보를 예쁘게 출력해주는 함수를 만들어볼까요?

```c
#include <stdio.h>
#include <string.h>

// 학생 구조체 정의
struct Student {
    char name[50];
    int student_id;
    double grade;
    char major[50];
};

// 학생 정보 출력 함수 선언 (프로토타입)
// Student 구조체 변수를 매개변수로 받습니다.
void print_student_info(struct Student s);

int main() {
    // 학생 구조체 변수 선언 및 초기화
    struct Student student1 = {"김철수", 20230001, 4.2, "컴퓨터공학과"};
    struct Student student2 = {"이영희", 20230002, 3.8, "전자공학과"};
    struct Student student3 = {"박민수", 20230003, 3.5, "기계공학과"};

    printf("--- 학생 정보 목록 ---\n");

    // 각 학생 정보를 출력 함수에 전달하여 출력
    print_student_info(student1); // student1 구조체 전체를 함수에 전달
    print_student_info(student2); // student2 구조체 전체를 함수에 전달
    print_student_info(student3); // student3 구조체 전체를 함수에 전달

    return 0;
}

// 학생 정보 출력 함수 정의
void print_student_info(struct Student s) {
    printf("---------------------------\n");
    printf("  이름: %s\n", s.name);
    printf("  학번: %d\n", s.student_id);
    printf("  학점: %.2f\n", s.grade);
    printf("  전공: %s\n", s.major);
    printf("---------------------------\n");
}
```

**코드 설명:**

*   `void print_student_info(struct Student s)`: 이 함수는 `struct Student` 타입의 변수 `s`를 매개변수로 받습니다. 함수 안에서는 `s.name`, `s.student_id` 등으로 해당 학생의 정보에 접근하여 출력합니다.
*   `print_student_info(student1);`: `main` 함수에서 `student1` 구조체 변수 전체를 `print_student_info` 함수로 전달합니다. 이렇게 하면 학생 한 명의 정보를 출력하는 코드를 여러 번 반복할 필요 없이, 함수 호출 한 줄로 깔끔하게 처리할 수 있습니다.

어때요? 함수와 구조체가 함께 만나니 코드가 훨씬 더 간결하고, 읽기 쉬워지고, 유지보수하기 좋게 변한 것을 알 수 있죠? 이것이 바로 **모듈화**와 **복합 데이터**의 힘입니다!

---

### 🎉 5강 마무리: 오늘 배운 내용을 정리해볼까요?

오늘 우리는 C 언어 코드를 더욱 강력하고 효율적으로 만들어주는 두 가지 핵심 개념, **'함수'** 와 **'구조체'** 에 대해 깊이 있게 알아보았습니다!

*   **함수(Function):**
    *   특정 작업을 수행하는 코드 묶음으로, **코드 재사용, 모듈화, 가독성 향상**에 필수적입니다.
    *   **선언(프로토타입), 정의, 호출** 세 단계를 통해 사용합니다.
    *   **매개변수**로 값을 받아들여 작업을 수행하고, **반환값**을 통해 결과를 돌려줄 수 있습니다.
*   **구조체(Struct):**
    *   서로 다른 종류의 데이터를 하나로 묶어 **'나만의 새로운 데이터 타입'** 을 만드는 문법입니다.
    *   `. (점) 연산자`를 사용하여 구조체 변수의 멤버에 접근합니다.
    *   여러 개의 구조체를 배열로 만들어 관리할 수 있습니다.
*   **함수와 구조체의 시너지:**
    *   함수에 구조체를 매개변수로 전달하거나 반환값으로 사용하여, **복합적인 데이터를 효율적으로 처리하고 모듈화된 프로그램**을 만들 수 있습니다.

이 두 개념은 앞으로 여러분이 만들 모든 C 프로그램에서 핵심적인 역할을 하게 될 거예요. 마치 건물을 지을 때 설계도(함수)와 미리 조립된 모듈(구조체)을 사용하는 것과 같답니다!

오늘 배운 내용들은 단순히 암기하는 것을 넘어, 직접 코드를 작성하고 실행해보면서 체득하는 것이 가장 중요합니다. 제가 제공한 예제 코드를 직접 타이핑해보시고, 숫자나 이름을 바꿔가며 실험해보세요. 분명 더욱 확실하게 여러분의 지식이 될 겁니다!

---

다음 6강에서는 C 언어의 꽃이자, 가장 강력하면서도 조금은 어려운 개념인 **'포인터(Pointer)'** 에 대해 다룰 예정입니다. 포인터는 C 언어의 성능을 극대화하고 메모리를 자유자재로 다룰 수 있게 해주는 마법 같은 도구예요. 오늘 배운 함수와 구조체를 가지고도 포인터와 함께라면 훨씬 더 놀라운 일들을 할 수 있답니다!

조금 어렵게 느껴질 수도 있지만, 저 쭈니가 여러분의 눈높이에 맞춰 아주 쉽고 재미있게 설명해 드릴 테니, 다음 강의도 기대 많이 해주세요!

오늘도 정말 고생 많으셨습니다! 여러분의 열정을 항상 응원합니다!
다음 강의에서 만나요! 안녕~ 👋

---

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
