---
layout: single
title: "Rust C 언어 실전 프로젝트: 간단한 데이터베이스 관리자"
date: 2026-06-25 19:26:21
categories: [Rust C 언어]
---

## 🚀 26강: Rust C 언어 실전 프로젝트: 간단한 데이터베이스 관리자 만들기

안녕하세요, 여러분의 친근한 코드 친구 **코드 멘토**입니다! 오늘은 Rust 언어를 이용해 정말 멋진 **간단한 데이터베이스 관리자**를 만들어 보는 시간을 가져볼게요. 마치 레고 블록으로 멋진 성을 쌓듯이, 하나씩 차근차근 쌓아가다 보면 어느새 당신도 데이터베이스의 왕이 될 수 있답니다! 🏰✨

### 🤔 데이터베이스, 그게 뭐길래?

**데이터베이스**는 쉽게 말해 정보의 저장고이자 관리자죠. 학교 도서관에서 책을 분류하고 찾는 것처럼, 데이터베이스는 데이터를 효율적으로 저장하고 검색할 수 있게 도와줍니다. 우리가 만드는 간단한 관리자는 사용자 이름과 비밀번호를 저장하고 확인하는 기능을 갖출 거예요. 

### 🛠️ 프로젝트 목표 설정

우리가 만들어볼 **"SimpleDB"** 프로젝트의 주요 목표는 다음과 같습니다:

- **사용자 정보 저장**: 이름과 비밀번호를 파일에 저장합니다.
- **비밀번호 확인**: 사용자 이름을 입력하면 비밀번호가 일치하는지 확인합니다.
- **간단한 인터페이스**: 터미널에서 쉽게 상호작용할 수 있는 인터페이스 제공

### 🧑‍💻 코드 탐험: 상세 가이드

#### 1. 프로젝트 구조 설정

먼저 프로젝트의 기본 구조를 잡아봅시다. `SimpleDB` 폴더를 생성하고 아래 파일들을 만들어 보세요:

```bash
SimpleDB/
│
├── main.rs          # 메인 프로그램 파일
├── user_manager.rs  # 사용자 관리 로직 파일
└── data.rs          # 데이터 저장 로직 파일
```

#### 2. `data.rs`: 데이터 저장 로직

데이터 저장을 위한 기본 파일을 만들어 봅시다. 여기서는 간단하게 `.txt` 파일을 사용할게요.

**data.rs 코드 예제:**

```rust
// data.rs 파일
use std::fs::File;
use std::io::{self, Write};

pub fn save_user_data(username: &str, password: &str) -> io::Result<()> {
    // 사용자 데이터를 저장할 파일 열기
    let file = File::create("users.txt")?;
    
    // 사용자 데이터를 파일에 쓰기
    writeln!(file, "{}:{}", username, password)?;
    Ok(())
}

pub fn load_user_data() -> io::Result<Vec<(String, String)>> {
    // 사용자 데이터 파일 읽기
    let file = File::open("users.txt")?;
    let mut lines = io::BufReader::new(file).lines();
    let mut users = Vec::new();
    
    // 각 줄을 읽어들여 사용자 정보로 변환
    for line in lines {
        let line = line?;
        let parts: Vec<&str> = line.split(':').collect();
        if parts.len() == 2 {
            let username = parts[0].to_string();
            let password = parts[1].to_string();
            users.push((username, password));
        }
    }
    Ok(users)
}
```

**코드 해설:**

- **`save_user_data` 함수**: 사용자 이름과 비밀번호를 `users.txt` 파일에 저장합니다. `File::create`로 파일을 생성하고 `writeln!`로 데이터를 쓰죠.
- **`load_user_data` 함수**: `users.txt` 파일을 열어 각 줄을 읽어들여 사용자 이름과 비밀번호 쌍을 벡터에 저장합니다. `io::BufReader`를 사용해 효율적으로 줄을 읽습니다.

#### 3. `user_manager.rs`: 사용자 인터페이스 로직

이제 사용자 인터페이스를 만들어 보겠습니다. 터미널에서 사용자 입력을 받아 처리하는 코드를 작성합니다.

**user_manager.rs 코드 예제:**

