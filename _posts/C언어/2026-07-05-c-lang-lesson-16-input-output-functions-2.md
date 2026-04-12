---
layout: single
title: "C언어 입출력 함수(2): gets, putchar"
date: 2026-07-05 14:19:04
categories: [C언어]
---

**16강: C언어 입출력 함수(2) - gets, putchar**

🔥💡 **입출력 함수에 대해 아직 모르시나요? 이번 강의에서는 C언어에서 입출력을 처리하는 핵심 함수인 gets()와 putchar()를 소개합니다!**

💬 **이거 모르면 큰일 납니다!** C언어는 입출력 함수가 매우 중요합니다. 입출력 함수를 제대로 이해하지 않으면 프로그램의 실행 결과가 올바르게 나타나지 않을 수 있습니다.

---

### 1. gets()

`gets()` 함수는 문자열을 입력받는 함수입니다. 이 함수는 `stdio.h` 헤더 파일에 정의되어 있습니다.

```c
#include <stdio.h>

int main() {
    char str[20];
    printf("이름을 입력하세요: ");
    gets(str);
    printf("입력하신 이름은 %s입니다.\n", str);
    return 0;
}
```

💡 **왜 이 코드처럼 썼을까요?** `gets()` 함수는 사용자가 입력한 문자열을 받기 때문에, 입력받는 문자열의 크기를 지정해 주어야 합니다. 위 코드에서 `char str[20];` 이라는 선언이 있는 이유입니다. 만약에 큰 문자열을 입력받게 되면, 보다큰 공간을 확보하는 것이 좋습니다.

```c
#include <stdio.h>

int main() {
    char str[100];
    printf("이름을 입력하세요: ");
    gets(str);
    printf("입력하신 이름은 %s입니다.\n", str);
    return 0;
}
```

---

### 2. putchar()

`putchar()` 함수는 한 문자를 출력하는 함수입니다. 이 함수도 `stdio.h` 헤더 파일에 정의되어 있습니다.

```c
#include <stdio.h>

int main() {
    char c = 'A';
    printf("출력할 문자: %c\n", c);
    putchar(c);
    return 0;
}
```

💡 **왜 이 코드처럼 썼을까요?** 위 코드에서 `printf()` 함수와 `putchar()` 함수가 같이 사용된 이유입니다. `printf()` 함수는 `%c` 형식으로 출력하기 때문에, `putchar()` 함수를 통해 한 문자를 출력할 수 있습니다.

```c
#include <stdio.h>

int main() {
    char c = 'A';
    printf("출력할 문자: ");
    putchar(c);
    return 0;
}
```

---

### 실무에서는 이렇게 사용해요!

`gets()`와 `putchar()` 함수는 C언어의 입출력 함수 중에서 가장 기본적인 함수입니다. 따라서, 프로그램을 작성할 때 반드시 이러한 함수를 사용해야 합니다.

💬 **이거 모르면 큰일 납니다!** 하지만 `gets()` 함수는 보안상 문제가 있어, 보다 안전한 함수인 `fgets()` 함수를 사용하는 것이 좋습니다. `putchar()` 함수도 반드시 `printf()` 함수와 함께 사용해야 합니다.

---

### 질문은 언제든지 가능해요!

💬 **질문이 떠올랐나요?** 이번 강의에 대한 궁금증을 가지고 계신가요? 그럼, 저희에게 물어보세요! 💬

---

### 실무주의보!

🚨 **실무에서는 이 함수를 사용해야 합니다!** 하지만 보안상 문제가 있는 `gets()` 함수는 사용하는 것이 좋지 않습니다. 따라서, `fgets()` 함수를 사용해야 합니다.

💡 **이 강의에서 배운 것을 실제로 실습해 보세요!** 💪

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
