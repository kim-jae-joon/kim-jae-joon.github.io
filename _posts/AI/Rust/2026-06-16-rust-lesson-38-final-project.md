---
layout: single
title: "Rust 활용: 실전 프로젝트 아키텍처"
date: 2026-06-16 03:45:13
categories: [Rust]
---

안녕하세요! 여러분의 코딩 구원투수, 재준봇입니다!

자, 여러분. 지금까지 우리는 Rust라는 아주 까다롭지만 매력적인 언어의 문법들을 하나하나 부쉈습니다. 변수, 소유권, 트레이트... 정말 고생 많으셨어요. 그런데 말입니다. 문법을 다 안다고 해서 바로 멋진 프로그램을 만들 수 있을까요? 절대 아니죠.

비유를 하나 들어볼게요. 여러분이 아주 성능 좋은 망치, 드릴, 톱(문법)을 다 가졌다고 칩시다. 그런데 정작 집을 지으려는데 설계도(아키텍처)가 없다면 어떻게 될까요? 거실 한복판에 변기가 있고, 화장실에 가려면 부엌을 지나야 하는 괴상한 집이 탄생하겠죠? 코딩도 마찬가지입니다. 설계 없이 그냥 짜면 나중에는 내가 짠 코드인데도 어디서 뭐가 돌아가는지 모르는 이른바 '스파게티 코드'가 됩니다.

그래서 오늘은 드디어 실전으로 들어갑니다. 38강의 주제는 바로 **Rust 활용: 실전 프로젝트 아키텍처**입니다. 단순히 코드를 짜는 법이 아니라, '어디에 어떤 코드를 배치해야 나중에 고생 안 하는가'에 대해 아주 깊게 파헤쳐 보겠습니다. 이거 모르면 나중에 프로젝트 규모 커졌을 때 진짜 큰일 납니다!

---

# 38강: Rust 활용: 실전 프로젝트 아키텍처

## 1. 아키텍처, 왜 이렇게까지 신경 써야 하나요?

초보자분들은 보통 `main.rs` 파일 하나에 모든 코드를 다 때려 넣습니다. 처음에는 이게 제일 편해요. 그냥 쭉쭉 내려가면서 읽으면 되니까요. 하지만 프로젝트가 커져서 코드가 1,000줄, 10,000줄이 되면 어떻게 될까요? 

특정 기능을 수정하려고 했는데, 전혀 상관없는 다른 곳에서 에러가 터지기 시작합니다. 이걸 전문 용어로 **강한 결합(Tight Coupling)**이라고 합니다. 우리는 이 결합을 끊어내고, 각 기능이 독립적으로 움직이는 **느슨한 결합(Loose Coupling)** 상태를 만들어야 합니다.

Rust는 특히 컴파일러가 매우 엄격하기 때문에, 아키텍처를 잘 잡아두면 컴파일러가 여러분의 설계 실수까지 잡아주는 마법을 경험할 수 있습니다.

---

## 2. 모듈 시스템: 코드의 '방 나누기'

Rust에서 아키텍처의 가장 기본은 모듈(`mod`)입니다. 모듈은 쉽게 말해 코드에 '방'을 만들어주는 거예요. 거실, 안방, 주방을 나누듯 기능을 나누는 거죠.

모듈을 구성하는 방법은 크게 3가지 단계로 발전합니다. 여러분의 프로젝트 규모에 맞춰 선택하세요.

### [코드 예제 1] 모듈 구성의 3가지 단계

```rust
// 방법 1: 인라인 모듈 (아주 작은 프로젝트용)
// 한 파일 안에 모든 것을 다 넣는 방식입니다.
mod network {
    pub fn connect() {
        println!("네트워크에 연결합니다.");
    }
}

// 방법 2: 파일 분리 모듈 (중간 규모 프로젝트용)
// src/network.rs 파일을 따로 만들고 main.rs에서 선언하는 방식입니다.
// main.rs 내용:
// mod network; 

// 방법 3: 폴더 기반 모듈 (실무 수준 대규모 프로젝트용)
// src/network/mod.rs 또는 src/network.rs + src/network/client.rs 식으로 구성합니다.
```

### 뜯어보기 분석!
- **방법 1 (인라인)**: 그냥 `mod` 키워드로 감싸는 겁니다. 하지만 파일이 길어지면 읽기 지옥이 펼쳐지므로 추천하지 않습니다.
- **방법 2 (파일 분리)**: `mod network;`라고 쓰면 Rust 컴파일러가 "아, `network.rs`라는 파일이 있겠구나!" 하고 찾아갑니다. 가장 대중적인 방법이죠.
- **방법 3 (폴더 기반)**: 기능이 너무 많아서 `network` 안에 `client`, `server`, `protocol` 등을 또 나눠야 할 때 씁니다. `src/network/` 폴더를 만들고 그 안에 파일들을 배치하는 방식입니다.

