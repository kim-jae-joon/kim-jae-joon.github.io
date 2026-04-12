---
layout: single
title: "C와 비교한 Rust 기본 문법: 'println!' 함수 사용하기"
date: 2026-07-18 15:28:35
categories: [Rust C]
---

## 3강: C와 비교한 Rust 기본 문법: `println!` 함수 사용하기 🚀

안녕하세요, 프로그래밍 천재님들! 👋  저는 대한민국 최고의 Rust 강사이자 15년 차 시니어 개발자인 **Rusty**입니다. 오늘은 C 언어와 비교하여 Rust의 기본 문법을 알아보고, 그 중에서도 가장 유용한 친구, `println!` 함수를 집중적으로 분석해 볼 거예요🔥

C언어는 꽤나 강력하고 역사가 오래된 언어죠. 하지만 때로는 코드가 복잡하게 생겨서 머리가 아프게 만드는 경우도 있어요 😅 Rust는 이러한 C의 단점을 보완하며 더욱 안전하고 직관적인 코딩 경험을 제공해줍니다!

### 💡 C 언어와 Rust: 문법의 차이 🧐

C언어에서 `printf` 함수를 사용해서 출력하는 방식과 Rust의 `println!` 함수는 약간 다르게 작동합니다.

**C:**
```c
#include <stdio.h>

int main() {
  printf("Hello, World!\n"); 
  return 0;
}
```

*  `printf` 함수는 포맷 문자열과 변수들을 함께 전달받아 화면에 출력하는 역할을 합니다.

**Rust:**
```rust
fn main() {
    println!("Hello, World!");
}
```

* `println!` 함수는 Rust의 특징인 "macro"라는 기능을 사용하여 코드를 간결하게 만들 수 있습니다. 


###  🚨 실무주의보:  'println!'은 강력한 친구지만 주의할 점도 있어요 😎

`println!` 함수는 매우 편리하지만, C와 비교했을 때 **더 많은 정보를 자동으로 처리**하기 때문에 코드 길이가 조금 더 길어질 수 있습니다. 하지만 Rust의 안정성과 강력한 타입 시스템 덕분에 이러한 추가적인 코드 부담은 작고 고급스러운 프로그래밍 경험을 제공하는 데 큰 도움이 된다는 점을 기억하세요!

###  `println!` 함수 사용하기: 실제 예시로 이해하기 🔥


**1. 단순한 문자열 출력:**
```rust
fn main() {
    println!("Rust is amazing!"); 
}
```

* `println!` 함수 안에 "Rust is amazing!"라는 문자열을 입력하면, 이 문자열이 화면에 출력됩니다.

**2. 변수를 포함한 출력:**
```rust
let name = "Rusty";  // 이름 변수 선언
fn main() {
    println!("Hello, {}!", name); // "{ }" 안에 변수 값 넣기!
}
```

* `name`라는 변수에 "Rusty"를 저장하고, `println!` 함수에서 이 변수를 출력하여 "Hello, Rusty!"라고 화면에 표시합니다.


**3. 다양한 타입을 출력:**

```rust
fn main() {
    let number = 123;  // 정수형 변수 선언
    let decimal = 3.14; // 부동 소수점 변수 선언
    println!("Number: {}, Decimal: {}", number, decimal);
}
```

* `number`와 `decimal` 변수에 각각 정수와 부동 소수점 값을 저장하고, `println!` 함수를 통해 두 값 모두 출력합니다.


### 💡 초보자 폭풍 질문! 🔥

- 'println!' 함수 안에서 문장의 끝부분에 ! 기호를 사용하는 이유가 무엇일까요?
- Rust에서 다른 변수 타입을 출력할 때 어떻게 해야 할까요? 예시 코드를 알려주세요!


**rusty**는 여러분이 프로그래밍 실력을 향상시키고 Rust의 매력에 빠지도록 돕기 위해 최선을 다하고 있습니다! 다음 강좌에서는 Rust에서 변수 선언과 자료형에 대해 자세히 살펴보겠습니다. 




<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
