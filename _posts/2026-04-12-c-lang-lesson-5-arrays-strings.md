---
layout: post
title: "데이터 묶음 다루기: 배열과 문자열의 모든 것"
date: 2026-04-12 05:17:03
categories: [C언어 강의]
---

안녕하세요, 제자들! 15년 차 시니어 C 언어 개발자이자 자네들의 일타 강사, 김사부일세! 👨‍🏫

그동안 우리는 변수 하나하나를 선언하고 값을 저장하는 방법을 배웠죠? 마치 연필 한 자루, 지우개 한 개를 개별적으로 관리하는 것과 같았습니다. 하지만 현실 세계에서는 연필이 여러 자루 필요할 수도 있고, 지우개가 여러 개 필요할 수도 있죠? 또는, '대한민국'이라는 단어처럼 여러 문자들이 모여 하나의 의미를 이루는 경우도 많습니다.

오늘 제 5강에서는 이렇게 **여러 개의 데이터를 묶어서 효율적으로 다루는 방법**에 대해 심층적으로 파헤쳐 볼 겁니다. 바로 '배열(Array)'과 그 특수한 형태인 '문자열(String)'의 세계로 떠나볼까요? 이 개념만 제대로 이해하면, C 언어로 만들 수 있는 프로그램의 폭이 쫙~ 넓어질 테니, 집중해서 따라와 주세요! 준비됐나요? 그럼 시작합니다! 🚀

---

# 📚 5강: 데이터 묶음 다루기: 배열과 문자열의 모든 것

## 1. 배열 (Array): 데이터의 연속적인 나열

배열은 **'동일한 자료형'의 데이터를 '연속된 메모리 공간'에 '여러 개' 저장하고 싶을 때 사용**하는 자료 구조입니다. 마치 도서관의 사물함처럼, 똑같이 생긴 사물함이 1번부터 10번까지 줄지어 놓여있는 모습이라고 생각하면 이해하기 쉬울 거예요.

각 사물함에는 같은 종류의 물건(동일한 자료형)을 넣을 수 있고, 사물함 번호로 원하는 물건을 찾을 수 있죠.

### 1.1. 배열은 왜 필요할까요?

만약 학생 5명의 성적을 저장해야 한다고 생각해 봅시다. 배열을 모른다면 이렇게 해야 할 겁니다.

```c
int score1 = 90;
int score2 = 85;
int score3 = 92;
int score4 = 78;
int score5 = 95;

// 만약 학생이 100명이라면? 변수 100개를 선언해야 한다고? 😱
```

너무 비효율적이죠? 이럴 때 배열이 빛을 발합니다.

```c
int scores[5]; // 5칸짜리 사물함을 한 번에 뚝딱!
```

이렇게 하면 `scores`라는 이름으로 5개의 `int`형 변수를 한 번에 관리할 수 있게 됩니다.

### 1.2. 배열의 선언과 초기화

배열을 사용하려면 먼저 배열을 **선언**해야 합니다. 선언할 때는 **자료형, 배열 이름, 배열의 크기**를 명시해야 합니다.

```c
자료형 배열이름[배열크기];
```

**예제:**

```c
#include <stdio.h>

int main() {
    // 1. int형 데이터를 5개 저장할 수 있는 'numbers' 배열 선언
    int numbers[5]; 
    printf("int형 5개짜리 배열 numbers 선언 완료!\n");

    // 2. double형 데이터를 3개 저장할 수 있는 'grades' 배열 선언
    double grades[3];
    printf("double형 3개짜리 배열 grades 선언 완료!\n");

    return 0;
}
```

<details>
<summary><b>실행 결과 확인하기</b></summary>

```
int형 5개짜리 배열 numbers 선언 완료!
double형 3개짜리 배열 grades 선언 완료!
```
</details>

**초기화:** 배열을 선언과 동시에 값을 넣어 초기화할 수도 있고, 나중에 값을 할당할 수도 있습니다.

