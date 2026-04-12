---
layout: single
title: "Rust 스레드 및 컨텍스트 스위칭 이해"
date: 2026-06-19 19:11:49
categories: [Rust C 언어]
---

# 32강: Rust 스레드 및 컨텍스트 스위칭 이해하기 - 세상을 더 빠르게 만드는 마법의 기술

안녕하세요, 열정 넘치는 Rust 주니어 개발자 여러분! 오늘은 `#Rust 스레드`와 `#컨텍스트 스위칭`에 대해 이야기해볼게요. 이거 진짜 신기하죠? 마치 슈퍼히어로 영화에서 시간을 조종하는 능력을 얻은 것 같아요! 😎

## 스레드: 팀플레이의 미학

### 기본 개념: 우리 모두가 한 팀이 되어

스레드란 무엇일까요? 쉽게 말해, **동시에 여러 작업을 수행하는 능력**이에요. 마치 팀 프로젝트에서 각자 맡은 역할을 동시에 해내는 것과 같아요. 한 팀이 여러 임무를 동시에 처리하면 프로젝트가 훨씬 빠르게 완료되죠!

#### 예제: 간단한 스레드 생성

```rust
use std::thread;
use std::sync::mutable::{AtomicUsize, Ordering};

fn main() {
    // 작업 카운터를 공유하기 위한 Atomic 변수 생성
    let counter = AtomicUsize::new(0);

    // 스레드 생성 함수 정의
    let handle1 = thread::spawn(|| {
        for _ in 0..5 {
            // 카운터 증가 (스레드 안전을 위해 Atomic 사용)
            counter.fetch_add(1, Ordering::SeqCst);
            println!("스레드 1 작업 완료");
        }
    });

    let handle2 = thread::spawn(|| {
        for _ in 0..5 {
            counter.fetch_add(1, Ordering::SeqCst);
            println!("스레드 2 작업 완료");
        }
    });

    // 스레드 종료 대기
    handle1.join().unwrap();
    handle2.join().unwrap();

    // 최종 카운터 값 출력
    println!("총 작업 완료 횟수: {}", counter.load(Ordering::SeqCst));
}
```

**코드 해설:**
- `AtomicUsize`를 사용하여 여러 스레드에서 안전하게 카운터를 증가시킵니다.
- `Ordering::SeqCst`는 모든 스레드가 순서대로 실행되도록 보장합니다.
- `thread::spawn` 함수로 새로운 스레드를 생성하고, 각 스레드가 5번 반복하며 작업을 수행합니다.
- `join()` 메서드는 스레드가 완료될 때까지 주 스레드가 기다리게 합니다.

### 다양한 스레드 제어 방법

#### 1. **반복문으로 스레드 제어**
```rust
fn main() {
    let handles: Vec<_> = (0..10)
        .map(|i| thread::spawn(move || {
            for _ in 0..i {
                println!("스레드 {} 실행 중", i);
            }
        }))
        .collect();

    for handle in handles {
        handle.join().unwrap();
    }
}
```
- **해설:** 반복문을 사용해 여러 스레드를 순차적으로 생성하고 관리합니다. 각 스레드는 다른 작업을 수행합니다.

#### 2. **채널을 이용한 데이터 교환**
```rust
use std::sync::mpsc::{channel, Sender};

fn main() {
    let (tx, rx) = channel();

    let handle = thread::spawn(move || {
        tx.send(format!("스레드 메시지: {}", thread::current().name().unwrap_or("default"))).unwrap();
    });

    handle.join().unwrap();

    for msg in rx {
        println!("메시지 수신: {}", msg);
    }
}
```
- **해설:** 스레드 간 데이터를 안전하게 주고받기 위해 `mpsc` 채널을 사용합니다. `tx`로 메시지를 보내고 `rx`로 수신합니다.

