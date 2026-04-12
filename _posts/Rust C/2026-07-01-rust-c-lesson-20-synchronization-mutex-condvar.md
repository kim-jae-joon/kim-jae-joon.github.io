---
layout: single
title: "동기화 메커니즘: Mutex와 Condvar"
date: 2026-07-01 18:33:16
categories: [Rust C]
---

### 20강: 동기화 메커니즘: Mutex와 Condvar - 코드 세계의 팀워크 마스터 되기

안녕하세요, 초보 개발자 여러분! 오늘은 Rust의 세계에서 가장 중요한 팀워크 기술 중 하나인 **Mutex와 Condvar**에 대해 깊이 들어가 보려 합니다. 🤯 "Mutex와 Condvar? 그거 뭐야?" 라고 생각하실 수 있지만, 걱정 마세요! 이 주제는 여러분의 프로그램이 깔끔하고 효율적으로 동작하도록 돕는 핵심 요소들입니다. 이 강의를 마치면, 여러분은 마치 코드 세계의 올스타 팀 코치가 될 수 있을 거예요!

---

### 1. 동기화의 중요성: 코드 세계의 오케스트라 지휘자

상상해보세요. 여러 스레드가 동시에 같은 데이터에 접근하려고 할 때, 혼란이 발생할 수 있습니다. 마치 오케스트라에서 모든 악기가 동시에 연주되면 소리가 혼돈에 빠지는 것과 같죠! 이때 **동기화 메커니즘**이 등장합니다. **Mutex**와 **Condvar**는 코드 세계에서 오케스트라의 지휘자 역할을 합니다. 정확히 어떻게 작동하는지 함께 살펴보겠습니다.

#### 1.1 Mutex: 단일 접근 권한 보장

**Mutex**는 "Mutual Exclusion"의 약자로, **단일 스레드만 데이터에 접근할 수 있도록 보장하는 잠금 장치**라고 생각하면 됩니다. 쉽게 말해, "한 번에 한 명만 들어갈 수 있는 클럽 문" 같은 역할을 합니다.

**예제 코드 1: Mutex 기본 사용**

```rust
use std::sync::{Mutex, Arc};
use std::thread;

fn main() {
    // 공유 데이터 생성
    let shared_data = Arc::new(Mutex::new(0));

    // 스레드 벡터 생성
    let mut handles = vec![];

    for _ in 0..10 {
        // 스레드 생성 및 데이터 접근 함수 할당
        let data = Arc::clone(&shared_data);
        let handle = thread::spawn(move || {
            // 잠금을 걸고 데이터 수정
            let mut num = shared_data.lock().unwrap();
            *num += 1;
            println!("수정된 값: {}", num);
        });
        handles.push(handle);
    }

    // 모든 스레드 종료 대기
    for handle in handles {
        handle.join().unwrap();
    }
}
```

**코드 설명:**
- `Arc<Mutex<i32>>`: 공유 데이터를 안전하게 다루기 위해 `Arc`와 `Mutex`를 사용합니다.
- `lock()` 메서드: 스레드가 데이터에 접근하기 전에 `Mutex`를 잠그고 해제합니다. 만약 다른 스레드가 이미 잠그고 있으면 대기 상태가 됩니다.
- `*num += 1`: 데이터를 안전하게 수정합니다.

#### 1.2 다양한 잠금 구조: 반복문 활용

Mutex를 사용하는 방법은 다양합니다. 예를 들어, 반복문을 통해 여러 번 시도하며 잠금을 획득하는 방식도 가능합니다.

**예제 코드 2: 반복문을 통한 잠금 획득**

```rust
use std::sync::{Mutex, Arc};
use std::thread;
use std::time::Duration;

fn main() {
    let shared_data = Arc::new(Mutex::new(0));
    let mut handles = vec![];

    for _ in 0..5 {
        let data = Arc::clone(&shared_data);
        let handle = thread::spawn(move || {
            let mut retries = 0;
            loop {
                // 잠금 획득 시도 (최대 10번 시도)
                let mut locked = false;
                for _ in 0..10 {
                    if locked = data.try_lock().is_ok() {
                        break;
                    }
                    retries += 1;
                    thread::sleep(Duration::from_millis(100)); // 일시 대기
                }
                if locked {
                    *data.lock().unwrap() += 1;
                    println!("시도 횟수: {}, 수정된 값: {}", retries, *data.lock().unwrap());
                    break;
                } else {
                    println!("잠금 실패, 다시 시도 중... 시도 횟수: {}", retries);
                }
            }
        });
        handles.push(handle);
    }

    for handle in handles {
        handle.join().unwrap();
    }
}
```

**코드 설명:**
- `try_lock()`: 잠금을 시도하지만 즉시 실패하면 `false`를 반환합니다.
- `thread::sleep()`: 실패 시 잠시 대기하고 다시 시도합니다.

---

### 2. Condvar: 조건 기반 대기

**Condvar**는 **Condition Variable**의 약자로, 스레드가 특정 조건이 만족될 때까지 기다리는 능력을 제공합니다. 마치 "신호 대기"와 같아요. 팀의 일부 스레드가 작업이 완료될 때까지 다른 스레드가 대기할 수 있게 해줍니다.

#### 2.1 Condvar 기본 사용 예제

**예제 코드 3: 스레드 간 동기화**

