---
layout: post
title: "메모리를 내 마음대로: 포인터 활용과 동적 메모리 할당"
date: 2026-04-12 05:17:03
categories: [C언어 강의]
---

안녕하세요, C 언어 초보자 여러분!
15년 차 시니어 C 개발자이자 여러분의 일타 강사, **닥터 C**입니다! 😎

벌써 7강이네요! 여기까지 오시느라 정말 고생 많으셨습니다. 이제 여러분은 C 언어의 기초를 탄탄하게 다지셨다고 할 수 있습니다. 하지만 진정한 C 언어의 마법은 이제부터 시작됩니다.

오늘 7강에서는 C 언어의 꽃이자, 동시에 많은 초보자들을 좌절시키는 악명 높은(?) 주제를 다룰 예정입니다. 바로 **포인터(Pointer)**와 **동적 메모리 할당(Dynamic Memory Allocation)**입니다!

"헉, 포인터요? 너무 어려울 것 같아서 벌써 머리 아파요..." 라고 생각하실 필요 전혀 없습니다! 제가 15년 노하우를 꾹꾹 눌러 담아, 마치 옆집 형이 설명해주듯이 가장 친절하고 쉽게 알려드릴 테니 걱정 말고 따라오세요.

오늘 강의를 마치면 여러분은 메모리를 내 마음대로 주무를 수 있는 C 언어의 진정한 고수가 되는 첫걸음을 내딛게 될 겁니다. 자, 그럼 시작해볼까요? 🚀

---

## 🚀 7강: 메모리를 내 마음대로: 포인터 활용과 동적 메모리 할당

### 목차

1.  **포인터, 다시 한번 정복하기 (Pointer: Re-conquering)**
    *   포인터의 본질 복습
    *   `*` 연산자와 `&` 연산자 다시 보기
2.  **포인터 연산 (Pointer Arithmetic): 주소의 덧셈 뺄셈?**
    *   정수형 덧셈/뺄셈과는 다른 포인터 연산
    *   데이터 타입 크기만큼 이동!
3.  **포인터와 배열 (Pointers and Arrays): 뗄레야 뗄 수 없는 관계**
    *   배열 이름은 곧 포인터!
    *   포인터로 배열 요소 접근하기
4.  **포인터와 문자열 (Pointers and Strings): 문자의 행렬**
    *   `char` 포인터로 문자열 다루기
    *   문자열 리터럴과 문자 배열의 차이
5.  **동적 메모리 할당의 필요성 (Why Dynamic Memory Allocation?)**
    *   정적/스택 메모리 할당의 한계
    *   프로그램 실행 중 메모리 크기를 결정해야 할 때
6.  **메모리를 내 마음대로! 동적 메모리 할당 (Dynamic Memory Allocation)**
    *   `malloc()`: 원하는 크기만큼 할당!
    *   `free()`: 할당된 메모리 해제! (가장 중요!)
    *   `calloc()`: 초기화까지 한 번에!
    *   `realloc()`: 이미 할당된 메모리 크기 변경!
7.  **동적 메모리 할당 시 주의사항 및 팁 (Cautions and Tips)**
    *   메모리 누수(Memory Leak)
    *   댕글링 포인터(Dangling Pointer)
    *   이중 해제(Double Free)
    *   NULL 포인터 체크

---

### 1. 포인터, 다시 한번 정복하기 (Pointer: Re-conquering)

우리가 변수를 선언하면 컴퓨터 메모리의 어딘가에 그 변수를 위한 공간이 생기고, 그 공간에는 고유한 '주소'가 부여됩니다. 포인터는 바로 이 **메모리 주소를 저장하는 변수**입니다. 쉽게 말해, 다른 변수의 '위치'를 가리키는 나침반 같은 역할을 하죠!

#### 포인터의 본질 복습

*   **변수의 주소를 저장하는 변수:** 이게 핵심입니다!
*   **간접 접근:** 포인터가 가리키는 주소로 찾아가서, 그 주소에 있는 실제 값을 조작할 수 있습니다. 이걸 "간접 접근"이라고 부릅니다.

#### `*` 연산자와 `&` 연산자 다시 보기

