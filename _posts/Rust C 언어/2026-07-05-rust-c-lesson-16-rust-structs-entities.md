---
layout: single
title: "Rust 구조체와 엔티티 사용"
date: 2026-07-05 19:07:47
categories: [Rust C 언어]
---

### 16강: Rust 구조체와 엔티티 사용 - 코딩의 마법 세계로 떠나보자!

안녕하세요, 초보자 친구들! 오늘은 Rust 언어에서 가장 흥미로운 주제 중 하나인 **구조체(Structs)**와 **엔티티(Entities)**에 대해 깊이 있게 탐험해볼게요. 혹시 Rust를 처음 접하는 분들껜 좀 낯설 수도 있겠지만, 걱정 마세요! 저와 함께라면 코딩의 마법 세계로 단숨에 빠져들 수 있을 거예요. 그럼 시작해볼까요?

#### 💡 초보자 폭풍 질문!
**Q:** 구조체와 엔티티, 정확히 어떤 차이가 있나요?
**A:** 좋은 질문이에요! **구조체**는 데이터를 그룹화하는 Rust의 기본 구성 요소예요. 여러 필드를 묶어서 복잡한 정보를 한 번에 관리할 수 있게 해줍니다. **엔티티**는 좀 더 구체적으로 말하면, 구조체를 실제 프로그램 내에서 활용하는 방식을 가리킵니다. 쉽게 말해, 구조체는 설계도이고 엔티티는 그 설계도를 바탕으로 만들어진 실제 건물 같은 존재라고 생각하면 돼요.

---

### 구조체 이해하기: 데이터의 마법사로 변신하기

#### 기본 개념
구조체는 Rust에서 데이터의 복잡한 집합을 표현하는 데 사용되는 핵심 요소입니다. 예를 들어, **사람**에 대한 정보를 관리한다고 상상해보세요. 이름, 나이, 직업 등 다양한 필드가 필요할 거예요.

#### 예제 1: 기본적인 구조체 정의
```rust
struct Person {
    name: String,    // 이름
    age: u32,        // 나이 (32비트 부호 없는 정수)
    job: String,     // 직업
}

fn main() {
    let alice = Person {
        name: String::from("Alice"),
        age: 30,
        job: String::from("Engineer"),
    };

    println!("이름: {}, 나이: {}, 직업: {}", alice.name, alice.age, alice.job);
}
```
**코드 설명:**
- **struct Person { ... }**: `Person` 구조체를 정의합니다. 여기서 `name`, `age`, `job`은 구조체의 필드입니다.
- **let alice = Person { ... }**: `Person` 구조체의 인스턴스를 생성합니다. 각 필드에 값을 할당합니다.
- **println!**: 생성된 `alice` 구조체의 정보를 출력합니다.

#### 예제 2: 필드 초기화의 다양한 방법
Rust는 초기화 방식에 유연성을 제공합니다. 여러 방법으로 필드를 초기화할 수 있어요.

```rust
fn main() {
    // 명시적 초기화
    let bob = Person {
        name: String::from("Bob"),
        age: 25,
        job: String::from("Developer"),
    };

    // 명시적 필드 초기화와 기본값 사용
    let eve = Person {
        name: String::from("Eve"),
        age: 28, // 명시적으로 지정
        ..Default::default() // 나머지 필드는 기본값 사용
    };

    println!("이름: {}, 나이: {}, 직업: {}", bob.name, bob.age, bob.job);
    println!("이름: {}, 나이: {}, 직업: {}", eve.name, eve.age, eve.job);
}
```
**코드 설명:**
- **명시적 초기화**: 모든 필드를 직접 지정합니다.
- **기본값 사용**: 일부 필드는 명시적으로 지정하고 나머지는 `Default::default()`로 기본값을 사용합니다. Rust의 기본값은 필드 타입에 따라 달라집니다 (예: `u32`의 기본값은 `0`).

#### 예제 3: 메소드와 구조체 결합하기
구조체에 직접 메소드를 정의할 수도 있어요. 이렇게 하면 데이터 조작이 훨씬 편리해집니다!

```rust
struct Car {
    make: String,
    model: String,
    year: u32,
}

impl Car {
    fn display_info(&self) {
        println!("차량 정보: {} {} {}, 연식: {}년", self.make, self.model, self.year);
    }
}

fn main() {
    let my_car = Car {
        make: String::from("Toyota"),
        model: String::from("Camry"),
        year: 2023,
    };

    my_car.display_info(); // 메소드 호출
}
```
**코드 설명:**
- **impl Car { ... }**: `Car` 구조체에 대한 구현 블록을 만듭니다.
- **fn display_info(&self)**: `display_info`라는 메소드를 정의합니다. `&self`는 구조체 인스턴스를 참조합니다.
- **my_car.display_info()**: 구조체 인스턴스에 직접 메소드를 호출하여 정보를 출력합니다.

#### 예제 4: 연관형 구조체 (Nested Structs) 활용하기
더 복잡한 데이터 구조를 다룰 때 연관형 구조체를 사용하면 매우 유용합니다.

```rust
struct Address {
    street: String,
    city: String,
    zip_code: u32,
}

struct Person {
    name: String,
    age: u32,
    address: Address, // 연관형 구조체
}

fn main() {
    let person = Person {
        name: String::from("Charlie"),
        age: 35,
        address: Address {
            street: String::from("123 Elm St"),
            city: String::from("Springfield"),
            zip_code: 12345,
        },
    };

    println!("이름: {}, 나이: {}, 주소: {}", person.name, person.age, person.address.street);
}
```
**코드 설명:**
- **연관형 구조체**: `Address` 구조체를 `Person` 구조체 내부에 포함시켜 복잡한 데이터 구조를 만듭니다.
- **인라인 초기화**: `Address` 구조체의 모든 필드를 `Person` 구조체 내부에서 초기화합니다.

---

### 💡 실무주의보
**Q:** 구조체를 많이 사용하면 코드가 복잡해지지 않나요?
**A:** 그렇지 않아요! 구조체는 코드의 가독성과 유지보수성을 크게 향상시킵니다. 복잡한 데이터를 체계적으로 관리할 수 있게 해주므로 장기적으로 더 간결하고 이해하기 쉬운 코드를 작성할 수 있습니다. 다만, 과도한 중첩은 가독성을 해칠 수 있으니 적절한 수준을 유지하는 것이 중요합니다.

---

### 마무리
오늘 배운 내용으로 Rust 구조체와 엔티티의 매력에 푹 빠져보셨기를 바라요! 구조체를 활용하면 데이터를 훨씬 효과적으로 관리할 수 있게 되고, 이는 실제 프로젝트에서도 큰 도움이 될 거예요. 아직 궁금한 점이 있다면 언제든지 질문해주세요!

**다음 강의에서는 더 깊게 들어갈 예정이니, 준비되셨나요?** 🚀

---

이 강의가 여러분의 코딩 여정에 작은 빛이 되길 바라며, 계속해서 성장하는 개발자가 되시길 응원합니다!

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
