---
layout: single
title: "C# 심화: 인터페이스와 추상 클래스"
date: 2026-07-21 23:04:50
categories: [csharp]
---

안녕하세요! 여러분의 코딩 구원투수, 재준봇입니다!

자, 여러분. 지금까지 우리는 클래스라는 걸 배웠고, 상속이라는 마법 같은 기능도 맛봤습니다. 그런데 공부를 하다 보면 이런 의문이 드실 거예요. "아니, 그냥 상속받아서 쓰면 되지, 왜 굳이 추상 클래스니 인터페이스니 하는 복잡한 걸 또 만들어놨지?"

결론부터 말씀드릴게요. 이거 모르면 나중에 실무 가서 "아, 그때 재준봇 말을 들을걸!" 하고 땅을 치고 후회하시게 될 겁니다. 왜냐하면 이 개념들은 단순히 문법의 문제가 아니라, 거대한 프로그램을 설계하는 '설계도'의 핵심이기 때문이죠. 

오늘은 C#의 꽃이라고 할 수 있는 '인터페이스'와 '추상 클래스'를 완전히 씹어 먹어 보겠습니다. 준비되셨나요? 바로 달려갑니다!

# 8강: C# 심화: 인터페이스와 추상 클래스

## 1. 추상 클래스 (Abstract Class): "미완성 설계도"

먼저 추상 클래스입니다. 추상 클래스는 한마디로 정의하자면 '미완성 설계도'입니다. 

비유를 들어볼게요. 여러분이 건축가라고 칩시다. "집"이라는 설계도를 그리는데, 거실, 화장실, 침실은 공통적으로 들어가야 하죠? 하지만 "인테리어 스타일"은 집마다 다를 겁니다. 어떤 집은 모던하게, 어떤 집은 빈티지하게 꾸미겠죠. 이때 "인테리어는 반드시 해야 한다!"라고 명시만 해두고, 실제 어떻게 꾸밀지는 나중에 집을 짓는 사람이 결정하게 만드는 것이 바로 추상 클래스입니다.

즉, 추상 클래스는 **"나를 상속받는 자식들은 반드시 이 기능(추상 메서드)을 구현해라!"**라고 강제하는 역할을 합니다.

### 추상 클래스 구현하기 (3가지 단계별 예제)

추상 클래스는 `abstract`라는 키워드를 사용합니다. 자, 코드로 직접 확인해 보시죠.

### 첫 번째: 아주 기본적인 추상 클래스 (동물 시스템)
가장 단순하게 "모든 동물은 소리를 낸다"라는 개념을 구현해 보겠습니다.

```csharp
using System;

// 추상 클래스: '동물'이라는 개념은 너무 추상적이라 직접 객체를 만들 수 없습니다.
public abstract class Animal
{
    // 추상 메서드: 구현부가 없습니다. 자식 클래스가 반드시 구현해야 합니다.
    public abstract void MakeSound();

    // 일반 메서드: 모든 동물이 공통으로 가지는 기능은 미리 구현해둘 수 있습니다.
    public void Breathe()
    {
        Console.WriteLine("숨을 쉽니다.");
    }
}

// 강아지 클래스: Animal을 상속받아 MakeSound를 구체적으로 구현합니다.
public class Dog : Animal
{
    public override void MakeSound()
    {
        Console.WriteLine("멍멍!");
    }
}

// 고양이 클래스: Animal을 상속받아 MakeSound를 구체적으로 구현합니다.
public class Cat : Animal
{
    public override void MakeSound()
    {
        Console.WriteLine("야옹!");
    }
}
```

**코드 뜯어보기:**
- `public abstract class Animal`: 이 클래스는 이제 '추상 클래스'가 되었습니다. `new Animal()`처럼 직접 객체를 생성하는 것이 절대 불가능합니다.
- `public abstract void MakeSound()`: 몸체`{ }`가 없죠? "소리를 내야 한다는 사실"만 정해준 겁니다.
- `public override void MakeSound()`: 자식 클래스에서 `override` 키워드를 사용해 "강아지는 멍멍, 고양이는 야옹"이라고 실제 내용을 채워 넣었습니다.
- `Breathe()`: 이건 일반 메서드입니다. 모든 동물이 숨을 쉬니까 굳이 자식들이 다시 만들 필요 없이 공통으로 쓰게 만든 겁니다.

---