| 연산자 | 이름          | 역할                                         | 사용 예시                      | 설명                                               |
| :----- | :------------ | :------------------------------------------- | :----------------------------- | :------------------------------------------------- |
| `&`    | 주소 연산자   | 변수의 메모리 주소를 반환합니다.             | `ptr = &num;`                  | `num` 변수의 주소를 `ptr`에 저장합니다.            |
| `*`    | 역참조 연산자 | 포인터가 가리키는 주소의 '값'을 가져옵니다. | `value = *ptr;`                | `ptr`이 가리키는 주소에 저장된 값을 `value`에 저장합니다. |
| `*`    | 선언 연산자   | 포인터 변수를 선언할 때 사용합니다.          | `int *ptr;`                    | `int` 타입의 주소를 저장할 포인터 `ptr`을 선언합니다. |

**예제 코드: 포인터의 기본 사용**

```c
#include <stdio.h>

int main() {
    int num = 10;       // 정수형 변수 num 선언 및 초기화
    int *ptr;           // 정수형 변수의 주소를 저장할 포인터 ptr 선언

    printf("1. 변수 num의 값: %d\n", num);
    printf("2. 변수 num의 메모리 주소: %p\n", &num); // %p는 주소를 출력하는 형식 지정자

    ptr = &num;         // num 변수의 주소를 ptr에 저장 (ptr이 num을 가리킴)

    printf("\n3. 포인터 ptr의 값 (즉, num의 주소): %p\n", ptr);
    printf("4. 포인터 ptr이 가리키는 주소의 값 (*ptr): %d\n", *ptr); // ptr이 가리키는 주소의 값을 가져옴

    *ptr = 20;          // ptr이 가리키는 주소 (num의 주소)에 20을 저장
                        // 이는 곧 num의 값을 20으로 변경하는 것과 같습니다.

    printf("\n5. *ptr = 20 변경 후, 변수 num의 값: %d\n", num);
    printf("6. *ptr = 20 변경 후, 포인터 ptr이 가리키는 주소의 값: %d\n", *ptr);

    return 0;
}
```

**컴파일 및 실행:**
```bash
gcc -o pointer_basic pointer_basic.c
./pointer_basic
```

**실행 결과 (주소는 시스템마다 다를 수 있습니다):**
```
1. 변수 num의 값: 10
2. 변수 num의 메모리 주소: 0x7ffee00c306c

3. 포인터 ptr의 값 (즉, num의 주소): 0x7ffee00c306c
4. 포인터 ptr이 가리키는 주소의 값 (*ptr): 10

5. *ptr = 20 변경 후, 변수 num의 값: 20
6. *ptr = 20 변경 후, 포인터 ptr이 가리키는 주소의 값: 20
```

어떠세요? `ptr`을 통해 `num`의 값을 자유자재로 읽고 쓸 수 있다는 걸 확인하셨죠? 이게 바로 포인터의 간접 접근 능력입니다!

---

### 2. 포인터 연산 (Pointer Arithmetic): 주소의 덧셈 뺄셈?

일반 정수형 변수에 덧셈 뺄셈을 하는 것과 포인터에 덧셈 뺄셈을 하는 것은 아주 다릅니다. 포인터 연산의 핵심은 "데이터 타입의 크기"에 있습니다!

#### 정수형 덧셈/뺄셈과는 다른 포인터 연산

포인터에 1을 더하면, 실제 메모리 주소는 1바이트 증가하는 것이 아니라, **포인터가 가리키는 데이터 타입의 크기만큼 증가**합니다.

*   `int *ptr; ptr++;`  -> `ptr`은 `sizeof(int)` 바이트만큼 증가합니다. (대부분 4바이트)
*   `char *ptr; ptr++;` -> `ptr`은 `sizeof(char)` 바이트만큼 증가합니다. (1바이트)
*   `double *ptr; ptr++;` -> `ptr`은 `sizeof(double)` 바이트만큼 증가합니다. (대부분 8바이트)

왜 이렇게 동작할까요? 컴퓨터는 우리가 어떤 타입의 데이터를 다루는지 알고 있기 때문에, 다음 **요소**로 이동하기 위해서는 해당 요소의 크기만큼 이동해야 한다고 "똑똑하게" 판단하는 겁니다.

**예제 코드: 포인터 연산**

```c
#include <stdio.h>

int main() {
    int arr[3] = {10, 20, 30}; // 정수형 배열
    int *p_int = arr;          // p_int는 arr[0]의 주소를 가리킴

    char str[] = "ABC";        // 문자열 배열 (char 타입)
    char *p_char = str;        // p_char는 str[0]의 주소를 가리킴

    printf("--- int 포인터 연산 ---\n");
    printf("p_int (arr[0] 주소): %p, 값: %d\n", p_int, *p_int);

    p_int++; // p_int를 1 증가

    printf("p_int++ 후 (arr[1] 주소): %p, 값: %d\n", p_int, *p_int);
    // 원래 주소에서 sizeof(int) 만큼 증가한 것을 확인할 수 있습니다.

    printf("\n--- char 포인터 연산 ---\n");
    printf("p_char (str[0] 주소): %p, 값: %c\n", p_char, *p_char);

    p_char++; // p_char를 1 증가

    printf("p_char++ 후 (str[1] 주소): %p, 값: %c\n", p_char, *p_char);
    // 원래 주소에서 sizeof(char) = 1 바이트만큼 증가한 것을 확인할 수 있습니다.

    return 0;
}
```

