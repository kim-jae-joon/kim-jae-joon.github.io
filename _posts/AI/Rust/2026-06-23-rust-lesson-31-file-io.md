---
layout: single
title: "Rust 응용: 파일 I/O 및 시스템 인터페이스"
date: 2026-06-23 02:54:53
categories: [Rust]
---

안녕하세요! 저는 여러분의 코딩 길잡이, 재준봇입니다.

자, 여러분! 지금까지 우리는 Rust라는 아주 까다롭지만 매력적인 언어의 문법을 하나하나 정복해 왔습니다. 그런데 말입니다. 문법만 공부하는 건 마치 요리책만 읽고 실제로 요리는 한 번도 안 해본 것과 같아요. 이제는 진짜로 '뭔가'를 만들어볼 때가 됐습니다.

오늘 배울 내용은 바로 '파일 I/O 및 시스템 인터페이스'입니다. 쉽게 말해서 우리 프로그램이 컴퓨터의 하드디스크에 있는 파일을 읽고 쓰고, 운영체제(OS)한테 "야, 이것 좀 해줘!"라고 명령을 내리는 방법입니다.

이거 모르면 그냥 메모리 안에서만 놀다가 끝나는 '방구석 프로그램'이 됩니다. 진짜 세상 밖으로 나가는 프로그램을 만들고 싶다면 오늘 강의, 눈 크게 뜨고 따라오세요!

# 31강: Rust 응용 - 파일 I/O 및 시스템 인터페이스

## 1. 파일 읽기: 컴퓨터의 기억 저장소를 뒤져라!

파일을 읽는다는 건, 쉽게 비유하자면 도서관에서 책을 꺼내 읽는 것과 같습니다. 그런데 책의 양에 따라 읽는 방법이 다르겠죠? 쪽지 한 장이면 그냥 슥 읽으면 되지만, 백과사전이면 한 장씩 넘기며 읽어야 합니다. Rust도 마찬가지입니다.

### 방법 1: 한 번에 다 읽기 (간편식 스타일)
내용이 짧은 파일이라면 굳이 복잡하게 읽을 필요가 없습니다. 그냥 통째로 메모리에 올려버리는 방법입니다.

```rust
use std::fs; // 파일 시스템 기능을 가져옵니다.

fn main() {
    // read_to_string 함수를 사용하여 파일 내용을 통째로 문자열로 읽어옵니다.
    // 여기서 unwrap()은 "에러 나면 그냥 프로그램 종료해!"라는 뜻입니다.
    let content = fs::read_to_string("hello.txt").expect("파일을 찾을 수 없거나 읽기에 실패했습니다.");

    println!("파일 내용 출력:\n{}", content);
}
```
- `fs::read_to_string("hello.txt")`: 지정한 경로의 파일을 읽어 문자열로 반환합니다.
- `.expect("...")`: Rust는 안전을 매우 중요하게 생각합니다. 파일이 없을 수도 있잖아요? 그래서 결과가 성공인지 실패인지 확인하는 과정이 필수입니다.

### 방법 2: 파일 객체를 만들어 직접 읽기 (정석 스타일)
파일이 조금 크거나, 세밀하게 제어하고 싶을 때 사용하는 방법입니다.

```rust
use std::fs::File; // 파일 객체를 다루기 위한 모듈
use std::io::{self, Read}; // 입출력을 위한 모듈

fn main() -> io::Result<()> {
    // 1. 파일을 엽니다.
    let mut file = File::open("hello.txt")?; 
    
    // 2. 내용을 담을 빈 바구니(버퍼)를 만듭니다.
    let mut content = String::new();
    
    // 3. 파일의 내용을 바구니에 쏟아붓습니다.
    file.read_to_string(&mut content)?;

    println!("정석대로 읽은 내용:\n{}", content);
    
    Ok(()) // 모든 과정이 성공했음을 알립니다.
}
```
- `File::open("hello.txt")?`: 파일을 엽니다. 여기서 `?` 연산자는 "에러가 나면 여기서 즉시 반환해!"라는 뜻으로, `unwrap`보다 훨씬 세련된 방식입니다.
- `String::new()`: 읽어온 내용을 저장할 빈 공간을 먼저 만들어야 합니다.
- `file.read_to_string(&mut content)`: 파일의 데이터를 가변 참조자(`&mut`)를 통해 문자열에 직접 채워 넣습니다.

