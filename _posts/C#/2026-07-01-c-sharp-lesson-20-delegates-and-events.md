---
layout: single
title: "Delegates and Events: 이벤트 기반 프로그래밍"
date: 2026-07-01 16:12:37
categories: [C#]
---

##  20강: Delegates and Events - 이벤트 기반 프로그래밍으로 코드가 춤추게 해볼까요? 🚀

안녕하세요! 15년 차 시니어 개발자이자 C# 일타 강사인 저입니다. 🔥 오늘은 C#에서의 **Delegate**와 **Event**를 배우는 시간을 가질게요! 이 부분은 초보자들에게 처음 접하면 어렵게 느껴지는 부분이지만, 걱정 마세요! 저처럼 천재적인 강사에게 배운다면 아주 재밌고 이해하기 쉬워지겠죠?😎

Delegate와 Event는 C#에서 **프로그래밍의 이벤트 기반 방식**을 구현하는 데 사용됩니다. 마치 프로그램이 자체적으로 "발생"되는 이벤트에 대처하고, 반응할 수 있도록 돕는 것과 같아요! 이해하기 위해 우리가 일상 생활에서 익숙한 예시로 들어볼까요?

**💡 초보자 폭풍 질문!**:
>  C#의 Delegate와 Event를 통해 무슨 이벤트를 구현할 수 있을지 생각해 보세요. 🤔


### 1. Delegates - 프로그래머의 특별한 전달인 🚀

Delegate는 **함수 포인터**라고 할 수 있습니다. 마치 간판을 하나 만들어 그에 함수를 적고, 다른 곳에서 그 간판을 가져와 실행하는 것처럼 말이죠! 이렇게 Delegate를 사용하면 함수 호출 방식을 훨씬 더 유연하게 만들 수 있습니다. 예를 들어, 다음과 같은 C# 코드는 `Delegate`를 사용하여 함수 포인터를 정의하고,  실제 함수를 이 Delegate에 연결합니다.

```C#
// 함수 정의 - 우리가 실행할 함수!
public int Add(int x, int y) {
    return x + y;
}

// Delegate 선언 - 숫자 두 개를 입력받고 정수 값을 반환하는 함수 포인터
public delegate int NumberAdder(int x, int y);

// Delegate에 실제 함수를 연결!
NumberAdder adder = Add; // 이제 'adder'는 Add 함수가 저장되어 있다.

// 결과 출력
int result = adder(5, 3);
Console.WriteLine($"결과: {result}");
```


* `public delegate int NumberAdder(int x, int y);` :  이 코드로 우리가 사용할 Delegate의 이름을 "NumberAdder"라고 지정하고, 입력값은 두 개의 정수이고 반환 값도 정수라는 것을 알려줍니다. 마치 '전달 인'이라 불리는 이 전문가들은 함수들을 엄격하게 분류해주는 역할을 한다는 게 중요해요!
* `NumberAdder adder = Add;` : 여기서 "adder" 라는 변수에 우리가 정의한 `Add` 함수를 연결합니다.  '전달 인'이 '함수'를 지니게 되면 이제 'Adder'라는 이름으로 알려진 핵심적인 기능을 가지게 된거죠!

### 2. Events - 프로그램의 소리, 마치 공연처럼✨


Delegate는 함수가 작동하는 방식을 간편하게 표현해주지만, Event는 **이벤트 발생 시 이벤트 처리기를 실행**하게 해줍니다. 예를 들어, 버튼 클릭이라는 이벤트가 발생하면 연결된 이벤트 처리기 함수가 실행되게 하는 거죠!

```C#
public class ButtonClickEventHandler {
    // 이벤트를 정의합니다. (버튼 클릭!) 
    public event EventHandler ButtonClicked;

    // 이벤트 발생 시 호출되는 메소드
    public void OnButtonClicked() {
        if (ButtonClicked != null) { 
            ButtonClicked(this, EventArgs.Empty); // 이벤트 처리기를 실행!
        }
    }
}
```

* `public event EventHandler ButtonClicked;` :  이 부분에서 '버튼 클릭' 이벤트를 정의합니다. 마치 공연 무대에 대한 준비와 같죠! 🎪

* `public void OnButtonClicked() { ... }`: 버튼을 누르면, 이 메소드가 실행되고 이벤트 처리기를 호출하는 역할을 합니다.  이는 '음악 시작' 신호를 주는 것과 같은 의미입니다! 🎶


### 3. Delegate와 Event의 활용 - C# 프로그래밍에서의 실력 향상 🚀

Delegate와 Event는 단순히 함수를 표현하고 이벤트 처리기를 실행하는 것이 아니라, **프로세스 간 소통**을 가능하게 합니다. 마치 여러 사람들이 서로 메시지를 주고받는 것과 같죠!  C#에서 Delegate와 Event는 다음과 같은 상황에서 유용하게 사용됩니다:

* **GUI 애플리케이션**: 버튼 클릭, 창 닫기 등 사용자 인터페이스 이벤트 처리
* **멀티쓰레딩 프로그래밍**: 여러 쓰레드 간의 통신 및 데이터 공유
* **오픈소스 라이브러리 구현**: 플러그인 시스템 구축 및 확장성 제공

**🚨 실무주의보!**: Delegate와 Event를 잘 이해하면 C# 프로그래밍을 훨씬 효율적이고 관리하기 쉬운 방식으로 만들 수 있습니다. 이 부분에 대한 이해는 C# 개발자로서의 성숙도를 높이는 데 매우 중요합니다!


### 결론:  이벤트 기반 프로그래밍, 마치 프로그램과 소통하는 것처럼!

Delegate와 Event를 통해 C# 프로그램은 더욱 효율적이고 유연하게 설계될 수 있습니다. 이번 강의를 통해 Delegate와 Event의 개념을 이해하고, 실제로 코드에 적용해보세요!  프로그램을 춤추게 하는 마법 같은 이벤트 기반 프로그래밍 세계로 오디션을 보고 싶으신가요? 🔥

**오늘도 C# 배워서 재밌는 코딩 여정을 함께 시작해 보세요! 😎**

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