#### 3. **동기화 구조체 활용**
```rust
use std::sync::{Arc, Mutex};

fn main() {
    let counter = Arc::new(Mutex::new(0));
    let mut handles = vec![];

    for _ in 0..10 {
        let counter_clone = Arc::clone(&counter);
        let handle = thread::spawn(move || {
            let mut num = counter_clone.lock().unwrap();
            *num += 1;
            println!("스레드 작업 완료, 카운터: {}", *num);
        });
        handles.push(handle);
    }

    for handle in handles {
        handle.join().unwrap();
    }

    println!("최종 카운터 값: {}", *counter.lock().unwrap());
}
```
- **해설:** `Arc`와 `Mutex`를 사용해 스레드 간 공유 자원을 안전하게 관리합니다. 모든 스레드가 카운터를 증가시키고 동기화됩니다.

## 컨텍스트 스위칭: 마법사의 손길

### 기본 개념: 슈퍼히어로의 순간 이동!

컨텍스트 스위칭은 컴퓨터가 여러 스레드 사이를 빠르게 전환하는 과정을 말해요. 마치 슈퍼히어로가 순간 이동을 통해 여러 장소를 오가는 것과 같죠! 📡

#### 컨텍스트 스위칭의 중요성

- **효율성 향상:** CPU 시간을 여러 작업에 분배하여 전체 시스템 성능을 높입니다.
- **자원 최적화:** 각 스레드가 필요한 만큼의 CPU 시간을 받을 수 있게 해줍니다.

### 컨텍스트 스위칭의 실제 적용

#### 1. **간단한 컨텍스트 스위칭 예시**
```rust
use std::thread;
use std::time::Duration;

fn main() {
    let mut handle = thread::spawn(|| loop {
        println!("스레드 작업 중...");
        thread::sleep(Duration::from_millis(500)); // 잠깐 대기
    });

    handle.join().unwrap(); // 스레드 종료까지 기다림
}
```
- **해설:** `thread::sleep`를 통해 컨텍스트 스위칭이 자연스럽게 일어나는 모습을 보여줍니다. 스레드가 일정 시간마다 작업을 수행하고 잠깐 대기하면서 다른 스레드에게 CPU 시간을 양보합니다.

#### 2. **동기화된 컨텍스트 스위칭**
```rust
use std::thread;
use std::sync::mpsc;

fn main() {
    let (tx, rx) = mpsc::channel();

    let sender = thread::spawn(move || {
        for i in 0..5 {
            tx.send(format!("스레드 메시지 {}: {}", thread::current().name(), i)).unwrap();
            thread::sleep(Duration::from_millis(100));
        }
    });

    for msg in rx {
        println!("메시지 수신: {}", msg);
    }

    sender.join().unwrap();
}
```
- **해설:** 채널을 통해 스레드 간 메시지를 주고받으며 컨텍스트 스위칭이 자연스럽게 이루어집니다. 각 스레드가 일정 시간마다 메시지를 보내고 기다립니다.

### 초보자 폭풍 질문! 🚀
**Q:** 스레드를 너무 많이 생성하면 성능이 떨어지지 않나요?
**A:** 맞아요! 스레드 수가 많아지면 컨텍스트 스위칭의 오버헤드가 커져 성능 저하가 발생할 수 있어요. 적절한 스레드 수를 유지하고, 스레드 간 자원 공유를 최적화하는 것이 중요해요. 실험해보면서 최적의 스레드 수를 찾아보세요!

### 실무 주의보! ⚠️
**주의사항:** 스레드 안전성이 중요합니다. 공유 자원에 대한 접근을 올바르게 동기화하지 않으면 **데이터 레이스** 현상이 발생할 수 있어요. 이는 프로그램의 예측 불가능한 동작으로 이어질 수 있으니 항상 주의하세요!

---

이렇게 `#Rust 스레드`와 `#컨텍스트 스위칭`에 대해 자세히 알아보았습니다. 이제 여러분도 슈퍼히어로처럼 여러 작업을 동시에 처리하는 능력을 갖추게 되었어요! 실전에서 다양한 상황에 적용해보면서 실력을 키워나가세요. 🤘

더 궁금한 점이 있으면 언제든지 물어보세요! 함께 성장해 나가요! 🚀

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
