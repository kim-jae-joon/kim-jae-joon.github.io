---
layout: single
title: "연산자: 산술 연산 및 비교 연산"
date: 2026-07-17 16:57:02
categories: [C#]
---

##  C# 공략! 연산자: 산술 연산 & 비교 연산 🚀

안녕하세요, 개발 세계로 뛰어들어보려는 여러분! 저는 당신을 위한 C# 마법사✨, 5년 차 주니어 개발자가 바로 제가시죠! 오늘은 "연산자"에 대해 알아볼 거예요. 연산자는 생각보다 신기한 존재이고, 코드를 쓰는 데 필수적이니까 집중해서 들어주세요! 

### 1. 산술 연산: 숫자가 달라지는 마법 ✨

먼저 **산술 연산**은 숫자에 대한 작동을 해서 새로운 숫자를 만들어내는 거예요. 마치 계산기처럼, 더하기, 빼기, 곱하기, 나누기 등이 있습니다!

- `+` (더하기): 두 숫자를 합쳐줍니다. 예를 들어 `5 + 3` 는 `8` 이 되지요! 😄
  ```C#
  int a = 5;
  int b = 3;
  int sum = a + b; // sum은 8이라는 값을 가집니다!
  Console.WriteLine(sum); // 결과값인 8을 출력해 주세요!
  ```

- `-` (빼기): 두 숫자의 차를 계산합니다. 예를 들어 `10 - 4` 는 `6` 이 되죠? 🤔

  ```C#
  int num1 = 10;
  int num2 = 4;
  int diff = num1 - num2; // diff는 6이라는 값을 가집니다!
  Console.WriteLine(diff); // 결과값인 6을 출력해 주세요!
  ```

- `*` (곱하기): 두 숫자를 곱합니다. 예를 들어 `7 * 3` 는 `21` 이죠? 😉

  ```C#
  int num3 = 7;
  int num4 = 3;
  int product = num3 * num4; // product는 21이라는 값을 가집니다!
  Console.WriteLine(product); // 결과값인 21을 출력해 주세요!
  ```

- `/` (나누기): 두 숫자를 나눕니다. 예를 들어 `12 / 3` 는 `4` 이죠? 👍


  ```C#
  int num5 = 12;
  int num6 = 3;
  int quotient = num5 / num6; // quotient는 4이라는 값을 가집니다!
  Console.WriteLine(quotient); // 결과값인 4를 출력해 주세요!
  ```

### 💡 초보자 폭풍 질문!

- "연산자 순서랑 무슨 관련 있을까요?" - 그건 다 나중에 자세히 알려드릴 테니까 지금은 기본 개념부터 익혀봐도 좋겠죠?
- "진짜 이걸로 계산할 수 있다면, 매시다..." - 응! 바로 계산 가능해요. 마치 연산자를 사용하는 것처럼 코드에서 직접 계산하는 거라고 생각하면 이해하기 더 쉬울 거예요!

### 2. 비교 연산: 두 값을 비교하여 True/False를 알려주는 요정🧚‍♀️

**비교 연산자**는 두 값을 비교해서 "참(true)" 또는 "거짓(false)"를 돌려줍니다. 이걸로 조건문에 활용해서 코드의 흐름을 바꿀 수 있죠!

- `==` (같음): 두 값이 같으면 true, 다르면 false입니다. 예를 들어, `5 == 5` 는 true이고, `10 == 7` 는 false예요.

  ```C#
  int num7 = 5;
  int num8 = 5;
  bool isEqual = num7 == num8; // isEqual은 true라는 값을 가집니다!
  Console.WriteLine(isEqual); // 결과값인 true를 출력해 주세요!
  ```

- `!=` (다름): 두 값이 같지 않으면 true, 같으면 false입니다. 예를 들어 `3 != 7` 는 true이고 `5 != 5` 는 false예요.

  ```C#
  int num9 = 3;
  int num10 = 7;
  bool isNotEqual = num9 != num10; // isNotEqual은 true라는 값을 가집니다!
  Console.WriteLine(isNotEqual); // 결과값인 true를 출력해 주세요!
  ```

- `>`, `<`, `>=`, `<=` (크기 비교): 각각 "더 큰", "더 작은", "같거나 크거나", "같거나 작거나" 라는 비교 조건을 나타냅니다.

  ```C#
  int num11 = 10;
  int num12 = 5;
  bool isGreater = num11 > num12; // isGreater은 true라는 값을 가집니다!
  Console.WriteLine(isGreater); // 결과값인 true를 출력해 주세요!
  ```

### 🚨 실무주의보: 조심해야 할 점!

- 산술 연산의 경우, 서로 다른 자료형을 사용하면 오류가 발생할 수 있습니다! 예를 들어, `int` 값과 `string` 값을 더하려면 데이터 형변환이 필요합니다. 주의하세요! ⚠️
- 비교 연산자는 항상 두 개의 값에 적용됩니다. 한개만 입력하면 에러가 나오기 때문에 주의해야 합니다!



### 3. 연습, 연습, 또 연습 💪

이제 이 모든 것을 바탕으로 코드를 직접 만들어보세요! 다양한 연산자를 사용해서 작은 계산 프로그램을 만들면서 C# 실력을 키워봐요! 😉




<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