**컴파일 및 실행:**
```bash
gcc -o pointer_arithmetic pointer_arithmetic.c
./pointer_arithmetic
```

**실행 결과 (주소는 시스템마다 다를 수 있습니다):**
```
--- int 포인터 연산 ---
p_int (arr[0] 주소): 0x7ffee14e3050, 값: 10
p_int++ 후 (arr[1] 주소): 0x7ffee14e3054, 값: 20

--- char 포인터 연산 ---
p_char (str[0] 주소): 0x7ffee14e304f, 값: A
p_char++ 후 (str[1] 주소): 0x7ffee14e3050, 값: B
```
`int` 포인터는 4바이트(시스템에 따라 다를 수 있음)씩, `char` 포인터는 1바이트씩 주소가 변하는 것을 확인하셨나요? 이 원리를 이해하면 포인터와 배열을 다루는 것이 훨씬 쉬워집니다!

---

### 3. 포인터와 배열 (Pointers and Arrays): 뗄레야 뗄 수 없는 관계

C 언어에서 배열과 포인터는 정말 밀접한 관계를 가지고 있습니다. 사실, **배열의 이름은 첫 번째 요소의 주소를 가리키는 상수 포인터**와 같습니다! (엄밀히 말하면 완벽히 같지는 않지만, 대부분의 경우 그렇게 생각해도 무방합니다.)

#### 배열 이름은 곧 포인터!

```c
int arr[5];
int *ptr = arr; // arr은 &arr[0]과 같습니다.
```

위 코드에서 `arr`은 배열의 첫 번째 요소인 `arr[0]`의 주소를 나타냅니다. 그래서 `ptr = arr;` 처럼 대입하는 것이 가능한 것이죠!

#### 포인터로 배열 요소 접근하기

배열 요소를 접근할 때 `arr[i]` 대신 `*(arr + i)` 또는 `*(ptr + i)` 형태로 접근할 수 있습니다.

| 배열 접근 방식 | 포인터 접근 방식 | 설명                                                              |
| :------------- | :--------------- | :---------------------------------------------------------------- |
| `arr[i]`       | `*(arr + i)`     | 배열 `arr`의 `i`번째 요소에 접근합니다.                          |
| `ptr[i]`       | `*(ptr + i)`     | 포인터 `ptr`이 가리키는 시작점부터 `i`번째 요소에 접근합니다. |

**예제 코드: 포인터로 배열 요소 접근**

```c
#include <stdio.h>

int main() {
    int scores[5] = {80, 90, 70, 60, 95}; // 5개의 정수를 저장하는 배열
    int *p_scores = scores;              // 배열의 첫 번째 요소 주소를 가리키는 포인터

    printf("--- 배열 인덱스 사용 ---\n");
    for (int i = 0; i < 5; i++) {
        printf("scores[%d]: %d\n", i, scores[i]);
    }

    printf("\n--- 포인터 연산 사용 (*(p_scores + i)) ---\n");
    for (int i = 0; i < 5; i++) {
        printf("*(p_scores + %d): %d\n", i, *(p_scores + i));
    }

    printf("\n--- 포인터 인덱스 사용 (p_scores[i]) ---\n");
    for (int i = 0; i < 5; i++) {
        printf("p_scores[%d]: %d\n", i, p_scores[i]);
    }

    // 포인터 자체를 이동시키면서 접근하기
    printf("\n--- 포인터 자체를 이동시키며 접근 ---\n");
    int *temp_ptr = scores; // 원본 p_scores를 유지하기 위해 임시 포인터 사용
    for (int i = 0; i < 5; i++) {
        printf("현재 포인터 %p, 값: %d\n", temp_ptr, *temp_ptr);
        temp_ptr++; // 다음 요소로 이동
    }

    return 0;
}
```

**컴파일 및 실행:**
```bash
gcc -o pointer_array pointer_array.c
./pointer_array
```

