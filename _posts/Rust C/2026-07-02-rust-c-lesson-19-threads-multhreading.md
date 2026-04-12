---
layout: single
title: "스레딩 및 멀티스레딩 기초"
date: 2026-07-02 18:33:00
categories: [Rust C]
---

## 19강: 스레딩 & 멀티스레딩, 🤯 컴퓨터의 멀티태스킹 마법사가 되어보자!

안녕하세요, 멋진 코드 모험가 여러분! 오늘은 **컴퓨터가 동시에 여러 일을 해내는 신비로운 세계**, 바로 **스레딩과 멀티스레딩**에 대해 탐험해 볼 거예요. 

**진짜 신기하죠?** 우리 인간은 아침에 커피 한 잔, 이메일 확인, 옷 고르기... 동시에 다 할 수 있나요? 🤔  하지만 컴퓨터는 좀 다릅니다. 과거에는 한 번에 하나의 작업만 처리할 수 있었죠. 마치 한 가지 일에 집중하는 **단일 스레드**처럼요!

하지만 시간이 흘러 **멀티코어 프로세서**가 등장하면서 컴퓨터도 **멀티스레딩의 마법**을 부릴 수 있게 되었답니다! 이제 컴퓨터도 **"아, 커피 내리면서 동시에 이메일 확인도 할 수 있겠네!"** 라는 생각을 할 수 있게 된 거죠! 😄

### 스레드란 무엇일까? – 스레드의 슈퍼 히어로 소개!

**스레드**는 프로그램 내에서 실행되는 독립적인 작업 단위라고 생각하면 됩니다. 마치 컴퓨터 안에 작은 로봇들이 각자 할 일을 책임지고 있는 것처럼요! 하나의 큰 프로그램이 여러 개의 스레드로 나뉘어 **병렬적으로** 실행될 수 있어요.

**💡 초보자 폭풍 질문!**

* 스레드가 여러 개면 컴퓨터 성능이 엄청 좋아지나요? 🤔

**답변:** 맞아요! 하지만 스레드가 너무 많아지면 오히려 성능 저하가 발생할 수 있어요. 컴퓨터 자원을 효율적으로 분배하는 게 중요해요!

#### 멀티스레딩: 팀워크의 진수!

**멀티스레딩**은 여러 개의 스레드를 동시에 실행하여 프로그램 성능을 극대화하는 기술입니다. 마치 **팀 프로젝트**처럼 각 스레드가 특정 작업을 담당하고 협력하여 큰 목표를 달성하는 거죠!

**🚨 실무주의보**

* 실제 프로젝트에서 멀티스레딩 구현 시 주의해야 할 점은? 🤔

**답변:** 데이터 공유 시 **경쟁 상태(Race Condition)** 문제를 꼭 주의해야 합니다. 여러 스레드가 동일한 데이터를 동시에 수정할 때 예상치 못한 결과가 발생할 수 있으니, **뮤텍스(Mutex)**나 **세마포어(Semaphore)** 같은 동기화 도구를 활용하는 것이 중요해요!

### 스레드 프로그래밍: 실전 코드 탐험!

이제 이론은 충분히 봤으니, 직접 코드로 스레드를 만나볼까요? Rust 언어를 사용해서 몇 가지 실용적인 예제를 살펴볼게요.

#### 1. **기본 스레드 생성:**

```rust
use std::thread;

fn main() {
    // 스레드 핸들을 저장할 변수 선언
    let handle1 = thread::spawn(|| {
        println!("스레드 1: 안녕하세요!"); // 익명 함수로 스레드 작업 정의
        // 스레드가 종료될 때까지 대기
        thread::sleep(std::time::Duration::from_millis(1000)); 
        println!("스레드 1 나가요!");
    });

    let handle2 = thread::spawn(|| {
        println!("스레드 2: 만나서 반가워요!");
        thread::sleep(std::time::Duration::from_millis(1500));
        println!("스레드 2 작별!");
    });

    // 두 스레드 모두 완료될 때까지 기다림
    handle1.join().unwrap();
    handle2.join().unwrap();

    println!("메인 스레드: 모든 스레드가 종료되었습니다!");
}
```

**코드 해설:**

