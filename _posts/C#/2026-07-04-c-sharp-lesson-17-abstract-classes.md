---
layout: single
title: "Abstract Class: 추상 클래스 이해"
date: 2026-07-04 16:12:00
categories: [C#]
---

## 🔥  17강: Abstract Class - 추상 클래스 이해? 지금부터 알아볼까요?! 🚀

안녕하세요, 여러분! 최고의 C# 강사 "멋진 코드"와 함께 즐거운 코딩 여정을 시작합니다. 😎 오늘은 다소 어려워 보이는 단어인 **추상 클래스 (Abstract Class)**를 알아보는데, 이게 뭐냐? 왜 필요한 거지? 🤔  걱정 마세요! 오늘 "멋진 코드" 선생님이 가르쳐드릴테니, 초보자도 금방 이해할 수 있을 거예요. 😉

### **🤔 추상 클래스란 무엇일까요?**

> 추상 클래스는 완벽한 틀만 가지고 있는 건축 계획같아요. 실제로 집은 지금부터 시작하는거죠! 🔨  

그래, 맞습니다! 🐶추상 클래스는 아직 완성되지 않은 클래스라고 생각하면 편하답니다. 🎉 함수를 정의할 수 있지만, 이 함수들이 구현되어 있는 상태가 아니라는 것도 기억해주세요. 추상 클래스는 자식 클래스에서 채워져야만 하는 '약속'을 가지고 있어요! 🤝

### **✨ 추상 클래스의 장점은 무엇일까요?**

> 추상 클래스를 사용하면 여러 클래스들이 하나의 공통된 방식으로 동작하도록 만들 수 있어요. 마치 "모든 자동차는 엔진이 있어야 한다"라는 규칙을 정한 것처럼!  🚗💨

자, 이제 '멋진 코드' 선생님의 유명 코딩 비유를 통해 자세히 알아볼게요! ✨

* **다형성 (Polymorphism):** 추상 클래스는 여러 자식 클래스들이 하나의 인터페이스로 동작하도록 돕습니다.  Think of it like a remote control that works with different TVs. 📺 You can use the same buttons to change channels, adjust volume, etc., regardless of the TV brand! 🤯
* **코드 재사용성 (Code Reusability):** 추상 클래스는 공통적인 기능을 정의하여 자식 클래스에서 코드를 복붙하지 않고 사용할 수 있도록 해줍니다.  Think of it like building blocks. You can use the same block to build different structures, saving time and effort! 🏗️

### **⚠️ 실무주의보: 추상 클래스는 객체 지향 프로그래밍의 기본 개념 중 하나이므로, C# 개발자로서 반드시 이해해야 하는 중요한 개념입니다.**⚠️


### **📑 코드 예제 분석**

```csharp
public abstract class Animal 
{ //추상 클래스 선언! 🦁🦅🐦🐒  
    public string Name { get; set; } // 속성 정의 

    public abstract void MakeSound(); // 추상 메서드, 자식 클래스에서 구현! 🗣️  
}

public class Dog : Animal // Dog이라는 자식 클래스 선언!🐶
{
    public override void MakeSound() //MakeSound 메서드를 구체적으로 구현해주고 있습니다. 📢
    {
        Console.WriteLine("멍!");
    }
}

public class Cat : Animal //Cat이라는 자식 클래스 선언!🐱
{
    public override void MakeSound() //MakeSound 메서드를 구체적으로 구현해주고 있습니다.  🐈‍⬛
    {
        Console.WriteLine("야옹!");
    }
}

class Program
{
    static void Main(string[] args)
    {
        Dog dog = new Dog(); 
        dog.Name = "코기"; 
        dog.MakeSound(); //"멍!" 출력!

        Cat cat = new Cat(); 
        cat.Name = "고양이"; 
        cat.MakeSound(); //"야옹!" 출력!
    }
}
```

**🤔 이해하셨나요? 🤔**  'Animal'이 추상 클래스이고, 'Dog'와 'Cat'이 자식 클래스예요.  🐶🐱 각각의 동물은 다양한 소리를 내는데, 이를 구현하는 'MakeSound()' 메서드는 각 자식 클래스에서 달리 정의되어있죠!


### **💡 초보자 폭풍 질문!:**

* 추상 클래스와 인터페이스는 무엇이 다른지 알고 싶어요? 🤔
* 추상 메서드를 구현하지 않으면 어떻게 되나요? 🤨





<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
