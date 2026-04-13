---
layout: single
title: "Rust 기초: 스마트 포인터: Box, Rc, Arc"
date: 2026-07-12 02:04:08
categories: [Rust]
---

# 11강: Rust 기초 마스터하기 – 스마트 포인터: `Box`, `Rc`, `Arc`

안녕하세요, 여러분의 친근한 주니어 개발자 파트너, 5년 차 러스트쟁이입니다! 오늘은 러스트 프로그래밍에서 꼭 알아야 하는 **스마트 포인터**에 대해 이야기해볼게요. 특히 `Box`, `Rc`, `Arc`에 대해 깊이 파고들어볼 거예요. 처음 듣는다면 좀 어려워 보일 수 있지만, 걱정 마세요! 함께라면 누구나 이해할 수 있어요.

## 스마트 포인터란 무엇인가요?

스마트 포인터는 메모리 관리를 자동화해주는 러스트의 마법 같은 도구예요. 일반 포인터와 달리, 메모리 안전성을 보장하면서 데이터를 참조하거나 소유하는 방식을 지능적으로 처리해줘요. 이제 본격적으로 들어가볼까요?

### 1. `Box<T>`: 메모리 힙에 데이터를 저장하는 마법사

`Box<T>`는 데이터를 힙 메모리에 할당해주는 역할을 해요. 스택에서 벗어나 힙에 데이터를 저장하면, 메모리 관리가 좀 더 유연해지죠.

#### 예제 코드 1: `Box<T>` 사용하기

```rust
fn main() {
    // 박스를 사용해 힙에 정수를 할당
    let b: Box<i32> = Box::new(42);
    
    // 참조 값 출력
    println!("Box에 담긴 값: {}", b);
    
    // 박스를 다른 변수로 이동
    let another_b = b;
    
    // 원래 변수는 이제 사용 불가능 (move semantics)
    // println!("b의 값: {}", b); // 이 줄은 컴파일 에러 발생
    println!("another_b의 값: {}", another_b);
}
```

**코드 설명:**
- `Box::new(42)`는 정수 `42`를 힙 메모리에 할당해요.
- `let another_b = b;`로 값을 이동할 때, `b`는 더 이상 유효하지 않게 되는 `move` 동작이 발생해요. 이는 메모리 안전성을 보장하는 핵심 기능 중 하나예요.

**💡 초보자 폭풍 질문!**
- **Q: `Box`를 사용하면 어떤 상황이 좋을까요?**
  - **A:** 큰 데이터 구조나 동적으로 크기를 결정해야 하는 경우에 특히 유용해요. 스택 오버플로우를 방지하는 데도 도움이 되죠!

### 2. `Rc<T>`: 참조 카운트를 활용한 공유 소유권

`Rc<T>`는 여러 곳에서 데이터를 공유할 수 있게 해주는 스마트 포인터예요. 참조 카운트를 통해 메모리를 자동으로 해제해요.

#### 예제 코드 2: `Rc<T>`로 공유 소유권 구현

```rust
use std::rc::Rc;

fn main() {
    // Rc를 사용해 공유 가능한 문자열 생성
    let shared_str = Rc::new("Hello, Rust!");
    
    // 여러 변수가 공유
    let ref1 = shared_str.clone();  // clone으로 참조 카운트 증가
    let ref2 = shared_str.clone();
    
    println!("ref1: {}", ref1);
    println!("ref2: {}", ref2);
    
    // 더 이상 참조하지 않을 때, 자동으로 메모리 해제되지만 명시적으로 확인
    std::mem::drop(ref1);
    std::mem::drop(ref2);
    
    // 여기서 Rc가 가리키는 메모리는 더 이상 참조되지 않으므로 해제됨
}
```

**코드 설명:**
- `Rc::new("Hello, Rust!")`로 문자열을 생성하고, `clone`을 통해 참조 카운트를 증가시켜 여러 변수에서 공유할 수 있어요.
- `drop`을 통해 더 이상 참조되지 않는 변수를 제거하면, 참조 카운트가 0이 되어 메모리가 해제됩니다.

**🚨 실무주의보**
- `Rc`는 멀티스레딩 환경에서는 안전하지 않아요. 멀티스레드 환경에서는 `Arc`를 사용해야 합니다.

### 3. `Arc<T>`: 멀티스레드 환경을 위한 공유 소유권

`Arc<T>`는 `Rc<T>`와 유사하지만, **Atomic Reference Counting**을 사용해 멀티스레드 환경에서도 안전하게 데이터를 공유할 수 있어요.

#### 예제 코드 3: `Arc<T>`를 이용한 멀티스레드 공유

```rust
use std::sync::Arc;
use std::thread;

fn main() {
    // Arc를 사용해 공유 가능한 데이터 생성
    let shared_data = Arc::new(42);
    
    // 여러 스레드에서 공유
    let handle1 = thread::spawn({
        let data = Arc::clone(&shared_data);
        move || {
            println!("Thread 1 sees: {}", data);
        }
    });
    
    let handle2 = thread::spawn({
        let data = Arc::clone(&shared_data);
        move || {
            println!("Thread 2 sees: {}", data);
        }
    });
    
    // 스레드 종료 대기
    handle1.join().unwrap();
    handle2.join().unwrap();
}
```

**코드 설명:**
- `Arc::new(42)`로 정수를 공유 가능한 형태로 생성해요.
- `Arc::clone(&shared_data)`로 여러 스레드에서 참조 카운트를 증가시키며 공유해요.
- 각 스레드에서 데이터를 출력하면서 안전하게 공유가 이루어지는 걸 볼 수 있어요.

**💡 초보자 폭풍 질문!**
- **Q: `Arc`는 언제 사용해야 하나요?**
  - **A:** 멀티스레드 환경에서 여러 스레드가 동일한 데이터를 안전하게 공유해야 할 때 사용해요. 예를 들어, 웹 서버에서 공유 상태를 관리할 때 유용하죠!

---

이렇게 `Box`, `Rc`, `Arc`에 대해 깊이 있게 살펴봤어요! 스마트 포인터는 러스트에서 메모리 관리를 쉽게 만들어주는 핵심 요소들이에요. 초보자라도 이제 이 개념들을 잘 이해하셨으리라 믿어요. 다음 강의에서도 더 재미있고 유용한 내용으로 찾아뵙겠습니다! 질문이 있으면 언제든지 물어봐주세요. 함께 성장해나가는 거죠!

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