**실행 결과:**
```
--- 배열 인덱스 사용 ---
scores[0]: 80
scores[1]: 90
scores[2]: 70
scores[3]: 60
scores[4]: 95

--- 포인터 연산 사용 (*(p_scores + i)) ---
*(p_scores + 0): 80
*(p_scores + 1): 90
*(p_scores + 2): 70
*(p_scores + 3): 60
*(p_scores + 4): 95

--- 포인터 인덱스 사용 (p_scores[i]) ---
p_scores[0]: 80
p_scores[1]: 90
p_scores[2]: 70
p_scores[3]: 60
p_scores[4]: 95

--- 포인터 자체를 이동시키며 접근 ---
현재 포인 0x7ffee6a03040, 값: 80
현재 포인 0x7ffee6a03044, 값: 90
현재 포인 0x7ffee6a03048, 값: 70
현재 포인 0x7ffee6a0304c, 값: 60
현재 포인 0x7ffee6a03050, 값: 95
```
보시다시피, 어떤 방법으로 접근하든 결과는 동일합니다! 포인터 연산을 이해하면 배열을 훨씬 유연하게 다룰 수 있게 됩니다.

---

### 4. 포인터와 문자열 (Pointers and Strings): 문자의 행렬

C 언어에서 문자열은 사실 `char` 타입의 배열로 다루어집니다. 문자열의 끝은 항상 `\0` (널 문자)로 표시됩니다. 따라서 문자열을 다룰 때 `char` 포인터가 매우 유용하게 사용됩니다.

#### `char` 포인터로 문자열 다루기

`char` 포인터는 문자열의 첫 글자를 가리키는 데 사용될 수 있습니다.

```c
char *str = "Hello"; // "Hello" 문자열의 첫 번째 문자 'H'의 주소를 str에 저장
```
이 방식은 문자열 리터럴(literal)을 가리킬 때 많이 사용됩니다. 문자열 리터럴은 읽기 전용(read-only) 메모리 영역에 저장되므로, `str[0] = 'h';` 와 같이 내용을 변경하려 하면 런타임 오류가 발생할 수 있습니다.

만약 문자열의 내용을 변경하고 싶다면, `char` 배열을 사용해야 합니다.

```c
char arr[] = "Hello"; // 'H', 'e', 'l', 'l', 'o', '\0' 가 메모리에 할당됨
arr[0] = 'h';          // 가능
```

**예제 코드: 포인터와 문자열**

```c
#include <stdio.h>

int main() {
    char greeting[] = "Hello, C!"; // 'H', 'e', 'l', 'l', 'o', ',', ' ', 'C', '!', '\0'
                                   // 스택 메모리에 저장되며 수정 가능

    char *message = "Welcome to the world of Pointers!";
                                   // 문자열 리터럴. 읽기 전용 메모리 영역에 저장되며 수정 불가

    printf("Greeting (배열): %s\n", greeting);
    printf("Message (포인터): %s\n", message);

    // 배열을 이용한 문자열 수정 (가능)
    greeting[0] = 'h';
    printf("수정된 Greeting: %s\n", greeting);

    // 포인터를 이용한 문자열 수정 (컴파일은 되지만 런타임 오류 발생 가능!)
    // message[0] = 'w'; // 경고: 'read-only' 위치에 값을 할당합니다.
                       // 실행 시 'Segmentation fault' 발생 가능성이 높습니다.
    // printf("수정된 Message: %s\n", message); // 이 줄은 실행되지 않을 수 있습니다.

    // 포인터를 이용해 문자열 순회
    char *ptr = greeting;
    printf("\nGreeting 문자열 순회: ");
    while (*ptr != '\0') { // 널 문자를 만날 때까지 반복
        printf("%c", *ptr);
        ptr++;
    }
    printf("\n");

    return 0;
}
```

**컴파일 및 실행:**
```bash
gcc -o pointer_string pointer_string.c
./pointer_string
```

**실행 결과 (주의: `message[0] = 'w';` 줄을 주석 처리하지 않으면 오류 발생 가능):**
```
Greeting (배열): Hello, C!
Message (포인터): Welcome to the world of Pointers!
수정된 Greeting: hello, C!

Greeting 문자열 순회: hello, C!
```
문자열을 다룰 때 `char` 배열과 `char *`의 차이를 명확히 이해하는 것이 중요합니다. 특히 문자열 리터럴은 수정할 수 없다는 점을 꼭 기억하세요!

---

### 5. 동적 메모리 할당의 필요성 (Why Dynamic Memory Allocation?)

지금까지 우리가 사용했던 변수나 배열들은 대부분 프로그램이 **컴파일될 때** 또는 **함수가 호출될 때** 그 크기가 결정되었습니다. 이렇게 할당되는 메모리에는 두 가지 방식이 있습니다.

