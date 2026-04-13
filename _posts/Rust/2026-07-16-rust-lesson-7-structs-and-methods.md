---
layout: single
title: "Rust 기초: 구조체와 메소드"
date: 2026-07-16 01:41:23
categories: [Rust]
---

# 7강: Rust 기초 - 구조체와 메소드: 세상을 구조화하는 마법의 도구들

안녕하세요, 여러분의 친근한 주니어 개발자 멘토, Rust 5년차 개발자입니다! 오늘은 Rust 프로그래밍에서 정말 중요한 두 가지 개념, **구조체(Struct)**와 **메소드(Method)**에 대해 이야기해볼게요. 이 두 가지는 마치 마법 지팡이 같아서, 복잡한 세상을 깔끔하게 정리하고 코드를 훨씬 더 직관적으로 만드는 데 엄청난 힘을 발휘합니다. 준비되셨나요? 그럼 함께 마법의 세계로 들어가볼까요?

## 구조체: 세상을 상자에 담아보자!

### 구조체란 무엇인가요?
구조체는 데이터의 조합체라고 생각하면 됩니다. 일상생활에서 보면, 사람을 설명할 때 이름, 나이, 키 등 여러 정보를 묶어 표현하는 것과 비슷해요. Rust에서는 이런 정보들을 한 덩어리로 관리할 수 있게 해주는 도구가 바로 구조체입니다.

#### 예제 코드: 사람을 표현하는 구조체
```rust
// 사람을 표현하는 구조체 정의
struct Person {
    name: String,  // 이름
    age: u8,       // 나이
    height: f32,   // 키 (cm)
}

fn main() {
    // 구조체 인스턴스 생성
    let alice = Person {
        name: String::from("앨리스"),
        age: 28,
        height: 165.5,
    };

    println!("이름: {}, 나이: {}, 키: {}cm", alice.name, alice.age, alice.height);
}
```
- **`struct Person`**: `Person`이라는 구조체를 정의합니다.
- **`name: String`**: 이름은 문자열 타입 `String`으로 저장합니다.
- **`age: u8`**: 나이는 부호 없는 8비트 정수 `u8`로 저장합니다.
- **`height: f32`**: 키는 부동소수점 숫자 `f32`로 저장합니다.
- **`let alice`**: 구조체의 인스턴스를 생성하고, 각 필드에 값을 할당합니다.

### 💡 초보자 폭풍 질문!
**Q: 구조체 필드에 값을 지정할 때 순서를 지켜야 하나요?**  
**A:** 네, 구조체 필드에 값을 할당할 때는 정의된 순서대로 값을 주는 것이 일반적입니다. 하지만 Rust에서는 **Key-Value Pair 방식**으로도 할당할 수 있어요!
```rust
let bob = Person {
    name: String::from("밥"),
    height: 175.0,  // 순서 상관없이 할당 가능
    age: 30,
};
```

## 메소드: 구조체에게 행동을 부여하자!

### 메소드의 마법
구조체는 데이터를 담는 상자라면, 메소드는 그 상자에게 행동을 부여하는 마법입니다. 예를 들어, `Person` 구조체에게 `introduce`라는 메소드를 부여해보겠습니다.

#### 예제 코드: 구조체에 메소드 추가
```rust
struct Person {
    name: String,
    age: u8,
    height: f32,
}

// 메소드 정의
impl Person {
    // 생성자 함수
    fn new(name: String, age: u8, height: f32) -> Person {
        Person { name, age, height }
    }

    // 소개 메소드
    fn introduce(&self) -> String {
        format!("안녕하세요, 저는 {}살 {}cm인 {}입니다.", self.age, self.height, self.name)
    }
}

fn main() {
    let charlie = Person::new(String::from("찰리"), 25, 180.0);
    println!("{}", charlie.introduce());
}
```
- **`impl Person`**: `Person` 구조체에 대한 구현 블록을 시작합니다.
- **`fn new`**: 생성자 함수로, 새로운 `Person` 인스턴스를 쉽게 만드는 역할을 합니다.
- **`fn introduce`**: `&self`를 매개변수로 받아, 자기 자신의 정보를 기반으로 문자열을 반환합니다.

