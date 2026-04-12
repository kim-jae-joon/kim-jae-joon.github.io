---
layout: single
title: "List와 같은 Collections (Generic)"
date: 2026-07-11 16:10:26
categories: [C#]
---

##  10강: List와 같은 Collections (Generic) - C# 프로그래밍의 기초 다지기 🔥🚀

안녕하세요! 개발자 되고 싶은 당신들을 위한 꿀팁 투자, C# 액정 강좌의 10강! 🎉 이번 주는 C# 프로그래머에게 반드시 알아야 할 "Collection" 에 대해 알아보겠습니다. 마치 음식을 정리하는 '냉장고'와 같이 여러 값들을 하나로 모으는 기능을 가진 Collection은 프로그램의 기본 골격을 만드는데 필수적이죠! 

**어쩌면 C# 처음 접하고 'Collection' 이라는 단어도 이해가 안 되실 수 있어요. 그래도 걱정 마세요! 저, 당신의 친절한 C# 선생님이 여기 있는 거예요! 😄  함께 C# 프로그래밍 세계를 탐험하는 즐거움을 느껴봐요! 😎**

### **1. Collection: 여러 값을 한 곳에 모으는 마법 가방🪄**


> *C#에서 Collection은 데이터를 효율적으로 관리하고 사용할 수 있도록 도와주는 '정렬된 저장소'라고 생각해보세요.*  일반적인 변수는 하나의 값만 담을 수 있지만, Collection은 여러 개의 값을 한 번에 저장할 수 있습니다! 마치 옷장에 다양한 옷들을 정리하는 것처럼, Collection은 프로그램 내에서 데이터를 효율적으로 관리하는 데 도움을 줍니다.

**✨  예제: 간단한 목록 만들기**

```csharp
List<string> names = new List<string>(); // "names" 라는 이름의 목록 생성
names.Add("홍길동");           // "홍길동" 이름 추가
names.Add("전우치");          // "전우치" 이름 추가
names.Add("고길동");           // "고길동" 이름 추가

foreach (string name in names) 
{  
    Console.WriteLine(name); // 각 이름 출력
}
```

*  `List<string>`: 문자열을 저장하는 List를 생성합니다. 이 코드는 `string` 유형의 데이터만 저장할 수 있는 "names"라는 목록을 만들고, "홍길동", "전우치", "고길동"과 같은 이름들을 추가합니다. 
*  `foreach`: 'for' 루프보다 간결하게 리스트 내용을 하나씩 순회하며 출력하는 방법입니다.



### **2. List: 가장 널리 사용되는 Collection 💪**

List는 C#에서 가장 많이 쓰이는 Collection 중 하나로, 데이터를 **순서대로** 저장하고 관리할 수 있습니다. 마치 '식사 메뉴'처럼 일정한 순서에 따라 요소들을 나열할 때 유용합니다!  
> * 생각보다 List를 사용하는 경우가 많아요! 예를 들어, 온라인 쇼핑몰에서 상품 목록을 표시하거나 게임 캐릭터의 이름과 레벨을 저장할 때 List가 활용됩니다.*

**💡 초보자 폭풍 질문!**

 "Collection은 어떻게 만들까요?" 🤔  C#은 다양한 Collection 타입을 제공하며, 각 타입마다 특징이 있습니다. 예를 들어, `List`는 순서대로 데이터를 저장하는 반면, `Dictionary`는 키-값 쌍으로 데이터를 저장하는 방식을 사용합니다. 어떤 Collection을 사용해야 할지 선택할 때는 데이터의 특징과 목적을 고려하면 좋습니다!


### **3. Generic: 다양한 유형을 한 번에 처리! 🚀**

C#에서 "Generic"는 코드 재사용성을 높이는 강력한 기능입니다. 

> * 예를 들어, 'List'만 사용하려면 여러번 동일한 코드를 작성해야 하는 불편함이 있었죠? 그런데 Generic이라는 마법의 도구가 등장하면서!  `List<string>`와 `List<int>` 처럼 다양한 데이터 유형을 저장하는 'List'를 한 번만 만들고 사용할 수 있습니다!*

### **4. 실무 활용 사례: 프로그램 효율성 UP! 💯**


```csharp
// 게임 캐릭터 정보를 List로 관리하기
List<Character> characters = new List<Character>();
characters.Add(new Character("철수", 10, "검")); // 캐릭터 추가
characters.Add(new Character("영희", 15, "마법"));

foreach (Character character in characters) 
{  
    Console.WriteLine($"{character.Name} - 레벨: {character.Level}, 무기: {character.Weapon}");
}
```



* **Game Development:** 게임 캐릭터들의 이름, 수준, 장비 정보를 저장하여 관리합니다.

**🚨 실무주의보!** Collection은 데이터를 효율적으로 처리하는 데 매우 유용하지만, 쓸모없는 데이터를 모아서 메모리 사용량을 증가시키지 않도록 주의해야 합니다! 프로그램 성능에 영향을 미칠 수 있으니 항상 효율적인 코드 작성이 중요합니다.


### **5. 마무리: C# 프로그래머로 향한 첫걸음 🚀**

Collection은 C# 프로그래밍 기초 중 하나이며, 다양한 프로그램 개발에 필수적으로 사용됩니다. 이 10강을 통해 Collection의 개념과 활용법을 이해했다면, C# 프로그래밍 세계를 더욱 쉽게 탐험할 수 있도록 도와줄 것입니다! 🎉


**앞으로도 여러분이 C# 프로그래머로 성장하는 데 도움이 되는 강좌들을 만들어 나갈 예정입니다!  👍 참고하세요. 그리고 언제든지 질문은 해주세요, 저는 항상 당신 곁에 있답니다! 😉**




<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
