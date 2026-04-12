---
layout: single
title: "Lambda Expression: 비어진 함수 정의"
date: 2026-06-29 16:13:08
categories: [C#]
---

## 22강: Lambda Expression - 비어진 함수 정의? 🤔  아니, 마법같은 코드 표현! ✨

안녕하세요, C# 신비사입니다! 매번 멋진 코딩 주문을 가르쳐드리는 천재 개발자들이죠.😎 이제 우리는 C#'s 최첨단 기술 "Lambda Expression" 을 배우게 될 거예요! 

🔥 **Lambda Expression**은 간결하고 강력한 코드 표현 방식으로, 함수를 직접 정의하지 않고 바로 사용할 수 있게 해주는 마법같은 존재입니다. 마치 요리하는데 레시피 대신 "매콤하게" 하라고 말하는 것처럼 쉽죠! 😉

### 🤔 Lambda Expression: 비어진 함수? 아니, 완벽한 표현!

`Lambda Expression` 은 이름에 비해 "비어있는 함수" 라는 오해를 가지고 있을 수 있습니다. 그러나 실제로는 단순히 함수의 구조를 간략하게 나타내는 도구일 뿐,  실체적인 함수를 정의하지 않는 역할을 합니다. 생각만 해도 신기하죠?🤯

예를 들어, "사람 이름"과 "나이"를 입력하면 "안녕하세요! [이름]님, 나이는 [나이]세 입니다." 라는 문장을 출력하는 간단한 함수를 만들어 보겠습니다. 

```C#
// 일반적인 함수 정의
public void PrintGreeting(string name, int age)
{
    Console.WriteLine("안녕하세요! " + name + "님, 나이는 " + age + "세 입니다.");
}

// Lambda Expression을 이용한 표현
Action<string, int> printGreeting = (name, age) =>
{
    Console.WriteLine("안녕하세요! " + name + "님, 나이는 " + age + "세 입니다.");
}; 

// 함수 호출
printGreeting("홍길동", 30); 
```


#### 코드 설명 분석 🚀

1.  `public void PrintGreeting(string name, int age)` : 이 부분은 이름이 'PrintGreeting'인 일반적인 함수 정의입니다. `string name`, `int age` 는 입력 값을 받는 변수를 선언하고,  `Console.WriteLine(...)` 은 문장 출력을 합니다. 

2. `Action<string, int> printGreeting = ...`: `Lambda Expression` 을 사용하는 부분입니다. `Action<string, int>` 는 두 개의 파라미터 (문자열, 정수)를 받아 실행되는 함수 타입을 나타내는 인터페이스입니다. 
    -  `printGreeting` 변수에 `Lambda Expression`을 할당하여 함수를 직접 정의하지 않고 사용합니다.

3. `(name, age) => { ... }`: 이 부분이 바로 `Lambda Expression` 입니다! 좌측은 파라미터 목록 ( `name`, `age`) , 우측은 함수 실행 코드 (`Console.WriteLine(...)`)입니다. 간결하게 표현하는 것이 가장 큰 특징입니다!

4. `printGreeting("홍길동", 30);`: 함수를 호출합니다. 일반적인 함수와 동일하게 작동합니다.


###  💡 초보자 폭풍 질문! 🔥

-  `Lambda Expression` 은 어떤 상황에서 가장 유용할까요? 🤔
-  다른 코드 표현 방식과 비교했을 때 장점이 무엇인가요? 🤩



### 🚨 실무주의보: 🎯 Lambda Expression의 활용

`Lambda Expression` 을 활용하면 C# 프로그래밍이 더욱 간결하고 효율적으로 작성될 수 있습니다. 다음은 `Lambda Expression` 을 사용하는  일반적인 예시입니다:


* ** LINQ (Language Integrated Query)** : 데이터베이스 또는 Collection 에서 특정 조건에 맞는 데이터를 검색할 때 활용되는 강력한 도구입니다.

```C#
var result = products.Where(p => p.Price > 100).ToList(); // 가격이 100원 이상인 상품 목록
```

* **Delegate** : 함수 포인터와 유사한 역할을 하며,  `Lambda Expression` 을 사용하여 간결하게 정의할 수 있습니다.


```C#
Func<int, int> square = x => x * x; 
// 'square'는 입력값을 제곱하는 함수를 나타냅니다.
```

* **Event Handling** : 이벤트 발생 시 특정 작업을 실행하는 코드 작성시 간결하게 표현할 수 있습니다.


```C#
button.Click += (sender, e) => Console.WriteLine("버튼 클릭!"); // 버튼 클릭 이벤트 발생 시 "버튼 클릭!" 출력
```





## ✨ 마무리:  Lambda Expression으로 당신의 C# 코딩 실력을 업그레이드!


`Lambda Expression` 은 C# 프로그래밍의 진정한 매력을 느낄 수 있는 훌륭한 도구입니다. 처음 접하는 것은 어려울 수 있지만, 꾸준히 연습하면 코드를 더욱 간결하고 효율적으로 작성할 수 있게 될 것입니다! 🚀




<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