### 🚨 실무주의보
**메소드 내부에서 구조체의 필드를 직접 수정할 때 주의사항**: 만약 메소드 내에서 필드 값을 변경하려 한다면, 구조체를 `mut` (수정 가능)로 선언해야 합니다. 예를 들어, 나이를 증가시키는 메소드를 만들어보겠습니다.

#### 수정 가능한 구조체와 메소드 예시
```rust
impl Person {
    // 나이 증가 메소드
    fn have_birthday(&mut self) {
        self.age += 1;
    }
}

fn main() {
    let mut dawn = Person::new(String::from("던"), 22, 160.0);
    println!("생일 전: {}", dawn.introduce());
    dawn.have_birthday();  // 생일을 맞이했습니다!
    println!("생일 후: {}", dawn.introduce());
}
```
- **`&mut self`**: 메소드가 구조체의 상태를 변경할 수 있도록 수정 가능한 참조를 받습니다.
- **`self.age += 1`**: 나이를 1 증가시킵니다.

## 구조체와 메소드의 실무 활용 사례

### 🛠️ 실무 사례: 게임 캐릭터 관리
게임 개발에서 캐릭터를 표현하는 데 구조체와 메소드를 어떻게 활용할 수 있을까요?

#### 예제 코드: 게임 캐릭터 구조체와 메소드
```rust
struct GameCharacter {
    name: String,
    health: u32,
    mana: u32,
}

impl GameCharacter {
    fn new(name: String, health: u32, mana: u32) -> GameCharacter {
        GameCharacter { name, health, mana }
    }

    fn take_damage(&mut self, damage: u32) {
        self.health -= damage;
        if self.health < 0 {
            self.health = 0;
        }
    }

    fn cast_spell(&mut self, spell_cost: u32) -> bool {
        if self.mana >= spell_cost {
            self.mana -= spell_cost;
            println!("주문 발동!");
            true
        } else {
            println!("마나가 부족합니다.");
            false
        }
    }

    fn status(&self) -> String {
        format!("이름: {}, 체력: {}/{}, 마나: {}/{}", self.name, self.health, 100, self.mana, 100)
    }
}

fn main() {
    let mut hero = GameCharacter::new(String::from("영웅"), 100, 50);
    println!("초기 상태: {}", hero.status());

    hero.take_damage(30);
    println!("피해 후: {}", hero.status());

    hero.cast_spell(20);
    println!("마나 사용 후: {}", hero.status());
}
```
- **`take_damage`**: 캐릭터가 피해를 받았을 때 체력을 감소시킵니다.
- **`cast_spell`**: 캐릭터가 주문을 사용할 때 마나를 감소시키고, 사용 가능 여부를 반환합니다.
- **`status`**: 캐릭터의 현재 상태를 문자열로 반환합니다.

### 마무리: 구조체와 메소드의 힘
구조체와 메소드는 Rust 프로그래밍에서 데이터를 효과적으로 관리하고, 그 데이터에 대해 행동을 부여하는 핵심 요소입니다. 이제 여러분도 이 마법 같은 도구들을 활용해 복잡한 시스템을 깔끔하게 구조화하고, 코드의 가독성과 유지보수성을 극대화할 수 있을 거예요!

오늘 배운 내용으로 여러분의 Rust 세계가 더욱 풍성해지길 바라며, 앞으로도 계속해서 도전하고 배우는 여정을 응원하겠습니다! 궁금한 점이 있다면 언제든지 물어봐주세요. 다음 강의에서 또 만나요!

---

이 강의가 초보자분들께 큰 도움이 되었길 바랍니다. Rust의 세계에서 멋진 프로젝트를 만들어 나가시길 기원합니다!

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