> **초보자 폭풍 질문!**
> **질문: "선생님, `pub`은 도대체 왜 붙이는 건가요? 그냥 다 공개하면 안 되나요?"**
> **재준봇의 답변**: 여기서 `pub`은 'Public'의 약자입니다. Rust는 기본적으로 모든 것이 '비공개'입니다. 이건 아주 강력한 보호 장치예요. 만약 모든 걸 공개하면, 외부에서 내 내부 변수를 아무렇게나 수정해서 프로그램을 망가뜨릴 수 있거든요. "필요한 문만 열어준다"는 개념으로 접근하세요. 그래야 안전한 집(프로그램)이 됩니다!

---

## 3. 계층형 아키텍처 (Layered Architecture)

이제 실전으로 들어갑니다. 실무에서 가장 많이 쓰이는 **계층형 아키텍처**를 소개합니다. 코드를 성격에 따라 크게 세 층으로 나누는 전략입니다.

1. **도메인 계층 (Domain Layer)**: 비즈니스 로직의 핵심입니다. "사용자는 이름을 가져야 한다", "주문은 결제가 되어야 완료된다" 같은 절대적인 규칙이 정의됩니다. 외부 환경(DB, API)에 절대 의존하지 않습니다.
2. **애플리케이션/서비스 계층 (Application/Service Layer)**: 도메인 계층을 조립해서 실제 기능을 수행합니다. "사용자가 로그인을 요청하면, DB에서 확인하고 세션을 생성한다" 같은 흐름을 제어합니다.
3. **인프라 계층 (Infrastructure Layer)**: 실제 외부 세상과 소통하는 곳입니다. 데이터베이스 쿼리를 날리거나, HTTP 요청을 보내는 구체적인 구현체들이 여기 들어갑니다.

### [코드 예제 2] 계층형 아키텍처 실전 구현

이 예제는 아주 간단한 '사용자 저장 시스템'을 가정하고 짠 코드입니다.

```rust
// --- [도메인 계층] ---
// 순수한 데이터와 비즈니스 규칙만 정의합니다.
pub struct User {
    pub id: u64,
    pub name: String,
}

// --- [인프라 계층] ---
// 실제 DB에 어떻게 저장할지를 결정합니다.
pub struct SqliteUserRepository {
    connection_string: String,
}

impl SqliteUserRepository {
    pub fn new(conn: &str) -> Self {
        Self { connection_string: conn.to_string() }
    }

    pub fn save(&self, user: &User) {
        println!("DB({})에 사용자 {}를 저장합니다.", self.connection_string, user.name);
    }
}

// --- [서비스 계층] ---
// 도메인과 인프라를 연결하여 실제 기능을 완성합니다.
pub struct UserService {
    repository: SqliteUserRepository, // 여기서는 일단 직접 의존성을 가졌습니다.
}

impl UserService {
    pub fn new(repo: SqliteUserRepository) -> Self {
        Self { repository: repo }
    }

    pub fn create_user(&self, id: u64, name: &str) {
        let user = User { id, name: name.to_string() };
        self.repository.save(&user);
        println!("서비스: 사용자 생성 완료!");
    }
}

fn main() {
    let repo = SqliteUserRepository::new("sqlite://my_db.db");
    let service = UserService::new(repo);
    service.create_user(1, "재준");
}
```

### 뜯어보기 분석!
- **User 구조체**: 아무런 외부 라이브러리 없이 데이터만 정의했습니다. 이게 가장 순수한 '도메인'입니다.
- **SqliteUserRepository**: 여기서 `println!`을 썼지만, 실제로는 SQL 문이 들어가겠죠? 구체적인 기술(Sqlite)이 명시된 '인프라' 층입니다.
- **UserService**: 사용자가 이름을 입력하면 `User` 객체를 만들고 `repository`를 통해 저장하게 만드는 '오케스트라 지휘자' 역할을 합니다.

---

## 4. 의존성 역전 (Dependency Inversion): 유연함의 끝판왕

위의 예제에서 치명적인 문제가 하나 있습니다. `UserService`가 `SqliteUserRepository`라는 특정 DB 구현체에 꽉 묶여 있다는 점입니다. 만약 내일 당장 "우리 이제 MongoDB로 바꿉니다!"라고 하면 어떻게 될까요? `UserService` 코드 전체를 뜯어고쳐야 합니다. 끔찍하죠.

이걸 해결하는 것이 바로 **트레이트(Trait)**를 이용한 의존성 역전입니다.

### [코드 예제 3] 트레이트를 활용한 유연한 아키텍처 (3가지 구현 방식)

여기서는 인터페이스(Trait)를 정의하고, 이를 어떻게 주입하느냐에 따라 3가지 방식으로 구현해 보겠습니다.

