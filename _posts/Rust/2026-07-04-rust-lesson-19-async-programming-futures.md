---
layout: single
title: "Rust 응용: Asynchronous Programming: futures"
date: 2026-07-04 02:51:38
categories: [Rust]
---

# 19강: Rust 응용: 비동기 프로그래밍 - `futures` 탐험대 출발!

안녕하세요, Rust의 세계에서 5년째 뛰어놀고 있는 주니어 개발자입니다! 오늘은 여러분을 미래로 이끄는 신기술, **비동기 프로그래밍**과 그 핵심 엔진인 `futures`에 대해 함께 탐험해볼 거예요. 진짜 신기하죠? 이거 모르면 큰일 납니다! 비동기 프로그래밍은 우리 코드를 더 효율적이고, 더 멋지게 만들어주는 마법 같은 힘을 가지고 있어요.

## 왜 비동기 프로그래밍이 필요한 걸까?

상상해보세요. 당신이 카페에서 커피를 주문하고, 기다리는 동안 친구와 이야기하거나 다른 일을 할 수 있다면 어떨까요? 비동기 프로그래밍이 바로 그런 원리예요! CPU가 한 작업이 끝날 때까지 기다리지 않고, 다른 작업을 처리할 수 있게 해줘요. 이렇게 하면 프로그램의 성능이 월등히 향상되죠.

### 💡 초보자 폭풍 질문!
- **Q: 비동기 프로그래밍이란 정확히 뭘 의미하나요?**
  - **A:** 비동기 프로그래밍은 작업이 완료될 때까지 기다리지 않고 다른 작업을 처리하는 방식입니다. 예를 들어, 네트워크 요청을 보내면 그 동안 다른 코드를 실행할 수 있어요. 이렇게 하면 프로그램이 더 효율적이고 반응성이 좋아집니다.

## Rust와 `futures`의 만남

Rust에서 비동기 프로그래밍을 구현할 때 가장 많이 쓰이는 도구 중 하나가 바로 `futures`입니다. `futures`는 미래에 완료될 작업을 표현하는 추상화입니다. 쉽게 말해, "이것은 나중에 결과를 줄 거야"라고 약속하는 거죠!

### 기본적인 `future` 사용법

먼저, 필요한 패키지를 임포트해야 합니다. `tokio`는 Rust에서 널리 사용되는 비동기 런타임입니다.

```rust
// Cargo.toml에 tokio 추가 필요
// [dependencies]
// tokio = { version = "1", features = ["full"] }

use tokio::future::Future;
use std::time::Duration;

#[tokio::main]
async fn main() {
    // 간단한 future 예시: 2초 후에 "Hello, Future!" 출력
    let future = async {
        // 2초 대기
        tokio::time::sleep(Duration::from_secs(2)).await;
        "Hello, Future!".to_string()
    };

    // future 실행 및 결과 받기
    let result = future.await;
    println!("{}", result);
}
```

#### 코드 설명:
1. **`tokio::time::sleep(Duration::from_secs(2)).await;`**: 이 줄은 2초 동안 일시정지합니다. `await` 키워드는 비동기 작업이 완료될 때까지 코드 실행을 일시 중단시킵니다.
2. **`async { ... }`**: 비동기 함수를 정의합니다. `async` 블록 내에서는 `await`를 사용해 비동기 작업을 수행할 수 있어요.
3. **`future.await;`**: 정의한 `future`를 실행하고 결과를 받아옵니다.

### 다양한 비동기 패턴

비동기 프로그래밍에서는 여러 패턴이 활용되는데, 몇 가지 주요 패턴을 살펴보겠습니다.

#### 1. **`async` 함수와 `.await`**

```rust
#[tokio::main]
async fn main() {
    // 간단한 비동기 함수
    async fn fetch_data() -> String {
        // 가정: 네트워크 호출을 시뮬레이션
        tokio::time::sleep(Duration::from_secs(1)).await;
        "Data from network".to_string()
    }

    // 비동기 함수 호출
    let data = fetch_data().await;
    println!("Fetched: {}", data);
}
```

- **`async fn fetch_data()`**: 비동기 함수를 정의합니다.
- **`.await`**: 비동기 함수 호출 시 결과를 기다립니다.

#### 2. **`select!`을 활용한 병렬 처리**

`select!`은 여러 비동기 작업을 동시에 처리할 수 있게 해줍니다.

```rust
#[tokio::main]
async fn main() {
    // 두 개의 비동기 작업 생성
    let task1 = async {
        tokio::time::sleep(Duration::from_secs(1)).await;
        "Task 1 Completed!"
    };

    let task2 = async {
        tokio::time::sleep(Duration::from_secs(2)).await;
        "Task 2 Completed!"
    };

    // select!을 이용해 병렬 처리
    let result = tokio::select! {
        res = task1 => res,
        res = task2 => res,
        // timeout 설정 (옵션)
        _ = tokio::time::after(Duration::from_secs(3)) => {
            "Timeout!"
        }
    };

    println!("Result: {}", result);
}
```

- **`tokio::select!`**: 여러 비동기 작업 중 하나가 완료되면 해당 결과를 반환합니다.
- **`timeout`**: 특정 시간 내에 결과가 나오지 않으면 타임아웃 처리를 할 수 있습니다.

### 🚨 실무주의보: 실제 프로젝트에서의 활용

실무에서 비동기 프로그래밍은 주로 I/O bound 작업 (네트워크 요청, 파일 입출력 등)에서 빛을 발합니다. 예를 들어, 웹 서버에서 여러 클라이언트 요청을 동시에 처리할 때 비동기 프로그래밍이 필수적입니다.

#### 예제: 간단한 비동기 웹 서버

```rust
use tokio::net::TcpListener;
use tokio::io::{AsyncReadExt, AsyncWriteExt};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let listener = TcpListener::bind("127.0.0.1:8080").await?;
    println!("Server listening on 127.0.0.1:8080");

    loop {
        let (mut socket, addr) = listener.accept().await?;
        println!("Accepted connection from {}", addr);

        tokio::spawn(async move {
            let mut buf = [0; 1024];
            if let Ok(n) = socket.read(&mut buf).await {
                if n > 0 {
                    socket.write_all(&buf[0..n]).await?; // Echo
                }
            }
            socket.shutdown(std::net::Shutdown::Both).await?;
        });
    }
}
```

- **`TcpListener::bind`**: 서버를 바인딩합니다.
- **`tokio::spawn`**: 각 클라이언트 연결을 별도의 스레드에서 처리합니다.
- **`read`와 `write`**: 비동기 방식으로 데이터를 주고받습니다.

### 마무리: 비동기 프로그래밍의 미래

비동기 프로그래밍은 복잡해 보일 수 있지만, 한 번 익숙해지면 코드의 효율성과 반응성을 극대화하는 데 엄청난 힘을 발휘합니다. `futures`와 함께 Rust의 강력한 비동기 기능을 활용하면, 여러분의 애플리케이션은 더욱 빠르고 안정적으로 진화할 수 있을 거예요!

이제 여러분도 비동기 마법사로 한 걸음 더 다가섰습니다! 질문이 있으시면 언제든지 물어보세요. 함께 성장해 나가요!

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
