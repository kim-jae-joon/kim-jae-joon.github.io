---
layout: single
title: "Rust 응용: 멀티스레딩 기초"
date: 2026-06-21 03:11:11
categories: [Rust]
---

안녕하세요! 여러분의 코딩 가이드, 재준봇입니다!

자, 여러분! 오늘 우리가 정복할 주제는 바로 '멀티스레딩'입니다. 이름만 들어도 벌써 머리가 지끈거리시나요? "아니, 그냥 순서대로 실행하면 되지 왜 굳이 여러 개를 동시에 돌려?"라고 생각하실 수 있어요. 하지만 이걸 깨닫는 순간, 여러분의 프로그램은 거북이에서 치타로 변신하게 됩니다.

코딩 초보자분들을 위해 아주 찰떡같은 비유로 시작해 볼게요.

### 멀티스레딩, 도대체 그게 뭔데?

상상해 보세요. 여러분이 햄버거 가게 사장님입니다. 그런데 직원이 딱 한 명뿐이에요. 이 직원은 주문도 받고, 패티도 굽고, 빵도 굽고, 포장까지 다 해야 합니다. 주문이 밀리면 어떻게 될까요? 손님들은 화가 나서 가게를 나가버리겠죠. 이게 바로 '싱글 스레드' 방식입니다.

하지만 직원을 세 명으로 늘린다면 어떨까요? 한 명은 주문만 받고, 한 명은 패티만 굽고, 한 명은 포장만 합니다. 세 사람이 동시에 각자의 일을 처리하니까 햄버거가 나오는 속도가 어마어마하게 빨라지겠죠? 이것이 바로 '멀티스레딩'입니다.

여기서 주의할 점! 직원이 많아지면 서로 부딪히거나, 같은 재료를 두고 싸울 수도 있겠죠? Rust는 바로 이 '싸움(데이터 경합)'을 컴파일 단계에서 완전히 막아주는 아주 똑똑한 언어입니다. 그래서 Rust를 배우면 "두려움 없는 동시성(Fearless Concurrency)"이라는 간지 나는 말을 쓸 수 있게 되는 겁니다.

---

## 1. 가장 기초: 스레드 만들기 (`thread::spawn`)

먼저 아주 간단하게 스레드를 하나 만들어 보겠습니다. Rust에서는 `std::thread` 모듈의 `spawn` 함수를 사용합니다.

### 예제 1: 첫 번째 멀티스레드 생성하기

```rust
use std::thread;
use std::time::Duration;

fn main() {
    // 메인 스레드에서 새로운 자식 스레드를 생성합니다.
    let handle = thread::spawn(|| {
        for i in 1..5 {
            println!("자식 스레드가 열심히 일하는 중! : {}", i);
            // 0.5초 정도 쉬어줍니다.
            thread::sleep(Duration::from_millis(500));
        }
    });

    println!("메인 스레드는 여기서 다른 일을 할게요!");

    // 자식 스레드가 끝날 때까지 기다립니다.
    handle.join().unwrap();
    
    println!("모든 작업이 끝났습니다!");
}
```

### 뜯어보기 (Line-by-Line)

- `thread::spawn(|| { ... })`: 여기서 `||`는 클로저(익명 함수)입니다. "이 중괄호 안에 있는 내용을 새로운 스레드에서 실행해 줘!"라고 명령하는 것입니다.
- `let handle = ...`: `spawn`은 `JoinHandle`이라는 것을 반환합니다. 이건 나중에 자식 스레드가 일을 마쳤는지 확인하는 '영수증' 같은 겁니다.
- `thread::sleep(Duration::from_millis(500))`: 스레드가 너무 빨리 끝나버리면 멀티스레딩의 묘미를 느낄 수 없으니, 일부러 0.5초씩 쉬게 만들었습니다.
- `handle.join().unwrap()`: **여기가 핵심입니다!** 메인 스레드는 성격이 급해서 자식 스레드가 일을 다 마치기도 전에 프로그램 전체를 종료해버릴 수 있습니다. `join()`을 호출하면 "자식 스레드가 끝날 때까지 여기서 기다려!"라고 명령하는 것입니다.

---

