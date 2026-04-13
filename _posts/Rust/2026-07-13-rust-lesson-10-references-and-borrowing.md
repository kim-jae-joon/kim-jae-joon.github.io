---
layout: single
title: "Rust 기초: 참조와 borrowing"
date: 2026-07-13 01:59:58
categories: [Rust]
---

# 10강: Rust 기초 - 참조와 Borrowing: 마법의 세계로 초대합니다!

안녕하세요, 여러분! Rust 5년차 주니어 개발자이자 이 글의 주인장입니다. 오늘은 Rust 프로그래밍의 핵심 중 하나인 **참조와 Borrowing**에 대해 이야기해볼게요. 이건 좀 신기하고도 중요한 주제니까, 집중하자구요! 진짜 신기하죠? 😄

## 왜 참조와 Borrowing이 필요한가요?

Rust는 메모리 안전성을 보장하면서도 성능을 극대화하려는 목표를 가지고 있어요. 그런데, 이런 목표를 이루려면 데이터를 어떻게 다루는지에 대한 철저한 관리가 필요하답니다. 바로 여기서 **참조(References)**와 **Borrowing**이 등장하는 거죠!

### 참조란 무엇인가요?

참조는 간단히 말해, 변수가 아닌 다른 변수의 메모리 주소를 가리키는 포인터 같은 존재예요. Rust에서는 직접 메모리를 다루는 대신, 참조를 통해 안전하게 데이터에 접근할 수 있어요.

#### 예제 1: 기본 참조 사용하기

```rust
fn main() {
    let num = 42;  // 정수 변수 선언
    let ref_num = &num;  // num의 참조 생성

    println!("Original number: {}", num);  // 원본 출력
    println!("Referenced number: {}", ref_num);  // 참조 출력
}
```

- `&num`: `&` 기호는 참조를 생성합니다. `ref_num`은 `num`의 참조입니다.
- 출력 결과: 둘 다 `42`를 보여줄 거예요. 신기하죠?

### Borrowing: 빌려쓰기의 미학

Borrowing은 Rust의 핵심 개념 중 하나로, 데이터를 "빌리는" 방식을 통해 메모리 안전성을 확보합니다. 한 번에 하나의 참조만이 데이터를 "빌릴" 수 있도록 제한하는 것이죠.

#### 예제 2: Borrowing의 기본

```rust
fn main() {
    let str_data = String::from("Hello, Rust!");

    // str_data를 빌려 사용
    borrow_string(&str_data);

    println!("Outside function: {}", str_data);
}

fn borrow_string(s: &str) {  // 함수 파라미터로 참조 전달
    println!("Inside function: {}", s);
}
```

- `&str_data`: `str_data`를 함수 `borrow_string`에 빌려줍니다.
- `borrow_string` 함수에서는 `s`라는 참조를 통해 `str_data`를 사용합니다.
- **💡 초보자 폭풍 질문!**: 왜 직접 값을 넘겨주지 않고 참조를 넘겨주는 걸까요?
  - **답변**: 직접 값을 넘기면 복사 비용이 발생하고, 큰 데이터 타입(예: `String`)의 경우 성능에 영향을 줄 수 있어요. 참조를 사용하면 데이터를 실제로 복사하지 않고 안전하게 접근할 수 있어요.

## Multiple Borrowing: 복잡한 상황에서도 안전하게!

Rust는 여러 참조를 동시에 관리하면서도 안전성을 유지하는 데 뛰어납니다. 하지만 주의해야 할 점이 있어요!

#### 예제 3: 불변 참조와 가변 참조의 조화

```rust
fn main() {
    let mut data = vec![1, 2, 3];

    // 불변 참조로 데이터 읽기
    print_data(&data);

    // 가변 참조로 데이터 수정 (단, 한 번에 하나만!)
    modify_data(&mut data);

    println!("Modified data: {:?}", data);
}

fn print_data(data: &[i32]) {  // 불변 참조
    println!("Printing data: {:?}", data);
}

fn modify_data(data: &mut Vec<i32>) {  // 가변 참조
    data.push(4);  // 데이터 추가
}
```

- `&data`: 불변 참조로 데이터를 읽기만 합니다.
- `&mut data`: 가변 참조로 데이터를 수정할 수 있습니다.
- **🚨 실무주의보**: 한 번에 불변 참조와 가변 참조를 동시에 가질 수 없습니다! 이 규칙을 어기면 컴파일 타임 에러가 발생합니다.

### 왜 이런 규칙이 필요한가요?

이런 엄격한 규칙은 데이터의 일관성을 유지하고, 메모리 오류를 방지하는 데 필수적이에요. 마치 마법의 규칙처럼 작동하지만, 실제로는 안전한 프로그래밍을 위한 Rust의 지혜랍니다!

---

이렇게 오늘은 Rust의 핵심 개념 중 하나인 참조와 Borrowing에 대해 깊게 파고들어봤어요. 처음엔 복잡해 보일 수 있지만, 꾸준히 연습하면 이 마법 같은 세계에 익숙해질 거예요. 다음 강의에서도 재미있는 주제로 다시 만나요!

궁금한 점이 있다면 언제든지 물어보세요. 함께 성장하는 거예요!

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
