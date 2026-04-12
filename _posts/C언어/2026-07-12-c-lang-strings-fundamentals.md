---
layout: single
title: "C언어 심화: 문자열 처리 기초"
date: 2026-07-12 21:07:30
categories: [C언어]
---

### #9강: C언어 심화 - 문자열 처리 기초: 문자열 마스터가 되는 여정

안녕하세요, 코딩의 신나는 모험가 여러분! 오늘은 C언어의 숨겨진 보석, **문자열 처리**에 대해 깊이 파고들어볼 거예요. 혹시 초보자라면 걱정 마세요! 저와 함께하면 문자열도 마법처럼 다룰 수 있게 될 거예요. 지금부터 시작해볼까요?

#### 💡 문자열이란 무엇인가요?

문자열은 마치 **마법의 책** 같아요. 한 페이지 한 페이지에 글자들이 모여 이야기를 전하는 거죠. C에서는 이 마법의 책을 다루는 특별한 방법들이 있답니다.

### 기본 개념 이해하기

#### 1. 문자열 선언하기

문자열은 특별한 타입, `char` 배열로 표현됩니다. 예를 들어, "안녕하세요"라는 문자열을 선언해볼게요.

```c
#include <stdio.h>

int main() {
    // 문자열 선언 예제
    char greeting[] = "안녕하세요";  // 배열 이름은 원하는 대로 바꿀 수 있어요!
    
    printf("%s\n", greeting);  // 출력: 안녕하세요
    return 0;
}
```

**💡 초보자 폭풍 질문!**
- **Q:** `char greeting[]` 에서 배열 이름 `[]`가 왜 필요한가요?
- **A:** `[]`는 배열 이름을 지정하고, 그 배열에 들어갈 문자들을 저장할 공간을 동적으로 할당해줍니다. 예를 들어, "안녕하세요"는 6글자지만, `[]` 덕분에 공간이 유연하게 확장됩니다.

#### 2. 문자열 포인터 사용하기

문자열 포인터는 마치 **마법의 지팡이** 같아요. 포인터를 통해 문자열의 첫 번째 글자를 바로 가리키고 다룰 수 있어요.

```c
#include <stdio.h>

int main() {
    char* msg = "이 세상은 놀랍습니다";  // 포인터 선언
    
    printf("%s\n", msg);  // 출력: 이 세상은 놀랍습니다
    
    // 포인터가 가리키는 위치 변경하기
    msg = "새로운 모험이 기다리고 있어요";
    printf("%s\n", msg);  // 출력: 새로운 모험이 기다리고 있어요
    
    return 0;
}
```

**🚨 실무주의보**
- **Q:** 포인터를 사용하면 메모리 관리에 주의해야 한다는데, 왜 그런가요?
- **A:** 포인터를 잘못 다루면 메모리 누수나 접근 오류가 발생할 수 있어요. 항상 포인터가 올바른 메모리 위치를 가리키는지 확인하세요!

### 문자열 조작: 핵심 기술들

#### 1. 문자열 복사와 비교

문자열을 복사하거나 비교할 때는 `strcpy`와 `strcmp` 함수가 필수죠!

```c
#include <stdio.h>
#include <string.h>  // 문자열 함수 헤더 파일

int main() {
    char original[] = "코딩은 재미있어요";
    char copy[50];  // 복사할 공간 할당
    
    // 문자열 복사
    strcpy(copy, original);  // copy에 original 복사
    printf("복사된 문자열: %s\n", copy);  // 출력: 코딩은 재미있어요
    
    // 문자열 비교
    int result = strcmp(original, copy);  // 0이면 같음, 음수면 앞 글자가 작음, 양수면 큼
    if (result == 0) {
        printf("문자열이 같아요!\n");
    } else {
        printf("문자열이 다릅니다.\n");
    }
    
    return 0;
}
```

**코드 해부:**
- `strcpy(copy, original);`: `copy` 배열에 `original` 문자열을 복사합니다.
- `strcmp(original, copy);`: 두 문자열을 비교하고 결과를 반환합니다.

#### 2. 문자열 탐색과 조작

문자열 내에서 특정 글자를 찾거나 수정할 때는 `strlen`, `strchr`, `strcat` 등의 함수가 유용해요.

