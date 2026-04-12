---
layout: single
title: "프로젝트 기반 학습: 간단한 게임 개발"
date: 2026-06-16 19:12:39
categories: [Rust C 언어]
---

### 35강: 프로젝트 기반 학습: 간단한 텍스트 어드벤처 게임 개발하기

안녕하세요, 젊은 개발자 여러분! 오늘은 여러분의 코딩 실력을 한 단계 업그레이드시켜줄 특별한 프로젝트로 **간단한 텍스트 어드벤처 게임**을 만들어 볼 거예요. 이 강의는 여러분이 단순히 코드를 복사 붙이는 것 이상으로, 게임 개발의 기본 원리와 Rust 언어의 매력을 깊이 이해하는 데 도움이 될 거예요. **"게임 개발"이라니, 좀 어려울 것 같아도 걱정 마세요!** 우리는 함께 이 흥미진진한 여정을 헤쳐나갈 거예요.

#### 🚀 게임 개발의 시작: 아이디어와 계획

**텍스트 어드벤처 게임**이란? 플레이어가 텍스트 기반의 대화나 명령어로 게임 세계를 탐험하는 게임이에요. 예를 들어, *“go north”* 라고 입력하면 캐릭터가 북쪽으로 이동한다고 인식하게 만드는 거죠.

**프로젝트 계획:**
- **세계 맵**: 간단한 맵 구조를 정의합니다.
- **캐릭터 이동**: 방향키 입력에 따른 이동 로직 구현.
- **대화 시스템**: 기본적인 대화 트리 구현.

#### 🧑‍💻 코드로 시작하기

##### 1. 기본 프로젝트 구조 설정

먼저, 프로젝트의 기본 구조를 설정해봅시다. `src/main.rs` 파일을 만들어 봅시다.

```rust
// src/main.rs

use std::io;

fn main() {
    println!("Welcome to the Adventure World!");
    start_game();
}

fn start_game() {
    let mut input = String::new();
    println!("Where would you like to go? (north, south, east, west): ");
    
    // 사용자 입력 받기
    io::stdin().read_line(&mut input).expect("Failed to read line");
    let input = input.trim(); // 입력의 공백 제거

    handle_direction(input);
}

fn handle_direction(direction: &str) {
    match direction {
        "north" => println!("You move north into a mysterious forest!"),
        "south" => println!("You head south towards a bustling village."),
        "east" => println!("You venture east to find an ancient castle."),
        "west" => println!("You walk west, discovering a hidden cave."),
        _ => println!("Invalid direction! Try again."),
    }
    // 게임 재시작 옵션 추가
    println!("Do you want to go another direction? (yes/no)");
    let mut retry = String::new();
    io::stdin().read_line(&mut retry).expect("Failed to read retry input");
    if retry.trim().to_lowercase() == "yes" {
        start_game(); // 게임 재시작
    } else {
        println!("Thanks for playing! Come back soon!");
    }
}
```

**해설:**
- **`main()` 함수**: 게임의 시작점입니다. 환영 메시지를 출력하고 `start_game()` 함수를 호출합니다.
- **`start_game()` 함수**: 사용자로부터 방향 입력을 받습니다. `io::stdin().read_line()`을 사용해 입력을 읽고, 입력을 처리하는 `handle_direction()` 함수로 넘깁니다.
- **`handle_direction()` 함수**: 입력된 방향에 따라 다양한 반응을 출력합니다. `match` 표현식을 활용해 각 방향에 대한 시나리오를 구현했습니다. 사용자가 다시 방향을 입력할지 묻고, `yes`일 경우 게임을 재시작합니다.

##### 2. 다양한 이동 방식 구현하기

게임의 재미를 더하기 위해 **반복문**을 활용해 보겠습니다. 여러 번의 시도를 통해 플레이어가 방향을 정확히 입력할 수 있도록 합니다.

