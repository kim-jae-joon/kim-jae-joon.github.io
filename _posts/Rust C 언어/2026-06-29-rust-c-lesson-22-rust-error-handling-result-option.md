---
layout: single
title: "Rust 에러 핸들링: Result 및 Option 타입"
date: 2026-06-29 19:09:09
categories: [Rust C 언어]
---

### 22강: Rust 에러 핸들링: Result 및 Option 타입 - 에러 시대를 벗어나다!

안녕하세요, 열정 가득한 초보자 여러분! 오늘은 Rust에서 가장 실용적이면서도 핵심적인 기술 중 하나인 **에러 핸들링**에 대해 배워볼 거예요. 특히 `Result`와 `Option` 타입에 집중해볼게요. 이 두 친구를 잘 이해하면 코드가 더 견고해지고, 디버깅이 훨씬 수월해집니다. 준비됐나요? **진짜 신기하죠?** 함께 에러 관리의 세계로 들어가볼게요!

#### # 에러 핸들링의 중요성

"이거 모르면 큰일 납니다!" 에러 핸들링 없이 프로그램을 만든다면, 작은 버그 하나가 큰 재앙으로 변할 수 있어요. 마치 요리를 하는데 소금을 넣는 대신에 물을 넣어버린 것과 같죠. Rust는 이런 문제를 미리 대비하기 위해 강력한 에러 핸들링 메커니즘을 제공해요. 오늘은 그 핵심인 `Result`와 `Option`에 대해 알아보겠습니다.

#### ## Option 타입: Null 안전의 왕

`Option` 타입은 가장 기본적인 안전 메커니즘이에요. 마치 당신이 맛있는 케이크를 찾을 때 **"케이크가 있을까?"**와 **"케이크가 없으면 대체할 게 있을까?"**라는 두 가지 가능성을 나타내는 것과 같아요.

##### **코드 예제 1: 기본 Option 사용**

```rust
fn find_book(library: &str, book_name: &str) -> Option<&str> {
    // 라이브러리에서 책을 찾는 함수
    if library.contains(book_name) {
        Some(book_name) // 책을 찾았다면 Some(책 이름) 반환
    } else {
        None // 책을 못 찾았다면 None 반환
    }
}

fn main() {
    let library = "과학";
    let book_name = "물리학";
    
    match find_book(library, book_name) {
        Some(book) => println!("찾은 책: {}", book), // 책을 찾았을 때 실행
        None => println!("찾는 책이 없습니다."), // 책을 못 찾았을 때 실행
    }
}
```

**코드 분석:**
- **`Option<&str>`**: 책 이름이 있으면 `Some(책 이름)`, 없으면 `None`을 반환합니다.
- **`match` 문**: `Option` 타입의 결과에 따라 다르게 동작합니다. `Some`일 때와 `None`일 때의 처리를 명확히 구분해요.

##### **코드 예제 2: 함수 반환 타입으로 활용**

```rust
fn fetch_data(url: &str) -> Option<String> {
    // 가상의 데이터 가져오기 함수
    if url == "https://valid-url.com" {
        Some("데이터 가져오기 성공".to_string()) // 데이터 성공적으로 가져오면 Some(데이터)
    } else {
        None // URL이 잘못되면 None 반환
    }
}

fn main() {
    let url = "https://invalid-url.com";
    match fetch_data(url) {
        Some(data) => println!("데이터: {}", data), // 데이터 성공 시 출력
        None => println!("데이터를 가져올 수 없습니다."), // 실패 시 출력
    }
}
```

**코드 분석:**
- **`fetch_data` 함수**: URL에 따라 데이터를 성공적으로 가져오면 `Some(데이터 문자열)`을 반환하고, 실패 시 `None`을 반환합니다.
- **`match` 문**: 이 역시 `Option` 타입의 결과에 따라 다른 동작을 수행합니다.

#### ## Result 타입: 에러 처리의 전문가