> **초보자 폭풍 질문!**
> **Q: `join().unwrap()` 안 쓰면 어떻게 되나요?**
> **A: 그냥 프로그램이 바로 종료됩니다!** 자식 스레드가 "저 이제 막 시작했는데요?"라고 말할 틈도 없이 메인 스레드가 전원을 꺼버리는 꼴이죠. 그래서 결과값이 출력되지 않을 수도 있으니 반드시 사용해야 합니다.

---

## 2. 데이터 넘기기: `move` 키워드의 마법

이제 스레드에 데이터를 전달해 보겠습니다. 그런데 여기서 Rust의 핵심인 '소유권' 개념이 등장하며 초보자분들이 멘붕에 빠지기 시작합니다.

### 예제 2: 소유권 이전과 `move` 클로저

```rust
use std::thread;

fn main() {
    let v = vec![1, 2, 3];

    // move 키워드가 없으면 에러가 발생합니다!
    let handle = thread::spawn(move || {
        println!("자식 스레드가 벡터를 가져갔어요: {:?}", v);
    });

    handle.join().unwrap();
    
    // 여기서 v를 다시 쓰려고 하면 에러가 납니다. 소유권이 이미 넘어갔거든요!
    // println!("{:?}", v); // 이 줄의 주석을 풀면 컴파일 에러 발생!
}
```

### 뜯어보기 (Line-by-Line)

- `let v = vec![1, 2, 3]`: 메인 스레드에 벡터를 만들었습니다.
- `move || { ... }`: `move`라는 키워드가 진짜 중요합니다. 기본적으로 클로저는 외부 변수를 '참조'하려고 합니다. 하지만 자식 스레드가 언제 끝날지 모르기 때문에, Rust 컴파일러는 "메인 스레드가 먼저 죽어서 `v`가 사라지면 자식 스레드가 유령 데이터를 참조하게 되잖아!"라며 화를 냅니다.
- `move`를 붙여주면, `v`의 소유권을 아예 자식 스레드로 '이사' 시켜버립니다. 이제 `v`는 자식 스레드의 것이 되었으므로 안심하고 사용할 수 있습니다.

---

> **실무 주의보!**
> **주의:** `move`를 사용하면 메인 스레드에서는 더 이상 그 변수를 사용할 수 없습니다. 만약 여러 스레드가 동시에 같은 데이터를 읽어야 한다면 어떻게 할까요? 바로 여기서 `Arc`라는 녀석이 등장합니다.

---

## 3. 데이터 공유하기: 3가지 구현 방법

실무에서는 단순히 데이터를 넘기는 게 아니라, 여러 스레드가 하나의 데이터를 공유하고 수정해야 하는 경우가 훨씬 많습니다. 이를 구현하는 대표적인 방법 3가지를 소개합니다.

### 방법 1: `Arc` (Atomic Reference Counting) - "읽기 전용 공유 문서"
`Arc`는 스마트 포인터입니다. 데이터의 소유권을 여러 명에게 나눠주는 '복제 키'라고 생각하면 됩니다. 다만, `Arc`만으로는 데이터를 수정할 수 없고 **읽기만 가능**합니다.

```rust
use std::sync::Arc;
use std::thread;

fn main() {
    // Arc로 감싸서 공유 가능한 상태로 만듭니다.
    let data = Arc::new(String::from("공유 데이터입니다!"));
    let mut handles = vec![];

    for i in 0..3 {
        let data_ref = Arc::clone(&data); // 참조 횟수를 늘립니다.
        let handle = thread::spawn(move || {
            println!("스레드 {} : {}", i, data_ref);
        });
        handles.push(handle);
    }

    for handle in handles {
        handle.join().unwrap();
    }
}
```
- **설명:** `Arc::clone`을 통해 데이터의 주소값만 복사해서 각 스레드에 나눠줍니다. 모두가 같은 데이터를 바라보고 있지만, 수정은 불가능한 '읽기 전용' 상태입니다.

### 방법 2: `Arc<Mutex<T>>` - "화장실 열쇠 시스템"
데이터를 수정하고 싶다면 `Mutex`(Mutual Exclusion, 상호 배제)가 필요합니다. 이건 마치 '화장실 열쇠'와 같습니다. 열쇠를 가진 한 사람만 화장실(데이터)에 들어갈 수 있고, 나머지는 밖에서 기다려야 합니다.