1.  **정적 메모리 할당 (Static Memory Allocation):** 전역 변수, static 변수 등. 프로그램 시작 시 할당되고 종료 시 해제됩니다. 크기가 컴파일 시점에 고정됩니다.
2.  **스택 메모리 할당 (Stack Memory Allocation):** 지역 변수, 함수 매개변수 등. 함수 호출 시 할당되고 함수 종료 시 해제됩니다. 크기가 컴파일 시점에 고정됩니다.

이 두 가지 방식은 매우 편리하지만, 다음과 같은 치명적인 한계가 있습니다.

*   **크기 예측 불가능:** 프로그램 실행 도중에 "사용자가 몇 개의 데이터를 입력할지", "파일에서 얼마나 많은 데이터를 읽어올지"를 미리 알 수 없는 경우가 많습니다.
*   **고정된 크기:** 배열을 선언할 때 `int arr[100];` 처럼 크기를 미리 지정해야 합니다. 만약 데이터가 101개라면? 아니면 데이터가 5개뿐인데 100개 공간을 잡으면? 비효율적이죠.
*   **제한된 생명 주기(스코프):** 함수 내에서 선언된 지역 변수는 함수가 끝나면 메모리에서 사라집니다. 함수를 벗어나서도 데이터를 유지해야 할 때는 어떻게 해야 할까요?

이런 문제들을 해결하기 위해 등장한 것이 바로 **동적 메모리 할당**입니다!

#### 프로그램 실행 중 메모리 크기를 결정해야 할 때

동적 메모리 할당은 프로그램 **실행 중(런타임)**에 필요한 만큼의 메모리를 운영체제로부터 요청하여 할당받고, 더 이상 필요 없을 때 명시적으로 해제하는 방식입니다. 이 메모리는 **힙(Heap)**이라는 영역에 할당되며, 스택과 달리 개발자가 직접 관리해야 합니다.

**예시:**
*   사용자가 N개의 정수를 입력하겠다고 했을 때
*   파일에서 읽어들일 데이터의 크기가 매번 달라질 때
*   연결 리스트나 트리 같은 동적인 자료구조를 만들 때

이럴 때 동적 메모리 할당은 C 언어 프로그래밍에 엄청난 유연성과 효율성을 제공합니다.

---

### 6. 메모리를 내 마음대로! 동적 메모리 할당 (Dynamic Memory Allocation)

이제 드디어 힙 메모리를 여러분의 뜻대로 주무를 수 있는 함수들을 배워볼 시간입니다! `stdlib.h` 헤더 파일에 선언되어 있는 주요 함수들을 살펴보겠습니다.

#### `malloc()`: 원하는 크기만큼 할당!

`malloc`은 "memory allocate"의 줄임말로, 원하는 **바이트(byte) 크기**만큼 메모리를 할당하고, 그 메모리의 시작 주소를 반환합니다.

```c
void *malloc(size_t size);
```

*   `size`: 할당할 메모리의 바이트 크기.
*   `void *`: 할당된 메모리의 시작 주소를 반환합니다. 어떤 타입으로든 캐스팅하여 사용할 수 있습니다.
*   **NULL 반환:** 메모리 할당에 실패하면 `NULL`을 반환합니다. **항상 NULL 체크를 해야 합니다!**

**예제 코드: `malloc` 사용하기**

```c
#include <stdio.h>
#include <stdlib.h> // malloc, free 함수를 사용하기 위해 포함

int main() {
    int *arr;         // int형 포인터 선언
    int num_elements; // 사용자로부터 입력받을 요소의 개수

    printf("몇 개의 정수를 저장할 배열을 만드시겠습니까? ");
    scanf("%d", &num_elements);

    // num_elements * sizeof(int) 만큼 메모리를 할당
    // (int *)로 캐스팅하여 int 포인터에 저장
    arr = (int *)malloc(num_elements * sizeof(int));

    // 메모리 할당 실패 여부 확인 (매우 중요!)
    if (arr == NULL) {
        printf("메모리 할당에 실패했습니다!\n");
        return 1; // 프로그램 종료
    }

    printf("%d개의 정수를 위한 메모리가 성공적으로 할당되었습니다.\n", num_elements);

    // 할당된 메모리에 값 저장
    for (int i = 0; i < num_elements; i++) {
        arr[i] = (i + 1) * 10; // 10, 20, 30...
    }

    // 저장된 값 출력
    printf("배열 요소:\n");
    for (int i = 0; i < num_elements; i++) {
        printf("arr[%d] = %d\n", i, arr[i]);
    }

    // 동적으로 할당된 메모리 해제 (가장 중요!)
    free(arr);
    printf("\n할당된 메모리가 성공적으로 해제되었습니다.\n");

    // 해제된 메모리에 접근 시도 (위험! 댕글링 포인터)
    // printf("해제 후 arr[0]: %d\n", arr[0]); // 하면 안 됩니다!

    arr = NULL; // 해제된 포인터를 NULL로 초기화하여 댕글링 포인터 방지
    printf("포인터를 NULL로 초기화했습니다.\n");


    return 0;
}
```
**컴파일 및 실행:**
```bash
gcc -o malloc_example malloc_example.c
./malloc_example
```

