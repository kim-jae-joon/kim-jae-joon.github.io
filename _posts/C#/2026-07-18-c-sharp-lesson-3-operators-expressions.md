---
layout: single
title: "C# 기초: 연산자와 표현식"
date: 2026-07-18 17:04:16
categories: [C#]
---

## 💥 C# 3강: 연산자와 표현식 - 코드 읽는 법을 배우세요!

**안녕하세요, C# 신입 개발자 여러분!**  🧙‍♂️ 저희 삼촌이 자랑스럽게 소개하는 **C# 기초 강좌**, 오늘은 "연산자와 표현식"에 집중해 볼 거예요. 흥미진진한 코드 세계로 들어서기 전, 잠시 여유를 가지고 우리 주변의 사물들을 생각해 보세요! 🤔  

* 당신이 좋아하는 과자 바구니는 어떻게 가득 채워졌을까요? (단순히 과자만큼 많을 수도 있지 않은가요?)
* 맛있는 피자 한 판은 몇 개의 토핑과 치즈로 만들어진 걸까요?
* 게임 캐릭터의 체력은 어떻게 계산되어 나올까요? (몬스터와의 격돌 후, 상황이 더욱 복잡해질 수 있죠?)

**예상하셨을까요? 이 세 가지 질문 모두 연산자와 표현식을 사용해서 답할 수 있습니다! 🎉**  바로 C# 코드에서도 똑같은 원리가 적용되고, 우리의 생각이 구체적인 결과물로 변화하는 것을 보여줄게요. 

### **연산자: 코드를 말하고 싶을 때,**

> "나에게 이 두 가지 값을 더해줘!"
> "이 두 값을 나눠서 소수점 아래까지 보기!"
> "이값만큼 자기 자신을 바꿔줄 수 있지 않을까?"  

연산자는 바로 **코드를 말할 때** 사용하는 도구예요. 코드가 더 정확하고 효율적으로 실행되도록 돕고, 생각한 방식으로 결과물을 얻을 수 있게 해줍니다. 🎉 마치 '더하기', '빼기', '곱하기', '나누기' 같은 연산자가 우리의 일상 생활에서 자주 사용되는 것처럼, 코드도 다양한 연산자를 통해 정보를 처리하고 변화시키는 거예요!  

#### 1. 산술 연산자: 계산을 좋아하는 친구들 😉

* **'+' (더하기):** 두 값을 합쳐 하나의 결과값으로 만듭니다.
    ```csharp
    int a = 5;
    int b = 3;
    int sum = a + b; // sum 변수에 8이 저장됩니다! 🤩
    Console.WriteLine(sum); // 화면에 "8"을 출력합니다!
    ```

* **'-' (빼기):** 첫 번째 값에서 두 번째 값을 뺍니다.
    ```csharp
    int a = 10;
    int b = 4;
    int difference = a - b; // difference 변수에 6이 저장됩니다! 🤩
    Console.WriteLine(difference); // 화면에 "6"을 출력합니다!
    ```

* **'*' (곱하기):** 두 값을 서로 곱하여 결과값을 만듭니다.
    ```csharp
    int a = 7;
    int b = 2;
    int product = a * b; // product 변수에 14가 저장됩니다! 🤩
    Console.WriteLine(product); // 화면에 "14"를 출력합니다!
    ```

* **'/' (나누기):** 첫 번째 값을 두 번째 값으로 나눕니다. 소수점이 발생하면 결과값은 실수 형태로 표현됩니다.
    ```csharp
    int a = 10;
    int b = 3;
    double quotient = a / b; // quotient 변수에 3.3333...가 저장됩니다! 🤩
    Console.WriteLine(quotient); // 화면에 "3.3333"를 출력합니다!
    ```

* **'%' (나머지 연산자):** 두 값을 나누었을 때 나머지를 구합니다. 

    ```csharp
    int a = 10;
    int b = 3;
    int remainder = a % b; // remainder 변수에 1이 저장됩니다! 🤩
    Console.WriteLine(remainder); // 화면에 "1"을 출력합니다!
    ```


#### 2. 비교 연산자:  같은지, 다른지는 알아보는 친구들 🤔

* **'==' (동등 연산자):** 두 값이 같은지를 확인합니다. 참(true) 또는 거짓(false) 값을 반환합니다.
    ```csharp
    int a = 5;
    int b = 5;
    bool isEqual = a == b; // isEqual 변수에 true가 저장됩니다! 🤩
    Console.WriteLine(isEqual); // 화면에 "True"를 출력합니다!
    ```

* **'!=' (불일치 연산자):** 두 값이 서로 다른지를 확인합니다. 참(true) 또는 거짓(false) 값을 반환합니다. 

   ```csharp
   int a = 5;
   int b = 10;
   bool isNotEqual = a != b; // isNotEqual 변수에 true가 저장됩니다! 🤩
   Console.WriteLine(isNotEqual); // 화면에 "True"를 출력합니다!
   ```

* **'>' (큰지 연산자):** 첫 번째 값이 두 번째 값보다 큰지 확인합니다. 참(true) 또는 거짓(false) 값을 반환합니다. 

    ```csharp
    int a = 10;
    int b = 5;
    bool isGreater = a > b; // isGreater 변수에 true가 저장됩니다! 🤩
    Console.WriteLine(isGreater); // 화면에 "True"를 출력합니다!
    ```

* **'<' (작은지 연산자):** 첫 번째 값이 두 번째 값보다 작은지 확인합니다. 참(true) 또는 거짓(false) 값을 반환합니다. 

   ```csharp
   int a = 5;
   int b = 10;
   bool isLess = a < b; // isLess 변수에 true가 저장됩니다! 🤩
   Console.WriteLine(isLess); // 화면에 "True"를 출력합니다!
   ```

* **'>=' (크거나 같은지 연산자):** 첫 번째 값이 두 번째 값보다 크거나 같은지를 확인합니다. 참(true) 또는 거짓(false) 값을 반환합니다. 

    ```csharp
    int a = 10;
    int b = 10;
    bool isGreaterOrEqual = a >= b; // isGreaterOrEqual 변수에 true가 저장됩니다! 🤩
    Console.WriteLine(isGreaterOrEqual); // 화면에 "True"를 출력합니다!
    ```

* **'<=' (작거나 같은지 연산자):** 첫 번째 값이 두 번째 값보다 작거나 같은지를 확인합니다. 참(true) 또는 거짓(false) 값을 반환합니다. 

   ```csharp
   int a = 5;
   int b = 10;
   bool isLessOrEqual = a <= b; // isLessOrEqual 변수에 true가 저장됩니다! 🤩
   Console.WriteLine(isLessOrEqual); // 화면에 "True"를 출력합니다!
   ```


#### 3. 논리 연산자: 진실과 거짓을 연결하는 친구들 🔗

* **'&&' (AND 연산자):** 두 조건 모두 참이어야 결과가 참(true)입니다.  🤔

    ```csharp
    bool condition1 = true;
    bool condition2 = false;
    bool result = condition1 && condition2; // result 변수에 false가 저장됩니다! 🤩
    Console.WriteLine(result); // 화면에 "False"를 출력합니다!
    ```

* **'||' (OR 연산자):** 두 조건 중 하나라도 참이면 결과가 참(true)입니다. 🤔

    ```csharp
    bool condition1 = true;
    bool condition2 = false;
    bool result = condition1 || condition2; // result 변수에 true가 저장됩니다! 🤩
    Console.WriteLine(result); // 화면에 "True"를 출력합니다!
    ```

* **'! ' (NOT 연산자):** 조건이 참인 경우 거짓(false)을, 거짓인 경우 참(true)으로 반환합니다. 🤔

   ```csharp
   bool condition = true;
   bool result = !condition; // result 변수에 false가 저장됩니다! 🤩
   Console.WriteLine(result); // 화면에 "False"를 출력합니다!
   ```



**💡 초보자 폭풍 질문!** 🤔

* 연산자는 무슨 일을 하는 건지 간단하게 설명해주세요.  🧐
* '!' 연산자가 왜 필요할까요? 🤔
* 코드에서 연산자를 사용하면 어떤 이점이 있나요? 🚀



### **표현식: 여러 개의 값을 조합하는 마법사** ✨

> "이렇게 계산한 결과값, 그 다음에 이것과 더하고..."
> "혹시 이런 조건이 맞다면, 그렇지 않으면..." 


연산자와 다양한 변수를 조합해서 만든 것입니다. 마치 레시피처럼 여러 재료들을 결합하여 완벽한 음식을 만들듯, 표현식은 C# 코드에서 복잡한 계산이나 판단을 수행하는 데 사용됩니다.

####  **예제 분석! : 더 간단하게 설명해 볼게요.**


```csharp
int age = 20;
bool isAdult = age >= 18; // "age" 값이 18보다 크거나 같으면 "true", 아니면 "false"로 반환합니다.

Console.WriteLine(isAdult); // 화면에 "True"를 출력합니다!
```


   * 여기서 'age'라는 변수에는 우리의 나이인 '20'을 저장했습니다. 🔢 
    *  다음으로, 연산자와 함께 조건문을 만들어 'age'가 18보다 크거나 같으면 'isAdult' 변수에 'true', 아니면 'false'를 저장합니다. 🤔 
    * 마지막으로, 'isAdult'의 값이 출력됩니다.  🥳

#### **표현식의 종류:**


* 산술 표현식: 연산자를 사용하여 수학적 계산을 수행하는 것 (예: `5 + 3`, `10 * 2`)
* 논리 표현식: 논리 연산자를 사용하여 참(true) 또는 거짓(false) 값을 얻는 것 (예: `a > b && c < d`)

* 비교 표현식: 변수나 값들을 비교하여 결과값으로 참(true) 또는 거짓(false) 값을 얻는 것 (예: `x == y`, `z != 5`)


### **실무주의보:**  🚨

연산자와 표현식은 C# 코드의 기본 요소입니다! 이를 이해하면 더 복잡하고 강력한 코드를 작성할 수 있게 될 거예요. 🚀 지금부터 연습문제를 해결하며, 스스로 코딩 실력을 키워봐요! 💪

**다음 시간에는 조건문과 루프 문에 대해 알아보도록 하겠습니다.** 🧙‍♂️




<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
