---
layout: single
title: "접근 지정자: private, public, protected"
date: 2026-07-11 16:58:26
categories: [C#]
---

##  C# 마스터 완벽 가이드: 10강 - 접근 지정자: private, public, protected

**🔥 안녕하세요! C# 주니어 개발자 '코딩 코치'입니다. 🔥** 오늘은 **접근 지정자**에 대해 알아보는 건데요, 이게 뭐냐고? 🤔  간단히 말하면, 우리 코드의 변수나 메서드가 어떤 부분에서 접근 가능할지 정하는 주석이라고 생각하면 돼요. 🤯 마치 게임 캐릭터를 만드는 거랑 비슷하죠! 캐릭터의 기술은 누구든 볼 수 있고, 맵은 유저만 보지만, 캐릭터 내부 코드는 개발자만 접근 가능하다는 식으로 말씀 드릴게요.

**💡 초보자 폭풍 질문!** 🤔 "코딩? 게임?" 라고 생각하고 계신가요?! 정말, 코드는 게임처럼 재밌어요! 🕹️


### **접근 지정자: 개념 이해하기**

접근 지정자는 우리 C# 코드의 구성 요소(변수, 메서드 등)를 다른 부분에서 접근할 수 있는 '범위'를 정해줍니다. 마치 주택에 들어갈 사람을 통제하는 '방문 인증 시스템'과 같은 역할이죠. 🔐

**🔑 세 가지 주요 접근 지정자**

1. **`private`**:  
   - 이게 가장 안전한 방어벽같아요! 💪  직접 정의된 클래스 내부에서만 사용 가능합니다. 마치 '개인 정보' 처럼, 외부로 노출시키지 않고 안전하게 보호하는 역할이죠.

2. **`public`**:
   - 이건 모든 곳에서 접근 가능하다는 '열린 문'과 같아요!  👋 어떤 클래스든 사용할 수 있습니다. 마치 공개된 정보처럼, 널리 공유하고 활용할 수 있도록 허용하는 역할이죠.

3. **`protected`**:
   - `private`보다는 조금 더 광범위하게 접근 가능하답니다. 🤔  같은 클래스나 그 클래스를 상속한 다른 클래스에서만 사용 가능합니다. 마치 '가족 단위' 처럼, 가족 구성원끼리만 공유할 수 있는 정보라는 식으로 생각하면 쉬워요!

**🚨 실무주의보:**
- 접근 지정자를 잘 활용하면 코드의 안전성과 유지 보수성을 크게 높일 수 있습니다.


### **코드 예제로 더 쉽게 이해하기**

```C#
public class Person // public이므로 모든 곳에서 사용 가능!
{
    private string name; // private으로 정의되어 클래스 내부에서만 접근 가능!
    protected int age; // protected로, 같은 클래스나 상속된 클래스에서만 접근 가능

    public void SetName(string newName) 
    {  // public 메서드로 이름을 변경
        name = newName;
    }

    public string GetName() // public으로 정의되어 모든 곳에서 이름 얻어올 수 있음
    {
        return name;
    }

    public int GetAge() 
    {  
        return age;
    }
}

public class Student : Person // Person을 상속하는 새로운 클래스!
{
    public void Study() // 학생만 할 수 있는 동작!
    {
        Console.WriteLine($"{this.GetName()}는 공부하고 있습니다.");
    }
}
```

**👨‍💻 코드 풀이 시간:**

1.  `public class Person`: 이 클래스는 `Person`과 같은 이름으로 정의되었고, 외부에서 사용할 수 있게 `public` 접근 지정자가 사용되었습니다. 😊

2.  `private string name`: 변수 `name`은 `private`로 정의되어, `Person` 클래스 내부에서만 접근 가능합니다. 마치 이름은 비밀이라고 생각하면 쉬워요! 😉

3.  `protected int age`: 변수 `age`는 `protected`로 정의되어, `Person`과 `Student`처럼 상속된 클래스에서도 접근 가능합니다. 학생 정보는 같은 가족인 성인에게 알려주면 좋지만, 바깥 사람들에게는 안 보여야 한다고 생각하면 됩니다!

4.  `public void SetName(string newName)`: 이 메서드는 이름을 변경하는 기능을 가지고 있으며, `public` 접근 지정자로 정의되어, 어떤 클래스에서든 사용할 수 있습니다.

5.  `public string GetName()`: 이 메서드는 현재 이름을 반환하는 기능을 가지고 있으며, `public` 접근 지정자로 정의되어, 어떤 클래스에서든 사용할 수 있습니다.

6.  `public int GetAge()`: 이 메서드는 나이를 반환하는 기능을 가지고 있으며, `public` 접근 지정자로 정의되어, 어떤 클래스에서든 사용할 수 있습니다.

7.  `public class Student : Person`: `Student` 클래스는 `Person` 클래스를 상속받았습니다! 继承


**👨‍💻코딩 코치 추천:**
- 위 코드처럼 접근 지정자를 잘 활용하면, 코드의 가독성과 유지보수성을 높일 수 있습니다.
- 다양한 예제를 통해 접근 지정자의 사용법을 익히고, 실제 프로젝트에서 적용해보세요!





<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
