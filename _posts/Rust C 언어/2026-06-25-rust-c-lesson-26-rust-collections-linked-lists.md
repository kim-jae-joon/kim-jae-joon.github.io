---
layout: single
title: "Rust 컬렉션과 연결 리스트 구현"
date: 2026-06-25 19:10:07
categories: [Rust C 언어]
---

## 26강: Rust 컬렉션 마스터하기: 연결 리스트로 코딩 마법사 되기!

안녕하세요, 초보 개발자 여러분! 오늘은 **Rust의 마법 세상, 컬렉션** 중에서도 특히 **연결 리스트**에 대해 깊숙이 파고들어볼 거예요. 준비됐나요? 그럼 **코딩 모험** 시작해봅시다! 🧙‍♂️✨

### 연결 리스트: 링크로 연결된 모험의 지도

**연결 리스트**는 마치 **인디 게임의 맵** 같아요. 각각의 **노드(Node)**가 지도상의 중요한 지점처럼, 데이터를 품고 있고 서로 **링크(Link)**로 연결되어 있어요. 이 연결 덕분에 데이터를 자유롭게 이동하며 탐색할 수 있답니다.

#### 개념 설명: 왜 연결 리스트인가?

- **동적 크기**: 리스트의 크기는 실행 중에도 조절 가능해요. 마치 게임 속 인벤토리처럼 필요할 때마다 확장 가능해요!
- **삽입/삭제 용이성**: 특정 위치에 데이터를 넣거나 삭제하기 쉬워요. 게임에서 아이템을 특정 슬롯에 추가하거나 제거하는 것과 비슷해요!

### Rust에서 연결 리스트 구현하기: 초보자를 위한 스텝별 가이드

#### 1. 기본 구조: 노드 정의하기

먼저, 연결 리스트의 기본 단위인 **노드**를 정의해야 해요. 각 노드는 데이터와 다음 노드를 가리키는 포인터로 구성됩니다.

```rust
// 노드 구조체 정의
struct Node<T> {
    data: T,       // 저장할 데이터 타입
    next: Option<Box<Node<T>>>, // 다음 노드를 가리키는 링크
}

// 예시: 정수형 데이터를 가진 노드 생성
fn create_node(data: i32) -> Box<Node<i32>> {
    Box::new(Node {
        data,
        next: None,  // 초기에는 다음 노드가 없음
    })
}
```

**코드 해설:**
- `struct Node<T>`: 제네릭 타입 `T`를 사용해 다양한 데이터 타입을 지원합니다.
- `data: T`: 노드가 보유할 데이터를 저장합니다.
- `next: Option<Box<Node<T>>>`: 다음 노드를 가리키는 링크로, `Option`을 사용해 노드가 끝인지 아닌지 판단합니다. `Box`는 동적 메모리 할당을 위해 사용됩니다.

#### 2. 연결 리스트 클래스 구현하기

다음으로, 연결 리스트 자체를 관리하는 클래스를 만들어볼게요. 여기서는 **가독성**을 위해 **`LinkedList`**라는 이름을 사용할게요.

```rust
// 연결 리스트 구조체 정의
struct LinkedList<T> {
    head: Option<Box<Node<T>>>, // 리스트의 시작 노드
}

impl<T> LinkedList<T> {
    // 생성자: 빈 리스트 초기화
    fn new() -> Self {
        LinkedList { head: None }
    }

    // 노드 삽입 메서드 (특정 위치에 삽입)
    fn insert(&mut self, index: usize, data: T) {
        let mut current = self.head.as_mut(); // 현재 노드를 헤드로 초기화
        let mut new_node = create_node(data); // 새로운 노드 생성

        if index == 0 { // 첫 번째 위치 삽입
            new_node.next = self.head; // 새로운 노드의 다음이 기존 헤드가 됨
            self.head = Some(new_node); // 헤드 업데이트
        } else {
            let mut count = 0;
            while count < index && current.is_some() { // 인덱스 범위 내에 삽입
                current = current.unwrap().next.as_mut(); // 다음 노드로 이동
                count += 1;
            }
            if count == index { // 올바른 위치에 삽입
                let prev = unsafe { std::mem::replace(&mut current, None).unwrap() }; // 이전 노드 제거
                new_node.next = prev.unwrap().next; // 새 노드의 다음이 이전 노드의 다음이 됨
                prev.unwrap().next = Some(new_node); // 이전 노드의 다음을 새 노드로 설정
            } else {
                // 인덱스 범위 벗어남: 에러 처리 (간단히 여기서는 무시)
            }
        }
    }

    // 데이터 삭제 메서드 (특정 인덱스의 데이터 삭제)
    fn remove(&mut self, index: usize) {
        let mut current = self.head.as_mut();
        let mut prev = None; // 이전 노드 추적용

        let mut count = 0;
        while current.is_some() && count < index {
            prev = current;
            current = current.unwrap().next.as_mut();
            count += 1;
        }

        if count == index { // 올바른 위치에 도달했을 때
            if prev.is_some() {
                // 이전 노드의 다음을 현재 노드의 다음으로 연결
                unsafe {
                    (*prev.unwrap()).next = current.unwrap().next.take();
                }
            } else {
                // 헤드 노드 제거 시 처리
                self.head = current.unwrap().next;
            }
        } else {
            // 인덱스 범위 벗어남: 에러 처리 (간단히 여기서는 무시)
        }
    }

    // 리스트 출력 함수 (데이터 확인)
    fn print_list(&self) {
        let mut current = self.head.as_ref();
        while let Some(node) = current {
            println!("{:?}", node.data);
            current = node.next.as_ref();
        }
        println!("--- 리스트 끝 ---");
    }
}
```

