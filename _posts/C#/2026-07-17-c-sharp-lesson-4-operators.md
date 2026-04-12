---
layout: single
title: "연산자: 산술 연산자, 비교 연산자, 논리 연산자"
date: 2026-07-17 16:08:56
categories: [C#]
---

##  🔥🔥 C# 연산자 강좌: 코드는 식이야! 🔥

안녕하세요, C# 신드롬에 오신 것을 환영합니다! 😎 저는 대한민국 최고의 C# 일타 강사이자 15년차 시니어 개발자로, C#를 통해 코드 烹饪을 즐기는 당신과 함께 **매력적인 코드 세계**를 만들어 갈 준비가 되셨습니다. 🎉

오늘은 C# 프로그램의 기본 구성 요소 중 하나인 **연산자**에 대해 알아보겠습니다! 🔥 연산자들은 코드에서 데이터를 조작하고 처리하는 핵심 역할을 담당하며, 마치 레시피 속 재료들을 결합하여 새로운 음식을 만드는 것과 같죠! 🍲

다양한 종류의 연산자가 존재하지만, 크게 **3가지 카테고리**로 나눌 수 있습니다:

* **산술 연산자**:  일반적인 숫자 계산에 사용되는 + , -, * , / , % 등의 연산자들이죠.
    💡 초보자 폭풍 질문! : “%” 는 무엇이라고? 🤔

* **비교 연산자**: 두 값을 비교하여 True 또는 False를 반환하는 연산자들입니다. 예를 들어, `==`, `<`, `>`,  `<=`, `>=`, `!=` 등이 있습니다.
    🚨 실무주의보 : 헷갈릴 수 있는 ‘=’와 ‘==’ 구분!  ‘=’는 값을 할당하고 ‘==’는 두 값의 비교를 한다는 것을 기억하세요!

* **논리 연산자**: 여러 조건들을 연결하여 True 또는 False를 결정하는 연산자들입니다. `&&` (AND), `||` (OR), `!` (NOT) 등이 있습니다.


### 👑 산술 연산자: 코드의 계산 기사!

산술 연산자는 C#에서 가장 기본적인 연산자 중 하나로, 우리가 일상생활에서 자주 사용하는 사칙연산에 해당합니다.  

```csharp
int num1 = 10;
int num2 = 5;

// 더하기 연산 (+)
int sum = num1 + num2;   // sum = 15
Console.WriteLine(sum);

// 뺴기 연산 (-)
int diff = num1 - num2;  // diff = 5
Console.WriteLine(diff);

// 곱하기 연산 (*)
int product = num1 * num2; // product = 50
Console.WriteLine(product);

// 나누기 연산 (/): 정수 나눗셈 결과는 음이 아닌 부분만 반환합니다.
int quotient = num1 / num2;  // quotient = 2
Console.WriteLine(quotient);

// 나머지 연산 (%): 두 수의 나눈 나머지를 구하는 연산자입니다.
int remainder = num1 % num2; // remainder = 0
Console.WriteLine(remainder);
```


### 🤔 비교 연산자: 코드의 판단관!

비교 연산자는 두 값을 비교하여 True 또는 False를 반환합니다. 이는 프로그램이 특정 조건에 따라 다른 작업들을 수행하는 데 매우 중요한 역할을 합니다! 

* `==` (같다): 두 값이 서로 같으면 True입니다.
   ```csharp
   int x = 5;
   int y = 5;
   bool isEqual = x == y; //isEqual = true
   ```
* `!=` (같지 않다): 두 값이 서로 다르면 True입니다.
    ```csharp
    int a = 10;
    int b = 7;
    bool isDifferent = a != b; //isDifferent = true
    ```

* `<` (작다): 첫 번째 값이 두 번째 값보다 작으면 True입니다.
   ```csharp
   int c = 3;
   int d = 8;
   bool isLess = c < d; //isLess = true
   ```
* `>` (크다): 첫 번째 값이 두 번째 값보다 크면 True입니다.
    ```csharp
    int e = 12;
    int f = 5;
    bool isGreater = e > f; //isGreater = true
    ```
* `<=` (작거나 같다): 첫 번째 값이 두 번째 값보다 작거나 같으면 True입니다.

   ```csharp
   int g = 10;
   int h = 10;
   bool isLessOrEqual = g <= h; //isLessOrEqual = true
   ```
* `>=` (크거나 같다): 첫 번째 값이 두 번째 값보다 크거나 같으면 True입니다.

   ```csharp
   int i = 20;
   int j = 15;
   bool isGreaterOrEqual = i >= j; //isGreaterOrEqual = true
   ```



### 🚀 논리 연산자: 코드의 조건문!

논리 연산자는 여러 조건을 연결하여 True 또는 False를 결정하는 역할을 합니다. 🤯

* `&&` (AND): 두 조건이 모두 True일 때만 True입니다.
   ```csharp
   bool isRaining = true;
   bool isCold = false;
   bool shouldCarryUmbrella = isRaining && isCold; //shouldCarryUmbrella = false
   Console.WriteLine(shouldCarryUmbrella); 
   ```
* `||` (OR): 두 조건 중 하나라도 True이면 True입니다.

   ```csharp
   bool isHungry = true;
   bool isTired = false;
   bool shouldEat = isHungry || isTired; //shouldEat = true
   Console.WriteLine(shouldEat);
   ```
* `!` (NOT): 조건의 값을 반전시킵니다.

   ```csharp
   bool isActive = true;
   bool isInactive = !isActive; //isInactive = false
   Console.WriteLine(isInactive); 
   ```



### 🚀 마지막으로, 연산자와 함께 만들어볼 코드!

* 우리는 C#를 사용하여 간단한 계산기를 구현해 보았습니다! 🎉 이러한 기본 연산자들을 활용하여 더 복잡하고 풍부한 프로그램을 개발할 수 있습니다. ✨





<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