```rust
use std::sync::{Condvar, Mutex};
use std::thread;
use std::time::Duration;

fn main() {
    let shared_data = Mutex::new(false);
    let cvar = Condvar::new();
    let mut handles = vec![];

    // 생산자 스레드
    let producer_handle = thread::spawn(move || {
        for _ in 0..5 {
            thread::sleep(Duration::from_secs(1)); // 대기 시간
            let mut data = shared_data.lock().unwrap();
            *data = true; // 데이터 변경
            println!("생산 완료!");

            // 조건 만족 알림
            cvar.notify_all();
            std::thread::sleep(Duration::from_secs(1)); // 다음 작업 대기
        }
    });
    handles.push(producer_handle);

    // 소비자 스레드
    let consumer_handle = thread::spawn(move || {
        loop {
            let mut data = shared_data.lock().unwrap();
            while !*data {
                // 조건 만족될 때까지 대기
                println!("대기 중...");
                data = cvar.wait(data).unwrap(); // 잠금 유지 상태에서 대기
            }
            println!("데이터 처리 완료!");
            // 데이터 처리 로직
        }
    });
    handles.push(consumer_handle);

    // 모든 스레드 종료 대기
    for handle in handles {
        handle.join().unwrap();
    }
}
```

**코드 설명:**
- `cvar.wait(data)`: 데이터 잠금을 유지한 채로 조건이 만족될 때까지 기다립니다.
- `cvar.notify_all()`: 모든 대기 중인 스레드에게 조건 만족 신호를 보냅니다.

#### 2.2 다양한 조건 대기 구조: if-else 활용

Condvar는 다양한 조건에 따라 스레드를 제어할 수 있습니다. 만약-else 구조를 활용해 더 복잡한 로직을 구현할 수도 있습니다.

**예제 코드 4: 복잡한 조건 기반 대기**

```rust
use std::sync::{Condvar, Mutex};
use std::thread;
use std::time::Duration;

fn main() {
    let shared_data = Mutex::new(0);
    let cvar = Condvar::new();
    let mut handles = vec![];

    // 스레드 생성
    let worker_handle = thread::spawn(move || {
        loop {
            let mut data = shared_data.lock().unwrap();
            if *data == 0 {
                println!("데이터 초기 상태, 대기...");
                data = cvar.wait(data).unwrap(); // 조건 만족까지 대기
            } else if *data == 1 {
                println!("데이터 상태 변경, 작업 중...");
                *data = 2; // 상태 업데이트
                cvar.notify_all(); // 다음 단계로 이동
            } else if *data == 2 {
                println!("작업 완료!");
                *data = 0; // 초기 상태로 복원
                cvar.notify_all(); // 다음 사이클 시작
            }
        }
    });
    handles.push(worker_handle);

    // 메인 스레드에서 조건 변경
    thread::sleep(Duration::from_secs(3));
    {
        let mut data = shared_data.lock().unwrap();
        *data = 1; // 조건 변경
        cvar.notify_all();
    }

    // 모든 스레드 종료 대기
    for handle in handles {
        handle.join().unwrap();
    }
}
```

**코드 설명:**
- `if-else` 구조: 다양한 상태에 따라 다른 동작을 수행합니다.
- `cvar.notify_all()`: 각 상태 변경 후 다른 스레드에게 신호를 보내어 다음 단계로 이동합니다.

---

### 🚨 실무주의보 🚨

**실무 팁:**
- **Mutex 사용 시 주의사항**: `lock()` 메서드는 블록킹 콜이므로, 장시간 잠근 상태가 지속되면 성능 저하가 발생할 수 있습니다. 가능한 한 빠르게 작업을 완료하고 잠금을 해제하세요.
- **Condvar 활용**: 복잡한 조건 기반 동기화에서는 `wait()`과 `notify_one()`, `notify_all()`을 적절히 조합하여 스레드 간의 효율적인 통신을 구현하세요.

### 💡 초보자 폭풍 질문! 💡

1. **Mutex와 Condvar를 함께 사용할 때 주의해야 할 사항은 무엇인가요?**
   - **답변**: 주로 데이터 잠금과 조건 대기를 동시에 관리할 때 발생할 수 있는 데드락(Deadlock)을 주의해야 합니다. 예를 들어, 한 스레드가 Mutex를 잡고 있는 상태에서 Condvar의 `wait()`를 호출하고, 다른 스레드가 그 상태에서 즉시 작업을 시작하면 문제가 생길 수 있습니다. 항상 잠금 해제와 조건 만족 신호 보내기의 순서를 명확히 유지하세요.

2. **Mutex를 사용할 때 반복문을 통한 잠금 획득 시도는 언제 유용한가요?**
   - **답변**: 잠금 획득이 즉시 이루어지지 않을 때 유용합니다. 예를 들어, 경쟁 조건(race condition)을 방지하기 위해 일시적으로 대기하면서 재시도하는 상황에서 유용합니다. 특히 시스템 부하가 높거나 경쟁이 심한 환경에서는 이런 방식이 안정성을 높여줍니다.

3. **Condvar를 사용하여 복잡한 상태 전환 로직을 구현하는 방법은 무엇인가요?**
   - **답변**: `if-else` 구조를 활용해 각 상태에 따라 다른 동작을 수행할 수 있습니다. 예를 들어, 데이터 상태에 따라 다른 조건을 설정하고, 해당 조건이 만족될 때까지 `wait()`를 호출하여 효율적으로 상태 전환을 관리할 수 있습니다.

---

이제 여러분은 Rust에서 동기화 메커니즘의 핵심인 Mutex와 Condvar를 마스터할 준비가 되었습니다! 코드 세계의 팀워크 코치가 되어 복잡한 문제도 함께 해결해 나가세요. 🚀 다음 강의에서도 더 재미있는 주제로 만나요!

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
