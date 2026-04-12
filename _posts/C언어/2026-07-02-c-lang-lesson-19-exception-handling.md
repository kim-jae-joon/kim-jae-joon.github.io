---
layout: single
title: "비정상 종료 처리: 예외 처리 기법"
date: 2026-07-02 15:56:35
categories: [C언어]
---

##  🔥 19강: 비정상 종료 처리: 예외 처리 기법 - C언어 일타 강좌 🔥

안녕하세요, 개발자 시니어이고 대한민국 최고의 C언어 일터 강사(自封)인 저입니다! 🚀 오늘은 **비정상 종료 처리** 와 **예외 처리 기법**에 대해 깊이 있게 알아보겠습니다. 이 부분은 C언어 개발자라면 필수로 알아야 하는 중요한 개념들이니, 주의 깊게 따라오세요! 😎

###  ❓ 문제점: 예상치 못한 오류와 프로그램 붕괴 😰


C언어는 강력하고 풍부한 기능을 제공하지만, 동시에 비정상 종료 처리에 대한 직접적인 지원이 부족합니다. 예를 들어, 파일을 열려고 하지만 해당 파일이 존재하지 않으면 프로그램이 중단되거나, 숫자 연산 시 나눗셈으로 0으로 나누는 오류가 발생하면 프로그램이 갑자기 종료되는 경우가 있습니다. 이런 상황은 개발자가 원치 않는 결과를 초래하며 **프로그램의 안정성을 저하시키고 사용자 경험을 악화**하게 합니다! 😩

###  💡 해결책: 예외 처리 기법 💪


예외 처리 기법은 프로그램 실행 중 발생하는 예상치 못한 오류나 비정상적인 상황에 대해 **체계적으로 대처하는 방법**입니다. 이를 통해 프로그램이 에러로 인해 갑자기 종료되는 것을 방지하고, 오류 메시지를 출력하여 사용자에게 문제 상황을 알리고, 필요하다면 프로그램 실행을 다시 시도하거나 다른 작업으로 전환할 수 있습니다! 🙌

###  📚 C언어에서 예외 처리 기법: `setjmp`와 `longjmp` 함수 🔎


C언어에서는 **`setjmp`** 와 **`longjmp`** 함수를 사용하여 간단한 형태의 예외 처리를 구현할 수 있습니다. 

*  **`setjmp`**: 특정 코드 블록(jump point)을 설정합니다. 이후 `longjmp` 함수가 실행되면 해당 jump point로 프로그램 실행이 재개됩니다.
    
* **`longjmp`**: 기존에 `setjmp` 함수를 통해 설정된 jump point로 프로그램 실행을 즉시 복귀시킵니다.

###  💻 실습: 예외 처리 기법 적용하기 🚀


```c
#include <stdio.h>
#include <setjmp.h>

jmp_buf env;

void error_handler(const char *message) {
    fprintf(stderr, "오류 발생! %s\n", message);
    longjmp(env, 1); // 예외 처리로 인해 setjmp 블록 복귀 
}

int main() {
    if (setjmp(env)) { // setjmp를 통해 프로그램 상태 저장
        printf("예외 처리 완료!\n");
        return 0; 
    }

    // 코드 실행 부분입니다. 예상치 못한 오류 발생 시 error_handler 호출
    int result = 10 / 0;  
    printf("%d\n", result); // 이 줄은 실행되지 않습니다.
    return 0; 
}
```

**코드 설명:**


1. `#include <setjmp.h>`: `setjmp` 와 `longjmp` 함수를 사용하기 위해 필요한 헤더 파일을 포함합니다.
2. `jmp_buf env`: 프로그램 상태를 저장할 `jmp_buf` 변수를 선언합니다.
3. `error_handler(const char *message)`: 예외 발생 시 오류 메시지를 출력하고 `longjmp` 함수를 사용하여 프로그램 실행을 재개하는 함수입니다.
4. `main()` 함수:
    *  `if (setjmp(env))`: `setjmp` 함수를 호출하여 현재 프로그램 상태를 저장하고, `longjmp`로 복귀했는지 확인합니다. 만약 1이 반환되면 이전에 `longjmp`가 호출되었음을 의미합니다.
    *  `int result = 10 / 0;`: 예외 발생 상황을 시뮬레이션하는 코드입니다. 
    *  위 코드를 실행하면 프로그램 상태 저장 후 `error_handler` 함수로 이동하여 오류 메시지를 출력하고 실행이 종료됩니다.


### 🎉 이제 C언어 개발자로서 비정상 종료 처리에 대한 신뢰도가 높아졌죠! 🎊

이번 강의를 통해 예외 처리 기법의 개념과 `setjmp` 와 `longjmp` 함수를 이해하셨기를 바랍니다. 다음 시간에는 더욱 흥미로운 C언어 주제로 만나요! 🔥




<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