### 방법 3: 버퍼를 이용해 한 줄씩 읽기 (효율성 끝판왕 스타일)
파일이 기가바이트 단위로 크다면? 통째로 읽다가 메모리가 터져버리겠죠. 이때는 '버퍼'라는 중간 바구니를 이용해 조금씩 나누어 읽어야 합니다.

```rust
use std::fs::File;
use std::io::{self, BufRead}; // BufRead 트레이트를 가져와야 합니다.

fn main() -> io::Result<()> {
    let file = File::open("hello.txt")?;
    
    // BufReader는 파일을 한꺼번에 읽지 않고 조금씩 읽어 메모리 효율을 높입니다.
    let reader = io::BufReader::new(file);

    // lines() 메서드를 통해 한 줄씩 읽어오는 반복문을 실행합니다.
    for (index, line) in reader.lines().enumerate() {
        let line = line?; // 각 줄을 읽을 때 발생할 수 있는 에러 처리
        println!("{}: {}", index + 1, line);
    }

    Ok(())
}
```
- `io::BufReader::new(file)`: 파일을 감싸서 버퍼링 기능을 추가합니다. 마치 빨대를 꽂아 조금씩 마시는 것과 같습니다.
- `reader.lines()`: 파일을 줄 단위로 쪼개서 주는 반복자(Iterator)를 반환합니다.
- `.enumerate()`: 몇 번째 줄인지 번호를 매기기 위해 사용했습니다.

> **초보자 폭풍 질문!**
> **Q: `unwrap()`이랑 `expect()`랑 `?` 연산자의 차이가 뭔가요? 다 그냥 에러 처리 하는 거 아닌가요?**
> **A: 재준봇이 답해드립니다!** 
> - `unwrap()`: "에러 나면 그냥 죽어라!" (가장 무책임한 방법, 테스트용으로만 쓰세요)
> - `expect("메시지")`: "에러 나면 이 메시지를 남기고 죽어라!" (어디서 죽었는지 알 수 있어 조금 더 친절합니다)
> - `?`: "에러가 났네? 내가 처리 못 하니까 나를 호출한 윗사람(함수)한테 이 에러를 던질게!" (실무에서 가장 많이 쓰는 전문적인 방식입니다)

---

## 2. 파일 쓰기: 내 흔적을 하드디스크에 남겨라!

읽기만 해서는 안 되죠. 우리가 만든 데이터나 로그를 파일로 저장해야 합니다. 쓰는 방법 역시 상황에 따라 3가지로 나뉩니다.

### 방법 1: 한 번에 다 쓰기 (퀵 샷 스타일)
기존 내용을 다 지워버리고 새로 쓰거나, 아주 간단하게 파일 하나를 만들 때 씁니다.

```rust
use std::fs;

fn main() {
    let data = "안녕하세요, 재준봇의 Rust 강의입니다!\n정말 쉽지 않나요?";
    
    // write 함수는 파일이 없으면 만들고, 있으면 덮어씁니다.
    fs::write("output.txt", data).expect("파일 쓰기에 실패했습니다.");
    
    println!("파일 쓰기 완료!");
}
```
- `fs::write("경로", "내용")`: 이 한 줄로 파일 생성과 쓰기가 동시에 끝납니다. 정말 편하죠? 하지만 파일 내용이 많다면 메모리 낭비가 심해집니다.

### 방법 2: 옵션을 정해서 쓰기 (디테일 스타일)
"기존 내용은 그대로 두고 끝에 덧붙이고 싶어!" 혹은 "파일이 없을 때만 만들고 싶어!" 같은 세밀한 조작이 필요할 때 사용합니다.

