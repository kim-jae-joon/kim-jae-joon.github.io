---
layout: single
title: "Rust 함수 작성: 매개변수와 반환값"
date: 2026-07-11 19:06:22
categories: [Rust C 언어]
---

## 10강: Rust 함수 작성: 매개변수와 반환값 - 함수의 마법을 배우다! 🪄

안녕하세요, 코딩의 신나는 여정에 함께하시는 여러분! 오늘은 마치 **마법의 지팡이를 얻은 마법사**처럼 느껴지는 주제, **함수 작성**에 대해 깊이 있게 알아보겠습니다. 특히 **매개변수**와 **반환값**이라는 신비로운 요소들을 통해 Rust 코드의 힘을 더욱 강하게 만들어볼게요!

### 🤔 함수, 왜 필요한 걸까요?

함수를 처음 접하는 분들은 "왜 복잡하게 함수를 써야 하는 거지?"라고 생각하실지도 모릅니다. 하지만 생각해보세요! 만약 마법 주문을 외우는 대신에 **마법의 레시피 책**을 갖고 있다면 어떨까요? 각 레시피는 특정 마법 효과를 쉽게 만들어줍니다. 바로 이런 역할이 함수가 하는 거예요!

함수는 **재사용 가능한 코드 블록**입니다. 예를 들어, 여러분이 자주 사용하는 **문자열 뒤집기 기능**을 함수로 만들어보겠습니다. 이렇게 하면 코드를 깔끔하게 유지하고, 필요할 때마다 쉽게 호출할 수 있어요.

### 🧙‍♂️ 함수의 기본 구조: 매개변수와 반환값

#### 1. 매개변수 (Parameters) - 마법 재료

매개변수는 함수가 동작할 때 필요한 **입력값**입니다. 마치 마법사가 마법을 부릴 때 필요한 재료처럼요! Rust에서 매개변수를 사용하는 방법을 살펴보겠습니다.

**예제 1: 문자열 뒤집기 함수**

```rust
fn reverse_string(text: String) -> String {
    // 문자열을 뒤집기 위한 로직
    let reversed: String = text.chars().rev().collect();
    reversed
}

fn main() {
    let original = String::from("Hello, Rust!");
    let reversed = reverse_string(original); // 매개변수 'original'을 전달
    println!("원래 문자열: {}", original);
    println!("뒤집힌 문자열: {}", reversed); // 결과 출력
}
```

- **코드 해설**:
  - `reverse_string` 함수는 `text`라는 매개변수를 받습니다. 이 매개변수는 함수가 동작하기 위한 **입력 재료**입니다.
  - `text.chars().rev().collect()`는 문자열을 문자 단위로 분리하고 역순으로 정렬한 후 다시 문자열로 만듭니다.
  - 함수의 마지막 줄에서 `reversed` 문자열을 반환합니다.

**질문 시간!** 💡 초보자 폭풍 질문!
- **Q**: 매개변수를 여러 개 넣을 수 있나요?
  - **A**: 네! 여러 매개변수를 사용할 수 있어요. 예를 들어:
    ```rust
    fn greet(name: String, age: u32) -> String {
        format!("안녕하세요, {}님! 나이는 {}살입니다.", name, age)
    }
    let greeting = greet(String::from("영희"), 25);
    println!("{}", greeting);
    ```

#### 2. 반환값 (Return Value) - 마법의 결과

반환값은 함수가 **결과물을 내놓는 방식**입니다. 마법사가 주문을 마친 후 **마법의 열매**를 내놓는 것과 같죠!

**예제 2: 숫자 더하기 함수**

```rust
fn add_numbers(a: i32, b: i32) -> i32 {
    // 두 숫자를 더하는 로직
    let sum = a + b;
    sum // 반환값
}

fn main() {
    let result = add_numbers(5, 7);
    println!("합계는 {}입니다!", result);
}
```

- **코드 해설**:
  - `add_numbers` 함수는 두 개의 정수 매개변수 `a`와 `b`를 받아 더한 결과를 반환합니다.
  - `let sum = a + b;`에서 계산이 이루어지고, 마지막에 `sum`을 반환합니다.
  - `main` 함수에서 `add_numbers`를 호출하고 결과를 출력합니다.

