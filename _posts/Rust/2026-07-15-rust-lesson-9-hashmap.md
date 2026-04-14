---
layout: single
title: "Rust 기초: 컬렉션 HashMap"
date: 2026-07-15 00:19:10
categories: [Rust]
---

안녕하세요! 저는 여러분의 코딩 길잡이, 재준봇입니다.

자, 여러분. 지금까지 우리는 변수, 함수, 그리고 벡터 같은 것들을 배웠습니다. 그런데 공부를 하다 보면 이런 생각이 드실 거예요. "아니, 데이터를 순서대로 저장하는 건 좋은데, 내가 원하는 이름을 딱 대면 바로 값이 튀어나오게 할 수는 없을까?"

예를 들어, 전교생 1,000명의 성적표가 벡터에 들어있다고 칩시다. '김철수'의 점수를 찾으려면 최악의 경우 1,000번을 다 뒤져야 합니다. 이건 너무 비효율적이죠. 여기서 등장하는 구원투수가 바로 오늘 배울 'HashMap'입니다.

오늘은 Rust의 컬렉션 끝판왕, HashMap을 아주 찰떡같이 설명해 드릴게요. 준비되셨나요? 가봅시다!

# 9강: Rust 기초 - 컬렉션 HashMap

## 1. HashMap이란 무엇인가? (feat. 마법의 이름표 보관함)

먼저 개념부터 잡고 가죠. HashMap은 쉽게 말해 '열쇠(Key)'와 '값(Value)'이 한 쌍으로 묶여 있는 저장소입니다. 

비유를 들어볼게요. 여러분이 아주 큰 사물함 센터의 관리자라고 생각하세요. 
- **벡터(Vector)**는 그냥 1번 사물함, 2번 사물함, 3번 사물함... 이렇게 번호표 순서대로 짐을 넣는 거예요. 
- **HashMap**은 사물함 앞에 '철수의 가방', '영희의 책'이라고 이름표를 붙여놓는 겁니다. 

우리는 이제 번호가 몇 번인지 외울 필요가 없습니다. 그냥 "철수 가방 가져와!"라고 하면 HashMap이 마법처럼 그 위치를 딱 짚어서 가져다줍니다. 진짜 신기하죠?

그런데 여기서 주의할 점! Rust의 HashMap은 기본 라이브러리의 루트에 들어있지 않습니다. 그래서 사용하려면 반드시 맨 위에 이 한 줄을 적어줘야 합니다. 이거 안 쓰면 컴파일러가 "HashMap이 뭐야? 나 그런 거 몰라!"라고 화낼 겁니다.

> `use std::collections::HashMap;`

---

## 2. HashMap에 데이터 넣기: 세 가지 방법

데이터를 넣는 방법은 여러 가지가 있습니다. 상황에 따라 골라 써야 하니, 제가 세 가지 패턴을 확실하게 보여드릴게요.

### [코드 예제 1: 데이터 삽입의 다양한 모습]

```rust
use std::collections::HashMap;

fn main() {
    // 방법 1: 빈 맵을 만들고 하나씩 insert 하기 (가장 기본)
    let mut scores = HashMap::new(); 
    scores.insert(String::from("Blue"), 10);
    scores.insert(String::from("Yellow"), 20);
    scores.insert(String::from("Red"), 30);
    // 하나씩 정성스럽게 넣는 방식입니다. 데이터가 적을 때 좋죠.

    // 방법 2: 튜플 벡터를 이용해서 한 번에 생성하기 (from 사용)
    // (키, 값) 쌍의 배열을 바로 HashMap으로 변환합니다.
    let players = HashMap::from([
        (String::from("Player1"), 100),
        (String::from("Player2"), 200),
        (String::from("Player3"), 300),
    ]);
    // 처음부터 데이터가 정해져 있을 때 아주 깔끔하게 작성할 수 있습니다.

    // 방법 3: 기존 맵에 다른 컬렉션의 데이터를 합치기 (extend 사용)
    let mut inventory = HashMap::new();
    inventory.insert(String::from("Sword"), 1);
    
    let new_items = vec![
        (String::from("Shield"), 1),
        (String::from("Potion"), 10),
    ];
    inventory.extend(new_items);
    // 기존의 맵에 리스트 형태의 데이터를 한꺼번에 들이부을 때 사용합니다.

    println!("전체 점수: {:?}", scores);
    println!("플레이어 정보: {:?}", players);
    println!("인벤토리: {:?}", inventory);
}
```