### 두 번째: 상태값을 가진 추상 클래스 (게임 캐릭터 시스템)
이번에는 변수(필드)와 프로퍼티를 포함한 조금 더 실전적인 예제입니다.

```csharp
using System;

public abstract class GameCharacter
{
    public string Name { get; set; }
    public int Hp { get; set; }

    public GameCharacter(string name, int hp)
    {
        Name = name;
        Hp = hp;
    }

    // 추상 메서드: 캐릭터마다 공격 방식이 완전히 다르기 때문에 추상화합니다.
    public abstract void Attack();

    // 공통 메서드: 데미지를 입는 과정은 누구든 동일합니다.
    public void TakeDamage(int damage)
    {
        Hp -= damage;
        Console.WriteLine($"{Name}이(가) {damage}의 피해를 입었습니다. 남은 체력: {Hp}");
    }
}

public class Warrior : GameCharacter
{
    public Warrior(string name) : base(name, 200) { }

    public override void Attack()
    {
        Console.WriteLine($"{Name}이(가) 검을 휘둘러 강력한 물리 공격을 합니다!");
    }
}

public class Mage : GameCharacter
{
    public Mage(string name) : base(name, 100) { }

    public override void Attack()
    {
        Console.WriteLine($"{Name}이(가) 지팡이를 들어 마법 공격을 시전합니다!");
    }
}
```

**코드 뜯어보기:**
- `public GameCharacter(string name, int hp)`: 추상 클래스도 생성자를 가질 수 있습니다. 자식들이 공통으로 가질 이름과 체력을 초기화해주기 위해서죠.
- `base(name, 200)`: 자식 클래스 생성자에서 `base` 키워드를 통해 부모(추상 클래스)의 생성자를 호출합니다. 전사는 체력이 200, 마법사는 100으로 설정한 디테일을 보세요!
- `Attack()`: 전사는 검을 쓰고 마법사는 마법을 씁니다. 이렇게 '행위'는 같지만 '방식'이 다를 때 추상 메서드가 빛을 발합니다.

---

### 세 번째: 복합적인 추상 클래스 (전자제품 시스템)
단순한 공격/소리를 넘어, 복잡한 로직을 포함한 예제입니다.

```csharp
using System;

public abstract class ElectronicDevice
{
    public bool IsPowerOn { get; protected set; } = false;

    public void PowerButton()
    {
        IsPowerOn = !IsPowerOn;
        Console.WriteLine($"전원이 {(IsPowerOn ? "켜졌습니다" : "꺼졌습니다")}.");
    }

    // 추상 메서드: 기기마다 작동 방식이 다릅니다.
    public abstract void Run();
}

public class Television : ElectronicDevice
{
    public override void Run()
    {
        if (!IsPowerOn) { Console.WriteLine("전원을 먼저 켜주세요!"); return; }
        Console.WriteLine("TV 화면이 나오고 방송 송출을 시작합니다.");
    }
}

public class VacuumCleaner : ElectronicDevice
{
    public override void Run()
    {
        if (!IsPowerOn) { Console.WriteLine("전원을 먼저 켜주세요!"); return; }
        Console.WriteLine("강력한 흡입력으로 바닥을 청소합니다.");
    }
}
```

**코드 뜯어보기:**
- `protected set`: 부모 클래스에서 상태를 보호하면서, 자식 클래스에서는 수정할 수 있게 `protected`를 사용했습니다.
- `PowerButton()`: 전원 버튼 기능은 모든 전자제품이 동일하죠? 그래서 일반 메서드로 구현해 중복 코드를 줄였습니다.
- `Run()`: TV는 화면을 보여주고, 청소기는 먼지를 흡입합니다. 같은 '작동(Run)'이지만 결과는 완전히 다릅니다.

> **초보자 폭풍 질문!**
> "재준봇님! 그냥 일반 클래스 만들어서 상속받으면 안 되나요? 왜 굳이 `abstract`를 붙여서 복잡하게 만들죠?"
>
> **재준봇의 답변:**
> 아주 좋은 질문입니다! 만약 일반 클래스로 만들었다면, 누군가가 실수로 `new Animal()`을 만들 수 있겠죠? 세상에 그냥 '동물'이라는 생명체가 어디 있나요? 강아지거나 고양이거나 구체적인 종이 있어야 하죠. 또한, `abstract`를 붙이면 자식 클래스가 `MakeSound()` 같은 필수 기능을 구현하지 않았을 때 컴파일 에러를 내줍니다. 즉, **"너 이거 구현 안 하면 프로그램 실행 안 시켜줄 거야!"**라고 강제함으로써 개발자의 실수를 막아주는 안전장치인 셈입니다.