```rust
// 1. 인터페이스 정의 (추상화)
pub trait UserRepository {
    fn save(&self, name: &str);
}

// 2. 구체적인 구현체 A (Sqlite)
pub struct SqliteRepo;
impl UserRepository for SqliteRepo {
    fn save(&self, name: &str) { println!("Sqlite에 {} 저장!", name); }
}

// 3. 구체적인 구현체 B (Postgres)
pub struct PostgresRepo;
impl UserRepository for PostgresRepo {
    fn save(&self, name: &str) { println!("Postgres에 {} 저장!", name); }
}

// --- 주입 방식 3가지 ---

// 방식 A: 제네릭을 이용한 정적 디스패치 (컴파일 타임에 결정, 성능 최상)
pub struct UserServiceStatic<T: UserRepository> {
    repo: T,
}

// 방식 B: Trait Object를 이용한 동적 디스패치 (런타임에 결정, 유연함 최상)
pub struct UserServiceDynamic {
    repo: Box<dyn UserRepository>,
}

// 방식 C: 팩토리 패턴을 이용한 생성 (생성 로직 분리)
pub struct UserFactory;
impl UserFactory {
    pub fn create_service(db_type: &str) -> UserServiceDynamic {
        let repo: Box<dyn UserRepository> = match db_type {
            "sqlite" => Box::new(SqliteRepo),
            _ => Box::new(PostgresRepo),
        };
        UserServiceDynamic { repo }
    }
}

fn main() {
    // 정적 방식 사용
    let service_static = UserServiceStatic { repo: SqliteRepo };
    service_static.repo.save("정적방식");

    // 동적 방식 사용
    let service_dynamic = UserServiceDynamic { repo: Box::new(PostgresRepo) };
    service_dynamic.repo.save("동적방식");

    // 팩토리 방식 사용
    let service_factory = UserFactory::create_service("sqlite");
    service_factory.repo.save("팩토리방식");
}
```

### 뜯어보기 분석!
- **`UserRepository` 트레이트**: "이걸 구현하는 놈은 무조건 `save` 함수가 있어야 해!"라는 계약서입니다.
- **정적 디스패치 (`T: UserRepository`)**: 컴파일러가 미리 어떤 타입을 쓸지 결정합니다. 속도가 엄청나게 빠르지만, 한 번 결정되면 바꾸기 어렵습니다.
- **동적 디스패치 (`Box<dyn UserRepository>`)**: `Box`라는 상자에 담아두고 런타임에 꺼내 씁니다. 약간의 성능 손실이 있지만, 실행 중에 DB를 갈아끼울 수 있을 정도로 유연합니다.
- **팩토리 패턴**: `main` 함수에서 복잡하게 `Box`를 만들 필요 없이, 설정값 하나로 적절한 서비스 객체를 생성하게 만드는 실무 패턴입니다.

> **실무주의보!**
> **경고: "오버 엔지니어링을 조심하세요!"**
> **해설**: 제가 방금 알려드린 트레이트 주입, 팩토리 패턴... 정말 멋지죠? 하지만 아주 작은 개인 프로젝트를 하는데 이렇게 짜면 오히려 배보다 배꼽이 더 커집니다. 코드가 복잡해지고 읽기 힘들어지죠. 아키텍처는 **"나중에 변경될 가능성이 있는가?"**를 고민하고 적용하는 겁니다. 바뀔 일이 없다면 그냥 간단하게 짜는 게 최고입니다!

---

## 5. 최종 정리: 재준봇의 아키텍처 체크리스트

자, 이제 여러분이 프로젝트를 시작할 때 스스로에게 던져야 할 질문 리스트를 드릴게요.

- [ ] **내 코드가 `main.rs` 하나에 다 들어있는가?** $\rightarrow$ 그렇다면 당장 `mod`를 이용해 방을 나누세요.
- [ ] **특정 DB나 외부 API 라이브러리가 내 비즈니스 로직 깊숙이 박혀있는가?** $\rightarrow$ 그렇다면 `Trait`을 만들어 추상화 층을 두세요.
- [ ] **도메인(핵심 규칙)과 인프라(기술적 구현)가 섞여 있는가?** $\rightarrow$ 계층형 아키텍처를 적용해 분리하세요.
- [ ] **새로운 기능을 추가할 때 기존 코드를 대대적으로 수정해야 하는가?** $\rightarrow$ 결합도가 너무 높다는 증거입니다. 의존성 주입을 고민하세요.

오늘 강의는 여기까지입니다. 아키텍처는 한 번에 완벽하게 짤 수 없습니다. 일단 짜보고, 불편함을 느끼고, 그때 조금씩 리팩토링하는 것이 정답입니다.

여러분이 만드는 프로그램이 스파게티가 아니라, 아주 정갈하고 멋진 코스 요리가 되길 응원하겠습니다! 궁금한 점은 언제든 질문 주세요. 지금까지 재준봇이었습니다!

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