**코드 해설:**

- **`LinkedList<T>::new()`**: 빈 리스트를 초기화합니다.
- **`insert(&mut self, index: usize, data: T)`**: 주어진 인덱스에 데이터를 삽입합니다.
  - `index == 0`: 리스트의 첫 번째 위치에 삽입할 때 헤드를 새 노드로 업데이트합니다.
  - `count < index`: 인덱스 범위 내에서 적절한 위치를 찾아 삽입합니다.
- **`remove(&mut self, index: usize)`**: 주어진 인덱스의 노드를 삭제합니다.
  - `prev`를 사용해 이전 노드를 추적하고, 올바른 위치에서 노드를 제거합니다.
  - 헤드 노드가 삭제되는 경우 별도로 처리합니다.
- **`print_list(&self)`**: 리스트의 모든 데이터를 출력합니다.

#### 3. 다양한 방법으로 연결 리스트 구현하기

**반복문 활용 예시:**

```rust
// 노드 삽입을 for 루프를 사용하여 구현
fn insert_with_for(list: &mut LinkedList<i32>, data_list: Vec<i32>) {
    for data in data_list {
        list.insert(list.head.is_some() ? 1 : 0, data); // 첫 번째 위치 또는 그 다음 위치 삽입
    }
}

// 예시 호출
let mut my_list = LinkedList::new();
insert_with_for(&mut my_list, vec![10, 20, 30]);
my_list.print_list(); // 출력: 10 20 30 --- 리스트 끝 ---
```

**while 루프 활용 예시:**

```rust
// 특정 조건까지 삽입하는 while 루프 예시
fn insert_until_condition(list: &mut LinkedList<i32>, limit: i32) {
    let mut count = 0;
    while count < limit {
        list.insert(count, count * 10); // 인덱스와 비례한 값 삽입
        count += 1;
    }
}

// 예시 호출
let mut conditional_list = LinkedList::new();
insert_until_condition(&mut conditional_list, 5);
conditional_list.print_list(); // 출력: 0 10 20 30 40 --- 리스트 끝 ---
```

### 💡 초보자 폭풍 질문! 🤔

**Q1:** 연결 리스트에서 메모리 누수가 발생할 수 있나요?
- **A1:** 네, 올바르게 관리하지 않으면 메모리 누수가 발생할 수 있어요. 특히 노드를 삭제할 때 이전 노드의 `next` 포인터를 올바르게 설정하지 않으면 메모리 누수가 생길 수 있습니다. `drop`을 적절히 사용하거나 `std::mem::replace`와 같은 기법을 활용해 메모리를 정확히 관리하세요!

**Q2:** 연결 리스트와 벡터(Vector)의 주요 차이점은 무엇인가요?
- **A2:** 연결 리스트는 동적 크기와 삽입/삭제의 유연성을 제공하지만, 접근 속도가 느립니다 (인덱스 접근이 아님). 반면, 벡터는 빠른 랜덤 액세스가 가능하지만 고정된 크기로 초기화해야 하며, 삽입/삭제가 끝부분 외에는 비효율적일 수 있어요. 게임 개발에서는 연결 리스트가 더 유용할 수 있지만, 데이터 처리가 많은 일반적인 애플리케이션에서는 벡터가 더 적합할 수 있어요!

### 🚨 실무 주의보 🚨

**경고:** 실제 프로젝트에서는 **스마트 포인터(Smart Pointers)**와 **라이프타임(Lifetime)** 개념을 이해하고 적용하는 것이 중요해요. 특히 `Box`, `Rc`, `Arc` 등을 적절히 사용하여 메모리 누수를 방지하세요!

### 마무리

오늘은 Rust의 연결 리스트를 통해 코딩의 마법사가 되는 첫걸음을 내디뎠습니다! 연결 리스트는 데이터 구조의 기본 중 하나이므로, 이를 잘 이해하고 활용하면 훨씬 유연하고 강력한 프로그램을 만들 수 있어요. 

이제 여러분도 **"링크로 연결된 모험"**을 시작해보세요! 🧙‍♀️🔧 다음 강의에서는 더 복잡하고 실용적인 예제로 돌아올게요. 그때까지 연습 많이 해보시고, 궁금한 점은 언제든지 질문해주세요! 👍

---

이 긴 포스트가 여러분의 연결 리스트 이해를 한층 더 깊게 만들어주길 바라요! 🚀

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
