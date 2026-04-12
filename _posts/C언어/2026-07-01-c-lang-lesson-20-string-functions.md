---
layout: single
title: "C언어 문자열 함수: strlen, strcpy 등"
date: 2026-07-01 14:19:39
categories: [C언어]
---

**20강: C언어 문자열 함수 strlen, strcpy 등** 🔥👨‍🏫

안녕하세요! 오늘은 C언어에서 가장 유용한 함수 중 하나인 **문자열 함수**에 대해 배워보겠습니다. 이 강의는 초보자도 쉽게 이해할 수 있도록 설명되었으며, 실무에서도 필수적인 내용을 전달할 것입니다.

### strlen() 함수: 문자열 길이 구하기

```c
#include <stdio.h>
#include <string.h>

int main() {
    char str[] = "Hello, World!";
    printf("문자열 길이: %d\n", strlen(str));
    return 0;
}
```

💡 **왜 이런 함수가 필요했을까?**

C언어는 문자열을 다루기 위해 별도의 라이브러리를 사용하지 않습니다. 이 때문에, 개발자들은 문자열 길이를 구하기 위해 따로 코드를 작성해야 합니다. 하지만 strlen() 함수는 이러한 문제를 해결해 주고 있습니다.

### strcpy() 함수: 문자열 복사

```c
#include <stdio.h>
#include <string.h>

int main() {
    char src[] = "원본 문자열";
    char dest[100];
    strcpy(dest, src);
    printf("복사된 문자열: %s\n", dest);
    return 0;
}
```

🚨 **실무주의보!**

strcpy() 함수는 문자열을 복사하는 데 사용합니다. 하지만 이 함수는 문자열의 크기가 넘으면 버퍼 오버플로를 발생시킬 수 있습니다. 따라서, 반드시 문자열의 크기를 확인하고, strncpy() 함수를 사용해야 합니다.

### strlen(), strcpy() 함수의 동작 원리

```c
#include <stdio.h>
#include <string.h>

// strlen() 함수의 동작 원리
char* my_strlen(char* str) {
    int length = 0;
    while (*str != '\0') {
        length++;
        str++;
    }
    return (char*)length;
}

int main() {
    char str[] = "Hello, World!";
    printf("문자열 길이: %d\n", my_strlen(str));
    return 0;
}
```

💡 **초보자 폭풍 질문!**

Q: strlen() 함수는 왜 \0를 찾을까?
A: 문자열의 끝은 항상 null terminated(\0)로 저장되기 때문에, strlen() 함수도 이를 찾아서 길이를 구합니다.

### 실무 활용: strcpy(), strncpy()

```c
#include <stdio.h>
#include <string.h>

int main() {
    char src[] = "원본 문자열";
    char dest[100];
    // strcpy(dest, src); // 버퍼 오버플로 발생
    strncpy(dest, src, 10); // 10자까지 복사
    printf("복사된 문자열: %s\n", dest);
    return 0;
}
```

### 정리

이 강의에서 배운 strlen(), strcpy() 함수는 C언어 개발자에게 필수적인 내용입니다. 하지만, 실무에서는 이러한 함수를 직접 사용하기보다, string.h 라이브러리를 포함하여 strlen(), strcpy(), strncpy() 함수를 사용하는 것이 좋습니다.

💡 **마지막 질문!**

Q: string.h 라이브러리에서 왜 strcpy(), strncpy() 함수가 제공되는지?
A: 문자열을 다루는 경우, 이러한 함수가 기본적으로 제공되어 있기 때문에, 직접 구현하기보다 라이브러리를 포함하여 사용하는 것이 더 좋습니다.

이상으로 C언어 문자열 함수 strlen, strcpy 등에 대해 배웠습니다. 여러분도 실무에서 이들 함수를 이용해 성과를 내 보세요! 👏👍

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