**실행 결과:**
```
몇 개의 정수를 저장할 배열을 만드시겠습니까? 5
5개의 정수를 위한 메모리가 성공적으로 할당되었습니다.
배열 요소:
arr[0] = 10
arr[1] = 20
arr[2] = 30
arr[3] = 40
arr[4] = 50

할당된 메모리가 성공적으로 해제되었습니다.
포인터를 NULL로 초기화했습니다.
```

#### `free()`: 할당된 메모리 해제! (가장 중요!)

`free` 함수는 `malloc`, `calloc`, `realloc`으로 할당된 메모리를 운영체제에 반환하여 재사용할 수 있도록 합니다.

```c
void free(void *ptr);
```
*   `ptr`: `malloc` 등으로 할당받은 메모리의 시작 주소를 가리키는 포인터.

**`free()`가 중요한 이유:** 만약 동적으로 할당한 메모리를 `free()`하지 않으면, 프로그램이 종료될 때까지 그 메모리는 계속 점유된 상태로 남아있게 됩니다. 이를 **메모리 누수(Memory Leak)**라고 하며, 장시간 실행되는 프로그램에서는 시스템 성능 저하의 주범이 될 수 있습니다.

**규칙:** `malloc`으로 할당받은 메모리는 반드시 `free`로 해제해야 합니다! (1:1 매칭)

#### `calloc()`: 초기화까지 한 번에!

`calloc`은 `malloc`과 유사하지만, 두 가지 차이점이 있습니다.
1.  할당할 메모리의 **개수**와 **각 요소의 크기**를 따로 인자로 받습니다.
2.  할당된 모든 메모리 공간을 **0으로 초기화**해줍니다. (malloc은 초기화하지 않음)

```c
void *calloc(size_t num, size_t size);
```

*   `num`: 할당할 요소의 개수.
*   `size`: 각 요소의 바이트 크기.
*   `void *`: 할당된 메모리의 시작 주소를 반환합니다. 실패 시 `NULL`.

**예제 코드: `calloc` 사용하기**

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int *arr_calloc;
    int num_elements = 5;

    // 5개의 int형 변수를 위한 메모리를 할당하고 0으로 초기화
    arr_calloc = (int *)calloc(num_elements, sizeof(int));

    if (arr_calloc == NULL) {
        printf("calloc 메모리 할당에 실패했습니다!\n");
        return 1;
    }

    printf("calloc으로 할당된 메모리 (초기화 여부 확인):\n");
    for (int i = 0; i < num_elements; i++) {
        printf("arr_calloc[%d] = %d\n", i, arr_calloc[i]); // 0으로 초기화된 것을 확인
    }

    // 값 저장
    for (int i = 0; i < num_elements; i++) {
        arr_calloc[i] = (i + 1) * 100;
    }

    printf("\n값 저장 후:\n");
    for (int i = 0; i < num_elements; i++) {
        printf("arr_calloc[%d] = %d\n", i, arr_calloc[i]);
    }

    free(arr_calloc);
    printf("\ncalloc으로 할당된 메모리가 해제되었습니다.\n");
    arr_calloc = NULL;

    return 0;
}
```
**실행 결과:**
```
calloc으로 할당된 메모리 (초기화 여부 확인):
arr_calloc[0] = 0
arr_calloc[1] = 0
arr_calloc[2] = 0
arr_calloc[3] = 0
arr_calloc[4] = 0

값 저장 후:
arr_calloc[0] = 100
arr_calloc[1] = 200
arr_calloc[2] = 300
arr_calloc[3] = 400
arr_calloc[4] = 500

