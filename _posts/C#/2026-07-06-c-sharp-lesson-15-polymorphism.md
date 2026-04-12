---
layout: single
title: "Polymorphism (다형성): 기본 개념 이해"
date: 2026-07-06 16:11:35
categories: [C#]
---

## 🔥  15강: Polymorphism (다형성) - 객체 지향 프로그래밍의 중심! 🚀

안녕하세요, C# 신입 개발자 여러분! 💪 이번 주에는 객체지향 프로그래밍에서 가장 매력적인 개념이기도 하고, 매우 중요한 개념인 **Polymorphism (다형성)**에 대해 깊이 있게 알아보겠습니다.  

진짜 이걸 이해하면 C# 개발 세계가 완전히 새로운 모습으로 변화할 거예요! 😎 

### ✨ 다형성의 의미? - 여러 모습을 가진 객체 🤔

자, Polymorphism이란 무엇일까요? 말 그대로 **'여러 형태를 가진 것'** 이라는 뜻이에요.  다형성은 하나의 인터페이스(혹은 기본적인 타입)에서 여러 다른 구현 방식을 가지게 하는 개념입니다. 다시 말해, 하나의 변수나 함수가 여러 다른 유형의 객체를 참조하는 능력을 말하는 거죠!

예를 들어, 가상 동물원을 생각해보세요. 🦁🐯🐰 다양한 종류의 동물이 있겠죠? 하지만 모두 '동물'라는 공통적인 특징을 가지고 있습니다. 그리고 모든 동물들은 '웃음소리를 내는', '걷는', '먹는' 등의 행동들을 합니다. 이때, 각 동물마다 웃음소리, 걸음 방식, 먹이는 것 등은 다르게 나타나는데요.  

바로 이런 **'동물'**이라는 공통적인 특징과 각 동물별로 다른 구현 방식을 **Polymorphism**라고 부릅니다. 🐘🦍🐒 멋진 비유였죠? 😉


### ## C# 에서의 다형성 - 코드로 살펴보기!

C#에서는 인터페이스와 추상 클래스를 사용하여 Polymorphism을 구현할 수 있습니다.

* **인터페이스:** 특정 행동이나 기능 세트를 정의하는 계약서라고 생각하면 됩니다.
* **추상 클래스:**  일부 메서드가 추상(구체적인 구현이 없음)이며, 실제로는 자손 클래스들이 구현해야 하는 부분을 제공합니다.

### 🤩 코드 예시: 다형성은 C# 개발자의 필수 도구! 🚀


```csharp
// 인터페이스를 정의합니다. '동물' 특징을 가지는 모든 동물이 이 인터페이스를 따릅니다.
public interface IDinosaurs
{
    void MakeSound(); 
    void Move(); 
}

// 공룡 클래스를 만들고, IDinosaurs 인터페이스를 구현합니다.
public class Tyrannosaurus : IDinosaurs
{
    public void MakeSound()
    {
        Console.WriteLine("RAWR!"); // 티라노사우루스 소리!
    }

    public void Move()
    {
        Console.WriteLine("강력하게 걷습니다."); 
    }
}

// 다른 공룡 종류를 만들고, IDinosaurs 인터페이스를 구현합니다.
public class Stegosaurus : IDinosaurs
{
    public void MakeSound()
    {
        Console.WriteLine("KREEEEEEEK!"); // 스테고사우루스 소리!
    }

    public void Move()
    {
        Console.WriteLine("차갑게 걷습니다.");
    }
}

// 다형성을 활용하여 여러 공룡 객체를 만들어봅니다.
IDinosaurs dino1 = new Tyrannosaurus(); 
IDinosaurs dino2 = new Stegosaurus();

dino1.MakeSound(); // "RAWR!" 출력
dino2.Move();     // "차갑게 걷습니다." 출력



```


### 🚀 다형성이 가져다주는 장점!

* **代码 재사용성 향상:** 한 인터페이스를 통해 여러 객체를 제어할 수 있어 코드 복잡성을 줄이고, 유지 보수가 용이합니다.

* **확장성 증대:** 새로운 클래스를 추가해도 기존 코드 변경 없이 동작하는 부분이 있기 때문에, 시스템 확장에 유리합니다.


### 💡 초보자 폭풍 질문! 🤔

Polymorphism이 정말 신기하게 보이죠? 🤩 다만 아직 복잡한 부분들이 많을 수 있어요. 마치 처음 타고난 자전거처럼, 어느 정도 달려야 본능적으로 이해가 된다는 거예요.  궁금해하는 점은 무엇인지 댓글로 남겨주세요!

---





<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