`Result` 타입은 에러 핸들링의 핵심입니다. 마치 **"길을 걷다가 갑자기 폭우가 오면 어떻게 해야 할까?"**라는 상황에서 **"우산을 쓰거나 집으로 돌아가야 한다"**는 두 가지 선택지를 나타내는 것과 같아요. `Result`는 성공(`Ok`) 또는 실패(`Err`)를 명확하게 구분합니다.

##### **코드 예제 3: 기본 Result 사용**

```rust
fn divide(a: i32, b: i32) -> Result<i32, String> {
    // 나눗셈 함수, 에러 처리 포함
    if b == 0 {
        Err("0으로 나눌 수 없습니다.".to_string()) // 에러 발생 시 Err 반환
    } else {
        Ok(a / b) // 성공 시 결과 반환
    }
}

fn main() {
    let result = divide(10, 0);
    match result {
        Ok(value) => println!("결과: {}", value), // 성공 시 출력
        Err(error) => println!("오류: {}", error), // 에러 발생 시 출력
    }
}
```

**코드 분석:**
- **`Result<i32, String>`**: 나눗셈 결과를 반환할 때 성공 시 `Ok(결과)`, 에러 발생 시 `Err(오류 메시지)`를 반환합니다.
- **`match` 문**: `Result` 타입의 결과에 따라 성공 케이스와 에러 케이스를 구분하여 처리합니다.

##### **코드 예제 4: 복잡한 에러 핸들링**

```rust
use std::fs::File;
use std::io::{self, Read};

fn read_file_contents(path: &str) -> Result<String, io::Error> {
    // 파일 읽기 함수
    let mut file = File::open(path)?; // 에러 발생 시 즉시 반환
    let mut contents = String::new();
    file.read_to_string(&mut contents)?; // 에러 처리
    Ok(contents) // 성공 시 내용 반환
}

fn main() {
    let path = "nonexistent_file.txt";
    match read_file_contents(path) {
        Ok(contents) => println!("파일 내용: {}", contents), // 성공 시 출력
        Err(error) => println!("파일 읽기 오류: {}", error), // 에러 처리
    }
}
```

**코드 분석:**
- **`File::open` 및 `read_to_string`**: 파일을 열고 내용을 읽는 과정에서 발생할 수 있는 에러를 `?` 연산자로 간결하게 처리합니다.
- **`match` 문**: 에러가 발생하면 즉시 오류 메시지를 출력하고, 성공 시 파일 내용을 출력합니다.

#### 💡 초보자 폭풍 질문!

**질문 예시:**
- **Q:** `Option`과 `Result`의 주요 차이점은 무엇인가요?
- **A:** `Option`은 주로 값의 존재 여부를 나타내는 데 사용되며, `None` 또는 `Some`을 통해 값의 유무를 표현합니다. 반면 `Result`는 주로 작업의 성공 여부를 나타내며, `Ok`로 성공한 결과와 `Err`로 에러 상황을 구분합니다. `Option`은 값이 있을 수도, 없을 수도 있는 상황에 적합하고, `Result`는 연산의 결과가 성공적이거나 실패적인 경우에 사용됩니다.

#### 🚨 실무주의보

- **주의사항**: 실제 프로젝트에서는 에러 처리를 간결하게 유지하면서도 명확하게 해야 합니다. `?` 연산자는 편리하지만, 너무 많은 중첩된 에러 처리는 코드의 가독성을 해칠 수 있으니 주의하세요!

#### 마무리

이렇게 `Result`와 `Option`을 통해 Rust에서 에러 핸들링을 효과적으로 관리할 수 있다는 걸 배웠어요. 이제 코드에서 에러가 발생했을 때도 침착하게 대응할 수 있을 거예요. **진짜 신기하죠?** 앞으로의 프로젝트에서 이 기술을 활용해보세요. 더 견고하고 안전한 코드를 작성할 수 있을 거예요! 

함께 성장해 나가는 여정, 계속 지켜봐주세요! 🚀

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