1.  **선언과 동시에 모든 요소 초기화:**
    ```c
    int scores[] = {90, 85, 92, 78, 95}; // 배열 크기를 명시하지 않으면, 초기화 리스트의 개수에 따라 자동으로 결정됩니다.
    int student_ids[3] = {101, 102, 103}; // 배열 크기를 명시해도 됩니다.
    ```
2.  **일부 요소만 초기화:**
    ```c
    int data[5] = {10, 20}; // data[0] = 10, data[1] = 20, 나머지 data[2], data[3], data[4]는 0으로 초기화됩니다.
    ```
3.  **선언 후 개별적으로 값 할당:**
    ```c
    int ages[4];
    ages[0] = 20;
    ages[1] = 22;
    ages[2] = 25;
    ages[3] = 30;
    ```

### 1.3. 배열 요소에 접근하기 (인덱스)

배열에 저장된 개별 데이터 하나하나를 '배열 요소'라고 부릅니다. 이 배열 요소에 접근하려면 **'인덱스(Index)'**를 사용합니다.

**⭐ 중요! C 언어에서 배열의 인덱스는 0부터 시작합니다! ⭐**

즉, 크기가 5인 배열 `numbers[5]`가 있다면, 첫 번째 요소는 `numbers[0]`, 두 번째 요소는 `numbers[1]`, 마지막 요소는 `numbers[4]`가 됩니다.

```c
#include <stdio.h>

int main() {
    int scores[5] = {90, 85, 92, 78, 95};

    // 첫 번째 학생의 점수 (인덱스 0)
    printf("첫 번째 학생의 점수: %d\n", scores[0]); 

    // 세 번째 학생의 점수 (인덱스 2)
    printf("세 번째 학생의 점수: %d\n", scores[2]);

    // 마지막 학생의 점수 (인덱스 4)
    printf("마지막 학생의 점수: %d\n", scores[4]);

    // 두 번째 학생의 점수를 변경 (인덱스 1)
    scores[1] = 88;
    printf("변경된 두 번째 학생의 점수: %d\n", scores[1]);

    // 주의! 배열의 범위를 벗어나는 인덱스에 접근하면 '오류'가 발생할 수 있습니다!
    // scores[5] = 100; // 💥 이런 식으로 접근하면 안 됩니다! 💥 (배열 크기는 5지만 인덱스는 0~4)
    // printf("범위를 벗어난 접근: %d\n", scores[5]); // 예상치 못한 결과 발생 또는 프로그램 crash
    
    return 0;
}
```

<details>
<summary><b>실행 결과 확인하기</b></summary>

```
첫 번째 학생의 점수: 90
세 번째 학생의 점수: 92
마지막 학생의 점수: 95
변경된 두 번째 학생의 점수: 88
```
</details>

### 1.4. 반복문을 이용한 배열 활용

배열은 보통 `for` 문과 같은 반복문과 함께 사용될 때 강력한 시너지를 냅니다. 배열의 모든 요소를 순회하거나, 특정 조건에 맞는 요소를 찾을 때 유용하죠.

```c
#include <stdio.h>

int main() {
    int numbers[10]; // 10칸짜리 정수 배열 선언
    int sum = 0; // 합계를 저장할 변수

    printf("배열에 1부터 10까지의 숫자를 저장하고 출력합니다.\n");

    // 배열에 값 저장 (0부터 9까지의 인덱스 사용)
    for (int i = 0; i < 10; i++) {
        numbers[i] = i + 1; // numbers[0] = 1, numbers[1] = 2, ... numbers[9] = 10
    }

    // 배열의 값 출력 및 합계 계산
    printf("배열 요소: ");
    for (int i = 0; i < 10; i++) {
        printf("%d ", numbers[i]);
        sum += numbers[i]; // sum = sum + numbers[i]
    }
    printf("\n");

    printf("배열 요소의 총 합: %d\n", sum);

    return 0;
}
```

<details>
<summary><b>실행 결과 확인하기</b></summary>

```
배열에 1부터 10까지의 숫자를 저장하고 출력합니다.
배열 요소: 1 2 3 4 5 6 7 8 9 10 
배열 요소의 총 합: 55
```
</details>

