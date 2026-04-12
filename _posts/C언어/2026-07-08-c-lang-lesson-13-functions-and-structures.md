---
layout: single
title: "함수와 구조체의 결합"
date: 2026-07-08 15:54:59
categories: [C언어]
---

## 🔥 13강: 함수와 구조체의 결합 - C 언어 마스터 되기 위한 최고 조합! 🚀

안녕하세요, 코드 탐험가 여러분! 😎 
저는 15년 차 C 언어 시니어 개발자이자 대한민국 최고 C 언어 일타 강사 '코드 쉐이크'로 알려져 있답니다. 이번 강좌에서는 함수와 구조체의 결합,  C 프로그래밍 세계의 **진짜 신기한 부분!** 🔥을 알아보겠습니다. 

> "그냥 코드가 더 복잡해지는 것 같은데?" 🤔
> 걱정 마세요! 함수와 구조체의 조합은 C 프로그래밍을 더욱 **멋지고 효율적으로 만들어주는 마법같은 기술**입니다! ✨ 이 마법을 배우면 프로그램을 더 가독성 있고 유연하게 작성할 수 있어요. 

###  函数과 구조체 - 서로를 위한 완벽한 파트너 🤩

* **함수**: 여러 작업들을 모아서 실행하는 단위, C 언어의 가장 기본적인 구성 요소죠. 마치 레시피처럼 코드를 효율적으로 분할하여 사용 가능합니다!
* **구조체**: 여러 데이터 타입을 하나로 묶는 도구입니다. 실제 세계에서 사람 정보를 생각해 보세요. 이름, 나이, 주소 등이 모여서 한 사람이 되죠? 구조체도 마찬가지로, 데이터를 집계하여 사용하기 좋게 만듭니다!

함수와 구조체는 서로에게 완벽한 파트너입니다. 함수는 구조체를 안전하게 다루고, 구조체는 함수에 필요한 정보를 제공해주죠. 이것이 바로 **C 프로그래밍의 심오한 매력**! 🔥

###  함수와 구조체 사용 예시: 직원 정보 관리 프로그램 💪

자, 실제 프로그램 코드를 통해 흥미진진한 결합 과정을 살펴보겠습니다! 😎 다음은 직원 정보를 저장하고 관리하는 간단한 C 프로그래밍 코드입니다.

```c
#include <stdio.h> // 표준 입출력 헤더파일
#define MAX_EMPLOYEES 100 // 최대 직원 수 설정

// 구조체 선언: 직원 정보를 담을 공간을 정의합니다.
struct Employee {
    int empID;        // 직원 ID (숫자)
    char name[50];     // 직원 이름 (문자열)
    int age;         // 직원 나이 (숫자)
    double salary;   // 직원 연봉 (소수점)
};

void displayEmployee(struct Employee employee) { // 함수 선언: 직원 정보 출력을 담당합니다.
    printf("ID: %d\n", employee.empID);         // 직원 ID 출력
    printf("Name: %s\n", employee.name);       // 직원 이름 출력
    printf("Age: %d\n", employee.age);        // 직원 나이 출력
    printf("Salary: %.2lf\n\n", employee.salary); // 직원 연봉 출력 
}

int main() {
    struct Employee employees[MAX_EMPLOYEES]; // 직원 정보를 저장할 배열 선언
    int numEmployees = 0;             // 현재 입력된 직원 수

    while (numEmployees < MAX_EMPLOYEES) { // 최대 직원 수까지 반복문을 실행합니다.
        printf("Enter employee details (or -1 to exit):\n");
        scanf("%d %s %d %lf", &employees[numEmployees].empID, employees[numEmployees].name, 
              &employees[numEmployees].age, &employees[numEmployees].salary);

        if (employees[numEmployees].empID == -1) { // 입력 값이 -1 이면 반복문 종료
            break;
        }

        numEmployees++;                      // 직원 수 증가

        displayEmployee(employees[numEmployees-1]); // 함수 호출하여 직원 정보 출력
    }
    return 0;
}
```

💡 **코드 분석**: 위 코드는 여러 직원의 정보를 저장하고 출력하는 간단한 프로그램입니다.


* 구조체 `struct Employee` 는 이름, ID, 나이, 연봉 등 직원 정보를 담을 수 있도록 정의합니다.
* `displayEmployee()` 함수는 직원 정보를 화면에 출력하는 역할을 합니다. 
* `main()` 함수에서는 사용자로부터 직원 정보를 입력받고, 구조체 배열에 저장합니다. 그리고 `displayEmployee()` 함수를 호출하여 직원 정보를 출력합니다.

###  함수와 구조체의 결합 - 당신이 C 프로그래밍 마스터가 될 수 있는 열쇠!🔑

> "어휴, 복잡한데..." 🤔
 아니요! 오히려 **C 프로그래밍의 진정한 매력**을 느끼게 해주죠. 
 함수와 구조체의 결합은 코드를 더욱 명확하고 효율적으로 작성할 수 있도록 도와줍니다! 🤩

*  코드 재사용성 향상: 함수는 동일한 작업을 여러 곳에서 사용할 수 있도록 합니다. 마치 요리 레시피처럼 여러 메뉴에 활용하는 것과 같습니다.
*  추가 기능 쉽게 추가하기: 구조체를 변형하여 새로운 기능을 추가하는 것이 매우 간편합니다. 마치 직원 정보에 '직책'이나 '부서' 같은 정보를 더 추가할 수 있는 것처럼!

### 🚨 실무주의보!: 함수와 구조체의 결합은 C 프로그래밍의 기본 기술이죠! 💪


* 코드 작성 시 **함수와 구조체를 효율적으로 사용하는 연습**을 통해 당신의 C 프로그래밍 실력을 향상시킬 수 있습니다.
* 다양한 온라인 자료나 강의를 활용하여 이 개념을 더욱 탄탄히 이해하도록 노력해보세요! 🚀



### 마지막으로, 질문이 있으신가요? 🤔

C 언어 학습에 어려움을 겪고 있는 분들, 저에게 주저하지 말고 댓글로 질문하세요! 😎 최선을 다하여 도와드리겠습니다. 💪

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
