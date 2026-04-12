---
layout: single
title: "C언어 표준 입출력 함수: getchar, putchar"
date: 2026-07-03 14:19:21
categories: [C언어]
---

**18강: C언어 표준 입출력 함수: getchar, putchar 🔥**

 안녕하세요! 여러분 모두 bienvenidos(환영합니다)! 오늘은 C언어에서 표준 입출력 함수인 `getchar`와 `putchar`에 대해 배웁니다. 이 두 함수는 자바스크립트의 `prompt`함수처럼 사용할 수 없지만, 그래도 그만큼의 강력한 기능을 가지고 있습니다. 😎

**개념 설명: getchar vs putchar**

`getchar` 함수는 표준 입력으로부터 한 문자를 읽어와서 반환하는 함수입니다. 반면에 `putchar` 함수는 표준 출력으로 한 문자를 출력하는 함수입니다.

```c
#include <stdio.h>

int main() {
    int c = getchar();
    printf("입력한 문자: %c\n", c);

    putchar('A');
    return 0;
}
```

위 코드에서 `getchar`함수는 표준 입력으로부터 한 문자를 읽어와서 그 값을 변수 `c`에 저장합니다. 그리고 `printf` 함수를 사용하여 이 문자를 출력합니다. `putchar` 함수는 단순하게 'A'라는 문자를 표준 출력로 출력하는 함수입니다.

**실무 활용: getchar**

`getchar`함수를 실무에서 어떻게 사용할 수 있을까요? 예를 들어, 프로그램을 개발할 때 사용자로부터 입력을 받을 필요가 있을 경우에 `getchar` 함수를 사용할 수 있습니다. 

```c
#include <stdio.h>

int main() {
    int age;
    printf("나이를 입력하세요: ");
    scanf("%d", &age);
    printf("당신의 나이는 %d입니다.\n", age);

    char name[10];
    printf("이름을 입력하세요: ");
    fgets(name, sizeof(name), stdin);
    printf("당신의 이름은 %s입니다.\n", name);

    return 0;
}
```

위 코드에서 `getchar` 함수는 사용자로부터 나이를 입력받고, 그 값을 변수 `age`에 저장합니다. 그리고 `printf` 함수를 사용하여 이 값을 출력합니다.

**실무 활용: putchar**

`putchar`함수를 실무에서 어떻게 사용할 수 있을까요? 예를 들어, 프로그램을 개발할 때 사용자에게 메시지를 출력하고 싶은 경우에 `putchar` 함수를 사용할 수 있습니다. 

```c
#include <stdio.h>

int main() {
    printf("Hello, world!\n");
    putchar('\n');
    return 0;
}
```

위 코드에서 `putchar` 함수는 단순하게 `\n` 문자를 표준 출력로 출력하는 함수입니다.

**🚨 실무주의보: 주의사항**

`getchar`과 `putchar`함수는 자바스크립트의 `prompt`함수처럼 사용할 수 없지만, 그래도 그만큼의 강력한 기능을 가지고 있습니다. 하지만 이 두 함수를 과다하게 사용하면 프로그램이 느려질 수 있으므로 주의하도록 합시다.

**💡 초보자 폭풍 질문!**

*   getchar와 putchar는 왜 필요할까요?
*   getchar와 putchar를 언제 사용해야 할까요?

이제까지 배운 내용을 요약하면, `getchar`함수는 표준 입력으로부터 한 문자를 읽어와서 반환하는 함수이며, `putchar`함수는 표준 출력으로 한 문자를 출력하는 함수입니다. 이 두 함수를 실무에서 사용할 때 주의사항에 유의해야 합니다.

**🔥 마무리**

이번 강의에서 배운 내용을 통해 C언어의 입출력 함수인 `getchar`와 `putchar`함수를 이해하셨기를 바랍니다. 다음 강의에서는 다른 표준 입출력 함수에 대해 배웁니다. 감사합니다! 🙏

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
