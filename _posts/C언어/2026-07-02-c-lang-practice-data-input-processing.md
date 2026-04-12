---
layout: single
title: "데이터 입력 및 처리: 실습 중심"
date: 2026-07-02 14:19:28
categories: [C언어]
---

**19강: 데이터 입력 및 처리, 실습 중심! 🔥**

안녕하세요, 여러분! 저는 최대한 편하게 잘 알려드릴게요. 오늘은 진짜 중요한 강의입니다! 💡 초보자 폭풍 질문!

### 개념부터 시작해 보겠습니다.

C언어에서 데이터 입력 및 처리는 정말 중요합니다. 그 이유는 간단합니다. **데이터가 없으면 프로그램이 아무것도 할 수 없어요**! 🤯

### 데이터 타입

C언어에서는 8가지 기본적인 데이터 타입을 제공합니다. 

#### 정수형

- `int` : 4바이트의 정수형, C99에서 지원하는 `_Int32_t`로 대체 가능
- `uint` : 4바이트의 부호없는 정수형

```c
#include <stdio.h>

int main() {
    int a = 10;
    printf("%d\n", sizeof(a));
    
    return 0;
}
```

#### 실수형

- `float` : 4바이트의 실수형, C99에서 지원하는 `_Float32_t`로 대체 가능
- `double` : 8바이트의 실수형
- `long double` : 10바이트의 실수형

```c
#include <stdio.h>

int main() {
    float a = 10.5;
    printf("%f\n", sizeof(a));
    
    return 0;
}
```

#### 문자열 형

- `char` : 1바이트의 문자형

```c
#include <stdio.h>

int main() {
    char a = 'A';
    printf("%c\n", sizeof(a));
    
    return 0;
}
```

#### 논리형

- `_Bool` : 1바이트의 논리형, C99에서 지원
- `bool` : 1바이트의 논리형, ANSI-C 표준에 추가됨

```c
#include <stdio.h>

int main() {
    _Bool a = true;
    printf("%d\n", sizeof(a));
    
    return 0;
}
```

#### Void 형

- `_Void_t` : C99에서 지원하는 void 타입의 대체 방법, ANSI-C 표준에 추가됨

```c
#include <stdio.h>

int main() {
    _Void_t a = NULL;
    printf("%p\n", &a);
    
    return 0;
}
```

#### 포인터 형

- `_Ptrdiff_t` : C99에서 지원하는 size_t, ptrdiff_t, time_t의 대체 방법
- `size_t` : 객체 크기를 표현하는 unsigned형

```c
#include <stdio.h>

int main() {
    int a = 10;
    printf("%lu\n", sizeof(a));
    
    return 0;
}
```

#### 시간 형

- `_Time_t` : C99에서 지원하는 time_t의 대체 방법, ANSI-C 표준에 추가됨

```c
#include <stdio.h>

int main() {
    _Time_t a = 10000000;
    printf("%lu\n", sizeof(a));
    
    return 0;
}
```

### 실습: 데이터 입력 및 출력

#### printf()

- `printf()` : 형식 문자열이 포함된 출력 함수

```c
#include <stdio.h>

int main() {
    int a = 10;
    char b[] = "Hello, World!";
    
    printf("a = %d\n", a);
    printf("b = %s\n", b);
    
    return 0;
}
```

#### scanf()

- `scanf()` : 사용자 입력을 읽어오는 함수

```c
#include <stdio.h>

int main() {
    int a, b;
    char c[] = "Hello, World!";
    
    printf("Enter your name: ");
    scanf("%s", c);
    printf("Hello, %s!\n", c);
    
    return 0;
}
```

#### getchar()

- `getchar()` : 사용자 입력을 읽어오는 함수

```c
#include <stdio.h>

int main() {
    char c = getchar();
    printf("%c\n", c);
    
    return 0;
}
```

### 실습: 데이터 입출력 예시

#### 파일 입출력

- `fopen()` : 파일을 연다.
- `fscanf()` : 파일에서 데이터를 읽어온다.
- `fprintf()` : 파일에 데이터를 출력한다.

```c
#include <stdio.h>

int main() {
    FILE *fp = fopen("example.txt", "w");
    
    if (fp == NULL) {
        printf("Failed to open file.\n");
        return 1;
    }
    
    fprintf(fp, "Hello, World!\n");
    
    fclose(fp);
    
    return 0;
}
```

#### 네트워크 입출력

- `socket()` : 소켓을 연다.
- `send()` : 데이터를 보낸다.
- `recv()` : 데이터를 받는다.

```c
#include <stdio.h>
#include <sys/socket.h>

int main() {
    int sock = socket(AF_INET, SOCK_STREAM, 0);
    
    if (sock == -1) {
        printf("Failed to create socket.\n");
        return 1;
    }
    
    // ...
    
    close(sock);
    
    return 0;
}
```

### 결론

이제 여러분은 데이터 입력 및 처리에 대해 충분히 이해하고 실습을 해보셨겠군요! 😊 기억하길 바라고, 다음 강의에서 더 많은 것을 알려드릴게요. 👋

**실무 주의보 🚨**

* 데이터 타입은 정확하게 선언하길 바랍니다.
* 입출력 함수는 사용에 주의하세요.

**질문과 답**

* Q: 이 데이터 타입이 뭔가요?
A: 데이터 타입은 변수가 저장할 수 있는 자료형입니다. 🔍
* Q: 입출력 함수를 사용하려면 어떻게 해야 하나요?
A: 입출력 함수는 파일이나 네트워크와 같은 외부 자원을 연동하여 사용합니다. 📚

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