```rust
fn move_around() {
    let mut directions = ["north", "south", "east", "west"];
    let mut attempts = 0;

    loop {
        println!("Try one of these directions: north, south, east, west");
        let mut input = String::new();
        io::stdin().read_line(&mut input).expect("Failed to read line");
        let input = input.trim();
        attempts += 1;

        // 입력 검증
        if directions.contains(&input) {
            println!("You moved successfully! Attempts: {}/3", attempts);
            break; // 성공 시 루프 종료
        } else {
            println!("Oops! Try again. Attempts left: {}/3", attempts);
            if attempts >= 3 {
                println!("Game Over! Better luck next time.");
                break; // 시도 횟수 초과 시 종료
            }
        }
    }
}
```

**해설:**
- **`move_around()` 함수**: `loop` 구조를 사용해 최대 3번까지 방향 입력을 반복적으로 받습니다. `contains()` 메소드로 입력이 유효한지 확인하고, 시도 횟수를 카운트합니다.
- **반복 구조의 장점**: 사용자에게 충분한 기회를 제공하고 게임의 재미를 높입니다.

##### 3. 대화 시스템 구현하기

게임에 대화 요소를 추가해 더욱 풍성하게 만들어 봅시다.

```rust
fn talk_to_npc() {
    let npc_dialogues = vec![
        ("greet", "Hello there! How can I assist you today?"),
        ("bye", "Goodbye! Have a great day!"),
        ("help", "Sure, I can help with basic tasks."),
    ];

    println!("Talk to the NPC:");
    loop {
        println!("Type 'greet', 'bye', or 'help': ");
        let mut input = String::new();
        io::stdin().read_line(&mut input).expect("Failed to read line");
        let input = input.trim().to_lowercase();

        if let Some((key, message)) = npc_dialogues.iter().find(|&&(k, _)| k == input.as_str()) {
            println!("{}", message);
            break; // 대화 완료 후 루프 종료
        } else {
            println!("Sorry, I didn't understand that. Try again.");
        }
    }
}
```

**해설:**
- **`talk_to_npc()` 함수**: `vec![]`로 NPC 대화 목록을 정의하고, 사용자 입력에 따라 적절한 반응을 출력합니다.
- **`if let` 구조**: 간결하게 일치하는 대화 키를 찾고 출력합니다. 일치하지 않으면 다시 입력을 요구합니다.

#### 🎯 핵심 개념 복습 및 실무 조언

**핵심 개념:**
- **반복문 (`loop`, `for`, `while`)**: 사용자 입력을 반복적으로 처리합니다.
- **조건문 (`match`, `if-else`)**: 다양한 입력에 따른 동작을 결정합니다.
- **함수 분리**: 코드의 가독성과 유지보수를 위해 기능별로 함수를 나눕니다.

**🚨 실무주의보**:
- **에러 처리**: 실제 프로젝트에서는 사용자 입력 오류나 시스템 에러에 대비한 에러 처리가 필수적입니다. 예를 들어, `expect("Failed to read line")` 대신 `Result` 타입을 사용해 안전하게 처리할 수 있습니다.
- **확장성**: 초기 프로젝트는 간단하지만, 점차 복잡한 맵 구조나 다양한 캐릭터 상호작용을 추가할 수 있도록 설계하세요.

**💡 초보자 폭풍 질문!**
- **Q**: 이 게임을 더 복잡하게 만들려면 어떤 기능을 추가할 수 있을까요?
  - **A**: 아이템 시스템, 전투 메커니즘, 더 깊은 스토리라인 등을 추가할 수 있습니다. 또한, 플레이어의 선택에 따라 게임의 결말이 달라지는 분기점을 구현해 볼 수도 있습니다.

이제 여러분의 차례입니다! 이 강의를 바탕으로 텍스트 어드벤처 게임을 시작해보세요. 어렵다고 느끼면 언제든지 질문하세요. 우리 모두 함께 성장하는 것이 목표니까요! 🚀🎮

행복 코딩 하세요!

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