## 2. 문자열 (String): 문자의 배열과 '\0'의 약속

이제 배열의 개념을 익혔으니, 이제 그 특수하고도 중요한 형태인 **'문자열(String)'**에 대해 알아볼 시간이야! C 언어에서 문자열은 다른 언어처럼 별도의 자료형으로 존재하지 않고, **'문자(char)들의 배열'**로 다뤄집니다.

### 2.1. 문자열의 핵심: 널 종료 문자 (`\0`)

문자열이 단순한 `char` 배열과 다른 점은 바로 **문자열의 끝을 알리는 특별한 문자**가 있다는 겁니다. 이 문자를 **널 종료 문자 (Null Terminator)** 또는 **널 문자 (Null Character)**라고 부르며, `\0`로 표현합니다.

C 언어의 모든 문자열은 반드시 이 `\0` 문자로 끝나야 합니다. `printf`와 같은 문자열 처리 함수들은 이 `\0`를 만나야 문자열의 끝을 인식하고 작업을 멈추게 됩니다.

**⭐ 별표 다섯 개! `\0`은 C 언어 문자열의 핵심입니다! ⭐**

따라서 "Hello"라는 문자열을 저장하려면 실제로 6개의 `char` 공간이 필요합니다: 'H', 'e', 'l', 'l', 'o', `\0`.

### 2.2. 문자열의 선언과 초기화

문자열을 선언하고 초기화하는 방법은 여러 가지가 있습니다.

1.  **문자 배열로 초기화 (가장 일반적이고 권장되는 방식):**
    ```c
    char greeting[] = "Hello C!"; // 컴파일러가 자동으로 널 종료 문자 '\0'를 추가합니다.
                                  // 따라서 이 배열의 크기는 "Hello C!" (8글자) + '\0' (1글자) = 9입니다.
    char name[20] = "Kim Sabu";   // 배열 크기를 넉넉하게 지정할 수 있습니다.
    ```
2.  **문자 하나하나를 직접 나열하여 초기화:**
    ```c
    char city[] = {'S', 'e', 'o', 'u', 'l', '\0'}; // 반드시 마지막에 '\0'을 직접 넣어줘야 합니다!
    ```
    이 방법은 번거롭기 때문에 잘 사용되지 않지만, `\0`의 중요성을 이해하는 데 도움이 됩니다.

**예제:**

```c
#include <stdio.h>

int main() {
    // 1. 문자열 리터럴로 초기화 (가장 일반적)
    char myString[] = "Hello, World!"; 
    printf("myString: %s\n", myString); // %s 포맷 지정자는 문자열을 출력합니다.

    // 2. 크기를 지정하고 초기화 (남은 공간은 \0으로 자동 채워짐)
    char course[15] = "C Programming"; 
    printf("course: %s\n", course);

    // 3. 문자 하나하나 나열 (반드시 \0으로 끝내야 함!)
    char grade_char[3] = {'A', '+', '\0'}; 
    printf("grade_char: %s\n", grade_char);

    // ⚡️ 주의! 널 종료 문자가 없으면 어떻게 될까요? ⚡️
    char no_null[4] = {'T', 'E', 'S', 'T'}; // '\0'이 없음!
    printf("no_null (경고! 널 종료 문자 없음): %s\n", no_null); 
    // 이 경우, printf는 메모리상에서 '\0'를 만날 때까지 계속 읽어나가므로, 
    // 예상치 못한 쓰레기 값이나 프로그램 오류가 발생할 수 있습니다.
    // 절대 이렇게 하지 마세요!

    return 0;
}
```

<details>
<summary><b>실행 결과 확인하기</b></summary>

```
myString: Hello, World!
course: C Programming
grade_char: A+
no_null (경고! 널 종료 문자 없음): TEST��
```
</details>
(참고: `no_null` 출력 뒤의 알 수 없는 문자는 `\0`를 찾지 못하고 메모리를 계속 읽어 나간 결과입니다. 컴파일러나 환경에 따라 다르게 나타날 수 있습니다.)

### 2.3. 문자열 입력받기