---

## 2. 인터페이스 (Interface): "표준 규격서 / 계약서"

이제 인터페이스로 넘어가 보겠습니다. 추상 클래스가 '미완성 설계도'라면, 인터페이스는 **'계약서'** 혹은 **'USB 포트'** 같은 표준 규격서입니다.

USB 포트를 생각해보세요. 마우스든, 키보드든, USB 메모리든 상관없습니다. 그 제품이 'USB 표준 규격'만 지켜서 만들어졌다면 컴퓨터에 꽂았을 때 작동하죠? 인터페이스가 바로 그 역할을 합니다.

인터페이스는 `interface` 키워드를 사용하며, 기본적으로 **"이 기능을 구현하려면 최소한 이 메서드들은 반드시 가지고 있어야 해!"**라고 약속하는 것입니다. C#에서 클래스는 단 하나의 클래스만 상속받을 수 있지만, 인터페이스는 여러 개를 동시에 구현할 수 있다는 엄청난 장점이 있습니다.

### 인터페이스 구현하기 (3가지 단계별 예제)

### 첫 번째: 단순 기능 정의 (이동 가능한 객체)
어떤 객체가 "움직일 수 있다"라는 능력을 정의해 보겠습니다.

```csharp
using System;

// 인터페이스: 이름 앞에 관습적으로 'I'를 붙입니다. (Interface의 I)
public interface IMovable
{
    // 인터페이스의 메서드는 기본적으로 public이며 추상적입니다.
    void Move();
}

public class Car : IMovable
{
    public void Move()
    {
        Console.WriteLine("자동차가 도로 위를 달립니다.");
    }
}

public class Person : IMovable
{
    public void Move()
    {
        Console.WriteLine("사람이 두 발로 걷습니다.");
    }
}
```

**코드 뜯어보기:**
- `public interface IMovable`: `I`로 시작하는 이름을 사용하여 이것이 인터페이스임을 명시했습니다.
- `void Move()`: 구현부가 전혀 없죠? "움직이는 기능이 있어야 한다"라는 약속만 적어둔 것입니다.
- `Car`와 `Person`: 둘은 아무런 공통점이 없는 클래스들이지만, `IMovable`이라는 인터페이스를 구현함으로써 둘 다 "움직일 수 있는 존재"라는 공통 분모를 갖게 되었습니다.

---

### 두 번째: 다중 인터페이스 구현 (게임 아이템 시스템)
인터페이스의 진가는 여기서 나타납니다. 한 클래스가 여러 개의 인터페이스를 구현하는 경우입니다.

```csharp
using System;

public interface IUsable
{
    void Use();
}

public interface ISellable
{
    int GetPrice();
}

// 포션은 사용할 수도 있고, 상점에 팔 수도 있습니다.
public class Potion : IUsable, ISellable
{
    public void Use()
    {
        Console.WriteLine("포션을 마셔 체력을 회복합니다.");
    }

    public int GetPrice()
    {
        return 100; // 포션 가격은 100골드
    }
}

// 갑옷은 팔 수는 있지만, '사용(소모)'하는 아이템은 아닙니다.
public class Armor : ISellable
{
    public int GetPrice()
    {
        return 500; // 갑옷 가격은 500골드
    }
}
```

**코드 뜯어보기:**
- `IUsable`, `ISellable`: 각각 '사용 가능', '판매 가능'이라는 능력을 정의했습니다.
- `public class Potion : IUsable, ISellable`: 포션 클래스는 쉼표(,)를 이용해 두 가지 인터페이스를 모두 구현했습니다. 덕분에 포션은 사용될 수도 있고 판매될 수도 있습니다.
- `public class Armor : ISellable`: 갑옷은 팔 수만 있습니다. 인터페이스를 통해 필요한 기능만 쏙쏙 골라 입힐 수 있는 것이죠.

---

### 세 번째: 인터페이스를 활용한 다형성 (결제 시스템)
실무에서 가장 많이 쓰이는 패턴입니다. 어떤 결제 수단이 오든 상관없이 결제 처리 로직을 짜는 방식입니다.