```rust
use std::fs::OpenOptions; // 파일 열기 옵션을 설정하는 구조체
use std::io::Write; // Write 트레이트를 가져와야 write_all을 쓸 수 있습니다.

fn main() {
    // OpenOptions를 사용하여 세부 설정
    let mut file = OpenOptions::new()
        .append(true)       // 기존 내용 뒤에 추가 (Append)
        .create(true)       // 파일이 없으면 생성 (Create)
        .open("output.txt")
        .expect("파일을 열 수 없습니다.");

    let log_entry = "\n새로운 로그 기록: 재준봇이 다녀감!";
    
    // write_all을 통해 바이트 슬라이스로 데이터를 씁니다.
    file.write_all(log_entry.as_bytes()).expect("쓰기 작업 중 오류 발생");
    
    println!("로그 추가 완료!");
}
```
- `OpenOptions::new()`: 파일을 어떻게 열지 결정하는 빌더 패턴입니다.
- `.append(true)`: 이게 핵심입니다! 이걸 안 하면 매번 파일 내용이 초기화됩니다.
- `.as_bytes()`: 파일에 직접 쓸 때는 문자열 그대로가 아니라 '바이트' 형태로 변환해서 전달해야 합니다. 컴퓨터는 결국 0과 1만 아니까요.

### 방법 3: 버퍼를 이용해 효율적으로 쓰기 (대량 생산 스타일)
매번 하드디스크에 접근해서 쓰는 건 매우 느린 작업입니다. 그래서 메모리에 어느 정도 모아뒀다가 한 번에 쏟아붓는 `BufWriter`를 사용합니다.

```rust
use std::fs::File;
use std::io::{BufWriter, Write};

fn main() -> std::io::Result<()> {
    let file = File::create("large_output.txt")?;
    let mut writer = BufWriter::new(file);

    for i in 1..=100 {
        let text = format!("이것은 {}번째 줄입니다.\n", i);
        writer.write_all(text.as_bytes())?;
    }
    
    // 중요: 버퍼에 남아있는 데이터를 완전히 파일에 기록하도록 강제합니다.
    writer.flush()?;

    println!("100줄의 데이터를 효율적으로 썼습니다!");
    Ok(())
}
```
- `BufWriter::new(file)`: 쓰기 전용 버퍼를 생성합니다.
- `writer.flush()`: 버퍼는 메모리에 데이터를 임시로 저장합니다. 프로그램이 끝나기 전에 `flush`를 호출해줘야 "남아있는 찌꺼기까지 다 써라!"라고 명령하는 꼴이 됩니다. 이거 빼먹으면 파일 끝부분이 잘릴 수 있어요!

---

## 3. 시스템 인터페이스: 운영체제와 대화하기

이제 파일 너머의 세상으로 가봅시다. 프로그램이 실행될 때 외부에서 값을 받거나, 다른 프로그램을 실행시키는 등의 작업입니다.

### 방법 1: 커맨드 라인 인자 받기 (외부 입력 스타일)
`cargo run -- 이름` 이렇게 실행했을 때 '이름'이라는 값을 가져오는 방법입니다.

```rust
use std::env; // 환경 변수 및 인자 관련 모듈

fn main() {
    // args()는 프로그램에 전달된 인자들의 반복자를 반환합니다.
    let args: Vec<String> = env::args().collect();

    if args.len() < 2 {
        println!("사용법: cargo run -- [이름]");
    } else {
        println!("안녕하세요, {}님! 재준봇의 세계에 오신 걸 환영합니다!", args[1]);
    }
}
```
- `env::args()`: 실행 시 입력한 인자들을 가져옵니다.
- `.collect()`: 반복자를 `Vec` (벡터) 형태로 변환하여 인덱스로 접근할 수 있게 만듭니다.
- `args[0]`은 항상 실행 파일의 경로이므로, 실제 사용자가 넣은 첫 번째 값은 `args[1]`부터 시작합니다.

### 방법 2: 환경 변수 읽기 (비밀번호 관리 스타일)
API 키나 DB 비밀번호 같은 민감한 정보는 코드에 직접 적으면 절대 안 됩니다! OS의 환경 변수에 넣어두고 읽어와야 합니다.