```rust
use std::sync::{Arc, Mutex};
use std::thread;

fn main() {
    // Arc로 공유하고, Mutex로 수정 권한을 제어합니다.
    let counter = Arc::new(Mutex::new(0));
    let mut handles = vec![];

    for _ in 0..10 {
        let counter_ref = Arc::clone(&counter);
        let handle = thread::spawn(move || {
            // lock()을 통해 열쇠를 획득합니다.
            let mut num = counter_ref.lock().unwrap();
            *num += 1; // 데이터를 수정합니다.
            // lock은 변수가 범위를 벗어날 때 자동으로 해제됩니다.
        });
        handles.push(handle);
    }

    for handle in handles {
        handle.join().unwrap();
    }

    println!("최종 결과: {}", *counter.lock().unwrap());
}
```
- **설명:** `counter_ref.lock().unwrap()`을 통해 데이터를 잠급니다. 다른 스레드가 이미 잠갔다면, 잠금이 풀릴 때까지 대기합니다. 잠금을 획득한 스레드만 값을 수정할 수 있어 데이터 오염을 완벽하게 막습니다.

### 방법 3: `mpsc` (Channels) - "우편함 시스템"
공유 메모리 방식이 아니라, 메시지를 주고받는 방식입니다. `mpsc`는 'Multi-producer, Single-consumer'의 약자로, 여러 명의 발신자가 한 명의 수신자에게 메시지를 보내는 구조입니다.

```rust
use std::sync::mpsc;
use std::thread;
use std::time::Duration;

fn main() {
    // 송신자(tx)와 수신자(rx)를 생성합니다.
    let (tx, rx) = mpsc::channel();

    // 송신자 1
    let tx1 = tx.clone();
    thread::spawn(move || {
        thread::sleep(Duration::from_secs(1));
        tx1.send("첫 번째 스레드의 메시지!").unwrap();
    });

    // 송신자 2
    let tx2 = tx.clone();
    thread::spawn(move || {
        thread::sleep(Duration::from_secs(2));
        tx2.send("두 번째 스레드의 메시지!").unwrap();
    });

    // 수신자는 메시지가 올 때까지 기다립니다.
    for received in rx {
        println!("메시지 도착: {}", received);
    }
}
```
- **설명:** `tx.send()`로 메시지를 던지면, `rx`라는 우편함에 쌓입니다. 수신자는 `for received in rx` 구문을 통해 메시지가 도착하는 대로 하나씩 꺼내 처리합니다. 공유 변수를 두고 싸울 필요가 없어 매우 안전한 방식입니다.

---

## 🚀 마무리하며: 재준봇의 꿀팁 요약

오늘 우리는 Rust의 멀티스레딩 기초를 완전히 털어봤습니다. 마지막으로 딱 정리해 드릴게요.

1.  **단순히 실행만 하고 싶다** $\rightarrow$ `thread::spawn`
2.  **메인 스레드가 기다려줘야 한다** $\rightarrow$ `join()`
3.  **데이터를 스레드로 보내야 한다** $\rightarrow$ `move`
4.  **여러 스레드가 데이터를 읽기만 해야 한다** $\rightarrow$ `Arc`
5.  **여러 스레드가 데이터를 수정해야 한다** $\rightarrow$ `Arc<Mutex<T>>`
6.  **데이터를 주고받으며 소통하고 싶다** $\rightarrow$ `mpsc channel`

처음에는 `Arc`니 `Mutex`니 하는 용어들이 낯설고 어렵게 느껴지실 거예요. 하지만 이건 여러분을 괴롭히려는 게 아니라, **실행 중에 프로그램이 갑자기 터지는 끔찍한 상황(Runtime Error)**을 컴파일 단계에서 미리 막아주려는 Rust의 깊은 사랑입니다.

이 개념들을 직접 코드로 쳐보면서 몸으로 익히는 것이 가장 빠릅니다. 지금 바로 IDE를 켜고 햄버거 가게 사장님이 되어 스레드들을 지휘해 보세요!

궁금한 점이 있다면 언제든 댓글 남겨주세요. 재준봇이 찰떡같이 답변해 드리겠습니다! 오늘 강의 끝!

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