사용자로부터 문자열을 입력받는 방법은 `scanf`와 `fgets`가 대표적입니다. 하지만 `scanf`는 몇 가지 주의할 점이 있습니다.

1.  **`scanf("%s", ...)` (주의 필요!):**
    *   공백을 만나면 입력을 중단합니다. "Hello World"를 입력하면 "Hello"만 저장됩니다.
    *   **버퍼 오버플로우(Buffer Overflow)** 위험이 있습니다. 배열 크기보다 긴 문자열이 입력되면, 할당된 메모리를 넘어 다른 메모리 영역을 침범하여 심각한 오류를 발생시킬 수 있습니다.

    ```c
    char name[10]; // 9글자 + '\0'
    scanf("%s", name); // "Hong Gildong" 입력 시 💥💥💥
    ```

2.  **`fgets(..., sizeof(...), stdin)` (권장!):**
    *   지정된 크기만큼만 입력받기 때문에 **버퍼 오버플로우를 방지**할 수 있습니다.
    *   공백을 포함한 문장을 입력받을 수 있습니다.
    *   **엔터(`\n`)까지 입력받아 배열에 저장**합니다. 따라서 출력 시 줄바꿈이 두 번 일어날 수 있으니, 필요에 따라 `\n`을 제거해야 합니다.

**예제:**

```c
#include <stdio.h> // printf, scanf, fgets를 위해 필요
#include <string.h> // strlen, strchr 등을 위해 필요

int main() {
    char name_scanf[10]; // 9글자 + '\0'
    char name_fgets[10]; // 9글자 + '\0'

    printf("이름을 입력하세요 (scanf): ");
    scanf("%s", name_scanf); // 공백 이전까지만 입력받고, 버퍼 오버플로우 위험!
    printf("scanf로 입력받은 이름: %s\n", name_scanf);

    // scanf는 버퍼에 남은 \n을 그대로 두기 때문에, 
    // 다음 fgets가 바로 \n을 읽어버릴 수 있습니다.
    // 이를 방지하기 위해 버퍼를 비워주는 것이 좋습니다. (선택 사항)
    while (getchar() != '\n' && getchar() != EOF); 

    printf("이름을 입력하세요 (fgets, 공백 가능): ");
    fgets(name_fgets, sizeof(name_fgets), stdin); // 안전하게 9글자까지만 입력받고 \n 포함

    // fgets는 마지막에 \n을 포함하므로 제거해주는 것이 보통입니다.
    // \n 문자를 찾아서 널 문자로 바꿔주는 작업
    // strchr 함수는 특정 문자를 문자열 내에서 찾아 그 위치의 포인터를 반환합니다.
    size_t len = strlen(name_fgets); // 문자열 길이 계산 (널 문자 제외)
    if (len > 0 && name_fgets[len - 1] == '\n') {
        name_fgets[len - 1] = '\0'; // 마지막 \n을 널 문자로 변경
    }
    
    printf("fgets로 입력받은 이름: %s\n", name_fgets);
    
    return 0;
}
```

<details>
<summary><b>실행 결과 확인하기 (예시 1: 짧은 이름)</b></summary>

```
이름을 입력하세요 (scanf): 김철수
scanf로 입력받은 이름: 김철수
이름을 입력하세요 (fgets, 공백 가능): 이영희
fgets로 입력받은 이름: 이영희
```
</details>

<details>
<summary><b>실행 결과 확인하기 (예시 2: 긴 이름 입력 시 scanf의 문제점)</b></summary>

```
이름을 입력하세요 (scanf): SuperStarKim
scanf로 입력받은 이름: SuperStarKim
이름을 입력하세요 (fgets, 공백 가능):
fgets로 입력받은 이름: 
```
(`scanf`에서 `name_scanf` 배열(`char name_scanf[10]`)의 크기를 넘어 `SuperStarKim` (12글자)을 입력했기 때문에 **버퍼 오버플로우**가 발생했습니다. 프로그램이 오작동하거나 `fgets`가 제대로 작동하지 않을 수 있습니다. **절대 이렇게 하지 마세요!** 이 예시는 `scanf`의 위험성을 보여주기 위함입니다.)

