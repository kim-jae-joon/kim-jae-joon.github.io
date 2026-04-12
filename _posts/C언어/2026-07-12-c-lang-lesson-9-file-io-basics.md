---
layout: single
title: "C언어 응용: 파일 입출력 기초"
date: 2026-07-12 19:37:52
categories: [C언어]
---

## 🚀 9강: C언어 응용 - 파일 입출력 기초: 컴퓨터와 대화하는 마법, 파일로!

안녕하세요, 코딩 탐험가 여러분! 오늘은 C 언어의 마법을 한층 더 넓혀줄 **파일 입출력** 기초를 탐험해 보려 합니다. 🤯  마치 컴퓨터와 직접 대화하는 마법사가 된 듯한 경험을 선사할게요!  

**진짜 신기하죠?** 컴퓨터는 단순히 코드를 실행하는 기계가 아니라, 데이터의 저장고이기도 합니다. 파일 입출력은 이 데이터 창고와 소통하는 열쇠와 같아요!

### 💡 기본 개념: 파일, 입출력, 그리고 그 이유

파일이란 간단히 말해 데이터를 저장하는 컨테이너입니다. 텍스트 파일, 이미지 파일, 프로그램 파일 등 다양하게 존재하죠. C 언어에서는 `fopen()`, `fread()`, `fwrite()`, `fclose()` 함수를 이용해 이 데이터와 멋지게 교류할 수 있습니다.

**왜 파일 입출력이 중요할까요?**

* **데이터 저장 및 관리:** 게임 점수, 사용자 정보, 로그 데이터 등을 영구적으로 저장하고 관리할 수 있어요. 마치 디지털 일기장처럼요!
* **데이터 공유:** 여러 프로그램이나 시스템 간에 데이터를 효율적으로 주고받을 수 있어요. 팀 프로젝트에서 파일 공유처럼 유용하죠!
* **작업 자동화:** 반복적인 데이터 처리 작업을 자동화하여 시간을 절약할 수 있어요. 생각만 해도 짜릿하죠? 🤩

### 📝 파일 열기: `fopen()` 함수 - 마법의 열쇠를 쥐다

파일 작업의 첫걸음은 바로 **열기**입니다! `fopen()` 함수가 우리의 손을 잡아주죠.

**예제 코드 1: 텍스트 파일 열기**

```c
#include <stdio.h>

int main() {
    FILE *filePtr; // 파일 포인터 변수 선언

    // "파일 이름"은 원하는 파일 경로로 변경하세요!
    filePtr = fopen("example.txt", "r"); // "r"은 읽기 모드

    if (filePtr == NULL) { // 파일 열기 실패 확인
        printf("파일을 열 수 없습니다!\n");
        return 1; // 에러 발생 시 프로그램 종료
    }

    printf("파일 열기 성공!\n");
    fclose(filePtr); // 작업 완료 후 닫기
    return 0;
}
```

**코드 해부:**

1. `FILE *filePtr;`: 파일 작업을 위한 포인터 변수를 선언합니다. 마치 마법 지팡이처럼 파일을 가리키는 역할을 해요!
2. `fopen("example.txt", "r");`: "example.txt" 파일을 **읽기 모드 ("r")**로 엽니다. 다른 모드로는 **쓰기 ("w"), 추가 ("a")** 등이 있어요.
3. `if (filePtr == NULL)`: 파일 열기가 성공했는지 확인합니다. `NULL`이면 실패! 마치 마법사가 마법 실패를 알리는 신호처럼요!
4. `fclose(filePtr);`: 파일 작업 완료 후 꼭 닫아주는 것이 중요해요! 마법 지팡이를 제자리에 돌려놓는 것과 같죠.

**💡 초보자 폭풍 질문!**

* `fopen()` 함수에서 사용 가능한 모드는 무엇이 있나요?

**답변:**  
주요 모드는 다음과 같습니다:
* `"r"`: 읽기 모드
* `"w"`: 쓰기 모드 (기존 파일 삭제 후 새로 쓰기)
* `"a"`: 추가 모드 (파일 끝에 데이터 추가)
* `"r+"`: 읽기 및 쓰기 모드
* `"w+"`: 읽기 및 쓰기 모드 (기존 파일 삭제)
* `"a+"`: 읽기 및 추가 모드

### 🔢 데이터 읽기: `fread()` 함수 - 마법의 책장에서 책 읽기

파일을 열었다면 이제 그 안의 데이터를 읽어낼 차례입니다! `fread()` 함수가 우리의 책장을 열어줍니다.

**예제 코드 2: 파일 내용 읽기**

```c
#include <stdio.h>

int main() {
    FILE *filePtr = fopen("example.txt", "r");
    if (filePtr == NULL) {
        printf("파일 열기 실패!\n");
        return 1;
    }

    char buffer[100]; // 읽어올 데이터를 저장할 버퍼
    size_t bytesRead; // 읽어온 바이트 수

    while ((bytesRead = fread(buffer, sizeof(char), sizeof(buffer), filePtr)) > 0) { // 한 줄씩 읽기
        printf("%s", buffer); // 읽은 내용 출력
    }

    if (ferror(filePtr)) { // 오류 발생 확인
        printf("파일 읽기 오류!\n");
    }

    fclose(filePtr);
    return 0;
}
```