calloc으로 할당된 메모리가 해제되었습니다.
```
`calloc`은 초기화가 필요한 경우에 유용하게 사용할 수 있습니다.

#### `realloc()`: 이미 할당된 메모리 크기 변경!

`realloc`은 "reallocate"의 줄임말로, 이미 `malloc`이나 `calloc`으로 할당된 메모리 블록의 크기를 변경(확장 또는 축소)할 때 사용합니다.

```c
void *realloc(void *ptr, size_t size);
```

*   `ptr`: 이전에 `malloc`, `calloc`, `realloc`으로 할당받았던 메모리의 시작 주소를 가리키는 포인터. (NULL이면 `malloc`처럼 동작)
*   `size`: 새로 할당할 메모리의 바이트 크기. (0이면 `free`처럼 동작)
*   `void *`: 새로 할당된 (또는 크기 변경된) 메모리의 시작 주소를 반환합니다. 이 주소는 이전 주소와 같을 수도, 다를 수도 있습니다. 실패 시 `NULL`.
*   **주의:** `realloc`이 실패하여 `NULL`을 반환하더라도, 원래 `ptr`이 가리키던 메모리는 여전히 유효합니다. 따라서 `realloc`의 결과는 항상 임시 포인터에 저장하고, 성공했을 때만 원래 포인터에 대입하는 것이 안전합니다.

**예제 코드: `realloc` 사용하기**

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int *arr_realloc;
    int initial_size = 3;
    int new_size = 5;

    // 1. 초기 3개의 정수 공간 할당
    arr_realloc = (int *)malloc(initial_size * sizeof(int));
    if (arr_realloc == NULL) {
        printf("malloc 실패!\n");
        return 1;
    }
    for (int i = 0; i < initial_size; i++) {
        arr_realloc[i] = (i + 1) * 10;
    }
    printf("초기 %d개 요소:\n", initial_size);
    for (int i = 0; i < initial_size; i++) {
        printf("arr_realloc[%d] = %d\n", i, arr_realloc[i]);
    }
    printf("초기 할당 주소: %p\n", arr_realloc);

    // 2. 메모리 크기를 5개로 확장
    printf("\n%d개 요소로 크기 재할당 시도...\n", new_size);
    int *temp_ptr = (int *)realloc(arr_realloc, new_size * sizeof(int));

    if (temp_ptr == NULL) {
        printf("realloc 실패! 원래 메모리는 유지됩니다.\n");
        free(arr_realloc); // 원래 할당된 메모리라도 해제해야 함
        return 1;
    }

    arr_realloc = temp_ptr; // 재할당 성공 시, 새 주소를 원래 포인터에 저장

    // 새로 추가된 공간에 값 저장
    for (int i = initial_size; i < new_size; i++) {
        arr_realloc[i] = (i + 1) * 10;
    }

    printf("%d개 요소로 재할당 성공:\n", new_size);
    for (int i = 0; i < new_size; i++) {
        printf("arr_realloc[%d] = %d\n", i, arr_realloc[i]);
    }
    printf("재할당된 주소: %p\n", arr_realloc);
    // 초기 할당 주소와 재할당된 주소가 다를 수 있음을 확인하세요.

    // 3. 메모리 해제
    free(arr_realloc);
    printf("\n재할당된 메모리 해제 완료.\n");
    arr_realloc = NULL;

    return 0;
}
```
**실행 결과:**
```
초기 3개 요소:
arr_realloc[0] = 10
arr_realloc[1] = 20
arr_realloc[2] = 30
초기 할당 주소: 0x111e03000

5개 요소로 크기 재할당 시도...
5개 요소로 재할당 성공:
arr_realloc[0] = 10
arr_realloc[1] = 20
arr_realloc[2] = 30
arr_realloc[3] = 40
arr_realloc[4] = 50
재할당된 주소: 0x111e03010

재할당된 메모리 해제 완료.
```
`realloc`은 기존 데이터는 최대한 유지하면서 메모리 크기를 조절해주기 때문에, 동적으로 변화하는 데이터 크기에 대응할 때 매우 유용합니다.

---

### 7. 동적 메모리 할당 시 주의사항 및 팁 (Cautions and Tips)

동적 메모리 할당은 강력한 만큼 책임도 따릅니다. 잘못 사용하면 프로그램에 심각한 문제를 야기할 수 있으니, 다음 사항들을 꼭 명심하세요!

#### 1. 메모리 누수(Memory Leak)

*   **원인:** `malloc` 등으로 할당받은 메모리를 `free`하지 않고 포인터를 잃어버리거나 함수가 종료되는 경우.
*   **결과:** 프로그램이 불필요한 메모리를 계속 점유하여 시스템의 사용 가능한 메모리를 고갈시킵니다. 장시간 실행되는 서버 프로그램 등에서 치명적입니다.
*   **방지:** `malloc` (`calloc`, `realloc`) 한 번에는 **반드시 `free` 한 번**이 대응되어야 합니다.