### [코드 뜯어보기]
1. **`HashMap::new()`**: 일단 빈 바구니를 만드는 겁니다. 내용을 수정해야 하니 반드시 `mut` 키워드를 붙여야 합니다.
2. **`insert(key, value)`**: 키와 값을 짝지어 넣습니다. 만약 이미 똑같은 키가 있다면? 기존 값은 사라지고 새로운 값으로 덮어씌워집니다.
3. **`HashMap::from([...])`**: 이 방식은 최근 Rust 버전에서 아주 유용하게 쓰입니다. 일일이 insert를 호출하지 않고 선언과 동시에 초기화를 할 수 있어 코드가 매우 간결해집니다.
4. **`extend()`**: 벡터 같은 다른 반복 가능한 컬렉션을 가져와서 맵에 추가하는 방식입니다. 대량의 데이터를 옮길 때 필수적입니다.

---

## 3. 데이터 꺼내 쓰기: 안전하게 접근하는 세 가지 방법

이제 넣었으니 꺼내야겠죠? 그런데 Rust는 매우 깐깐한 언어입니다. "만약 없는 키를 달라고 하면 어떡할 거야?"라고 계속 물어봅니다. 그래서 단순히 값을 주는 게 아니라 `Option`이라는 상자에 담아 줍니다.

### [코드 예제 2: 데이터 조회 및 처리]

```rust
use std::collections::HashMap;

fn main() {
    let mut scores = HashMap::new();
    scores.insert(String::from("Blue"), 10);
    scores.insert(String::from("Yellow"), 20);

    // 방법 1: get() 메서드와 match 문 사용하기 (가장 정석)
    let team_name = String::from("Blue");
    match scores.get(&team_name) {
        Some(score) => println!("{} 팀의 점수는 {}점입니다.", team_name, score),
        None => println!("해당 팀을 찾을 수 없습니다."),
    }
    // get은 Option<&V>를 반환합니다. 값이 있으면 Some, 없으면 None이 나오므로 안전합니다.

    // 방법 2: contains_key()로 먼저 확인하고 접근하기
    let target = "Yellow";
    if scores.contains_key(target) {
        println!("{} 팀이 존재합니다!", target);
    } else {
        println!("{} 팀은 등록되지 않았습니다.", target);
    }
    // 값이 있는지 없는지만 빠르게 확인하고 싶을 때 사용합니다.

    // 방법 3: unwrap() 사용하기 (위험한 방법)
    // 주의: 키가 없으면 프로그램이 그대로 종료(panic)됩니다.
    let score_val = scores.get("Blue").expect("값이 반드시 있어야 합니다!");
    println!("Blue 팀 점수: {}", score_val);
    // 확실히 데이터가 있다는 보장이 있을 때만 쓰세요. 아니면 큰일 납니다!
}
```

### [코드 뜯어보기]
1. **`get(&team_name)`**: 여기서 중요합니다! `get`은 값을 직접 가져오는 게 아니라 '참조자'를 가져옵니다. 그래서 `&`를 붙여서 넘겨줍니다.
2. **`match` 문**: `Option` 타입을 처리하는 Rust의 가장 강력한 도구입니다. 값이 있을 때와 없을 때의 행동을 명확히 정의해서 런타임 에러를 원천 봉쇄합니다.
3. **`contains_key()`**: 불리언(true/false) 값을 반환합니다. 로직 상에서 존재 여부만 체크해야 할 때 매우 효율적입니다.
4. **`expect()`**: `unwrap()`과 비슷하지만, 패닉이 발생했을 때 출력할 메시지를 지정할 수 있습니다. 하지만 초보자분들은 가급적 `match`나 `if let`을 쓰시는 것을 추천합니다.

---

## 4. 데이터 업데이트하기: 지능적으로 값 수정하는 세 가지 방법

단순히 덮어쓰는 것 말고, "값이 없으면 넣고, 있으면 더해라" 같은 복잡한 로직이 필요할 때가 있습니다. 이때 Rust의 `Entry` API라는 기가 막힌 기능을 사용합니다.

### [코드 예제 3: 스마트한 값 업데이트]

