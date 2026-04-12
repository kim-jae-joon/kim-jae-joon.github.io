---
layout: single
title: "함수와 메서드 작성법"
date: 2026-07-17 18:09:08
categories: [C#]
---

## 4강: 함수와 메서드, 코딩의 레시피 마스터하기! 🧑‍🍳

안녕하세요, 코딩 초보자 여러분! 오늘은 마치 **코딩의 주방에서 가장 핵심적인 재료**인 **함수와 메서드**를 완벽하게 다루는 시간을 가져볼게요. 이거 모르면 코딩이라는 요리 제대로 만들기 힘들답니다! 😅 진짜 신기하죠? 오늘은 간단하면서도 강력한 기능들을 익혀, 당신의 코드를 **훨씬 맛있고 효율적인 요리**로 만들어 줄 거예요. 준비됐나요? 그럼 시작해볼까요!

### 1. 함수와 메서드: 코딩의 레고 블록

#### 🤔 개념부터 시작해볼까요?

**함수**와 **메서드**는 마치 코딩 세계의 레고 블록 같아요. 각각의 블록이 특정 역할을 수행하면서 큰 구조물을 만드는 거죠!

- **함수 (Function)**: 독립적으로 실행 가능한 코드 블록입니다. 예를 들어, **케이크를 굽는 레시피**라고 생각해보세요. 모든 재료와 조리 과정이 하나의 함수 안에 담겨 있어요. 필요할 때마다 호출해서 사용할 수 있어요.
- **메서드 (Method)**: 클래스 안에서 정의된 함수라고 볼 수 있어요. **오븐 안의 특별한 기능**이라고 생각하면 돼요. 오븐 클래스 안에 있는 다양한 조리 기능들이 메서드들이죠.

#### 🧑‍💻 코드 예시: 함수 작성하기

```csharp
// 간단한 함수 예시: 숫자의 제곱을 계산하는 함수
public static int CalculateSquare(int number)
{
    // 숫자를 제곱합니다.
    int result = number * number;
    return result; // 계산 결과를 반환합니다.
}

// 함수 호출 예시
int squareOfFive = CalculateSquare(5); // 5의 제곱을 계산합니다.
Console.WriteLine($"5의 제곱은 {squareOfFive}입니다."); // 출력: 5의 제곱은 25입니다.
```

**설명:**
- `public static int CalculateSquare(int number)`: 함수 선언 부분입니다. `public`은 접근 가능한 범위를, `static`은 클래스 메서드임을 의미합니다. `int`는 반환 타입을 지정합니다.
- `int result = number * number;`: 여기서 `number`를 제곱합니다.
- `return result;`: 계산된 결과를 반환합니다.
- `int squareOfFive = CalculateSquare(5);`: 함수를 호출하고 결과를 변수에 저장합니다.
- `Console.WriteLine`: 결과를 화면에 출력합니다.

### 2. 함수의 다양한 활용법: 코딩의 마법사가 되어보세요!

#### 반복문과 함께 사용하기

함수는 반복문과 찰떡궁합이에요. 마치 **요리 레시피를 여러 번 반복해서 만드는 것** 같죠!

##### 예제 1: `for` 문 활용

```csharp
// 1부터 5까지의 숫자를 출력하는 함수
public static void PrintNumbers(int start, int end)
{
    for (int i = start; i <= end; i++) // 반복문 시작
    {
        Console.WriteLine(i); // 각 숫자를 출력
    }
}

// 함수 호출 예시
PrintNumbers(1, 5); // 1부터 5까지 출력
```

**설명:**
- `for (int i = start; i <= end; i++)`: `start`부터 `end`까지 반복합니다.
- `Console.WriteLine(i);`: 각 반복마다 숫자를 출력합니다.

##### 예제 2: `while` 문 활용

```csharp
// 사용자가 종료할 때까지 숫자를 입력받는 함수
public static void NumberInput()
{
    int number;
    while (true) // 무한 반복
    {
        Console.Write("숫자를 입력하세요 (종료하려면 0 입력): ");
        number = Convert.ToInt32(Console.ReadLine()); // 사용자 입력 받기
        if (number == 0) break; // 0 입력 시 반복 종료
        Console.WriteLine($"입력한 숫자: {number}");
    }
    Console.WriteLine("종료합니다!");
}

// 함수 호출 예시
NumberInput();
```

**설명:**
- `while (true)`: 무한 반복 조건을 설정합니다.
- `Console.ReadLine()`: 사용자 입력을 받아옵니다.
- `if (number == 0) break;`: 0이 입력되면 반복을 종료합니다.

##### 예제 3: `do-while` 문 활용

```csharp
// 최소한 한 번은 실행되는 조건 확인 함수
public static void SimpleConfirmation()
{
    bool continueInput = true;
    while (continueInput) // 최소한 한 번 실행
    {
        Console.Write("확인하시겠습니까? (예/아니오): ");
        string input = Console.ReadLine().ToLower();
        if (input == "예")
        {
            Console.WriteLine("확인 완료!");
            continueInput = false; // 다음 반복 건너뛰기
        }
        else
        {
            Console.WriteLine("확인 다시 시도해주세요.");
        }
    }
}

// 함수 호출 예시
SimpleConfirmation();
```

**설명:**
- `do-while` 문은 최소한 한 번은 코드 블록을 실행합니다.
- `continueInput` 변수를 통해 반복 조건을 제어합니다.

### 💡 초보자 폭풍 질문! 🚨

**Q1:** 함수와 메서드의 주요 차이점은 무엇인가요?

**A1:** 함수는 독립적으로 정의되고 호출될 수 있는 코드 블록입니다. 반면, 메서드는 클래스 내부에 정의되어 해당 클래스의 객체를 통해 호출됩니다. 마치 **함수가 독립적인 식당 메뉴이고 메서드는 오븐 안의 조리 기능**이라고 생각하면 쉽겠죠?

**Q2:** 어떤 상황에서 반복문과 함수를 함께 사용하는 것이 유용한가요?

**A2:** 반복문과 함수를 함께 사용하면 반복적인 작업을 간결하게 처리할 수 있어요! 예를 들어, **매일 동일한 루틴을 반복적으로 수행하는 일상적인 작업** (예: 데이터 처리, 웹 크롤링 등)을 함수로 묶어두고 반복문으로 여러 번 실행하면 훨씬 효율적이죠.

### 🏆 실무주의보

**주의사항:** 함수와 메서드를 과도하게 작게 만들면 코드가 복잡해질 수 있어요. **유지보수와 가독성**을 위해 적절한 크기와 책임을 가진 함수를 작성하는 것이 중요합니다. **일관성 있는 네이밍 컨벤션**도 필수예요! 함수 이름은 그 역할을 명확하게 나타내야 합니다. 예를 들어, `CalculateDiscount()` 보다는 `ApplyCustomerDiscount()`가 더 명확하죠.

### 마무리: 코딩 마스터의 길로 접어드세요!

오늘 배운 함수와 메서드는 코딩에서 가장 기본적이면서도 강력한 도구입니다. 이 레시피를 잘 익혀두면, 복잡한 문제도 차근차근 해결해 나갈 수 있을 거예요. 실습을 많이 해보시고, 궁금한 점이 있으면 언제든지 질문해주세요! 여러분의 코딩 여정이 항상 달콤하고 성공적인 맛으로 가득 차길 바랍니다! 🎉👍

그럼 다음 강의에서 또 만나요! 오늘도 코딩 잘하셨어요! 😊

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