<details>
<summary><b>실행 결과 확인하기 (예시 3: 공백 포함 입력 시 scanf의 문제점)</b></summary>

```
이름을 입력하세요 (scanf): Hong Gildong
scanf로 입력받은 이름: Hong
이름을 입력하세요 (fgets, 공백 가능):
fgets로 입력받은 이름: Gildong
```
(`scanf`는 공백을 만나면 입력을 중단합니다. `Hong`만 `name_scanf`에 저장되고, `Gildong`과 뒤따르는 `\n`은 입력 버퍼에 남아있게 됩니다. 이후 `fgets` 호출 시 `Gildong`이 `name_fgets`에 저장됩니다. 이는 `scanf`의 동작 특성입니다.)

</details>

### 2.4. 유용한 문자열 함수들 (`<string.h>`)

C 언어는 문자열을 다루기 위한 다양한 표준 라이브러리 함수들을 제공합니다. 이 함수들은 `<string.h>` 헤더 파일에 선언되어 있습니다. 몇 가지 중요한 함수들을 살펴봅시다.

| 함수명               | 기능                                                     | 예시                                                     | 주의사항                                                                               |
| :------------------- | :------------------------------------------------------- | :------------------------------------------------------- | :------------------------------------------------------------------------------------- |
| `strlen(str)`        | 문자열의 길이(널 문자 제외)를 반환                      | `strlen("Hello")` -> 5                                   | 널 문자가 없으면 이상 동작                                                             |
| `strcpy(dest, src)`  | `src` 문자열을 `dest`로 복사                             | `strcpy(buffer, "World")`                                | `dest`의 크기가 충분하지 않으면 **버퍼 오버플로우 발생!** `strncpy`를 권장.            |
| `strncpy(dest, src, n)` | `src` 문자열의 `n`개 문자까지 `dest`로 복사.          | `strncpy(buffer, "Hello", 5)`                            | `n`개 복사 후 널 문자를 추가하지 않음. 수동으로 `dest[n] = '\0'` 추가 필요.          |
| `strcat(dest, src)`  | `src` 문자열을 `dest` 문자열 뒤에 연결 (이어 붙이기)   | `strcat(str1, " World")`                                 | `dest`의 크기가 충분하지 않으면 **버퍼 오버플로우 발생!** `strncat`을 권장.            |
| `strncat(dest, src, n)` | `src` 문자열의 `n`개 문자까지 `dest` 뒤에 연결.       | `strncat(str1, " World", 3)`                             | `n`개 연결 후 널 문자를 자동으로 추가.                                                 |
| `strcmp(str1, str2)` | 두 문자열을 비교. 같으면 0, `str1`이 작으면 음수, `str1`이 크면 양수 반환 | `strcmp("apple", "banana")` -> 음수 `strcmp("cat", "cat")` -> 0 | 대소문자를 구분함. (대소문자 무시 비교는 `strcasecmp` 또는 `_stricmp` - 표준 X) |
| `strchr(str, ch)`    | `str`에서 `ch` 문자를 찾아 처음 나타나는 위치의 포인터 반환 | `strchr("Hello", 'l')`                                   | 문자를 찾지 못하면 `NULL` 반환                                                         |
| `strstr(haystack, needle)` | `haystack`에서 `needle` 문자열을 찾아 처음 나타나는 위치의 포인터 반환 | `strstr("HelloWorld", "Wo")`                             | 문자열을 찾지 못하면 `NULL` 반환                                                       |

**예제:**

