---
layout: single
title: "Rust C 언어 심화: 고급 타입 시스템 (enum, struct)"
date: 2026-07-13 19:21:50
categories: [Rust C 언어]
---

### 8강: Rust C 언어 심화 - 고급 타입 시스템: `enum`과 `struct` 마스터하기

안녕하세요, 여러분의 Rust 및 C 언어 모험 가이드인 [이름]입니다! 오늘은 코딩의 마법 세계로 여러분을 안내할 거예요. 특히 고급 타입 시스템의 핵심인 `enum`과 `struct`에 대해 깊이 들어가 보겠습니다. 이 강의를 마치고 나면, 복잡한 데이터 구조를 다루는 데 있어 훨씬 더 자신감을 갖게 될 거예요! 🤓

#### 💡 초보자 폭풍 질문! 🤔
**Q: `enum`과 `struct`가 뭐길래 이렇게 중요한 걸까요?**

**A:** `enum`은 다양한 상태나 범주를 표현하는 데 사용되고, `struct`는 복잡한 데이터 구조를 묶어 관리하는 데 쓰여요. 이 둘은 코드의 가독성과 유지보수성을 크게 향상시키는 핵심 요소랍니다. 이제 본격적으로 배워볼까요?

---

### #1. `enum`: 다양성의 마법사

`enum`은 "enumerate"의 약자로, 여러 개의 가능한 상태나 범주를 정의하는 데 사용됩니다. 마치 슈퍼마켓의 카테고리처럼, 각각의 항목이 특정 의미를 갖는 거죠.

#### 기본 `enum` 예시
```c
// 상태를 나타내는 enum 예시
enum TrafficLight {
    RED,     // 빨간불
    YELLOW,  // 노란불
    GREEN    // 초록불
};

int main() {
    enum TrafficLight currentLight = RED;  // 변수 선언 및 초기화

    switch (currentLight) {
        case RED:    printf("빨간불! 정지하세요.\n"); break;  // 빨간불 상태 출력
        case YELLOW: printf("노란불! 주의하세요.\n"); break; // 노란불 상태 출력
        case GREEN:  printf("초록불! 통행 가능!\n"); break; // 초록불 상태 출력
        default:     printf("알 수 없는 상태!\n"); break;     // 디폴트 처리
    }
    return 0;
}
```

**코드 해부:**
- `enum TrafficLight`: 상태를 정의합니다. 각 값(`RED`, `YELLOW`, `GREEN`)은 해당 상태를 나타냅니다.
- `enum TrafficLight currentLight = RED;`: `RED` 상태를 가진 변수를 생성합니다.
- `switch` 문: 각 상태에 따라 다른 동작을 수행합니다. 이는 `enum`을 사용하면 코드가 명확해지고 가독성이 향상된다는 걸 보여줍니다.

#### 고급 `enum`: 연관 데이터 포함하기
Rust에서는 `enum` 내부에 구조체를 포함할 수 있어 더 유연한 데이터 모델링이 가능합니다.

```rust
// Rust에서의 연관 데이터를 포함한 enum 예시
enum Vehicle {
    Car { doors: u32, fuel_type: &'static str },  // 차량 정보
    Bike { has_sidecar: bool },                   // 오토바이 정보
}

fn main() {
    let my_vehicle = Vehicle::Car { doors: 4, fuel_type: "Petrol" };
    match my_vehicle {
        Vehicle::Car { doors, fuel_type } => {
            println!("차량: {} 문, 연료 유형: {}", doors, fuel_type);
        }
        Vehicle::Bike { has_sidecar } => {
            println!("오토바이: {}", if has_sidecar { "사이드카 있음" } else { "사이드카 없음" });
        }
    }
}
```

**코드 해부:**
- `Vehicle` enum: `Car`와 `Bike`라는 두 가지 상태를 정의합니다.
- `Car` 타입은 `doors`와 `fuel_type`이라는 두 개의 필드를 가집니다.
- `match` 문: 각 상태에 따라 다른 정보를 출력합니다. Rust의 강력한 패턴 매칭 기능이 여기서 빛을 발휘합니다!

---

### #2. `struct`: 데이터의 묶음 마법사

`struct`는 여러 필드를 하나로 묶어 복잡한 데이터 구조를 표현하는 데 사용됩니다. 마치 책장에 책들을 정리하듯이, 다양한 정보를 한 곳에 모아 관리할 수 있게 해줍니다.

#### 기본 `struct` 예시
```c
// 간단한 사용자 정보 구조체 예시
struct User {
    char name[50];  // 이름
    int age;        // 나이
    float height;   // 키
};

int main() {
    User person = { "Alice", 30, 165.5 };  // 구조체 초기화

    printf("이름: %s, 나이: %d, 키: %.2f\n", person.name, person.age, person.height);
    return 0;
}
```

**코드 해부:**
- `struct User`: 이름, 나이, 키 세 가지 필드를 가진 구조체를 정의합니다.
- `User person = { ... };`: 구조체 변수를 초기화합니다. 각 필드에 값을 할당합니다.
- `printf`: 구조체의 각 필드에 접근하여 출력합니다.

#### 고급 `struct` 활용: 함수 인자로 전달
`struct`를 함수 인자로 전달하면 더 유연한 코드 설계가 가능해집니다.

```rust
// Rust에서 struct를 함수 인자로 전달하는 예시
struct PersonalDetails {
    name: String,
    address: String,
}

fn print_details(details: PersonalDetails) {
    println!("이름: {}, 주소: {}", details.name, details.address);
}

fn main() {
    let details = PersonalDetails {
        name: String::from("Bob"),
        address: String::from("서울시 강남구"),
    };
    print_details(details);  // 함수 호출
}
```

**코드 해부:**
- `PersonalDetails` struct: 이름과 주소를 포함합니다.
- `print_details` 함수: `PersonalDetails` 타입의 인자를 받습니다.
- `main` 함수: `PersonalDetails`를 생성하고 함수에 전달하여 정보를 출력합니다.

---

### 💡 실무주의보 🚨
**Q: `enum`과 `struct`를 잘못 사용하면 어떤 문제가 생길 수 있나요?**

**A:** 잘못된 설계로 인해 코드가 복잡해지고 유지보수가 어려워질 수 있습니다. 예를 들어, `enum`에 너무 많은 상태를 넣거나 `struct`에 불필요한 필드를 추가하면 가독성이 떨어지고 오류 발생 가능성이 높아집니다. 항상 간결하고 명확한 설계를 추구하세요!

---

### 결론
`enum`과 `struct`는 코드를 구조화하고 가독성을 높이는 데 필수적인 도구입니다. 이들을 적절히 활용하면 복잡한 시스템을 관리하는 데 큰 도움이 될 거예요. 이제 여러분도 이 강력한 도구들을 자유자재로 다루며 더 멋진 소프트웨어를 만들어 보세요! 🚀

### 추가 학습 자료
- Rust 공식 문서에서 `enum`과 `struct`에 대한 자세한 내용 확인: [Rust Docs](https://doc.rust-lang.org/book/ch06-01-defining-structs.html)
- C 언어에서의 구조체 활용 예제: [C 언어 튜토리얼 사이트](https://www.tutorialspoint.com/cprogramming/struct.htm)

🌟 여러분의 코딩 여정이 계속 성공적으로 이어지길 바랍니다! 다음 강의에서 또 만나요!

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