**코드 해부:**

1. `char buffer[100];`: 파일에서 읽어올 데이터를 임시로 저장할 버퍼를 선언합니다. 마치 마법 책장에서 한 장씩 꺼내는 듯한 느낌이죠!
2. `fread(buffer, sizeof(char), sizeof(buffer), filePtr)`: 
    * `buffer`: 데이터를 저장할 메모리 위치
    * `sizeof(char)`: 읽어올 데이터 단위 (문자 하나)
    * `sizeof(buffer)`: 읽어올 데이터 개수 (버퍼 크기)
    * `filePtr`: 열린 파일 포인터
    * `bytesRead`: 실제로 읽어온 바이트 수를 반환합니다.
3. `while` 루프: 파일 끝까지 데이터를 한 줄씩 읽어옵니다. 마치 책장을 넘겨가며 이야기를 읽는 것처럼요!

### 📝 데이터 쓰기: `fwrite()` 함수 - 마법의 펜으로 글 남기기

데이터를 파일에 쓰는 것도 마찬가지로 중요합니다! `fwrite()` 함수로 마법의 펜을 이용해 내용을 기록해 보세요.

**예제 코드 3: 텍스트 파일에 데이터 쓰기**

```c
#include <stdio.h>

int main() {
    FILE *filePtr = fopen("output.txt", "w"); // 쓰기 모드로 열기 (기존 파일 삭제)
    if (filePtr == NULL) {
        printf("파일 열기 실패!\n");
        return 1;
    }

    char *message = "안녕하세요, 파일에 쓰인 마법!\n"; // 쓸 데이터
    size_t bytesWritten = fwrite(message, sizeof(char), strlen(message), filePtr);

    if (bytesWritten != strlen(message)) { // 쓰기 오류 확인
        printf("파일 쓰기 오류!\n");
    } else {
        printf("데이터 쓰기 성공!\n");
    }

    fclose(filePtr);
    return 0;
}
```

**코드 해부:**

1. `fopen("output.txt", "w");`: "output.txt" 파일을 **쓰기 모드 ("w")**로 엽니다. 기존 내용은 사라집니다. 마치 깨끗한 빈 종이에 새로운 글을 쓰는 것과 같죠!
2. `fwrite(message, sizeof(char), strlen(message), filePtr);`:
    * `message`: 쓸 데이터의 시작 주소
    * `sizeof(char)`: 데이터 단위 (문자 하나)
    * `strlen(message)`: 쓸 데이터의 길이
    * `filePtr`: 열린 파일 포인터
    * `bytesWritten`: 실제로 쓴 바이트 수를 반환합니다.

### ⚙️ 반복문과 조건문 활용: 파일 작업의 유연성 증대

파일 입출력은 단순히 데이터 읽고 쓰는 것 이상으로, 다양한 상황에 맞춰 유연하게 활용할 수 있습니다. 반복문과 조건문을 활용하면 더욱 강력한 마법을 만들 수 있습니다!

**예제 코드 4: 여러 줄 읽기 (for문 활용)**

```c
#include <stdio.h>

int main() {
    FILE *filePtr = fopen("data.txt", "r");
    if (filePtr == NULL) {
        printf("파일 열기 실패!\n");
        return 1;
    }

    char line[200]; // 한 줄씩 읽을 버퍼

    // 각 줄을 읽기 위한 for 루프
    for (int i = 0; fgets(line, sizeof(line), filePtr) != NULL; i++) {
        printf("%d번째 줄: %s", i + 1, line); // 각 줄 번호와 함께 출력
    }

    fclose(filePtr);
    return 0;
}
```

**코드 해부:**

1. `fgets(line, sizeof(line), filePtr)`: 각 줄을 읽습니다. `fgets()`는 줄 끝 문자 (`\n`)를 포함하여 읽습니다.
2. `for` 루프: 파일 끝까지 각 줄을 읽어 처리합니다. 마치 책 한 권을 한 페이지씩 넘기며 읽는 것처럼요!

**🚨 실무주의보**

* 파일 경로는 절대 경로 또는 상대 경로를 정확하게 지정해야 합니다. 잘못된 경로는 데이터 손실로 이어질 수 있으니 주의하세요!
* 파일 작업 중 오류 발생 시 (예: 파일이 존재하지 않음), 적절한 에러 처리를 통해 프로그램 안정성을 확보하세요.

### 🎓 마무리: 파일 입출력, 코딩의 힘을 키우는 열쇠

오늘 배운 파일 입출력 기초는 C 언어 개발자로서 필수적인 기술입니다. 데이터를 저장하고 공유하며 자동화하는 능력은 당신의 코딩 실력을 한층 업그레이드 시켜줄 거예요! 

이제 여러분도 컴퓨터와 활발하게 대화하며 데이터를 자유자재로 다룰 수 있는 마법사가 되셨습니다! 🧙‍♂️✨ 앞으로 더 멋진 프로그램을 만들어갈 당신을 응원합니다!

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
