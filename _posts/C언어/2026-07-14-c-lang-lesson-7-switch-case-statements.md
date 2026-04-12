---
layout: single
title: "switch-case 문: 다양한 선택-case"
date: 2026-07-14 14:17:34
categories: [C언어]
---

**7강: switch-case 문 - 다양한 선택, case**

안녕하세요! 여러분, 오늘은 C언어의 switch-case 문을 배워볼 시간입니다. 🎉 이 문법은 우리가 흔히 사용하는 if-else 문과 달리, 여러 경우를 한 번에 처리할 수 있는 유용한 기능입니다.

** 왜 switch-case 문이 필요했는가?**

당신은 이미 C언어의 기본 문법을 잘 알고 계시죠? 😊 그럼, 여러분은 이전 강의에서 배우었던 if-else 문을 어떻게 사용하셨나요? 바로 그 문제점을 해결하기 위해 switch-case 문이 등장했습니다.

이전 강의에서 배우았던 if-else 문은 여러 경우를 처리할 때 매우 많은 코드가 필요합니다. 예를 들어, 다음과 같은 시나리오가 있습니다:

```c
int x = 5;
if (x == 1) {
    printf("x는 1입니다.\n");
} else if (x == 2) {
    printf("x는 2입니다.\n");
} else if (x == 3) {
    printf("x는 3입니다.\n");
} else if (x == 4) {
    printf("x는 4입니다.\n");
} else if (x == 5) {
    printf("x는 5입니다.\n");
}
```

이 코드는 매우 길고 번잡합니다. switch-case 문은 이러한 문제를 해결해 주는 기능으로, 여러 경우를 한 번에 처리할 수 있습니다.

**switch-case 문 구조**

switch-case 문의 기본 구조는 다음과 같습니다:

```c
switch (조건) {
    case 값1:
        // 코드를 실행합니다.
        break;
    case 값2:
        // 코드를 실행합니다.
        break;
    ...
}
```

* `조건` : switch 문의 조건입니다. 반드시 정수형 변수여야 합니다.
* `case 값1`, `case 값2` ... : 여러 경우를 처리할 수 있습니다. 각 경우는 `break;` 키워드를 사용하여 구분합니다.

**실무 활용**

이제, switch-case 문을 실무에서 어떻게 활용할 수 있는지 한번 살펴보겠습니다. 예를 들어, 다음과 같은 시나리오가 있습니다:

```c
int day = 3;
switch (day) {
    case 1:
        printf("월요일입니다.\n");
        break;
    case 2:
        printf("화요일입니다.\n");
        break;
    case 3:
        printf("수요일입니다.\n");
        break;
    case 4:
        printf("목요일입니다.\n");
        break;
    case 5:
        printf("금요일입니다.\n");
        break;
    default:
        printf("기타 요일입니다.\n");
}
```

이 코드는 매우 깔끔하고 직관적입니다. switch-case 문을 사용하면, 여러 경우를 한 번에 처리할 수 있습니다.

**중요한 점**

* `break;` 키워드는 반드시 필요합니다. 없으면, 다음 case 문의 코드가 실행됩니다.
* `default` keyword는 optional입니다. 그만큼의 코드블록이 생길 것입니다.

**Q&A 시간**

💡 초보자 폭풍 질문!

1. switch-case 문은 언제 사용해야 하나요? 🤔
2. default 키워드는 꼭 필요한가요? ❓

🚨 실무주의보! 🚨

switch-case 문을 사용할 때, 주의하실 점이 있습니다.

* 조건은 반드시 정수형 변수여야 합니다.
* 여러 case 문의 코드를 중복되지 않게 작성해야 합니다.

**정리**

오늘은 switch-case 문을 배웠습니다. 다양한 경우를 한 번에 처리하는 유용한 기능입니다. 이제, switch-case 문을 실무에서 어떻게 활용할 수 있는지 조금 더 공부해 보겠습니다. 👍

**도전 과제**

* 다음 코드를 작성하십시오.

```c
int month = 5;
switch (month) {
    case 1:
        printf("일월입니다.\n");
        break;
    case 2:
        printf("이월입니다.\n");
        break;
    case 3:
        printf("삼월입니다.\n");
        break;
    default:
        printf("기타 월입니다.\n");
}
```

답은 다음에요!

```c
int month = 5;
switch (month) {
    case 1:
        printf("일월입니다.\n");
        break;
    case 2:
        printf("이월입니다.\n");
        break;
    case 3:
        printf("삼월입니다.\n");
        break;
    default:
        printf("기타 월입니다.\n");
}
```

만약, 문제가 이해가 안 가요? 😅

이 글을 다시 한번 읽어보세요. 또는, 질문을 하시면 좋겠죠? 🤔

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
