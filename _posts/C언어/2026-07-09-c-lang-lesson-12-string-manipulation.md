---
layout: single
title: "문자열: 문자의 합성과 다루기"
date: 2026-07-09 14:18:28
categories: [C언어]
---

**12강: 문자열 - 문자의 합성과 다루기 🔥**

안녕하세요! 반갑게 여쭤보겠습니다. 초보자 분들께서는 아직도 "문자열은 뭔지?" 라고 생각하시나요? 😅 오늘 강의에서는 가장 중요한 개념인 "문자열"에 대한 모든 것을 알려드리겠습니다.

**1. 문자열이란 무엇인가요?**

문자열은 C언어에서 사용하는 가장 기본적인 자료형 중 하나입니다. 다른 언어에서도 찾아볼 수 있는 자료형입니다. 하지만, 간단한 말로 하면 "한 줄 한 줄의 글자"라고 이해할 수 있습니다.

예를 들어, 이름, 나이, 주소, 전화번호 등은 모두 문자열이라고 할 수 있습니다. 단순히 숫자만 있는 경우도 있지만, 공백이나 특수문자가 섞여있는 것도 가능합니다.

**2. 문자열의 종류**

문자열에는 두 가지 종류가 존재합니다. 첫 번째는 "리터럴"이고, 두 번째는 "변수"입니다.

- **리터럴**: 직접 사용하는 것을 의미합니다. 예를 들어, `"Hello"`는 리터럴이라고 합니다.
- **변수**: 이름이 있는 변수로, 값을 저장하는 공간입니다. 예를 들어, `name`은 변수입니다.

**3. 문자열의 합성**

문자열을 합성할 때에는 여러 가지 방법이 있습니다. 가장 일반적인 방법은 `+` 연산자를 사용하는 것입니다.

예를 들어, `"Hello"`와 `"World"`를 합치면 `"Hello World"`가 됩니다.

```c
#include <stdio.h>

int main() {
    char str1[10] = "Hello";
    char str2[10] = "World";
    
    printf("%s %s\n", str1, str2);
    
    return 0;
}
```

이 코드는 위에서 설명한 대로 `"Hello World"`를 출력합니다.

**4. 문자열의 다루기**

문자열을 다룰 때에는 다양한 함수가 사용됩니다. 가장 일반적인 함수는 `strcpy()`, `strcat()`입니다.

- **strcpy()**: 문자열을 복사하는 함수입니다.
- **strcat()**: 문자열을 합치는 함수입니다.

예를 들어, `"Hello"`와 `"World"`를 합치면 `"Hello World"`가 됩니다.

```c
#include <stdio.h>
#include <string.h>

int main() {
    char str1[10] = "Hello";
    char str2[10] = "World";
    
    printf("%s %s\n", strcpy(str1, str2), str1);
    
    return 0;
}
```

이 코드는 위에서 설명한 대로 `"World Hello"`를 출력합니다.

**5. 문자열의 활용**

문자열은 프로그램을 개발할 때 매우 중요합니다. 다양한 종류의 데이터를 저장하고 다루기 때문에, 기본적인 개념에 대한 이해가 필요합니다.

예를 들어, 이름, 나이, 주소, 전화번호 등은 모두 문자열로 처리됩니다.

```c
#include <stdio.h>
#include <string.h>

int main() {
    char name[10] = "Lee";
    int age = 25;
    char addr[20] = "Seoul";
    char phone[15] = "010-1234-5678";
    
    printf("이름: %s\n", name);
    printf("나이: %d\n", age);
    printf("주소: %s\n", addr);
    printf("전화번호: %s\n", phone);
    
    return 0;
}
```

이 코드는 위에서 설명한 대로 `"이름:", "25", "Seoul", "010-1234-5678"`을 출력합니다.

**🚨 실무주의보**

문자열은 매우 중요하지만, 잘못 사용하면 큰일 나버리게 됩니다. 그래서, 실무에서는 반드시 주의를 기울여야 합니다.

예를 들어, 문자열의 길이를 제대로 확인하지 않고 사용하면 버그가 발생할 수 있습니다.

```c
#include <stdio.h>
#include <string.h>

int main() {
    char str[10] = "HelloWorld";
    
    printf("%s\n", str);
    
    return 0;
}
```

이 코드는 `"HelloWorld"`를 출력합니다. 하지만, 주의할 점은 `"HelloWorld"`가 길이가 넘는지 확인하지 않았을 때입니다.

```c
#include <stdio.h>
#include <string.h>

int main() {
    char str[10] = "Hello";
    
    printf("%s\n", strcat(str, "World"));
    
    return 0;
}
```

이 코드는 `"HelloWorld"`를 출력합니다. 하지만, 주의할 점은 `"Hello"`와 `"World"`가 함께 연결된다는 것입니다.

**💡 초보자 폭풍 질문!**

문자열에 대한 모든 것을 이제는 이해한 것 같은데요. 하지만, 여전히 어려운 부분이 있을 수 있습니다. 그래서, 저에게 질문을 하시면 좋습니다!

질문하고 싶은 부분이 있으시면, 저에게 알려주세요! 💬

**💕 감동의 끝!**

이상으로 12강: 문자열 - 문자의 합성과 다루기 강의가 모두 끝났습니다. 문자열에 대한 모든 것을 이제는 이해한 것 같은데요? 🤔 하지만, 여전히 어려운 부분이 있을 수 있습니다. 그래서, 저에게 질문을 하시면 좋습니다! 💬

감사합니다! 👏

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