* `thread::spawn()` 함수로 새로운 스레드를 생성하고 익명 함수(`|| {}`)로 스레드 작업을 정의합니다. 마치 스레드에게 임무를 주는 것과 같죠!
* `thread::sleep()`는 스레드가 잠시 멈추도록 합니다. 여기서는 각 스레드가 작업을 마치고 메시지를 출력하기 전에 짧게 휴식을 취하는 역할을 합니다.
* `handle1.join().unwrap();` 와 `handle2.join().unwrap();` 는 메인 스레드가 스레드 작업이 완료되었는지 확인하고 결과를 기다립니다. 마치 팀원들의 업무 완료를 확인하는 것과 같아요!

#### 2. **데이터 공유와 동기화 (뮤텍스 활용):**

```rust
use std::sync::Mutex;
use std::thread;

fn main() {
    let shared_counter = Mutex::new(0); // 공유 데이터 보호를 위한 뮤텍스 생성

    let mut handles = vec![];
    for _ in 0..4 { // 4개의 스레드 생성
        let counter = shared_counter.clone(); // 뮤텍스 소유권 공유
        let handle = thread::spawn(move || {
            let mut num = counter.lock().unwrap(); // 뮤텍스 잠금
            *num += 1; // 공유 데이터 접근 및 수정
            println!("스레드 번호: {}, 카운터: {}", thread::current().id(), num);
        });
        handles.push(handle);
    }

    for handle in handles {
        handle.join().unwrap(); // 모든 스레드 완료 대기
    }

    println!("메인 스레드: 모든 스레드 작업 완료! 최종 카운터 값: {}", *shared_counter.lock().unwrap());
}
```

**코드 해설:**

* `Mutex::new(0)`으로 공유 변수 `shared_counter`를 생성하고, 여러 스레드에서 동시에 접근할 때 발생할 수 있는 **경쟁 상태**를 방지합니다.
* `counter.lock().unwrap()`는 뮤텍스를 잠금하여 유일하게 데이터에 접근할 수 있도록 합니다. 마치 동시에 문을 열고 들어가려는 사람들을 하나씩 통과시키는 문지기 역할을 하는 거죠!
* `move` 키워드는 스레드 함수 내부에서 `counter`를 이동시켜 소유권을 이전합니다.

#### 3. **채워 넣기: 조건문과 스레드 제어**

```rust
use std::thread;
use std::sync::ConditionVariable;
use std::time::Duration;

fn main() {
    let cond_var = ConditionVariable::new(); // 조건 변수 생성
    let mut ready = false;

    // 스레드 1: 작업 수행 후 조건 변수 대기
    thread::spawn(move || {
        // 장시간 작업 시뮬레이션
        thread::sleep(Duration::from_secs(2));
        println!("스레드 1: 작업 완료!");
        ready = true; // 조건 변경
        cond_var.notify_one(); // 대기 중인 스레드 알림
    });

    // 메인 스레드: 조건 변수 기다림
    let mut guard = cond_var.lock().unwrap();
    while !ready {
        guard = cond_var.wait(guard).unwrap(); // 조건 확인 및 대기
    }

    println!("메인 스레드: 스레드 1 작업 완료 신호 받음!");
}
```

**코드 해설:**

* `ConditionVariable`은 스레드 간의 **협력적인 대기**를 가능하게 합니다. 마치 신호등처럼 특정 조건이 충족될 때까지 스레드들이 기다리는 모습입니다.
* `cond_var.wait(guard).unwrap();`는 조건 변수가 변경될 때까지 기다리는 역할을 합니다. `guard`는 뮤텍스와 유사하게 동기화를 담당합니다.

### 마무리: 멀티스레딩 마스터가 되어보자!

오늘 함께 스레딩과 멀티스레딩의 기본을 탐험했어요! 아직 어색하게 느껴질 수도 있지만, 꾸준히 연습하고 다양한 예제를 접하다보면 **컴퓨터의 숨겨진 멀티태스킹 능력**을 자유자재로 다룰 수 있는 마법사가 될 거예요!

**추가 학습 팁:**

* **Rust의 `async/await`** 를 활용한 비동기 프로그래밍도 탐색해보세요. 현대 애플리케이션에서 매우 중요한 기술이에요!
* **실제 프로젝트**에 스레딩을 적용해보는 경험은 최고의 학습 방법입니다. 작은 프로젝트부터 시작해도 좋아요!

**💪 자신감을 가지세요!** 멀티스레딩은 처음에는 어려울 수 있지만, 꾸준히 노력하면 분명 멋진 결과를 만들어낼 수 있을 거예요. 코드로 세상을 변화시켜 봐요! 👍

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