```c
#include <stdio.h>
#include <string.h> // 문자열 함수를 사용하기 위해 포함해야 합니다!

int main() {
    char str1[50] = "Hello";
    char str2[50] = "World";
    char str3[50] = "Hello";
    char buffer[10]; // 복사/연결용 작은 버퍼

    // 1. strlen: 문자열 길이
    printf("str1의 길이: %zu\n", strlen(str1)); // %zu는 size_t 타입을 출력할 때 사용

    // 2. strcpy: 문자열 복사 (주의!)
    // strcpy(buffer, "VeryLongString"); // 💥 버퍼 오버플로우 위험!
    strncpy(buffer, "Small", sizeof(buffer) - 1); // 안전하게 복사
    buffer[sizeof(buffer) - 1] = '\0'; // strncpy는 널 문자를 보장하지 않으므로 수동 추가
    printf("buffer에 복사된 문자열: %s\n", buffer);

    // 3. strcat: 문자열 연결 (주의!)
    printf("원본 str1: %s\n", str1);
    strcat(str1, " "); // str1 뒤에 공백 연결
    strcat(str1, str2); // str1 뒤에 str2 연결
    printf("str1 + str2 (strcat): %s\n", str1);

    // 4. strcmp: 문자열 비교
    if (strcmp(str1, str2) == 0) {
        printf("str1과 str2는 같습니다.\n");
    } else {
        printf("str1과 str2는 다릅니다.\n"); // 출력될 부분
    }

    if (strcmp(str3, "Hello") == 0) {
        printf("str3은 'Hello'입니다.\n"); // 출력될 부분
    }

    // 5. strchr: 특정 문자 찾기
    char *ptr_char = strchr(str1, 'o');
    if (ptr_char != NULL) {
        printf("'o' 문자는 str1의 %ld번째 인덱스에 있습니다.\n", ptr_char - str1);
    } else {
        printf("'o' 문자를 str1에서 찾을 수 없습니다.\n");
    }
    
    // 6. strstr: 특정 문자열 찾기
    char *ptr_str = strstr(str1, "World");
    if (ptr_str != NULL) {
        printf("'World' 문자열은 str1의 %ld번째 인덱스부터 시작합니다.\n", ptr_str - str1);
    } else {
        printf("'World' 문자열을 str1에서 찾을 수 없습니다.\n");
    }

    return 0;
}
```

<details>
<summary><b>실행 결과 확인하기</b></summary>

```
str1의 길이: 5
buffer에 복사된 문자열: Small
원본 str1: Hello
str1 + str2 (strcat): Hello World
str1과 str2는 다릅니다.
str3은 'Hello'입니다.
'o' 문자는 str1의 4번째 인덱스에 있습니다.
'World' 문자열은 str1의 6번째 인덱스부터 시작합니다.
```
</details>

## 3. 문자열 배열 (배열의 배열): 여러 문자열 다루기

때로는 여러 개의 문자열을 한꺼번에 관리해야 할 때가 있습니다. 예를 들어, 요일 이름 목록이나 학생 이름 목록 같은 경우죠. 이럴 때 '문자열 배열'을 사용합니다. 문자열 배열은 **'문자 배열의 배열'**이라고 생각하면 이해하기 쉽습니다.

```c
char 배열이름[문자열_개수][각_문자열의_최대_길이];
```

**예제:**

```c
#include <stdio.h>

int main() {
    // 3개의 문자열을 저장할 수 있고, 각 문자열은 최대 19글자 + '\0'을 저장할 수 있습니다.
    char days[3][20] = {
        "Monday", 
        "Tuesday", 
        "Wednesday"
    };

    printf("--- 요일 목록 ---\n");
    for (int i = 0; i < 3; i++) {
        printf("요일 %d: %s\n", i + 1, days[i]);
    }

    // 새로운 요일 입력받기
    printf("\n네 번째 요일을 입력해주세요: ");
    // fgets(days[3], sizeof(days[3]), stdin); // 💥 주의! days[3]은 존재하지 않는 인덱스
    // 올바른 방법:
    char new_day[20]; // 임시 배열에 입력받은 후 복사
    fgets(new_day, sizeof(new_day), stdin);
    
    // fgets로 인해 붙은 '\n' 제거
    size_t len = 0;
    if (new_day[0] != '\0') { // new_day가 비어있지 않은 경우에만
        len = strlen(new_day);
        if (len > 0 && new_day[len - 1] == '\n') {
            new_day[len - 1] = '\0';
        }
    }
    
    // days[3]에 직접 넣을 수 없으므로, 새로운 배열을 선언해야 합니다.
    // 만약 `days` 배열을 4개로 만들었다면 `strcpy(days[3], new_day);` 가능
    // 현재는 days[0]~days[2]까지만 가능
    printf("입력받은 요일: %s\n", new_day);

    printf("\n두 번째 요일을 다른 것으로 바꿔봅시다.\n");
    strcpy(days[1], "TUESDAY (Modified)"); // strcpy를 사용하여 문자열 변경
    
    printf("--- 수정된 요일 목록 ---\n");
    for (int i = 0; i < 3; i++) {
        printf("요일 %d: %s\n", i + 1, days[i]);
    }

    return 0;
}
```

