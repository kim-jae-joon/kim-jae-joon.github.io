---
layout: single
title: "Rust 기초: 에러 핸들링: Result와 Option"
date: 2026-07-11 02:09:40
categories: [Rust]
---

# 12강: Rust 기초 - 에러 핸들링: Result와 Option

안녕하세요, 여러분의 친근한 주니어 개발자 친구입니다! 오늘은 Rust 프로그래밍에서 정말 중요한 주제 중 하나인 **에러 핸들링**에 대해 이야기해볼게요. 특히 `Result`와 `Option`에 대해 알아볼 예정입니다. 이 두 가지는 마치 프로그래밍 세계의 '슈퍼히어로 팀' 같아요. 코드가 예상치 못한 상황에서도 흔들리지 않게 도와주는 존재들입니다. 🦸‍♂️🦸‍♀️

## 왜 이런 문법이 필요한가요?

Rust는 안전성과 효율성을 최우선으로 생각하는 언어입니다. 그래서 에러가 발생할 가능성이 있는 상황을 미리 예측하고 관리하는 메커니즘이 필수적이죠. `Result`와 `Option`은 바로 이런 목적을 위해 탄생했습니다.

### **Result: 에러의 왕**

`Result`는 두 가지 상태를 표현합니다: 성공(`Ok`)과 실패(`Err`). 이 개념을 이해하면 코드가 예상치 못한 오류에 대처하는 능력이 엄청나게 향상됩니다!

#### 코드 예제 1: 파일 읽기 예시

```rust
use std::fs::File;
use std::io::{self, Read};

fn read_file(path: &str) -> Result<String, io::Error> {
    let mut file = File::open(path)?; // 파일 열기 실패 시 에러 반환
    let mut contents = String::new();
    file.read_to_string(&mut contents)?; // 읽기 실패 시 에러 반환
    Ok(contents) // 성공 시 파일 내용 반환
}

fn main() {
    match read_file("example.txt") {
        Ok(content) => println!("파일 내용: {}", content),
        Err(e) => println!("오류 발생: {}", e),
    }
}
```

- **파일 열기 (`File::open`)**: `?` 연산자는 함수가 `Result`를 반환할 때, 만약 `Err` 상태라면 즉시 에러를 반환하고 함수를 종료합니다.
- **파일 읽기 (`read_to_string`)**: 마찬가지로 `?`를 사용해 에러 처리를 간결하게 합니다.
- **결과 처리 (`match`)**: `match` 문을 사용해 `Result`의 상태에 따라 코드를 분기합니다.

**💡 초보자 폭풍 질문!**
> `?` 연산자가 뭔지 잘 모르겠어요!

**답변**: `?` 연산자는 함수 호출 결과가 `Result` 타입일 때, 에러가 발생하면 즉시 그 에러를 상위 스코프로 반환하는 역할을 합니다. 이렇게 하면 에러 처리 코드를 간결하게 만들 수 있어요. 마치 "만약 에러가 나면 여기서 멈추고 에러를 넘기자"는 마법의 주문 같은 거죠!

### **Option: 값이 있을 수도, 없을 수도**

`Option`은 값이 존재할 수도 있고, 존재하지 않을 수도 있는 상황을 표현합니다. 주로 데이터 검색이나 컬렉션에서 특정 요소를 찾을 때 유용합니다.

#### 코드 예제 2: 맵에서 값 찾기

```rust
use std::collections::HashMap;

fn find_value(data: &HashMap<String, i32>, key: &str) -> Option<&i32> {
    data.get(key) // 키가 있으면 값을 반환, 없으면 None 반환
}

fn main() {
    let mut scores = HashMap::new();
    scores.insert("Alice".to_string(), 95);
    scores.insert("Bob".to_string(), 88);

    match find_value(&scores, "Alice") {
        Some(score) => println!("Alice의 점수: {}", score),
        None => println!("Alice의 점수 정보가 없습니다."),
    }

    match find_value(&scores, "Charlie") {
        Some(score) => println!("Charlie의 점수: {}", score),
        None => println!("Charlie의 점수 정보가 없습니다."),
    }
}
```

- **`HashMap::get`**: 키가 존재하면 `Some(값)`을, 존재하지 않으면 `None`을 반환합니다.
- **`match` 문**: `Option`의 상태에 따라 다른 동작을 수행합니다.

**🚨 실무주의보**
> 실제 프로젝트에서 `Option`을 제대로 처리하지 않으면 '누락된 데이터'로 인한 버그가 생길 수 있어요. 항상 `Some`과 `None` 케이스를 고려해야 합니다!

### **Result와 Option의 연계 활용**

두 개념을 함께 사용하면 복잡한 시나리오에서도 안정적인 코드를 작성할 수 있습니다. 예를 들어, 데이터 검색 후 특정 조건을 체크하는 상황을 생각해볼까요?

#### 코드 예제 3: 복합 시나리오

```rust
use std::collections::HashMap;

fn process_data(data: &HashMap<String, Option<i32>>, key: &str) -> Result<String, String> {
    match data.get(key) {
        Some(Some(value)) if value > 90 => Ok(format!("{}의 점수는 우수합니다: {}", key, value)),
        Some(Some(value)) => Ok(format!("{}의 점수는 보통입니다: {}", key, value)),
        Some(None) => Err("점수 정보가 없습니다.".to_string()),
        None => Err("해당 사용자가 존재하지 않습니다.".to_string()),
    }
}

fn main() {
    let mut user_scores = HashMap::new();
    user_scores.insert("Alice".to_string(), Some(92));
    user_scores.insert("Bob".to_string(), Some(85));
    user_scores.insert("Charlie".to_string(), None);

    match process_data(&user_scores, "Alice") {
        Ok(msg) => println!("{}", msg),
        Err(e) => println!("에러: {}", e),
    }

    match process_data(&user_scores, "Charlie") {
        Ok(msg) => println!("{}", msg),
        Err(e) => println!("에러: {}", e),
    }
}
```

- **`HashMap`에 `Option<i32>`**: 점수가 있을 수도, 없을 수도 있는 상황을 표현합니다.
- **복합 조건 처리**: `match`를 통해 다양한 케이스를 처리하며, `Result`로 최종 결과를 반환합니다.

## 마무리: 에러 핸들링의 힘

`Result`와 `Option`을 잘 활용하면 코드의 안정성과 가독성을 크게 향상시킬 수 있어요. 이들은 단순히 에러를 처리하는 도구가 아니라, 프로그램의 견고성을 높이는 핵심 요소랍니다. 이제 여러분도 이런 강력한 무기를 손에 넣었으니, 복잡한 프로젝트에서도 자신감을 가지고 도전해보세요!

---

이 강의가 여러분의 Rust 여정에 큰 도움이 되길 바라며, 궁금한 점이 있으면 언제든지 물어보세요! 함께 성장하는 여정이 되길 기원합니다. 💪💡

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
