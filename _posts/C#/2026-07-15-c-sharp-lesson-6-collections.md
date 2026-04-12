---
layout: single
title: "컬렉션과 리스트 사용법"
date: 2026-07-15 18:09:39
categories: [C#]
---

# 6강: 컬렉션과 리스트 사용법 - 코딩 세상의 마법사가 되다!

안녕하세요, 초보자 여러분! 오늘은 코딩의 마법 세계로 여러분을 안내할 거예요. **컬렉션과 리스트**는 마치 당신의 코딩 도구 상자에서 가장 자주 쓰이는 마법 지팡이 같은 존재랍니다. 이걸 잘 다루면 데이터를 정리하고 관리하는 데 있어서 정말 멋진 마법사가 될 수 있을 거예요!

## 컬렉션이란 무엇인가요? 🤔

컬렉션은 여러 개의 항목들을 하나로 묶어서 쉽게 관리할 수 있게 해주는 도구라고 생각하면 돼요. 예를 들어, 여러분이 좋아하는 음식들을 한 그릇에 모아놓는 것과 같죠. 

### 리스트: 마법의 마법 지팡이 🪄

**리스트**는 가장 기본적이면서도 강력한 컬렉션 타입입니다. 여러 항목을 순서대로 저장할 수 있어요. 마치 카드 덱처럼 카드 하나하나가 데이터를 나타내죠!

#### 예제: 숫자 리스트 만들기

```csharp
using System;
using System.Collections.Generic;

class ListMagician
{
    static void Main()
    {
        // 리스트 생성 및 항목 추가
        List<int> magicalNumbers = new List<int>(); // 타입을 명시해 생성
        
        // 1. 항목 추가하기: 마법 주문처럼!
        magicalNumbers.Add(5); // 마법 주문 "ADD"로 숫자 5 추가
        magicalNumbers.Add(10); // "ADD"로 숫자 10 추가
        magicalNumbers.Add(15); // "ADD"로 숫자 15 추가
        
        // 2. 항목 출력하기: 주문 실행!
        Console.WriteLine("마법의 숫자 리스트:"); // 주문 시작 신호
        foreach (int number in magicalNumbers) // 각 항목을 순서대로 출력
        {
            Console.WriteLine(number); // "출력" 주문
        }
        
        // 결과 예시:
        // 마법의 숫자 리스트:
        // 5
        // 10
        // 15
    }
}
```

**코드 해설:**
- `List<int> magicalNumbers = new List<int>();`: 정수형 리스트를 생성합니다. `List<T>`는 제네릭 타입으로, 여기서는 `int`를 사용했어요.
- `.Add(숫자)`: 리스트에 새로운 항목을 추가합니다. 마치 마법 주문처럼요!
- `foreach` 루프: 리스트의 각 항목을 순차적으로 접근하여 출력합니다. 이는 마법사가 마법의 카드를 한 장씩 펼치는 것과 같죠!

### 다양한 컬렉션 타입 탐험 🗺️

컬렉션은 여러 종류가 있어요. 각각의 특징을 살펴보면서 어떤 상황에 어떤 컬렉션을 사용할지 배워볼게요!

#### 1. **리스트 (List<T>)**
   - **특징**: 순서가 있으며 중복 허용, 동적 크기 조절 가능
   - **사용 예**: 학생 명단, 일정 관리

#### 예제: 학생 명단 관리

```csharp
using System;
using System.Collections.Generic;

class SchoolManager
{
    static void Main()
    {
        List<string> studentNames = new List<string>(); // 학생 이름 리스트 생성
        
        // 항목 추가
        studentNames.Add("김철수");
        studentNames.Add("이영희");
        studentNames.Add("박지민");
        
        // 출력
        Console.WriteLine("현재 학생 명단:");
        foreach (string name in studentNames)
        {
            Console.WriteLine(name);
        }
        
        // 결과 예시:
        // 현재 학생 명단:
        // 김철수
        // 이영희
        // 박지민
    }
}
```

**코드 해설:**
- `List<string> studentNames`: 문자열 타입의 리스트를 생성합니다.
- `.Add(이름)`: 학생 이름을 리스트에 추가합니다.
- `foreach` 루프: 각 학생 이름을 출력합니다. 마치 학교에서 학생 명단을 부르는 것 같죠!

#### 2. **배열 (Array)**
   - **특징**: 고정 크기, 순서 유지
   - **사용 예**: 고정된 크기의 데이터 저장 (예: 게임 맵 셀)

#### 예제: 간단한 점수 배열 관리

```csharp
using System;

class ScoreKeeper
{
    static void Main()
    {
        // 배열 생성 및 초기화 (크기 고정)
        int[] scores = new int[5]; // 5개의 점수를 저장할 배열 생성
        scores[0] = 90; // 점수 1 설정
        scores[1] = 85; // 점수 2 설정
        scores[2] = 78; // 점수 3 설정
        scores[3] = 92; // 점수 4 설정
        scores[4] = 88; // 점수 5 설정

        // 배열 출력
        Console.WriteLine("학생들의 점수:");
        for (int i = 0; i < scores.Length; i++) // 반복문으로 배열 항목 출력
        {
            Console.WriteLine($"학생 {i + 1}의 점수: {scores[i]}");
        }
        
        // 결과 예시:
        // 학생들의 점수:
        // 학생 1의 점수: 90
        // 학생 2의 점수: 85
        // 학생 3의 점수: 78
        // 학생 4의 점수: 92
        // 학생 5의 점수: 88
    }
}
```

**코드 해설:**
- `int[] scores = new int[5];`: 크기가 고정된 정수 배열을 생성합니다.
- `scores[인덱스] = 값`: 각 인덱스에 값을 할당합니다. 마치 학급 점수판에 점수를 기록하는 것 같죠!
- `for` 루프: 배열의 각 요소를 순차적으로 출력합니다.

#### 3. **딕셔너리 (Dictionary<TKey, TValue>)**
   - **특징**: 키-값 쌍으로 데이터 저장, 빠른 검색 가능
   - **사용 예**: 사용자 정보, 설정 값 저장

#### 예제: 간단한 사용자 정보 저장

```csharp
using System;
using System.Collections.Generic;

class UserDatabase
{
    static void Main()
    {
        Dictionary<string, string> userDetails = new Dictionary<string, string>(); // 키-값 쌍 딕셔너리 생성
        
        // 항목 추가
        userDetails.Add("이름", "김철수"); // 키: "이름", 값: "김철수"
        userDetails.Add("나이", "20"); // 키: "나이", 값: "20"
        userDetails.Add("주소", "서울시 강남구"); // 키: "주소", 값: "서울시 강남구"
        
        // 출력
        Console.WriteLine("사용자 정보:");
        foreach (KeyValuePair<string, string> entry in userDetails) // 딕셔너리 항목 출력
        {
            Console.WriteLine($"{entry.Key}: {entry.Value}");
        }
        
        // 결과 예시:
        // 사용자 정보:
        // 이름: 김철수
        // 나이: 20
        // 주소: 서울시 강남구
    }
}
```

**코드 해설:**
- `Dictionary<string, string> userDetails`: 문자열 키와 값으로 구성된 딕셔너리 생성합니다.
- `.Add(키, 값)`: 키와 해당 값 쌍을 추가합니다. 마치 주소록에 연락처를 기록하는 것 같죠!
- `foreach` 루프: 각 키-값 쌍을 출력합니다.

## 실전에서의 활용법 🏆

### 리스트의 강력한 기능들

1. **포커스: 반복문 활용**
   - **예제: 모든 요소에 10 더하기**
     ```csharp
     foreach (int num in magicalNumbers)
     {
         num += 10; // 각 숫자에 10 더하기
         Console.WriteLine($"수정된 숫자: {num}");
     }
     ```

2. **조건 체크: 조건문 활용**
   - **예제: 특정 조건에 맞는 숫자 찾기**
     ```csharp
     int targetNumber = 15;
     bool found = false;
     foreach (int num in magicalNumbers)
     {
         if (num == targetNumber) // 특정 숫자 찾기
         {
             Console.WriteLine($"목표 숫자 {targetNumber}을 찾았습니다!");
             found = true; // 찾았다는 표시
             break; // 종료
         }
     }
     if (!found) // 찾지 못한 경우 메시지 출력
     {
         Console.WriteLine("목표 숫자를 찾을 수 없었습니다.");
     }
     ```

### 초보자 폭풍 질문! 💡

**Q1:** 리스트와 배열의 주요 차이점은 무엇인가요?
**A1:** 배열은 고정된 크기와 타입으로 초기화되어 변경이 어렵지만, 리스트는 동적으로 크기를 조정할 수 있고, 타입도 유연하게 다룰 수 있어요. 마치 책상 위의 고정된 책상 서랍과 언제든지 물건을 추가하거나 뺄 수 있는 서랍 같은 느낌이죠!

**Q2:** 딕셔너리에서 키는 반드시 문자열이어야 하나요?
**A2:** 아니요! 키는 `int`, `double` 등 다양한 타입이 될 수 있어요. 단지 `string` 타입을 주로 사용하는 이유는 텍스트 정보를 쉽게 처리하기 때문이죠. 다양한 데이터 타입을 키로 사용할 수 있으니 창의력을 발휘해보세요!

## 실무주의보 🚨

**주의사항:**
- **성능 고려**: 배열의 크기를 자주 변경하면 성능에 영향을 줄 수 있어요. 리스트는 동적으로 크기를 조정하기 때문에 이런 상황에서 더 유리합니다.
- **중복 방지**: 딕셔너리에서 키는 고유해야 하므로 중복 키가 허용되지 않아요. 이 점을 놓치면 데이터 관리에 오류가 생길 수 있으니 주의하세요!

오늘 배운 컬렉션과 리스트의 마법을 통해 이제 코딩 세상에서 훨씬 더 강력한 마법사가 되셨기를 바라요! 계속 연습하고 탐구하면서 자신만의 코딩 세계를 넓혀가세요. 다음 강의에서 또 만나요! 🌟

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