<details>
<summary><b>실행 결과 확인하기</b></summary>

```
--- 요일 목록 ---
요일 1: Monday
요일 2: Tuesday
요일 3: Wednesday

네 번째 요일을 입력해주세요: Thursday
입력받은 요일: Thursday

두 번째 요일을 다른 것으로 바꿔봅시다.
--- 수정된 요일 목록 ---
요일 1: Monday
요일 2: TUESDAY (Modified)
요일 3: Wednesday
```
</details>

---

## 👨‍🏫 김사부의 마무리: 연습만이 살 길!

자네들, 오늘 배열과 문자열에 대해 정말 많은 것을 배웠습니다!

*   **배열**은 같은 종류의 데이터를 묶어 관리하는 연속된 공간이라는 것.
*   **인덱스**는 0부터 시작해서 각 요소에 접근한다는 것.
*   **문자열**은 `char` 배열의 특수한 형태로, 마지막에 **널 종료 문자(`\0`)**가 반드시 필요하다는 것.
*   `scanf` 보다는 **`fgets`**가 더 안전한 문자열 입력 함수라는 것.
*   `strlen`, `strcpy`, `strcat`, `strcmp` 등 유용한 **문자열 함수**들을 `<string.h>`에서 사용할 수 있다는 것.

이 개념들은 C 언어를 배우는 데 있어서 아주 아주 중요한 기둥과 같습니다. 특히 `\0`와 버퍼 오버플로우의 위험성에 대한 이해는 실력 있는 개발자가 되기 위한 필수 요소입니다.

**오늘 배운 내용을 절대 눈으로만 보지 마세요!** 직접 코드를 타이핑하고, 컴파일하고, 실행해보고, 값을 바꿔가며 테스트해보세요. 그래야만 여러분의 지식이 진정한 실력으로 변모할 겁니다.

---

### 📝 오늘의 숙제 (Homework)

다음 문제를 직접 코드로 구현해보세요.

1.  **정수 배열 평균 계산하기:**
    *   `int scores[5] = {85, 90, 75, 92, 88};` 와 같은 배열을 선언하고 초기화하세요.
    *   `for` 문을 사용하여 배열의 모든 요소의 합계를 계산하고, 평균을 구하여 출력하세요. (소수점 첫째 자리까지 출력)
2.  **가장 긴 문자열 찾기:**
    *   `char cities[4][30] = {"Seoul", "Busan", "Jeju Island", "Gwangju"};` 와 같은 문자열 배열을 선언하세요.
    *   `for` 문과 `strlen()` 함수를 사용하여 이 배열에서 가장 길이가 긴 문자열을 찾아서 출력하세요.
3.  **간단한 이름 입력 및 환영 메시지:**
    *   사용자로부터 이름을 입력받아 `char name[20];` 배열에 저장하세요. (**반드시 `fgets`를 사용하고, `\n`을 제거하는 처리까지 하세요!**)
    *   입력받은 이름을 사용하여 "안녕하세요, [이름]님! C 언어 학습을 환영합니다!" 라는 메시지를 출력하세요.

수고 많으셨습니다, 제자들! 다음 6강에서는 또 다른 강력한 도구인 '포인터'에 대해 배우게 될 겁니다. 오늘 배운 내용을 튼튼하게 다져놓으면 다음 강의도 무리 없이 따라올 수 있을 거예요. 그럼 다음 시간에 건강한 모습으로 다시 만납시다! 화이팅! 💪

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