```rust
use std::env;

fn main() {
    // "MY_API_KEY"라는 이름의 환경 변수를 읽어옵니다.
    match env::var("MY_API_KEY") {
        Ok(val) => println!("API 키를 찾았습니다: {}", val),
        Err(e) => println!("에러 발생: {}. 환경 변수를 설정해 주세요!", e),
    }
}
```
- `env::var("변수명")`: OS에 설정된 환경 변수 값을 가져옵니다.
- `match` 문: 환경 변수가 없을 가능성이 매우 높기 때문에 `Ok`와 `Err`로 나누어 처리하는 것이 Rust다운 방식입니다.

### 방법 3: 외부 명령어 실행하기 (명령 하달 스타일)
Rust 프로그램 안에서 `ls`나 `dir` 같은 시스템 명령어를 실행하고 그 결과를 가져올 수 있습니다.

```rust
use std::process::Command; // 프로세스 제어 모듈

fn main() {
    // 'echo' 명령어를 실행하고 "Hello from System!"이라는 인자를 전달합니다.
    let output = Command::new("echo")
        .arg("Hello from System!")
        .output()
        .expect("명령어 실행에 실패했습니다.");

    if output.status.success() {
        let s = String::from_utf8_lossy(&output.stdout);
        println!("시스템 출력 결과:\n{}", s);
    } else {
        println!("명령어 실행 중 오류가 발생했습니다.");
    }
}
```
- `Command::new("명령어")`: 실행할 프로그램 이름을 지정합니다.
- `.arg("인자")`: 명령어 뒤에 붙을 옵션이나 값을 추가합니다.
- `.output()`: 명령어를 실행하고 그 결과(표준 출력, 표준 에러 등)를 기다렸다가 가져옵니다.
- `String::from_utf8_lossy()`: 시스템에서 나온 바이트 데이터를 우리가 읽을 수 있는 문자열로 변환합니다. (약간 깨진 글자가 있어도 최대한 살려서 변환해 줍니다)

> **실무주의보!**
> **주의: 외부 명령어를 실행할 때 사용자 입력을 그대로 `Command::new`에 넣지 마세요!**
> **이유:** 이른바 '커맨드 인젝션(Command Injection)'이라는 심각한 보안 취약점이 발생합니다. 예를 들어 사용자가 입력창에 `; rm -rf /` 같은 명령어를 넣으면 서버의 모든 파일이 날아갈 수 있습니다. 반드시 입력값을 검증하거나, 허용된 명령어 리스트(White List)만 사용하세요!

---

## 마무리하며

자, 오늘 우리는 Rust를 이용해 파일을 읽고 쓰는 세 가지 방법, 그리고 시스템 인터페이스를 다루는 세 가지 방법까지 총 6가지의 핵심 기법을 배웠습니다.

- **단순한 작업** $\rightarrow$ `fs::read_to_string`, `fs::write`
- **정밀한 제어** $\rightarrow$ `File::open`, `OpenOptions`
- **대용량/효율적 작업** $\rightarrow$ `BufReader`, `BufWriter`
- **시스템 상호작용** $\rightarrow$ `env::args`, `env::var`, `Command`

이 내용들만 완벽하게 이해하고 활용할 수 있다면, 여러분은 이제 단순한 문법 공부자를 넘어 진짜 '프로그램'을 만드는 개발자의 길로 들어선 것입니다. 진짜 신기하죠? Rust가 이렇게 강력한 도구들이 많다는 것이!

오늘 배운 내용을 직접 코드로 구현해 보세요. 직접 파일을 만들고, 이름을 입력받아 파일에 기록하고, 다시 그 파일을 읽어 출력하는 작은 프로그램을 만들어 보는 것을 강력하게 추천합니다.

그럼 저는 다음 강의에서 더 유머러스하고 찰떡같은 비유로 돌아오겠습니다. 지금까지 재준봇이었습니다! 열공하세요!

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
