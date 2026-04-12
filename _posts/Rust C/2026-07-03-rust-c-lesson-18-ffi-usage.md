---
layout: single
title: "FFI(Foreign Function Interface) 사용법"
date: 2026-07-03 18:32:47
categories: [Rust C]
---

# 18강: FFI (Foreign Function Interface) 사용법 - 외부 세계와 소통하는 마법의 길

안녕하세요, 초보자 여러분! 🚀 오늘은 우리가 코드 속에서 숨겨진 보물을 찾는 듯한 경험을 하게 될 거예요. 바로 **FFI (Foreign Function Interface)** 사용법입니다. 혹시 "이게 뭐야?" 하고 의문을 품고 계신가요? 걱정 마세요! 이 강의를 마치고 나면 외부 라이브러리와 원활하게 소통하는 마스터가 될 거예요. 그럼, 시작해볼까요?

## 왜 FFI가 필요한 걸까요?

### **외부 세계와 소통하기**

우리가 코딩을 하면서 때로는 Rust의 힘만으로 모든 것을 해결하기 어려울 때가 있죠. 특히, 이미 잘 정제된 외부 라이브러리들이 있는 상황에서는 더욱 그렇습니다. 예를 들어, 고성능 계산이 필요할 때 C의 **OpenCV**나 **OpenSSL** 같은 라이브러리를 활용하면 훨씬 빠르고 효율적으로 작업할 수 있습니다. 이걸 바로 **FFI**를 통해 연결하는 거죠!

**진짜 신기하죠?** 마치 마법사가 마법의 힘을 다른 세계와 연결하는 것 같지 않나요? 🧙‍♂️

## FFI 기본 개념 이해하기

### **기본 용어 정리**

- **Foreign Function Interface (FFI)**: 다른 언어로 작성된 함수를 현재 언어에서 호출할 수 있게 해주는 인터페이스입니다. Rust에서는 `extern "C"` 키워드를 사용해 C 함수를 호출할 수 있어요.
- **C 호환성**: Rust에서 `extern "C"`를 사용하면 C 언어와의 호환성을 유지할 수 있어요. 이렇게 하면 C 코드와 Rust 코드가 서로 잘 소통할 수 있답니다.

### **간단한 예제로 시작해보기**

#### **예제 1: 간단한 C 함수 호출**

```rust
// C 코드 (예시로 간단히 작성해봄)
// libexample.c
#include <stdio.h>

void greet() {
    printf("안녕하세요, Rust 세계에서 온 친구들아!\n");
}

// Rust에서 이 C 코드를 사용하기 위해 빌드
// 터미널에서 다음 명령어로 라이브러리 생성
// gcc -c -o libexample.o libexample.c
// gcc -shared -o libexample.so libexample.o

// Rust 코드
extern crate libc; // libc crate를 사용해 C 타입을 가져옴
extern "C" {
    fn greet(); // C 함수 선언
}

fn main() {
    greet(); // C 함수 호출
}
```

**해설:**
- `extern crate libc;`: C 타입을 사용하기 위해 `libc` crate를 가져옵니다.
- `extern "C" { fn greet(); }`: `greet` 함수를 외부에서 가져온다고 선언합니다.
- `main` 함수에서 `greet()`를 호출하면 됩니다.

**왜 이렇게 했나요?**
- `extern "C"`는 Rust가 C 함수의 서명을 정확히 이해하고 호출할 수 있게 해줍니다. 마치 통역관 같은 역할을 하는 거죠!

### **다양한 호출 방식: 반복해보기**

#### **예제 2: 반복문을 이용한 함수 호출**

```rust
extern "C" {
    fn add(a: i32, b: i32) -> i32; // 두 정수를 더하는 C 함수
}

fn main() {
    let mut num_calls = 0;
    for _ in 0..5 { // 5번 호출
        num_calls += add(3, 4); // C 함수 호출
        println!("덧셈 결과: {}", num_calls);
    }
}
```

**해설:**
- `for` 루프를 사용해 `add` 함수를 5번 호출하고 결과를 출력합니다.
- 각 호출마다 결과를 누적하여 보여줍니다.

#### **예제 3: 조건문과 함께 사용하기**

```rust
extern "C" {
    fn multiply(a: i32, b: i32) -> i32; // 곱셈 함수
}

fn main() {
    let num = 5;
    if num > 3 {
        let result = multiply(num, 2); // 조건 만족 시 호출
        println!("곱셈 결과: {}", result);
    } else {
        println!("조건 불만족");
    }
}
```

**해설:**
- `if` 문을 사용해 특정 조건을 만족할 때만 `multiply` 함수를 호출합니다.
- 이렇게 하면 함수 호출을 더 세밀하게 제어할 수 있어요.

#### **예제 4: 다형적 호출: `while` 루프 활용**

```rust
extern "C" {
    fn subtract(a: i32, b: i32) -> i32; // 뺄셈 함수
}

fn main() {
    let mut count = 0;
    while count < 3 { // 3번까지 반복
        let result = subtract(10, count);
        println!("뺄셈 결과: {}", result);
        count += 1;
    }
}
```

**해설:**
- `while` 루프를 사용해 `subtract` 함수를 조건에 따라 반복 호출합니다.
- 이 방법은 반복적인 작업에서 유용해요.

## 💡 초보자 폭풍 질문! 💡

**질문 1:** `extern "C"` 외에 다른 옵션은 없나요?

**답변:** 네, 있습니다! `extern "System"`이나 `extern "D"` 등도 있지만, 주로 C 호환성을 위해 `extern "C"`를 사용합니다. 다른 옵션은 특정 시스템이나 언어 특성에 따라 사용될 수 있어요.

**질문 2:** C 라이브러리를 Rust에서 호출할 때 주의해야 할 점은 무엇인가요?

**답변:** 메모리 관리와 타입 안전성에 주의해야 합니다. 특히, C 함수가 포인터를 사용할 때 Rust의 소유권 규칙과 충돌하지 않도록 주의해야 해요. 스마트 포인터나 `unsafe` 블록을 적절히 활용하는 것이 중요합니다.

## 🚨 실무주의보 🚨

FFI를 사용할 때는 **타입 안전성**과 **메모리 관리**에 특히 신경 써야 합니다. 잘못된 사용은 런타임 오류나 메모리 누수를 초래할 수 있어요. 테스트를 충분히 거치고, 필요한 경우 `unsafe` 블록을 적절히 활용하는 습관을 들이세요!

## 마무리

오늘 배운 FFI를 통해 외부 라이브러리와의 원활한 소통이 가능해졌어요. 이제 여러분은 마치 마법사이자 뛰어난 협업자가 된 거죠! 계속 연습하고, 다양한 라이브러리를 탐색해보세요. 더 많은 것을 배우고, 더 멋진 프로그램을 만들 수 있을 거예요.

다음 강의에서도 함께 성장해나가요! 👋💪

---

이 강의가 여러분의 개발 여정에 큰 도움이 되길 바라며, 궁금한 점이 있으면 언제든지 물어봐 주세요! 🚀💪

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
