---
layout: single
title: "C 함수를 Rust에서 사용하기: unsafe 블록과 binding"
date: 2026-07-11 15:30:13
categories: [Rust C]
---

## 🔥 Rust와 C의 설렘 가득한 만남! 10강: C 함수를 Rust에서 사용하기 🚀

**안녕하세요, 개발자 여러분! 👋  저는 당신들의 Rust 여정을 함께 해주고, 이 아름다운 언어의 모든 매력을 듬뿍 선사하는 대한민국 최고의 Rust C 일타 강사입니다! 😎**

오늘은 저희가 오랜 시간 기대해 온 만남이라니, 진짜 설레는 마음으로 10강을 시작하고자 합니다.  맞아요, 바로 **"C 함수를 Rust에서 사용하기: unsafe 블록과 binding"** 에 대해 알아보겠습니다!

 C 언어의 오랜 역사와 풍부한 라이브러리들은 Rust 개발에 큰 도움이 될 수 있습니다. 하지만 Rust는 엄격하고 안전한 메모리 관리를 강조하는 언어죠. 그렇기 때문에 C 함수를 Rust에서 사용할 때, 주의가 필요합니다!

**🤔 이번 강좌에서는 무엇을 배울까요?**

*  Rust와 C 간의 세계인 연결고리: binding
*  `unsafe` 블록과 왜 존재하는지? 그 비밀을 드러냅니다!
*  C 함수를 Rust에서 호출하는 실제 코드 예시 분석! 🤯


---



### **1. Binding: C와 Rust의 세계를 연결하는 마법진**

Rust에서 C 라이브러리를 사용하려면 "binding"이라는 개념을 이해해야 합니다. 바로, 두 언어 사이의 통역관일 수 있습니다.  C 함수들을 Rust가 이해할 수 있게 변환하는 작업이죠! 🪄

두 언어를 연결하기 위한 가장 일반적인 방법은 **`cbindgen`**과 같은 라이브러리를 사용하는 것입니다. 예시로, 다음 C 코드를 생각해보세요.


```c
#include <stdio.h>

void say_hello(const char* name) {
  printf("Hello, %s!\n", name);
}
```

이 C 함수는 이름을 입력받아 "Hello, [name]!" 라고 출력하는 간단한 함수입니다. `cbindgen` 을 사용하면 이 C 함수를 Rust에서 호출할 수 있는 Rust 함수로 변환해 줄 수 있습니다!


```rust
extern "C" {
    fn say_hello(name: *const i8);
}

// ...Rust 코드에서 쓸 때는 다음과 같이 사용합니다...

unsafe {
   say_hello(CString::new("World").unwrap().into_raw()); // CString을 사용하여 Rust 문자열을 C 함수에 전달
}
```



---



### **2. unsafe 블록: 위험하면서도 설레는 낯선 세계**

`unsafe` 블록은 Rust의 가장 특징적인 개념 중 하나입니다! 🤔 이 블록 내에서는 메모리 관리와 같은 안전성 규칙을 따르지 않습니다.  Rust 개발자가 직접 메모리를 다룰 수 있게 해주는, 위험하면서도 흥미로운 영역이죠. 🔥

`unsafe` 블록은 C 함수를 Rust에서 호출할 때 필수적으로 사용됩니다. 왜냐하면 C 언어는 Rust의 안전성 기준을 따르지 않기 때문입니다!  Rust에서 `unsafe` 블록을 사용하는 것은 마치 산악 등반처럼, 위험하지만 아름다운 경관을 감상할 수 있다는 의미가 담겨 있습니다. 🏔️

---



### **💡 초보자 폭풍 질문!**


*   왜 Rust에서는 C 함수를 호출할 때 `unsafe` 블록이 필수적인 걸까요? 🤔
*  `cbindgen` 이란 무엇이고, Rust에서 C 라이브러리를 사용하기 위해 어떻게 도움을 주나요? ❔



### **3. 실제 코드 예시: C 함수를 Rust로 호출하는 방법**

지금까지 이론적인 부분들을 다 써봤는데,  실제로 Rust에서 C 함수를 호출하는 방법을 알아보겠습니다! 💪


```rust
use std::ffi::CString; // CString 라이브러리를 사용해서 문자열 전달 가능하게 만듭니다

// 이부분은 "cbindgen" 을 통해 생성된 코드입니다. 
extern "C" {
    fn add(x: i32, y: i32) -> i32;
}

fn main() {
    let result = unsafe { add(5, 10) }; //  unsafe 블록에서 C 함수를 호출합니다.
    println!("Result: {}", result); // 결과값을 출력합니다.
}
```



**이 코드를 설명해 드릴게요! 😊**


*   `use std::ffi::CString;`: Rust의 `CString` 라이브러리를 사용하여 C 함수에 문자열을 전달할 수 있도록 합니다. 

*   `extern "C" { ... }`: 이 블록은 C 함수를 Rust에서 호출하기 위한 정의입니다!  
*   `fn add(x: i32, y: i32) -> i32;`: `cbindgen`을 사용하여 C의 `add` 함수가 Rust로 변환된 모습이죠. Rust는 범위를 명시하기 때문에 `i32` 형으로 정의됩니다.

*   `unsafe { ... }`: C 함수를 호출할 때 `unsafe` 블록을 사용해야 합니다! Rust은 안전성을 최우선으로 하는 언어라기 때문에, 메모리 관리 등에 대한 주의가 필요합니다. 
*   `add(5, 10)`:  Rust에서 C 함수의 `add`를 호출하고 결과 값을 저장합니다.



**🚨 실무주의보!**


*  C와 Rust 간의 호출은 주의가 필요하며, 메모리 누수나 부동점 오류 등 발생 가능성이 있습니다. 
*   Rust 공식 문서를 참고하여 사용하는 함수에 대한 정보를 항상 확인하고, `unsafe` 블록을 최소한으로 사용해야 합니다!


---

** Rust와 C의 세계는 이제 연결되었습니다! 😎  강력한 C 라이브러리를 사용하며 Rust 개발 능력을 한 단계 업그레이드하세요! 🚀**





<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