**질문 시간!** 💡 초보자 폭풍 질문!
- **Q**: 함수가 반환값이 없을 때 어떻게 해야 하나요?
  - **A**: 반환값이 없는 경우 `->` 뒤에 명시적으로 `()`를 추가해야 합니다. 예를 들어:
    ```rust
    fn print_message() -> () {
        println!("마법이 작동합니다!");
    }
    ```

### 🌟 다양한 함수 구조 살펴보기

함수는 다양한 방식으로 작성될 수 있습니다. 조건에 따라 여러 구조를 적용해보세요!

#### 반복문과 함수의 조합: 몇 가지 예시

**예제 3: 리스트의 요소 합계 구하기**

```rust
fn sum_elements(numbers: Vec<i32>) -> i32 {
    let mut total = 0;
    for number in numbers {
        total += number; // 반복문을 통해 합계 계산
    }
    total // 반환값
}

fn main() {
    let numbers = vec![1, 2, 3, 4, 5];
    let sum = sum_elements(numbers);
    println!("합계: {}", sum);
}
```

- **코드 해설**:
  - `sum_elements` 함수는 리스트 `numbers`를 받아 각 요소를 더한 합계를 반환합니다.
  - `for number in numbers` 반복문을 사용해 각 요소를 순회하며 합계를 계산합니다.

**예제 4: 최대값 찾기 함수**

```rust
fn find_max(numbers: Vec<i32>) -> Option<i32> {
    if numbers.is_empty() {
        return None; // 빈 리스트일 경우 None 반환
    }
    let mut max = numbers[0];
    for &number in &numbers {
        if number > max {
            max = number; // 최대값 업데이트
        }
    }
    Some(max) // 최대값 반환
}

fn main() {
    let numbers = vec![3, 1, 4, 1, 5, 9];
    match find_max(numbers) {
        Some(max_value) => println!("최대값: {}", max_value),
        None => println!("리스트가 비어 있습니다."),
    }
}
```

- **코드 해설**:
  - `find_max` 함수는 리스트에서 최대값을 찾아 `Option<i32>` 형태로 반환합니다. `Option` 타입은 값이 있거나 없을 때 유용합니다.
  - 반복문을 통해 리스트의 각 요소를 비교하며 최대값을 찾아냅니다.

### 🚨 실무주의보

함수를 작성할 때 **타입 안전성**을 잊지 마세요! Rust의 강력한 타입 시스템은 오류를 미리 잡아줍니다. 매개변수와 반환값의 타입을 명확하게 지정하면 코드의 안정성이 크게 향상됩니다. 예를 들어:

```rust
// 잘못된 타입 지정 예시 (컴파일 오류 발생)
fn divide(a: i32, b: i32) -> f64 { // 예상치 못한 타입 충돌
    a as f64 / b as f64 // 타입 변환 필요
}

// 올바른 타입 지정 예시
fn divide_safe(a: i32, b: i32) -> Option<f64> {
    if b == 0 {
        None // 나누기 오류 처리
    } else {
        Some(a as f64 / b as f64)
    }
}
```

### 마무리: 함수의 힘을 느껴보세요!

오늘 배운 내용으로 함수의 마법을 경험해보셨나요? 매개변수와 반환값을 잘 이해하고 활용하면 코드가 훨씬 직관적이고 유지보수하기 쉬워집니다. 

**다음 도전 과제:**
- 여러분만의 작은 프로젝트를 만들어보세요! 예를 들어, 간단한 계산기 프로그램을 함수로 구현해보세요. 매개변수와 반환값을 활용해 다양한 연산을 수행할 수 있게 해보세요!

이제 여러분도 코딩 마법사가 되어 가는 중이에요! 💪 계속해서 배우고 실험하며 성장해나가세요. 다음 강의에서도 더 재미있는 주제로 만나요!

---

이렇게 상세하고 재미있게 작성해봤어요! 궁금한 점이 있으면 언제든지 물어보세요!

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
