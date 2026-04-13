---
layout: single
title: "Rust 심화: 컨테이닝과 컬렉션: Vec, HashMap"
date: 2026-07-08 02:28:50
categories: [Rust]
---

# 15강: Rust 심화 - 컨테이닝과 컬렉션: Vec, HashMap 🛠️✨

안녕하세요, 여러분의 코딩 여행에 함께하는 주니어 개발자 동료입니다! 오늘은 Rust의 핵심 컬렉션 타입 중 두 가지, **Vec**과 **HashMap**에 대해 깊이 있게 파고들어볼 거예요. 이거 모르면 큰일 납니다! (웃음) 코딩 세계에서 데이터를 효과적으로 관리하는 건 정말 중요하니까요. 그럼 시작해볼까요?

## 🌟 Vec: 가변 크기 배열의 마법사

**Vec**은 Rust에서 가장 기본적이면서도 강력한 동적 배열 타입이에요. 배열처럼 사용할 수 있지만, 크기가 고정되어 있지 않아 필요에 따라 늘어나거나 줄어들 수 있어요. 진짜 신기하죠?

### Vec 기본 사용법

```rust
fn main() {
    // 빈 Vec 생성
    let mut numbers: Vec<i32> = Vec::new();
    
    // 요소 추가
    numbers.push(10);  // "10을 추가해!"라고 명령하는 거예요.
    numbers.push(20);  // "20도 추가해!"라고 말하는 거죠.
    
    // 요소 접근
    println!("첫 번째 숫자: {}", numbers[0]);  // 인덱스 0부터 시작해요.
    
    // 길이 확인
    println!("현재 Vec의 길이: {}", numbers.len());
}
```

#### 코드 설명:
1. **`let mut numbers: Vec<i32> = Vec::new();`**: `Vec<i32>` 타입의 가변 크기 배열을 선언하고 초기화합니다. `mut` 키워드는 이 변수가 변경 가능하다는 걸 알려줘요.
2. **`numbers.push(10);`**: 배열 끝에 `10`을 추가합니다.
3. **`println!("첫 번째 숫자: {}", numbers[0]);`**: 첫 번째 요소를 접근합니다. 주의할 점은 배열 인덱스는 0부터 시작한다는 거예요!
4. **`println!("현재 Vec의 길이: {}", numbers.len());`**: 현재 Vec에 몇 개의 요소가 있는지 확인해요.

### 💡 초보자 폭풍 질문!
- **Q**: 인덱스 범위를 벗어나면 어떻게 되나요?
  - **A**: Rust는 컴파일 시점에 안전성을 최우선으로 하기 때문에, 범위를 벗어난 접근을 시도하면 컴파일 에러가 발생합니다. 이를 방지하려면 항상 `len()`을 확인하는 습관을 들이는 게 좋아요!

### 🚨 실무주의보
- **데이터 관리**: 대규모 데이터셋을 다룰 때는 `Vec`의 메모리 할당과 해제 과정을 고려해야 합니다. Rust의 소유권 및 빌림 시스템을 잘 이해하고 활용하면 성능 최적화에 큰 도움이 됩니다.

## 🔑 HashMap: 키-값 쌍의 마법사

**HashMap**은 키-값 쌍을 관리하는 데 최고의 도구예요. 빠르게 데이터를 검색하고 업데이트할 수 있게 해줍니다. 마치 마법의 보물상자 같죠!

### HashMap 기본 구현

```rust
use std::collections::HashMap;

fn main() {
    // 빈 HashMap 생성
    let mut user_scores: HashMap<String, i32> = HashMap::new();
    
    // 키-값 쌍 추가
    user_scores.insert("Alice".to_string(), 95);
    user_scores.insert("Bob".to_string(), 88);
    
    // 값 접근
    if let Some(score) = user_scores.get("Alice") {
        println!("Alice의 점수: {}", score);
    } else {
        println!("Alice 정보가 없어요!");
    }
    
    // 값 업데이트
    user_scores.insert("Bob".to_string(), 92);  // 기존 값이 있으면 대체됩니다.
    
    // 키 존재 여부 확인
    if user_scores.contains_key("Charlie") {
        println!("Charlie가 있어요!");
    } else {
        println!("Charlie는 아직 등록되지 않았어요.");
    }
}
```

#### 코드 설명:
1. **`use std::collections::HashMap;`**: `HashMap`을 사용하기 위해 필요한 모듈을 가져옵니다.
2. **`let mut user_scores: HashMap<String, i32> = HashMap::new();`**: `String` 키를 가진 `i32` 값을 저장하는 `HashMap`을 생성합니다.
3. **`user_scores.insert("Alice".to_string(), 95);`**: 키 `"Alice"`에 값 `95`를 추가합니다.
4. **`user_scores.get("Alice")`**: 키 `"Alice"`에 해당하는 값을 가져옵니다. `get` 메서드는 `Option<&V>`를 반환하므로 `if let`을 사용해 안전하게 처리합니다.
5. **`user_scores.insert("Bob".to_string(), 92);`**: 기존 키 `"Bob"`의 값을 업데이트합니다.
6. **`contains_key` 메서드**: 특정 키가 존재하는지 확인합니다.

### 💡 초보자 폭풍 질문!
- **Q**: 키 중복은 어떻게 처리되나요?
  - **A**: 동일한 키가 다시 삽입되면 이전 값은 덮어쓰기 됩니다. 즉, 가장 최근에 삽입된 값만 유지됩니다.

### 🚨 실무주의보
- **성능 고려**: `HashMap`은 빠른 검색을 제공하지만, 해시 충돌이 발생할 경우 성능에 영향을 줄 수 있습니다. 키 선택 시 충돌 가능성을 최소화하는 것이 중요해요.

## 🎉 마무리: 활용 사례와 팁

### Vec 활용 사례
- **동적 리스트**: 사용자 입력을 받아 동적으로 리스트를 관리할 때.
- **스택 구현**: `push`와 `pop` 메서드를 활용해 스택 구조를 쉽게 구현할 수 있어요.

### HashMap 활용 사례
- **데이터 매핑**: 사용자 ID와 점수를 매핑하거나, 단어와 정의를 관리할 때.
- **캐싱**: 자주 사용되는 데이터를 빠르게 접근할 수 있도록 캐싱 용도로 활용.

### 🛠️ 팁
- **소유권과 빌림**: `Vec`과 `HashMap`을 다룰 때 소유권과 빌림 규칙을 잘 이해하고 활용하면 메모리 관리와 성능 최적화에 큰 도움이 됩니다.
- **성능 모니터링**: 큰 데이터셋을 다룰 때는 성능 프로파일링 도구를 활용해 병목 현상을 찾아보세요.

오늘 배운 내용으로 Rust의 컬렉션 관리 능력이 한층 업그레이드되었기를 바라요! 질문이 있으면 언제든지 물어봐주세요. 다음 강의에서 또 만나요! 😄

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
