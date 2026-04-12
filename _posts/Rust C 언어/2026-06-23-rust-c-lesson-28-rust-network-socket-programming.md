---
layout: single
title: "Rust 네트워크 통신: 소켓 프로그래밍"
date: 2026-06-23 19:10:44
categories: [Rust C 언어]
---

### 28강: Rust 네트워크 통신 - 소켓 프로그래밍: 네트워크의 마법사가 되어보자

안녕하세요, 여러분의 네트워크 마법사 **[닉네임]**입니다! 오늘은 Rust 언어를 이용해 소켓 프로그래밍에 대해 알아보는 시간을 가져볼게요. 네트워크 통신은 마치 마법 같은 능력을 가진 것 같아요. 데이터를 전송하고 받는 순간, 세상과 연결되는 느낌이죠! 진짜 신기하죠? 이 강의를 통해 여러분도 이 멋진 기술의 마법사가 될 수 있을 거예요. 그럼 시작해볼까요?

#### 🌟 소켓 프로그래밍의 기본 이해 🌟

**소켓**이란 무엇일까요? 쉽게 말해, 소켓은 컴퓨터 네트워크에서 데이터를 주고받는 데 사용되는 통신 통로라고 생각하면 됩니다. 마치 우편함과 같아요. 한쪽에서 메시지를 넣으면 다른 쪽 우편함으로 전달되는 거죠!

##### 1. 소켓 생성하기

네트워크 마법을 시작하기 전에 먼저 소켓을 생성해야 합니다. Rust에서는 `std::net` 모듈을 사용해요.

```rust
use std::net::{TcpListener, TcpStream};

fn main() {
    // 소켓 생성
    let listener = TcpListener::bind("127.0.0.1:8080").expect("서버 바인딩 실패");
    println!("서버가 127.0.0.1:8080에서 실행되고 있습니다.");

    // 클라이언트 연결을 기다리며 루프를 돌려볼게요
    for stream in listener.incoming() {
        match stream {
            Ok(stream) => {
                println!("클라이언트 연결 수락!");
                handle_client(stream);  // 클라이언트 핸들러 함수 호출
            }
            Err(e) => {
                println!("클라이언트 연결 에러: {}", e);
            }
        }
    }
}

fn handle_client(mut stream: TcpStream) {
    // 클라이언트와의 데이터 교환 로직
    let message = stream.read_to_string().expect("데이터 읽기 실패");
    println!("클라이언트 메시지: {}", message);
    stream.write_all(b"응답 받았어요!").expect("데이터 쓰기 실패");
    stream.shutdown(std::net::Shutdown::Both).expect("스트림 종료 실패");
}
```

**코드 해설:**

- **`TcpListener::bind("127.0.0.1:8080")`**: 이 코드는 로컬 호스트의 127.0.0.1 주소에서 포트 8080을 바인딩합니다. 이는 서버가 이 주소와 포트에서 클라이언트의 연결을 기다릴 수 있게 해줍니다.
- **`listener.incoming()`**: 이 함수는 연결 요청을 기다리는 무한 루프를 생성합니다. 각 연결이 들어오면 `Ok(stream)`을 반환합니다.
- **`handle_client` 함수**: 연결된 클라이언트와의 데이터 교환을 처리합니다. 여기서 `read_to_string()`으로 클라이언트의 메시지를 읽고, `write_all()`으로 응답 메시지를 보냅니다. `shutdown(std::net::Shutdown::Both)`는 연결을 안전하게 종료합니다.

#### 💡 초보자 폭풍 질문! 💡
- **Q:** `expect("에러 메시지")` 부분은 왜 필요한 건가요?
  - **A:** `expect` 메서드는 오류 발생 시 프로그램이 중단되도록 강제해요. 이는 디버깅 과정에서 매우 유용해요. 실제 프로덕션 환경에서는 좀 더 우아하게 예외 처리를 하는 것이 좋습니다.

#### 다양한 제어 구조로 소켓 핸들링하기

##### 1. 반복문으로 클라이언트 처리하기
**for 문 예시:**

```rust
for connection in listener.incoming() {
    match connection {
        Ok(stream) => {
            println!("새로운 클라이언트 연결 수락!");
            handle_client(stream);
        }
        Err(e) => {
            println!("클라이언트 연결 에러: {}", e);
        }
    }
}
```

**코드 해설:**
- **`for connection in listener.incoming()`**: 각 클라이언트 연결을 반복하면서 처리합니다. 이 방식은 간결하고 직관적이죠!

##### 2. while 문으로 클라이언트 처리하기
**while 문 예시:**

```rust
let mut listener = TcpListener::bind("127.0.0.1:8080").expect("서버 바인딩 실패");
loop {
    let stream = match listener.accept() {
        Ok((stream, _)) => stream,
        Err(e) => {
            println!("클라이언트 연결 에러: {}", e);
            continue;  // 에러 처리 후 다시 시도
        }
    };
    handle_client(stream);
}
```

**코드 해설:**
- **`loop`**: 무한 루프를 돌려 클라이언트 연결을 계속 기다립니다. `match listener.accept()`로 연결을 수락하고, 에러가 발생하면 `continue`로 다음 반복으로 넘어가요.

##### 3. do-while 문처럼 동작하는 반복 구조
Rust에는 전통적인 `do-while` 문이 없지만, 조건에 따라 동작하는 구조를 만들 수 있습니다:

```rust
let listener = TcpListener::bind("127.0.0.1:8080").expect("서버 바인딩 실패");
let mut keep_running = true;

while keep_running {
    let stream = listener.accept().expect("클라이언트 연결 수락 실패");
    handle_client(stream);
    // 특정 조건에 따라 keep_running 업데이트
    if /* 조건 */ {
        keep_running = false;  // 루프 종료 조건
    }
}
```

**코드 해설:**
- **`while keep_running`**: `keep_running` 변수를 통해 루프의 종료 조건을 제어합니다. 특정 조건이 만족되면 루프를 빠져나가요.

#### 🚨 실무주의보 🚨
- **에러 핸들링**: 실제 애플리케이션에서는 모든 `expect`를 `Result` 기반의 안전한 오류 처리로 바꾸는 것이 좋습니다. 이는 디버깅을 용이하게 하고 안정성을 높여줍니다.
- **동기화**: 다수의 클라이언트를 동시에 처리할 때는 멀티스레딩이나 비동기 I/O를 고려해야 합니다. `tokio`나 `async-std`와 같은 라이브러리를 활용해보세요!

#### 요약
네트워크의 마법사가 되는 여정은 여기서 끝나지 않아요! 소켓 프로그래밍은 복잡해 보일 수 있지만, 기초부터 차근차근 익혀가면 네트워크 통신의 마법을 자유롭게 구사할 수 있을 거예요. 여러분이 이 기술의 힘을 느끼는 그날까지, 계속해서 탐구하고 배우는 자세를 잃지 마세요!

💪 **지금 바로 프로젝트에 적용해보세요!** 네트워크 게임 서버를 만들어보거나 간단한 채팅 앱을 개발해보는 건 어떨까요? 여러분의 창의성이 네트워크 세계를 더욱 흥미롭게 만들어줄 거예요!

---

이 강의가 여러분의 네트워크 코딩 여정에 큰 도움이 되길 바랍니다! 추가 질문이 있으면 언제든지 물어보세요. 함께 성장해 나가요!

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
