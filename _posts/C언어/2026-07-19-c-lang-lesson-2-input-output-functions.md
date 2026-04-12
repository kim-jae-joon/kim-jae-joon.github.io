---
layout: single
title: "C언어 입출력 함수: scanf, printf"
date: 2026-07-19 14:16:46
categories: [C언어]
---

**2강: C언어 입출력 함수 - scanf, printf 💡**

안녕하세요, 여러분! 오늘은 C언어의 입출력 함수, scanf와 printf에 대해 공부할 날입니다! 😎

**scanf: 입출력 함수 중 가장 중요한것! 🔥**

scanf는 C언어에서 사용하는 input/output 함수 중 하나로, 변수에 사용자가 입력한 값을 저장하는 함수입니다. 이 함수를 잘못사용하면 프로그램이 무조건 먹통이 된다고 할 수 있습니다! 😨

**왜 scanf가 이렇게 위험할까? 🤔**

scanf는 사용자가 입력한 값을 바로 변수에 대입해 주기 때문에, 사용자의 입력 형식과 변수의 자료형을 잘못-match하면 프로그램이 오류를 발생합니다. 예를 들어, int형 변수에 string을 입력하려고 하면 오류가 발생하게 됩니다!

```c
#include <stdio.h>

int main() {
    int a;
    scanf("%s", &a); // 에러 발생! 😨
    return 0;
}
```

**printf: 입출력 함수 중 가장 편리한것! 🚀**

printf는 C언어에서 사용하는 output 함수로, 변수의 값을 출력하는 함수입니다. 이 함수를 잘못사용하면 프로그램이 무조건 먹통이 된다고 할 수 있습니다!

```c
#include <stdio.h>

int main() {
    int a = 10;
    char b[] = "hello";
    printf("%d %s", a, b); // 정상 출력!
    return 0;
}
```

**printf 포맷 문자열 🔍**

printf의 가장 강력한 기능 중 하나는 포맷 문자열입니다. 이 포맷 문자열을 통해 우리는 변수의 값을 다양한 형식으로 출력할 수 있습니다!

```c
#include <stdio.h>

int main() {
    int a = 10;
    double b = 3.14;
    printf("%d %f", a, b); // 정상 출력!
    return 0;
}
```

**포맷 문자열의 예시 🎉**

| 포맷 문자열 | 설명 |
| --- | --- |
| `%c` | 문자 |
| `%s` | 문자열 |
| `%d` | 정수 |
| `%f` | 실수 |
| `%x` | 16진수 |

**실무 활용 💻**

scanf와 printf를 잘 사용하면 프로그램의 개발이 매우 편리하게 됩니다! 이 함수들은 실제 프로젝트에서 가장 많이 사용되는 함수 중 하나입니다!

```c
#include <stdio.h>

int main() {
    int num;
    scanf("%d", &num);
    if (num > 10) {
        printf("larger than 10\n");
    } else {
        printf("not larger than 10\n");
    }
    return 0;
}
```

**🚨 실무주의보!**

scanf와 printf를 사용할 때, 포맷 문자열과 변수의 자료형을 항상 일치시켜 주세요!

```c
#include <stdio.h>

int main() {
    char name[10];
    scanf("%s", name); // 에러 발생! 😨
    return 0;
}
```

**💡 초보자 폭풍 질문!**

Q: 왜 scanf와 printf를 항상 함께 사용해야 하나요? 🤔

A: scanf는 입력한 값을 저장하고, printf는 출력할 때 포맷 문자열을 사용하므로 함께 사용하면 프로그램의 개발이 매우 편리하게 됩니다!

Q: 왜 포맷 문자열을 항상 일치시켜 주어야 하나요? 🤯

A: 포맷 문자열과 변수의 자료형을 맞지 않으면 오류가 발생하거나 프로그램이 먹통이 될 수 있습니다! 따라서 항상 일치시키세요!

**🚀 결론**

scanf와 printf는 C언어에서 사용하는 입출력 함수 중 가장 중요한것입니다! 이 함수들을 잘못사용하면 프로그램이 무조건 먹통이 된다고 할 수 있습니다! 따라서 포맷 문자열과 변수의 자료형을 항상 일치시켜 주세요! 💪

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
