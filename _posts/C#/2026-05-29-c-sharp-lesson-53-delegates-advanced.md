---
layout: single
title: "C# Delegates: 함수를 인자로 전달하기"
date: 2026-05-29 16:20:42
categories: [C#]
---

##  🔥53강: C# Delegates - 함수를 인자로 전달하기! 함수가 친구와 같이 놀 수 있는 마법 ✨


안녕하세요, 여러분! 👋 세계 최고의 C# 강사, 저희 엄마같은 시니어 개발자인 김태수입니다. 😎 오늘은 C# Delegates에 대해 알아보겠습니다.  

Delegates는 함수를 인자로 전달하는 마법 ✨  함수가 친구와 같이 놀 수 있게 하는 기능을 가졌다는 점, 듣고도 신기하죠? 😉


### 1. 함수란 무엇일까요? 🤔

먼저, 함수란 프로그램에서 특정 작업을 수행하는 블록입니다. 마치 레시피처럼 단계별로 지침이 들어있어서, 입력값을 받고 결과값을 반환하는 역할을 합니다. 🧑‍🍳


```csharp
// 간단한 함수 예시: 두 수를 더하는 함수
public int Add(int a, int b)
{
    return a + b; // 두 수의 합을 반환합니다
}

// 함수 호출 예시
int result = Add(5, 3); // result 변수에 8이 저장됩니다

```

* `public int Add(int a, int b)`:  이 부분은 함수 이름(Add), 자료형(인트), 입력값(a, b)을 정의하는 부분입니다.


### 2. Delegates는 왜 필요할까요? 🤔

C#에서 Delegates는 함수를 다른 변수에 저장하고, 그 변수를 사용하여 함수를 실행하는 역할을 합니다.  함수를 마치 물건처럼 전달하는 것과 같이 생각하면 이해하기 쉬워요! 🚀


```csharp
// Add 함수를 Delegates로 정의합니다
public delegate int Operation(int a, int b);

Operation add = Add; // Add 함수를 delegates 변수에 저장합니다

// delegates 변수를 사용하여 함수를 호출합니다
int result = add(5, 3); // result 변수에 8이 저장됩니다
```

* `public delegate int Operation(int a, int b);`: 이 부분은  'Operation'라는 Delegates 이름으로, 두 개의 인트값을 받고 int 값을 반환하는 함수를 대표할 수 있도록 정의합니다.


### 3. Delegates 활용 사례: 행사 발생 및 처리! 🎉

Delegates는 특정 작업이 일어날 때 어떤 동작을 수행해야 하는지 정의하는 데 유용하게 사용됩니다.  예를 들어, 창문에 클릭 이벤트가 발생했을 때 뭘 해야할지 Delegates를 이용하여 설정할 수 있습니다. 🪟🖱️


```csharp
// ClickEvent라는 Delegates를 정의합니다.
public delegate void ClickEvent(string message);

// 버튼 클릭 함수를 정의합니다.
public void ButtonClick(string message)
{
    Console.WriteLine("버튼이 클릭되었습니다! 메시지: {0}", message); 
}

// Delegates에 함수를 할당합니다.
ClickEvent clickHandler = ButtonClick;

// 버튼을 클릭하면 ClickEvent 함수가 실행됩니다.
clickHandler("Hello, World!"); // "버튼이 클릭되었습니다! 메시지: Hello, World!" 출력

```



### 💡 초보자 폭풍 질문! 🤔


* Delegates는 함수를 저장하는 변수라고 하는데, 정말 그렇게 생각해도 될까요?
* 어떤 상황에서 Delegates가 특히 유용하게 사용될 수 있을까요?
*  Delegates의 장점과 단점은 무엇일까요?

---


### 4. 실무주의보🚨: Delegates는 C# 코딩에 필수적인 요소입니다! 🤩

Delegate를 이해하면 프로그램 구조화, 이벤트 처리 등 다양한 부분에서 더 효율적이고 전문적인 코드를 작성할 수 있습니다.  Delegates는 C# 개발자로서 꼭 알아야 하는 기술 중 하나이므로, 오늘 강의를 통해 Delegates에 대한 기본적인 이해를 갖도록 노력하겠습니다! 👍



---

**감사합니다! 😄 다음 강좌에서 C#의 또 다른 매력적인 기능을 함께 알아보자! 🚀  **





<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
