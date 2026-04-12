---
layout: single
title: "스마트 포인터: Rc와 Arc"
date: 2026-07-10 18:31:03
categories: [C언어]
---

## 11강: 스마트 포인터 마스터하기 - Rc와 Arc: 메모리 관리의 마법사가 되다!

**진짜 신기하죠?**  Rust에서 메모리 관리는 마치 마법사가 복잡한 주문을 외우며 물체를 움직이는 것 같아요. 그 중에서도 **스마트 포인터**는 특히 강력한 마법 도구죠! 특히 `Rc`와 `Arc`는 공유 데이터를 다루는 데 있어서 절대 놓칠 수 없는 핵심 요소입니다. 오늘은 이 두 스마트 포인터를 통해 메모리 관리의 신비를 밝혀내는 여정을 떠나볼게요. 초보자 여러분, 따라오세요!

### 🤔 Rc: 공유 소유권의 마법사

`Rc`는 **RefCount (참조 카운트)**의 약자로, 여러 곳에서 동일한 데이터를 참조할 수 있게 해주는 포인터입니다. 마치 친구들끼리 책을 함께 읽다가 누가 마지막까지 책을 보유하고 있는지 확인하는 것과 같죠!

#### 기본 개념 설명

- **참조 카운트**: 데이터를 참조하는 객체의 수를 추적합니다.
- **삭제 조건**: 참조 카운트가 0이 되면 메모리 해제.

#### 실용적 예제: Rc를 이용한 간단한 공유 데이터 구조

```rust
use std::rc::Rc;
use std::sync::Mutex;

fn main() {
    // 데이터와 참조 카운트를 함께 관리하는 Rc 객체 생성
    let shared_data = Rc::new(Mutex::new(vec![1, 2, 3])); // 벡터 예시 데이터

    // 공유 데이터 복사 (새로운 Rc 참조 생성)
    let mut data1 = Rc::clone(&shared_data); // 데이터1이 데이터를 참조
    let mut data2 = Rc::clone(&shared_data); // 데이터2도 데이터를 참조

    // 데이터 수정 예시 (Mutex를 사용하여 동시 접근 방지)
    {
        let mut lock = shared_data.lock().unwrap(); // Mutex 락 획득
        lock.push(4); // 데이터 추가
    }

    // 출력 확인
    println!("데이터: {:?}", *shared_data.lock().unwrap()); // [1, 2, 3, 4] 출력

    // 참조 카운트 확인
    println!("data1 참조 카운트: {}", Rc::strong_count(&data1)); // 출력 예시: 2
    println!("data2 참조 카운트: {}", Rc::strong_count(&data2)); // 출력 예시: 2

    // 데이터1을 드롭 (참조 카운트 감소)
    drop(data1);
    println!("data1 드롭 후 참조 카운트: {}", Rc::strong_count(&data2)); // 출력 예시: 1
}
```

**코드 해설:**

1. **`Rc::new(Mutex::new(vec![1, 2, 3]))`**: 공유 데이터를 `Rc`와 함께 `Mutex`로 감싸서 동시 접근을 안전하게 관리합니다.
2. **`Rc::clone(&shared_data)`**: `shared_data`의 참조를 복사하여 `data1`과 `data2`가 동일한 데이터를 참조하게 만듭니다.
3. **`lock.push(4)`**: `Mutex`를 사용해 동시 접근을 방지하며 데이터를 안전하게 수정합니다.
4. **`Rc::strong_count(&data)`**: 현재 참조 카운트를 확인합니다. 참조 수가 줄어들면 메모리 해제 조건에 도달합니다.

### 🌪️ Arc: 멀티스레드 세상의 수호자

`Arc`는 **Atomic Reference Counting**의 약자로, 멀티스레드 환경에서 안전하게 공유 데이터를 관리하는 데 사용됩니다. `Arc`는 `Rc`보다 더 강력한 동기화 기능을 제공하여 여러 스레드에서 동시에 데이터를 참조할 수 있게 합니다.

#### 멀티스레드 환경에서의 활용

멀티스레드 환경에서는 각 스레드가 안전하게 데이터에 접근해야 합니다. `Arc`는 이를 위해 `Mutex`와 결합하여 사용됩니다.

#### 실용적 예제: Arc를 이용한 멀티스레드 데이터 접근

```rust
use std::sync::{Arc, Mutex};
use std::thread;

fn main() {
    // 공유 데이터와 Mutex로 감싸기
    let shared_data = Arc::new(Mutex::new(vec![10, 20, 30]));

    // 스레드 벡터 생성
    let mut handles = vec![];

    // 스레드 생성 및 데이터 접근
    for _ in 0..5 {
        let data_clone = Arc::clone(&shared_data); // 공유 데이터 복제
        let handle = thread::spawn(move || {
            let mut lock = data_clone.lock().unwrap(); // Mutex 락 획득
            lock.push(40); // 데이터 추가
            println!("스레드 ID: {}, 데이터: {:?}", thread::current().id(), *lock);
        });
        handles.push(handle);
    }

    // 모든 스레드 종료 대기
    for handle in handles {
        handle.join().unwrap();
    }

    // 최종 데이터 출력
    println!("최종 데이터: {:?}", *shared_data.lock().unwrap()); // [10, 20, 30, 40] 출력
}
```

**코드 해설:**

1. **`Arc::new(Mutex::new(vec![10, 20, 30]))`**: 공유 데이터를 `Arc`와 `Mutex`로 감싸서 안전한 멀티스레드 접근을 보장합니다.
2. **`Arc::clone(&shared_data)`**: 각 스레드가 데이터를 참조할 수 있도록 `Arc` 복제본을 생성합니다.
3. **`thread::spawn`**: 새로운 스레드를 생성하고 각 스레드에서 데이터를 안전하게 수정합니다.
4. **`lock.push(40)`**: `Mutex`를 사용해 동시 접근을 방지하며 데이터를 추가합니다.
5. **`handle.join()`**: 모든 스레드가 완료될 때까지 기다립니다.

### 💡 초보자 폭풍 질문! 🚨

**Q1:** `Rc`와 `Arc` 중 어떤 상황에서 어떤 것을 써야 하나요?
- **A1:** `Rc`는 단일 스레드 환경에서 여러 위치에서 데이터를 공유할 때 사용합니다. 반면, `Arc`는 멀티스레드 환경에서 안전한 공유 데이터 관리가 필요할 때 사용합니다.

**Q2:** `Mutex`와 함께 사용하는 이유는 무엇인가요?
- **A2:** `Mutex`는 데이터의 동시 접근을 방지하여 데이터 일관성을 유지하는 데 필수적입니다. `Rc`와 `Arc`만으로는 스레드 안전성을 보장할 수 없습니다.

### 🏆 실무 주의보!

`Rc`와 `Arc`는 강력한 도구지만, 과도한 사용은 성능 이슈를 초래할 수 있습니다. 특히 참조 카운트가 높게 유지되는 경우 메모리 누수 위험이 있으므로 주의가 필요합니다. 코드 리뷰와 프로파일링을 통해 최적화를 지속적으로 검토하세요!

### 마무리

오늘 배운 `Rc`와 `Arc`는 메모리 관리의 핵심 마법 도구입니다. 이들을 잘 활용하면 Rust에서 복잡한 데이터 공유 문제를 쉽게 해결할 수 있어요. 계속 연습하고 다양한 시나리오에서 적용해보세요! 

**다음 강의에서는 더 깊은 메모리 관리 기법과 최적화 방법에 대해 살펴보겠습니다. 지금까지 함께 성장해온 여러분, 정말 대단해요!**

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
