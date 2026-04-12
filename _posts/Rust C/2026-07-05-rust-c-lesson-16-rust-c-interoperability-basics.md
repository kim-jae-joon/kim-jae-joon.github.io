---
layout: single
title: "Rust과 C 상호 운용성 기초"
date: 2026-07-05 18:32:17
categories: [Rust C]
---

## 16강: Rust과 C, 🧑‍💻👨‍💻 서로 손 잡고 코딩 왕국 정복하기!

안녕하세요, 코딩 초보 왕들이여! 오늘은 💥 **Rust과 C의 마법 같은 협업**💥에 대해 탐험해볼 거예요. 이건 마치 고대 로마 시대에 두 강력한 제국이 동맹을 맺어 더 큰 영토를 확장하는 것과 같죠! C는 오래된 전설 속 영웅이고, Rust는 그 위에 빛나는 강인한 방패를 더해주는 현대의 전사라고 생각하면 됩니다. 🤘

### 🚨 실무주의보: 왜 이 조합이 중요할까요?

**"Rust은 C 코드와 완벽하게 호환되니까, 기존 프로젝트를 업그레이드하거나 새로운 기능을 쉽게 추가할 수 있어요!"** 💯 이렇게 생각하면 됩니다. 기존에 C로 만든 멋진 코드베이스를 버리지 않고, Rust의 안전성과 성능을 활용할 수 있다니? 이건 마치 낡은 전차에 최첨단 무기를 장착하는 것과 같죠! 🌟

### 🤔 초보자 폭풍 질문!

**Q: Rust 코드를 어떻게 C 코드와 함께 실행시킬 수 있나요?**
**A:** 간단해요! **FFI (Foreign Function Interface)** 를 사용하면 됩니다. 마치 다른 언어로 만들어진 문을 통과하는 문지기처럼, Rust 코드에서 C 함수를 호출하고 반대로 C 코드에서 Rust 함수를 호출할 수 있어요.

### 🔑 핵심 개념: FFI를 활용한 상호 운용성

#### 1. **함수 포인터 사용하기**

C에서 함수 포인터를 사용하는 방법을 먼저 알아볼게요. C에서는 함수를 직접 호출하는 것처럼 Rust 함수를 호출할 수 있어요.

```c
// C 코드 예시
#include <stdio.h>

// Rust 함수를 호출할 C 함수 선언
void greetFromC(const char* name);

int main() {
    // Rust 함수 포인터 선언
    void (*greetFunc)(const char*) = greetFromC; // 함수 포인터에 Rust 함수 주소 할당

    // 함수 호출
    greetFunc("Rust 친구!"); // 출력: Rust 친구!
    printf("✨ 잘 작동하죠?\n");
    return 0;
}
```

**코드 설명:**
- **`void (*greetFunc)(const char*) = greetFromC;`**: 이 줄에서 `greetFunc`이라는 함수 포인터에 `greetFromC` 함수의 주소를 할당합니다. 이렇게 하면 C에서 Rust 함수를 간접적으로 호출할 수 있어요.
- **`greetFunc("Rust 친구!");`**: 함수 포인터를 통해 Rust 함수를 호출합니다.

#### 2. **Rust에서 C 함수 호출하기**

반대로 Rust에서 C 함수를 호출하는 방법도 살펴볼게요. 이는 `#[no_mangle]` 속성을 사용해 함수를 외부에서 접근 가능하게 만드는 것이 핵심입니다.

```rust
// Rust 코드 예시
#[no_mangle] // 외부에서 호출 가능하도록 설정
pub extern "C" fn greetFromRust(name: *const libc::c_char) {
    unsafe {
        // C 문자열을 Rust 문자열로 변환
        let rust_str = std::ffi::CStr::from_ptr(name).to_str().unwrap();
        println!("👋 {}!", rust_str); // 출력: 👋 Rust 친구!
    }
}

fn main() {
    // C 코드에서 사용할 Rust 함수 호출 예시 (실제로는 C 코드에서 호출됩니다)
    // extern { fn greetFromRust(name: *const libc::c_char); } // C 코드에서 선언
    // greetFromRust(b"Rust 친구!\0".as_ptr() as *const libc::c_char);
}
```