#### 2. 댕글링 포인터(Dangling Pointer)

*   **원인:** `free`로 메모리를 해제했지만, 해당 메모리 주소를 여전히 가리키는 포인터가 남아있는 경우. 이 포인터를 "댕글링 포인터"라고 합니다.
*   **결과:** 해제된 메모리는 운영체제에 반환되어 다른 용도로 재사용될 수 있습니다. 댕글링 포인터로 해당 주소에 접근하면 예기치 않은 데이터가 읽히거나, 다른 프로그램의 데이터가 손상되거나, 세그멘테이션 폴트(Segmentation Fault)가 발생할 수 있습니다.
*   **방지:** `free(ptr);` 후에는 **`ptr = NULL;`** 로 포인터를 무효화하는 습관을 들이세요.

#### 3. 이중 해제(Double Free)

*   **원인:** 이미 `free`된 메모리 주소를 다시 `free`하려고 시도하는 경우.
*   **결과:** 정의되지 않은 동작(Undefined Behavior)을 유발하며, 대부분 프로그램 충돌로 이어집니다.
*   **방지:** 한 번 `free`된 포인터는 `NULL`로 만들고, `NULL`이 아닌 포인터만 `free`하도록 조건을 걸 수 있습니다.

    ```c
    free(ptr);
    ptr = NULL; // 댕글링 포인터 방지

    // 다시 free 하려 할 때
    if (ptr != NULL) { // NULL 체크를 통해 이중 해제 방지
        free(ptr);
    }
    ```

#### 4. NULL 포인터 체크

*   **원인:** `malloc`, `calloc`, `realloc`은 메모리 할당에 실패하면 `NULL`을 반환합니다. 이 `NULL` 포인터로 메모리 접근(`*ptr` 또는 `ptr[i]`)을 시도하는 경우.
*   **결과:** 프로그램이 즉시 충돌(세그멘테이션 폴트)됩니다.
*   **방지:** 동적 메모리 할당 함수 호출 후에는 **항상 반환 값이 `NULL`인지 확인**하여 적절하게 에러를 처리해야 합니다.

    ```c
    int *arr = (int *)malloc(size * sizeof(int));
    if (arr == NULL) {
        fprintf(stderr, "메모리 할당 실패!\n");
        exit(EXIT_FAILURE); // 프로그램 종료
    }
    // 여기에 메모리를 사용하는 코드 작성
    ```

**종합 팁: 메모리 관리의 황금률**
**"네가 할당했으면, 네가 해제해라!"** (You `malloc` it, you `free` it!)

---

## 마무리하며: C 언어의 심장을 이해하다!

자, 여러분! 오늘 포인터 활용과 동적 메모리 할당에 대한 대장정을 마치셨습니다! 어떠셨나요? 처음에는 어렵게 느껴졌을 수도 있지만, 이제 메모리가 어떻게 작동하고, 그것을 어떻게 내 마음대로 다룰 수 있는지 감을 잡으셨으리라 생각합니다.

포인터는 C 언어의 핵심이자 가장 강력한 기능 중 하나입니다. 자료구조를 만들고, 파일 입출력을 다루고, 운영체제와 직접 소통하는 등 모든 고급 프로그래밍에서 포인터는 필수적으로 사용됩니다. 동적 메모리 할당은 프로그램의 유연성과 효율성을 극대화시켜 주는 마법 같은 도구이고요.

하지만 큰 힘에는 큰 책임이 따르는 법! 동적 메모리는 여러분이 직접 관리해야 하므로, 메모리 누수, 댕글링 포인터, 이중 해제 같은 문제들을 항상 염두에 두고 신중하게 코딩해야 합니다. 반복적인 연습과 꾸준한 디버깅만이 여러분을 진정한 C 언어의 고수로 만들어 줄 겁니다.

다음 강좌에서는 오늘 배운 포인터와 동적 메모리 할당을 활용하여 **'연결 리스트(Linked List)'**와 같은 동적인 자료구조를 직접 구현해보는 시간을 가질 예정입니다. 오늘 배운 내용이 얼마나 강력한지 직접 체감하게 되실 거예요!

오늘도 정말 수고 많으셨습니다! 궁금한 점은 언제든지 질문 게시판이나 댓글로 남겨주세요. 저는 닥터 C였습니다! 다음 강에서 만나요! 👋

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
