---
layout: single
title: "Rust 응용: Concurrency: Threads와 Channels"
date: 2026-07-05 02:46:19
categories: [Rust]
---

# 18강: Rust 응용: Concurrency: Threads와 Channels - 함께 미래의 코드를 짜봅시다!

안녕하세요, 여러분의 곁을 늘 지켜주는 5년차 주니어 개발자 [닉네임]입니다! 오늘은 Rust의 매력 중 하나인 **Concurrency**, 특히 **Threads**와 **Channels**에 대해 깊이 파헤쳐 보려고 합니다. 이 주제를 통해 코드가 마치 슈퍼히어로처럼 여러 작업을 동시에 처리하는 법을 배워볼 거예요. 준비되셨나요? 그럼, 함께 출발해볼까요?

## 📚 왜 Concurrency가 중요할까요?

**Concurrency**란, 쉽게 말해 "한 번에 여러 일을 처리하는 능력"입니다. 요즘 세상이 빠르게 돌아가는 만큼, 우리 코드도 그에 맞춰 빠르고 효율적으로 움직여야 합니다. 특히, CPU를 최대한 활용하거나 I/O 대기 시간을 줄이는 데 있어서 Concurrency는 필수입니다. **Threads**는 이런 동시 작업을 구현하는 기본 도구이고, **Channels**는 이들 사이에서 데이터를 안전하게 주고받는 방법을 제공합니다.

## 🧵 Threads: 코드의 멀티태스킹 마스터

### 기본적인 Thread 생성하기

Rust에서 Thread를 만드는 방법은 `std::thread` 모듈을 사용하는 것입니다. 간단하게 예제를 통해 살펴보겠습니다.

```rust
use std::thread;

fn main() {
    // 새로운 스레드 생성: "Hello from thread!" 출력
    thread::spawn(|| {
        println!("Hello from thread!");
    });

    // 주 스레드에서 출력
    println!("Hello from main thread!");
}
```

**코드 설명:**
- `thread::spawn` 함수를 통해 새로운 스레드를 생성합니다.
- 클로저 (`|| { ... }`) 안에 스레드가 실행할 코드를 작성합니다.
- 주 스레드와 스레드가 동시에 실행되므로 출력 순서는 환경에 따라 달라질 수 있습니다.

### 🛠 스레드 안전과 데이터 공유

스레드 간 데이터 공유는 주의가 필요합니다. Rust는 메모리 안전성을 위해 컴파일 타임에 엄격한 검사를 실시합니다. 이를 위해 **Mutex**와 같은 동기화 도구를 사용합니다.

```rust
use std::sync::{Arc, Mutex};
use std::thread;

fn main() {
    let counter = Arc::new(Mutex::new(0)); // 공유 데이터: 카운터

    let mut handles = vec![];

    for _ in 0..10 {
        let counter = Arc::clone(&counter); // Arc를 통해 데이터 공유
        let handle = thread::spawn(move || {
            let mut num = counter.lock().unwrap(); // 뮤텍스 잠금
            *num += 1;
        });
        handles.push(handle);
    }

    for handle in handles {
        handle.join().unwrap(); // 모든 스레드가 완료될 때까지 대기
    }

    println!("Final counter value: {}", *counter.lock().unwrap());
}
```

**코드 설명:**
- `Arc`는 원자 참조 카운팅을 통해 데이터를 여러 스레드에서 공유할 수 있게 합니다.
- `Mutex`는 데이터에 대한 접근을 동기화하여 여러 스레드가 동시에 수정하는 것을 방지합니다.
- `lock()` 메서드로 뮤텍스를 잠그고, 작업 후 해제됩니다 (자동 해제).

## 🚀 Channels: 스레드 간 통신의 마법사

Channels은 스레드 간에 데이터를 안전하게 주고받는 데 사용되는 도구입니다. **Send**와 **Sync** 트레이트를 만족하는 타입만 채널을 통해 전송 가능합니다.

### 채널 생성과 사용하기

```rust
use std::sync::mpsc; // Multi-Producer Single-Consumer 채널

fn main() {
    let (tx, rx): (mpsc::Sender<i32>, mpsc::Receiver<i32>) = mpsc::channel();

    // 스레드에서 데이터 보내기
    thread::spawn(move || {
        tx.send(42).unwrap(); // 데이터 전송
        println!("Data sent!");
    });

    // 메인 스레드에서 데이터 받기
    let received = rx.recv().unwrap();
    println!("Received: {}", received);
}
```

**코드 설명:**
- `mpsc::channel`을 통해 송신자 (`Sender`)와 수신자 (`Receiver`)를 생성합니다.
- `tx.send()`로 데이터를 보내고, `rx.recv()`로 데이터를 받습니다.
- `unwrap()`은 에러 처리를 간단히 처리하는 방법이지만, 실제 프로젝트에서는 더 안전한 에러 핸들링이 필요합니다.

### 💡 초보자 폭풍 질문!
**Q: 스레드와 프로세스의 차이는 무엇인가요?**
- **A:** 스레드는 동일한 프로세스 내에서 실행되는 실행 단위입니다. 메모리 공간을 공유하므로 데이터 교환이 쉽지만, 프로세스는 독립적인 메모리 공간을 가지므로 더 안전하지만, 데이터 교환이 복잡해집니다.

### 🚨 실무주의보!
**스레드와 채널을 사용할 때 주의할 점:**
- **에러 핸들링:** 채널을 통해 데이터를 주고받을 때 발생할 수 있는 에러를 적절히 처리해야 합니다.
- **라이프사이클 관리:** 스레드가 종료되기 전에 모든 작업이 완료되었는지 확인해야 합니다 (예: `join()` 사용).

## 📌 요약 및 미래를 향한 도약

오늘은 Rust에서 **Threads**와 **Channels**를 활용해 동시성 프로그래밍의 기초를 다졌습니다. 이 기술들은 복잡한 시스템을 효율적으로 설계하고 관리하는 데 있어 핵심적인 역할을 합니다. 앞으로 더 많은 동시성 개념과 고급 패턴을 배워가면서, 여러분의 코드는 더욱 강력하고 유연해질 거예요!

혹시 궁금한 점이 있으면 언제든지 물어봐주세요. 함께 성장하는 여정에 여러분을 초대합니다! 다음 강의에서 또 만나요!

---

이렇게 디테일하게 설명드렸는데, 이해가 잘 되셨나요? 더 궁금한 점이 있으면 언제든지 말씀해 주세요!

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