**코드 설명:**
- **`#[no_mangle]`**: Rust 함수가 외부에서 호출될 수 있도록 이름을 변경하지 않게 합니다.
- **`extern "C"`**: C 호환성을 위해 ABI를 명시합니다.
- **`unsafe { ... }`**: C 문자열을 안전하게 다루기 위해 `unsafe` 블록을 사용합니다.
- **`std::ffi::CStr::from_ptr(name).to_str().unwrap();`**: C 문자열을 Rust 문자열로 변환합니다.

#### 3. **다양한 호출 방식: 반복 예시**

다양한 상황에서 함수 호출을 어떻게 적용할 수 있는지 몇 가지 예를 더 들어볼게요.

**반복문 활용 예시:**

**C 코드:**
```c
#include <stdio.h>

void sayHelloNTimes(int n, void (*sayHello)(void)) {
    for (int i = 0; i < n; i++) {
        sayHello(); // Rust 함수 호출
    }
}

void sayHello() {
    printf("Hello, Rust!\n");
}

int main() {
    sayHelloNTimes(5, sayHello); // 출력: Hello, Rust! (5번 반복)
    return 0;
}
```

**Rust 코드:**
```rust
// Rust 함수 정의
#[no_mangle]
pub extern "C" fn sayHello() {
    println!("👋 Rust와 C가 협업 중!");
}

fn main() {
    // C 코드에서 호출하는 예시 (실제 호출은 C 측에서 이루어집니다)
    // extern { fn sayHello(); } // C 코드에서 선언
    // unsafe { std::sys::Sys::call_msvcrt(std::ffi::c_void_ptr::from_raw_ptr(sayHello as *const libc::c_void)); } // 호환성 처리
}
```

**조건문 활용 예시:**

**C 코드:**
```c
#include <stdio.h>

void greetDependingOnChoice(int choice, void (*greetFunc)(void)) {
    if (choice == 1) {
        greetFunc = sayHello; // 함수 포인터 변경
    } else {
        greetFunc = sayGoodbye; // 다른 함수로 변경
    }
    greetFunc(); // 선택된 함수 호출
}

void sayHello() {
    printf("Hello there!\n");
}

void sayGoodbye() {
    printf("Goodbye!\n");
}

int main() {
    greetDependingOnChoice(1, NULL); // 출력: Hello there!
    return 0;
}
```

**Rust 코드:**
```rust
// Rust 함수 정의
#[no_mangle]
pub extern "C" fn sayHello() {
    println!("👋 안녕하세요!");
}

#[no_mangle]
pub extern "C" fn sayGoodbye() {
    println!("👋 안녕히 계세요!");
}

fn main() {
    // C 코드에서 호출하는 예시 (실제 호출은 C 측에서 이루어집니다)
    // extern { fn sayHello(); fn sayGoodbye(); } // C 측에서 함수 선언
    // unsafe { std::sys::Sys::call_msvcrt(std::ffi::c_void_ptr::from_raw_ptr(sayHello as *const libc::c_void)); } // 호환성 처리
}
```

### 💡 초보자 폭풍 질문!

**Q: `#[no_mangle]` 이란 뭔가요? 왜 필요한 건가요?**
**A:** `#[no_mangle]` 은 Rust 컴파일러에게 특정 함수 이름을 변경하지 말라고 지시하는 속성입니다. C 코드에서 직접 함수를 호출할 때, Rust 컴파일러가 함수 이름을 바꿔버리면 문제가 생기거든요. 그래서 `#[no_mangle]` 을 사용하여 함수 이름을 그대로 유지시켜 외부 호출이 가능하게 만듭니다. 마치 마법의 주문 같죠? 🧙‍♂️✨

### 🏆 마무리: 협력의 힘으로 코딩 왕국 확장하기

Rust과 C의 협업은 마치 고대 영웅들이 힘을 합쳐 새로운 지평을 개척하는 것과 같습니다. 기존의 안정성과 새로운 안전성을 결합하면, 여러분의 프로젝트는 더욱 강력하고 효율적이게 변할 거예요. 이제 여러분도 이 강력한 듀오를 활용해 더 큰 코딩 왕국을 건설해보세요!

👨‍💻👩‍💻 함께 성장하고, 서로 배우며, 코딩의 신비를 탐구해 나가요! 🚀

---

이제 여러분의 질문이나 추가적인 예제 요청이 있으면 언제든지 알려주세요! 함께 성장하는 여정, 즐겁게 이어가요! 🎉

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