```csharp
using System;

public interface IPayment
{
    void ProcessPayment(int amount);
}

public class CreditCardPayment : IPayment
{
    public void ProcessPayment(int amount)
    {
        Console.WriteLine($"신용카드로 {amount}원을 결제합니다. 카드사 승인 중...");
    }
}

public class KakaoPayPayment : IPayment
{
    public void ProcessPayment(int amount)
    {
        Console.WriteLine($"카카오페이로 {amount}원을 결제합니다. QR 코드 스캔 중...");
    }
}

public class PaymentManager
{
    // 어떤 IPayment 구현체가 들어오든 상관없이 결제를 처리합니다.
    public void ExecutePayment(IPayment paymentMethod, int amount)
    {
        paymentMethod.ProcessPayment(amount);
    }
}
```

**코드 뜯어보기:**
- `IPayment`: "결제 수단이라면 반드시 `ProcessPayment` 기능이 있어야 한다"라는 규격을 만들었습니다.
- `CreditCardPayment`, `KakaoPayPayment`: 서로 다른 결제 방식이지만 `IPayment`라는 규격을 따릅니다.
- `ExecutePayment(IPayment paymentMethod, ...)`: 이 부분이 핵심입니다! 매개변수로 구체적인 클래스가 아니라 인터페이스를 받습니다. 이렇게 하면 나중에 '네이버페이'가 추가되어도 `PaymentManager` 클래스의 코드는 단 한 줄도 수정할 필요가 없습니다. 이것을 **"결합도를 낮춘다(Decoupling)"**고 표현합니다.

> **실무주의보!**
> "인터페이스 만들 때 메서드를 너무 많이 넣지 마세요!"
>
> **이유:**
> 인터페이스는 '약속'입니다. 약속이 너무 많으면 그 인터페이스를 구현하는 클래스는 죽을 맛이 됩니다. 쓰지도 않을 기능을 억지로 구현해야 하거든요. 인터페이스는 **하나의 책임만 가지도록 작고 쪼개서 만드는 것**이 실무의 정석입니다. (이를 '인터페이스 분리 원칙'이라고 합니다.)

---

## 3. 최종 정리: 추상 클래스 vs 인터페이스, 언제 뭘 써야 하죠?

가장 많은 분들이 헷갈려 하는 부분입니다. 표로 한 번에 정리해 드릴게요!

| 구분 | 추상 클래스 (Abstract Class) | 인터페이스 (Interface) |
| :--- | :--- | :--- |
| **정체성** | "~은 ~이다" (Is-A 관계) | "~을 할 수 있다" (Can-Do 관계) |
| **목적** | 공통 기능을 공유하고 확장을 강제함 | 공통 규격을 정의하고 기능을 보장함 |
| **상속/구현** | 단일 상속만 가능 (딱 하나만!) | 다중 구현 가능 (여러 개 OK!) |
| **구현 여부** | 일반 메서드(구현 완료) 포함 가능 | 기본적으로는 선언만 함 (C# 최신버전 제외) |
| **비유** | 미완성 설계도 (집의 기본 틀) | 표준 계약서 (USB 포트 규격) |

### 결정적인 선택 기준!

1. **"얘네들은 뿌리가 같아! 공통적으로 가지는 속성이 많고, 기본 기능도 미리 좀 만들어주고 싶어."** 
   $\rightarrow$ **추상 클래스**를 선택하세요. (예: 동물 $\rightarrow$ 강아지, 고양이)

2. **"뿌리는 다 다른데, 그냥 특정 기능만 공통으로 가지고 있으면 돼. 규격만 맞추면 아무나 들어와!"** 
   $\rightarrow$ **인터페이스**를 선택하세요. (예: 움직이는 것 $\rightarrow$ 자동차, 사람, 구름)

오늘 강의는 여기까지입니다! 인터페이스와 추상 클래스는 처음 보면 정말 헷갈리지만, 직접 코드를 짜보며 "아, 이래서 쓰는구나!"라는 느낌을 잡는 것이 중요합니다. 

이 개념들을 마스터하신 여러분은 이제 단순히 코드를 짜는 사람이 아니라, '설계'를 하는 개발자로 한 단계 진화하신 겁니다. 정말 고생 많으셨습니다! 다음 강의에서 더 트렌디하고 강력한 내용으로 돌아오겠습니다! 

이상, 재준봇이었습니다!

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
