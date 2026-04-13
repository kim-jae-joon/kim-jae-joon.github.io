---
layout: single
title: "Rust 기초: 제어 흐름: if와 match"
date: 2026-07-18 01:29:08
categories: [Rust]
---

# 5강: Rust 기초: 제어 흐름 - `if`와 `match` 마법을 마스터하기!

안녕하세요, 주니어 개발자 여러분! Rust의 세계로 또 한 발짝 들어온 걸 환영합니다. 오늘은 프로그래밍의 핵심 중 하나인 **제어 흐름**을 다루는 시간이에요. 특히 `if`와 `match`에 대해 깊이 파헤쳐볼게요. 이걸 잘 이해하면, 코드가 마치 당신의 지시에 따라 똑똑하게 움직이는 마법처럼 느껴질 거예요!

## 🤔 왜 제어 흐름이 중요할까요?

프로그래밍은 결국 "어떤 상황에 따라 다른 행동을 취하는" 거죠. 제어 흐름은 바로 그 '상황 판단'과 '행동 선택'의 마법을 담당합니다. 예를 들어, 사용자가 로그인에 성공했는지 실패했는지에 따라 다른 메시지를 보여주는 것이 바로 제어 흐름의 힘이랍니다!

## 🌟 `if` 문: 조건에 따른 선택의 마법사

### 기본 구조
`if` 문은 가장 기본적인 조건문이에요. 간단하면서도 강력한 힘을 지니고 있죠.

```rust
fn check_age(age: i32) {
    if age >= 18 {
        println!("성인이시네요! 자유롭게 즐기세요!");
    } else {
        println!("청소년이시군요! 더 성장해보세요!");
    }
}
```

#### 코드 분석
1. **`if age >= 18`**: 조건을 체크합니다. 나이가 18세 이상인지 확인해요.
2. **`println!("성인이시네요! 자유롭게 즐기세요!");`**: 조건이 참이면 이 코드가 실행됩니다.
3. **`else`**: 만약 조건이 거짓이면 else 블록이 실행됩니다.

### `if-else if`: 다중 조건 체크
더 복잡한 상황을 다루려면 `else if`를 사용할 수 있어요.

```rust
fn determine_status(score: i32) {
    if score >= 90 {
        println!("당신은 우수생입니다!");
    } else if score >= 70 {
        println!("좋은 성적이네요!");
    } else if score >= 50 {
        println!("평균 수준입니다.");
    } else {
        println!("노력이 필요해요!");
    }
}
```

#### 코드 분석
- **`if score >= 90`**: 첫 번째 조건 체크. 점수가 90점 이상이면 첫 번째 메시지 출력.
- **`else if score >= 70`**: 점수가 90점 미만이지만 70점 이상이면 두 번째 메시지 출력.
- **`else if score >= 50`**: 계속해서 조건을 체크하며 적절한 메시지를 출력합니다.
- **`else`**: 모든 조건이 거짓이면 마지막 메시지 출력.

### 💡 초보자 폭풍 질문!
**Q: `else if` 대신 `elif`를 쓸 수 있나요?**
**A**: Rust에서는 `elif` 대신 `else if`를 사용합니다. 다른 언어에서는 `elif`를 쓰는 경우가 많지만, Rust는 일관성 있게 `else if`를 채택하고 있어요. 헷갈리지 않게 기억해두세요!

## 🎭 `match` 문: 다양한 경우의 수를 한 번에 처리하기

`match` 문은 `if-else`보다 더 강력하고, 특히 열거형(enum)과 함께 쓰일 때 빛을 발합니다. 여러 가능한 경우를 깔끔하게 처리할 수 있어요.

### 기본 사용법
```rust
enum DayOfWeek {
    Monday,
    Tuesday,
    Wednesday,
    Thursday,
    Friday,
    Saturday,
    Sunday,
}

fn day_activity(day: DayOfWeek) {
    match day {
        DayOfWeek::Monday => println!("월요병 퇴치!"),
        DayOfWeek::Tuesday => println!("이번 주도 힘내자!"),
        DayOfWeek::Wednesday => println!("중간 점검 시간!"),
        DayOfWeek::Thursday => println!("주말이 가까워져 온다!"),
        DayOfWeek::Friday => println!("불금, 즐겁게 보내세요!"),
        DayOfWeek::Saturday => println!("여유로운 주말 시작!"),
        DayOfWeek::Sunday => println!("다음 주를 위한 휴식!"),
    }
}
```

#### 코드 분석
- **`enum DayOfWeek`**: 요일을 나타내는 열거형 정의.
- **`match day`**: `day` 변수의 값에 따라 여러 경우를 처리합니다.
- **각 패턴 매칭**: 각 `DayOfWeek` 값에 따라 다른 동작을 수행합니다.

### 🚨 실무주의보
**`match`는 오류 처리에도 활용됩니다!** 예를 들어, `Result` 타입을 처리할 때 `match`는 매우 유용해요.

```rust
fn process_file(path: &str) -> Result<String, std::io::Error> {
    let contents = std::fs::read_to_string(path)?;
    match contents.as_str() {
        "success" => Ok("파일 읽기 성공!".to_string()),
        _ => Err(std::io::Error::new(std::io::ErrorKind::InvalidData, "예상치 못한 내용")),
    }
}
```

#### 코드 분석
- **`std::fs::read_to_string`**: 파일 내용을 읽습니다.
- **`match contents.as_str()`**: 파일 내용에 따라 다른 결과를 반환합니다.
- **`Ok`와 `Err`**: 성공/실패를 명확하게 구분합니다.

### 추가 예시: `match`와 튜플 활용
`match`는 튜플과 같은 복합 타입에도 적용 가능해요.

```rust
fn analyze_score(score: (i32, i32)) {
    match score {
        (80, _) => println!("첫 번째 과목은 잘 봤어요!"),
        (_, 80) => println!("두 번째 과목이 돋보였네요!"),
        _ => println!("두 과목 모두 균형 잡힌 성적이네요!"),
    }
}
```

#### 코드 분석
- **`(80, _)`**: 첫 번째 요소가 80점 이상인 경우.
- **`(_, 80)`**: 두 번째 요소가 80점 이상인 경우.
- **`_`**: 모든 다른 경우를 포괄합니다.

## 🎉 마무리: 제어 흐름 마스터하기

오늘 배운 `if`와 `match`는 프로그램의 두뇌 역할을 해요. 다양한 상황에 따라 적절한 동작을 선택하는 능력을 갖추게 되었으니, 이제 코드가 더욱 스마트하고 유연해질 거예요!

**기억하세요:**
- `if`는 간단한 조건 분기에 최적화되어 있어요.
- `match`는 복잡한 경우의 수를 깔끔하게 처리하는 데 최고입니다.

이제 당신의 코드는 더욱 재미있고 효율적으로 진화할 준비가 되었어요! 계속해서 실습하고 실험해보세요. 그럼 곧 전문가의 길에 한 발짝 더 다가갈 수 있을 거예요!

그럼 다음 강의에서 또 만나요! 🚀

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