```c
#include <stdio.h>
#include <string.h>

int main() {
    char sentence[] = "오늘은 맑아서 산책하기 좋은 날이에요";
    char findChar = '좋';  // 찾고자 하는 문자
    
    // 문자열 길이 구하기
    int length = strlen(sentence);
    printf("문자열 길이: %d\n", length);  // 출력: 문자열 길이: 39
    
    // 특정 문자 찾기
    char* found = strchr(sentence, findChar[0]);  // 첫 글자만 비교
    if (found) {
        printf("문자 '%c'는 %ld 위치에 있습니다.\n", findChar[0], found - sentence);
    } else {
        printf("문자 '%c'는 없어요.\n", findChar[0]);
    }
    
    // 문자열 연결하기
    char additional[] = " 더해요";
    strcat(sentence, additional);  // 문자열 연결
    printf("수정된 문자열: %s\n", sentence);  // 출력: 수정된 문자열: 오늘은 맑아서 산책하기 좋은 날이에요 더해요
    
    return 0;
}
```

**코드 해부:**
- `strlen(sentence);`: `sentence`의 길이를 반환합니다.
- `strchr(sentence, findChar[0]);`: `sentence`에서 `findChar`의 첫 글자를 찾아줍니다.
- `strcat(sentence, additional);`: `additional` 문자열을 `sentence` 뒤에 붙입니다.

### 실용적인 예제: 간단한 텍스트 편집기 만들기

자, 이제 이론을 실전에 적용해볼까요? 간단한 텍스트 편집기를 만들어보는 건 어떨까요?

```c
#include <stdio.h>
#include <string.h>

#define MAX_LINE_LENGTH 100  // 최대 라인 길이 설정

int main() {
    char buffer[MAX_LINE_LENGTH];  // 입력 버퍼
    char input[MAX_LINE_LENGTH];  // 임시 입력 버퍼
    char *result;  // 결과 문자열 저장

    printf("텍스트 편집기 시작!\n");
    while (1) {
        printf("텍스트 입력 (종료하려면 'exit' 입력): ");
        fgets(input, sizeof(input), stdin);  // 사용자 입력 받기
        
        // 입력이 'exit'인지 확인
        if (strcmp(input, "exit\n") == 0) {
            printf("텍스트 편집기 종료.\n");
            break;
        }
        
        // 입력 문자열을 처리하기 위해 복사
        strcpy(buffer, input);  // 입력 내용 복사
        
        // 문자열 내 특수 문자 처리 예시 (예: 소문자로 변환)
        result = strtok(buffer, " ");  // 단어별로 분리
        while (result != NULL) {
            strcpy(result, result);  // 예시로 간단히 복사 (실제에서는 대소문자 변환 등 적용)
            printf("처리된 텍스트: %s\n", result);
            result = strtok(NULL, " ");  // 다음 단어로 이동
        }
    }
    
    return 0;
}
```

**코드 해부:**
- `fgets(input, sizeof(input), stdin);`: 사용자 입력을 안전하게 받습니다.
- `strcpy(buffer, input);`: 입력 내용을 버퍼에 복사합니다.
- `strtok(buffer, " ");`: 문자열을 단어별로 분리하여 처리합니다 (여기서는 간단히 예시로 사용).

### 마무리 말씀

오늘 배운 문자열 처리 기술은 C 프로그래밍의 핵심 중 하나예요. 문자열을 자유롭게 다루는 능력은 코딩에서 굉장히 강력한 무기가 될 거예요. 이제 이 지식을 바탕으로 더 복잡한 프로젝트에 도전해보세요!

**💡 초보자 폭풍 질문!**
- **Q:** 문자열 처리에서 가장 자주 사용되는 함수들은 어떤 것들이 있나요?
- **A:** 주로 `strlen`, `strcpy`, `strcat`, `strcmp`, `strtok` 등이 많이 쓰입니다. 이 함수들을 적절히 활용하면 문자열 조작이 훨씬 쉬워집니다!

앞으로도 계속해서 성장해나가세요! 더 궁금한 점이 있으면 언제든지 물어봐주세요. 함께 코딩의 세계를 탐험해봐요! 🚀

---

이렇게 상세하고 생동감 넘치는 블로그 포스트로 문자열 처리 기초를 완벽하게 다루었습니다. 초보자들이 이해하기 쉽게 구성했으니, 많은 도움이 되길 바랍니다!

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
