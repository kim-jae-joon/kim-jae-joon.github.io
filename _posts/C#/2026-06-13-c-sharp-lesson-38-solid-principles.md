---
layout: single
title: "SOLID Principles: 소프트웨어 설계 원칙"
date: 2026-06-13 16:16:43
categories: [C#]
---

## 38강: SOLID Principles -  프로그램 설계의 비밀스러운 마법사 🧙‍♂️

안녕하세요, C# 마스터 가이드로 유명한 저(역할 부여 기준 맞춰서 이걸 적었습니다! 😎)가 다시 돌아왔습니다! 15년 동안 천지일과 달리 많은 개발자들을 지도해 온 경험을 바탕으로 오늘은  "SOLID Principles" 이야기를 나눠보려고 합니다. 🔥

**SOLID Principles? 🤔 그게 무슨 말이냐요?** 잠깐, 상상하세요. 건축가는 단순히 벽돌을 쌓는 게 아니라, 집의 구조, 기능, 미래 확장성까지 고려해서 설계를 한다죠?  프로그래밍 역시 마찬가지! SOLID Principles은 소프트웨어 '건물'을 설계할 때 사용하는 똑똑한 원칙들이에요.  💡 

이 원칙들은 코드의 질을 높이고 유지보수를 용이하게 만들며, 장기적인 프로젝트 성공에도 필수적인 요소라고 할 수 있습니다! 🚀


### 1. Single Responsibility Principle (SRP) - 한 줄로 정리하기는 어려워요!

> **"한 클래스가 하나의 책임만 가지도록 하라!"**  이게 SRP의 마법 비밀입니다. 마치 한 명의 서재에서 다양한 종류의 책을 관리하는 대신, 각 유형별로 따로 분류하여 관리한다는 느낌이죠. 📚

> 예를 들어, "User" 클래스가 있다고 가정해 보세요. 이 클래스가 사용자 정보 저장뿐만 아니라 로그인 기능도 담당하고 있을까요? 🤔 아닙니다! SRP에 따르면, User 클래스는 데이터 관리 역할에 집중하고 로그인 기능은 별도의 "AuthenticationService" 클래스로 분리해야 합니다.

```C#
// 잘못된 디자인: 모든 책임을 하나의 클래스에 뭉쳐놓음
public class User { //  사용자 정보, 로그인 기능, 데이터 저장 등... 😫

    public string Name { get; set; }
    public string Password { get; set; }

    public bool Login(string username, string password) {
        // ... 로직 ...
    }
}

// 올바른 디자인: 각 책임을 분담하여 유지보수 용이하게 설계함 🤘
public class User {
    public string Name { get; set; }

    // 사용자 정보 저장 로직 (데이터 관리)
    public void SaveUser(string name, string password){
        // ... 로직 ...
    }
}

public class AuthenticationService {
    public bool Login(string username, string password) { 
        // ... 로그인 기능 로직 ...
    }
}
```

### 2. Open/Closed Principle (OCP) -  변화는 막을 수 없죠!

> **"클래스는 확장되어야 하지만, 수정될해서는 안 된다!"** OCP는 새로운 기능 추가 시 코드를 변경하지 않고 확장할 수 있도록 설계하는 원칙입니다. 마치 가구에서 새 부품을 붙여 개선하는 것과 같죠!

> 예를 들어, "PaymentProcessor" 클래스가 있다고 가정해 보세요. 현재 신용카드 결제만 처리하고 있지만, 앞으로 은행 이체 등 다른 결제 방법을 추가해야 할 수 있습니다. 🤔  OCP에 따라, 새로운 결제 방법을 위한 인터페이스를 정의하고, 각 결제 유형별로 구현 클래스를 생성하여 PaymentProcessor 클래스에 연결하면 됩니다.

```C#
public interface IPaymentProcessor {
    void ProcessPayment(decimal amount);
}

public class CreditCardProcessor : IPaymentProcessor { // 신용카드 결제 처리 로직
    public void ProcessPayment(decimal amount) {
        // ... 신용 카드 결제 로직 ...
    }
}

public class BankTransferProcessor : IPaymentProcessor { // 은행 이체 결제 처리 로직
    public void ProcessPayment(decimal amount) {
        // ... 은행 이체 로직 ...
    }
}

public class PaymentProcessor {
    private readonly IPaymentProcessor _processor;

    public PaymentProcessor(IPaymentProcessor processor) { 
        _processor = processor; 
    }

    public void MakePayment(decimal amount){
        _processor.ProcessPayment(amount); // 결제 처리 로직 실행!
    }
}
```



### 3. Liskov Substitution Principle (LSP) -  아기 코끼리가 대신할 수 있어야 합니다!

> **"자식 클래스는 부모 클래스의 모든 역할을 제대로 수행해야 한다!"** LSP는 상속 관계에서 자식 클래스가 부모 클래스를 완벽하게 대체할 수 있도록 설계하는 원칙입니다. 마치 아기 코끼리가 어른 코끼리처럼 나무 뿌리를 먹거나 강물을 건너갈 수 있어야 하는 것과 같죠!

> 예를 들어, "Bird" (새) 클래스가 있다고 가정해 보세요. 이 클래스는 "Fly()" 메서드를 가지고 있습니다. 하지만 "Penguin" (펭귄) 같은 자식 클래스는 날지 못하므로 LSP에 위배됩니다. 

> 따라서, Penguin 클래스는 Fly() 메서드 대신 "Swim()" 메서드를 가진다면 LSP를 준수하게 되겠죠! 😎


```C#
public abstract class Bird { // 부모 클래스: 새
    public abstract void Fly(); // 날 수 있는 행동 (추상 메서드) 

}

public class Sparrow : Bird {  // 자식 클래스: 제비
    public override void Fly() {
        Console.WriteLine("제비가 하늘을 나는 모습!");
    }
}

public class Penguin : Bird { // 자식 클래스: 펭귄 (날지 못함!)
   // public override void Fly() {  // 날 수 없는 행동은 오류! 🚫
   //     Console.WriteLine("펭귄은 날수 없습니다."); 
   // }
    public void Swim(){ 
        Console.WriteLine("펭귄이 물 속에서 헤엄치는 모습!");
    }
}

```


### 4. Interface Segregation Principle (ISP) -  너무 많은 것을 요구하지 마세요!

> **"클래스가 필요로 하는 인터페이스만 구현하라!"** ISP는 클래스가 너무 많은 메서드를 가진 큰 인터페이스를 구현하게 되는 문제를 해결하는 원칙입니다. 마치 한 칼집으로 모든 종류의 채소를 잘게 자르려고 하기보다는, 각 채소에 맞는 다양한 도구를 사용하는 것과 같습니다!

> 예를 들어, "Animal" 인터페이스가 존재하고, 동물은 모두 "Move()" 메서드만 구현해야 하는 상황이라고 가정해 보세요. 하지만 낙타와 물개의 경우 "Swim()" 메서드는 필요하지 않습니다. 🤔 ISP에 따라, 각 동물 유형별로 적절한 인터페이스를 정의하여 클래스 설계를 세분화하는 것이 좋습니다.


```C#
public interface Animal {
    void Move(); // 모든 동물이 움직일 수 있다는 가정! 
}

// ISP 위반: 다양한 동물 유형들이 필요하지 않은 메서드를 구현해야 함
public class Camel : Animal{
    public void Move() {
        Console.WriteLine("낙타가 걸어갑니다.");
    }
}

public class Seal : Animal{
    public void Move() {
        Console.WriteLine("바다 개미가 헤엄칩니다.");
    }
}


// ISP 준수: 각 동물 유형에 맞는 인터페이스를 정의하여 코드 분산화 
public interface LandAnimal {
    void MoveOnLand(); // 땅 위에서 움직이는 동물

}

public interface SwimAnimal {
    void MoveInWater(); // 물속에서 움직이는 동물 
}


public class Camel : LandAnimal{
    public void MoveOnLand() {
        Console.WriteLine("낙타가 걸어갑니다.");
    }
}

public class Seal : SwimAnimal{
    public void MoveInWater() {
        Console.WriteLine("바다 개미가 헤엄칩니다.");
    }
}


```



### 5. Dependency Inversion Principle (DIP) -  존재하지 않는 걸 의존하게 하지 마세요!

> **"높은 레벨 모듈은 낮은 레벨 모듈을 직접 의존하지 말고, 추상적인 인터페이스를 통해 의존해야 한다!"** DIP는 프로그래밍의 심리학적 문제에 대한 해결책인 동시에 코드 유연성 향상 원칙입니다. 마치  전자제품이 특정 브랜드의 부품만 사용하도록 제작되는 것과 달리, 모든 제품에서 공통적으로 사용 가능한 인터페이스를 통해 의존성을 분리해야 합니다!

> 예를 들어, "EmailSender" 클래스가 있다고 가정해 보세요. 이 클래스는 현재 "GmailService"와 연결되어 이메일을 보내는 기능을 수행합니다. 

> 하지만 추후 "NaverMailService" 등 다른 이메일 서비스를 추가해야 하는 상황이 발생할 수 있습니다. DIP에 따라, EmailSender 클래스는 추상적인 "IEmailService" 인터페이스를 사용하도록 설계하여 변경 없이 새로운 이메일 서비스와 연결 가능하게 만들 수 있습니다!


```C#
// 잘못된 디자인: 구체적인 서비스에 의존 (DIP 위반) 🚨
public class EmailSender { 
    private GmailService _gmailService = new GmailService();

    public void SendEmail(string to, string subject, string body){
        _gmailService.SendEmail(to, subject, body); // GmailService에 직접 의존!
    }
}


// 올바른 디자인: 추상 인터페이스를 통해 의존성 분리 (DIP 준수)🤘 
public interface IEmailService {
    void SendEmail(string to, string subject, string body);
}

public class GmailService : IEmailService {
    public void SendEmail(string to, string subject, string body){
        // Gmail을 이용한 이메일 전송 로직
    }
}

public class NaverMailService : IEmailService { 
    public void SendEmail(string to, string subject, string body){
        // 네이버 메일에 이메일 전송 로직 
    }
}


public class EmailSender {  
    private readonly IEmailService _emailService;

    public EmailSender(IEmailService emailService) {
        _emailService = emailService; // 다른 서비스로 바꿔서 사용 가능!
    }

    public void SendEmail(string to, string subject, string body){
        _emailService.SendEmail(to, subject, body); 
    }
}



```





##  자료 정리 시간: SOLID Principles 리뷰🔥

* **SRP (Single Responsibility Principle):** 하나의 책임만 가진 클래스! 💪
* **OCP (Open/Closed Principle):** 확장 가능하되 수정 불가능! 🔓
* **LSP (Liskov Substitution Principle):** 자식 클래스는 부모를 완벽히 대체할 수 있어야 합니다! 🐧
* **ISP (Interface Segregation Principle):** 필요한 것만 구현하세요! 🎯
* **DIP (Dependency Inversion Principle):** 추상 인터페이스를 사용하여 의존성 분리!  🤝

## 마무리: SOLID Principles로 당신의 코드를 강화하세요 🚀

SOLID Principles는 단순히 문법이 아니라, 오랜 시간 동안 개발자들이 얻어낸 지혜입니다. 이 원칙들을 적용하면 유지보수가 쉬운, 확장성 있는 프로그램을 만들 수 있습니다! 😉  




<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