```rust
// user_manager.rs 파일
use std::io::{self, Write};
use crate::data::{save_user_data, load_user_data};

fn main() {
    loop {
        println!("👨‍🏫 SimpleDB 관리자 모드에 오신 것을 환영합니다!");
        println!("1. 사용자 등록");
        println!("2. 비밀번호 확인");
        println!("3. 종료");
        println!("선택: ");

        let mut choice = String::new();
        io::stdin().read_line(&mut choice).expect("입력 오류");
        let choice: u32 = choice.trim().parse().expect("숫자 입력 필요");

        match choice {
            1 => {
                // 사용자 등록
                println!("이름을 입력하세요: ");
                let mut name = String::new();
                io::stdin().read_line(&mut name).expect("입력 오류");
                let name = name.trim();

                println!("비밀번호를 입력하세요: ");
                let mut password = String::new();
                io::stdin().read_line(&mut password).expect("입력 오류");
                let password = password.trim();

                if save_user_data(name, password).is_ok() {
                    println!("사용자 등록 완료!");
                } else {
                    println!("등록에 실패했습니다. 다시 시도해주세요.");
                }
            }
            2 => {
                // 비밀번호 확인
                println!("사용자 이름을 입력하세요: ");
                let mut userName = String::new();
                io::stdin().read_line(&mut userName).expect("입력 오류");
                let userName = userName.trim();

                let users = load_user_data().expect("데이터 로드 실패");
                if let Some((username, password)) = users.iter().find(|&(n, _)| n == userName) {
                    println!("비밀번호 확인: {}\n정확합니다!", password);
                } else {
                    println!("해당 사용자가 없습니다.");
                }
            }
            3 => {
                println!("감사합니다! 👋 SimpleDB 관리자 모드를 종료합니다.");
                break;
            }
            _ => println!("잘못된 선택입니다. 다시 선택해주세요."),
        }
    }
}
```

**코드 해설:**

- **메인 루프**: 사용자에게 메뉴를 보여주고 입력을 받습니다. `loop`을 이용해 반복적으로 동작합니다.
- **사용자 등록**: 이름과 비밀번호를 입력받아 `save_user_data` 함수로 저장합니다.
- **비밀번호 확인**: 이름을 입력받아 `load_user_data`로 데이터를 읽고 일치 여부를 확인합니다.
- **입력 처리**: `io::stdin().read_line`을 사용해 사용자 입력을 받고, `expect`로 오류 처리를 합니다.

### 💡 초보자 폭풍 질문!

**질문 1:** `File::create` 함수에서 오류가 발생하면 어떻게 해야 하나요?
- **답변:** `File::create`는 파일이 이미 존재하면 오류를 반환합니다. 이를 처리하기 위해 `expect("파일 생성 오류")`를 사용해 간단하게 오류 메시지를 출력할 수 있습니다. 하지만 더 안전하게 처리하려면 `match` 문을 사용해 오류 코드를 체크하고 적절한 메시지를 보여주는 것이 좋습니다.

**질문 2:** 왜 `expect`를 사용할 때 오류 메시지를 넣는 건가요?
- **답변:** `expect`는 오류가 발생했을 때 간단한 메시지를 출력하고 프로그램을 종료합니다. 이는 디버깅 시 문제의 원인을 빠르게 파악할 수 있게 도와줍니다. 실제 프로덕션 코드에서는 더 세밀한 오류 처리를 권장합니다.

### 🚨 실무주의보

**주의사항:** 이 프로젝트는 **교육적 목적**으로 간단하게 구현한 것입니다. 실제 데이터베이스 시스템은 훨씬 복잡하며 보안 측면에서도 더 많은 고려사항이 필요합니다. 예를 들어, 암호화된 비밀번호 저장, 트랜잭션 처리, 확장성 등 다양한 요소를 고려해야 합니다. 실무에서는 PostgreSQL이나 MySQL과 같은 데이터베이스 시스템을 활용하는 것이 훨씬 안전하고 효율적입니다.

### 마무리

오늘 배운 내용을 바탕으로 **SimpleDB**를 직접 만들어 보세요! 조금씩 코드를 쌓아가다 보면 데이터베이스 관리의 기본 원리를 체감할 수 있을 거예요. 🤝

다음 강의에서도 더욱 멋진 프로젝트로 찾아뵙겠습니다! 지금까지 **코드 멘토**였습니다. **함께 성장해요!** 🚀💪

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