```rust
use std::collections::HashMap;

fn main() {
    let mut scores = HashMap::new();
    scores.insert(String::from("Blue"), 10);

    // 방법 1: 단순 덮어쓰기 (insert)
    scores.insert(String::from("Blue"), 15); 
    // 기존 10점이 사라지고 15점이 됩니다. 단순 교체입니다.

    // 방법 2: or_insert() 사용하기 (없을 때만 삽입)
    // "Blue"가 있으면 그 값을 반환하고, 없으면 50을 넣고 그 값을 반환합니다.
    scores.entry(String::from("Yellow")).or_insert(50);
    // Yellow가 없었으므로 50이 들어갑니다. 만약 Blue에 썼다면 아무 일도 일어나지 않았을 겁니다.

    // 방법 3: and_modify().or_insert() 조합하기 (있으면 수정, 없으면 삽입)
    // "Blue"가 있으면 5점을 더하고, 없으면 10점을 새로 넣습니다.
    scores.entry(String::from("Blue"))
          .and_modify(|e| *e += 5)
          .or_insert(10);
    // Blue는 이미 15점이었으므로 5점이 더해져 20점이 됩니다.

    println!("최종 성적표: {:?}", scores);
}
```

### [코드 뜯어보기]
1. **`insert()`**: 가장 무식한(?) 방법입니다. 기존 데이터가 무엇이든 상관없이 그냥 밀어버립니다.
2. **`entry()`**: 이 메서드는 해당 키가 맵에 있는지 확인하고, 그 위치에 대한 '권한'을 가져오는 입구 역할을 합니다.
3. **`or_insert(value)`**: "값이 없니? 그럼 이거라도 넣어!"라는 뜻입니다. 매우 자주 쓰이는 패턴입니다.
4. **`and_modify(|e| *e += 5)`**: 클로저(Closure)를 사용합니다. 값이 존재할 때만 실행되며, 여기서 `*e`라고 쓴 이유는 전달받은 값이 참조자이기 때문에 실제 값에 접근하기 위해 역참조를 해준 것입니다.

---

## 💡 초보자 폭풍 질문!

**Q: 선생님, 파이썬의 Dictionary랑 똑같은 거 아닌가요? 왜 이렇게 복잡하게 `Option`이니 `Entry`니 하는 걸 써야 하죠?**

**A: 재준봇의 답변:**
맞습니다! 개념적으로는 거의 똑같습니다. 하지만 Rust는 '안전'에 미친 언어입니다. 파이썬은 없는 키를 부르면 런타임에 `KeyError`가 나면서 프로그램이 뻗어버리죠? Rust는 그걸 컴파일 단계에서 막고 싶어 합니다. "여기 값이 없을 수도 있는데, 그 경우에 어떻게 할지 미리 정해놔!"라고 강제하는 겁니다. 조금 귀찮지만, 덕분에 한 번 실행된 Rust 프로그램은 웬만해서는 갑자기 죽지 않는 무적의 상태가 되는 것이죠!

---

## ⚠️ 실무 주의보

**주의사항: 소유권(Ownership) 문제!**

HashMap의 키나 값으로 `String` 같은 힙 할당 데이터를 넣을 때, HashMap이 그 데이터의 소유권을 가져가 버립니다. 

예를 들어:
```rust
let name = String::from("Rust");
map.insert(name, 100);
println!("{}", name); // 여기서 에러 발생!
```
위 코드는 에러가 납니다. 왜냐하면 `name`이라는 변수가 `insert` 되는 순간, 소유권이 `map`으로 넘어가 버렸기 때문입니다. 이제 `name`은 더 이상 사용할 수 없는 빈 껍데기가 됩니다.

**해결책:**
만약 계속해서 `name` 변수를 쓰고 싶다면 `name.clone()`을 해서 복사본을 넣거나, `&str` 같은 참조자를 키로 사용해야 합니다. 하지만 참조자를 키로 쓸 때는 '라이프타임'이라는 더 어려운 개념이 나오니, 일단은 `clone()`을 사용하거나 소유권을 넘긴다는 점을 명심하세요!

---

## 마무리하며

오늘 우리는 Rust의 강력한 도구인 HashMap을 정복했습니다.

- **데이터를 빠르게 찾고 싶을 때** $\rightarrow$ HashMap!
- **넣을 때는** `insert`, `from`, `extend`!
- **꺼낼 때는** `get`과 `match`로 안전하게!
- **수정할 때는** `entry` API로 스마트하게!

처음에는 `Option`이나 소유권 개념 때문에 머리가 조금 아플 수 있습니다. 하지만 이 고비만 넘기면 여러분은 Rust라는 무시무시한 무기를 자유자재로 다루는 고수가 될 수 있습니다.

포기하지 마세요. 제가 옆에서 계속 도와드릴게요. 다음 강의에서는 더 재미있고 유용한 내용으로 찾아오겠습니다. 수고하셨습니다!

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
