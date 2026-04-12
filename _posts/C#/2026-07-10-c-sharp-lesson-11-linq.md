---
layout: single
title: "LINQ를 이용한 데이터 쿼리"
date: 2026-07-10 18:10:56
categories: [C#]
---

### 11강: LINQ를 이용한 데이터 쿼리 - 데이터 마법사가 되어보자!

안녕하세요, 코딩의 마법사 여러분! 오늘은 여러분의 코딩 모험을 한 단계 업그레이드 시켜줄 **LINQ (Language Integrated Query)**에 대해 깊이 들어갈 시간입니다. LINQ는 마치 데이터의 마법사 같아요. 복잡한 데이터 숲 속에서 필요한 정보만을 정확하게 뽑아내는 능력을 당신에게 선사할 거예요!

#### 🤔 LINQ란 무엇인가?

LINQ는 C#에서 제공하는 통합 쿼리 언어로, 다양한 데이터 소스에서 정보를 추출하고 조작하는 데 사용됩니다. 쉽게 말해, 데이터베이스나 리스트에서 원하는 데이터를 찾아내는 마법사의 지팡이 같은 역할을 합니다. 

**진짜 신기하죠?** 여러분이 지금까지 수동으로 반복적으로 데이터를 필터링하고 검색해왔다면, LINQ는 그 과정을 몇 줄의 코드로 간결하게 해결해줍니다!

### 개념부터 실전까지: 단계별 가이드

#### 1. 기본 개념 이해하기

LINQ는 크게 두 가지 주요 구성 요소로 이루어져 있습니다: **쿼리 표현식**과 **쿼리 연산자**.

- **쿼리 표현식**: 데이터에서 원하는 결과를 얻기 위한 표현식입니다.
- **쿼리 연산자**: 데이터를 필터링하고 정렬하며 조작하는 데 사용되는 함수들입니다 (예: `Where`, `Select`, `OrderBy`, `GroupBy` 등).

##### 예시 1: 간단한 리스트 필터링

```csharp
using System;
using System.Linq;
using System.Collections.Generic;

class DataQueryMagic
{
    static void Main()
    {
        // 간단한 숫자 리스트 생성
        List<int> numbers = new List<int> { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };

        // LINQ를 이용한 숫자 필터링 (짝수만 남기기)
        var evenNumbers = numbers.Where(n => n % 2 == 0);

        // 결과 출력
        Console.WriteLine("짝수 리스트:");
        foreach (var num in evenNumbers)
        {
            Console.WriteLine(num);
        }

        // 코드 설명:
        // 1. `numbers.Where(n => n % 2 == 0)`: 각 숫자 `n`이 짝수인지 확인하는 람다 표현식을 사용합니다.
        // 2. `evenNumbers` 변수는 짝수만 담긴 새로운 IEnumerable<int> 컬렉션을 생성합니다.
        // 3. `foreach` 루프를 통해 필터링된 결과를 출력합니다.
    }
}
```

**💡 초보자 폭풍 질문!**  
*Q: 람다 표현식(`n => n % 2 == 0`)이란 뭔가요?*  
*A: 람다 표현식은 간단한 익명 함수로, 여기서는 각 숫자 `n`이 짝수인지 판별하는 역할을 합니다. 쉽게 말해, 조건을 간결하게 표현하는 방법이에요!*

#### 2. 다양한 쿼리 연산자 활용하기

##### 예시 2: 정렬된 리스트 생성

```csharp
using System;
using System.Linq;
using System.Collections.Generic;

class DataSorterMagician
{
    static void Main()
    {
        // 예제 데이터 리스트 생성
        List<Person> people = new List<Person>
        {
            new Person("Alice", 25),
            new Person("Bob", 30),
            new Person("Charlie", 22),
            new Person("David", 28)
        };

        // 이름으로 정렬하기 (오름차순)
        var sortedByName = people.OrderBy(p => p.Name);

        // 나이로 정렬하기 (내림차순)
        var sortedByAge = people.OrderByDescending(p => p.Age);

        // 결과 출력 예시
        Console.WriteLine("이름 순으로 정렬:");
        foreach (var person in sortedByName)
        {
            Console.WriteLine($"{person.Name}, 나이: {person.Age}");
        }

        // 코드 설명:
        // 1. `people.OrderBy(p => p.Name)`: `Name` 속성 기준으로 오름차순 정렬.
        // 2. `people.OrderByDescending(p => p.Age)`: `Age` 속성 기준으로 내림차순 정렬.
        // 3. 각 정렬된 결과를 출력합니다.
    }
}

// Person 클래스 정의
public class Person
{
    public string Name { get; set; }
    public int Age { get; set; }

    public Person(string name, int age)
    {
        Name = name;
        Age = age;
    }
}
```

**🚨 실무주의보**  
*Q: 실제 프로젝트에서 LINQ를 사용할 때 주의할 점은 뭔가요?*  
*A: 성능 최적화에 주의하세요. 대규모 데이터셋에서는 LINQ 쿼리가 메모리에 모든 결과를 로드할 수 있으므로, 필요한 경우 `ToList()`, `Take()`, `Skip()` 등의 메서드를 적절히 사용하여 데이터 처리를 최적화해야 합니다.*

##### 예시 3: 복잡한 조건 필터링

```csharp
using System;
using System.Linq;
using System.Collections.Generic;

class ComplexFiltering
{
    static void Main()
    {
        // 예제 학생 리스트 생성
        List<Student> students = new List<Student>
        {
            new Student("김철수", "컴퓨터공학", 88),
            new Student("이영희", "소프트웨어공학", 92),
            new Student("박지민", "컴퓨터공학", 76),
            new Student("최다은", "전자공학", 85)
        };

        // 컴퓨터공학 전공이면서 점수가 85점 이상인 학생 필터링
        var filteredStudents = students.Where(s => s.Major == "컴퓨터공학" && s.Score >= 85);

        // 결과 출력
        Console.WriteLine("조건에 맞는 학생들:");
        foreach (var student in filteredStudents)
        {
            Console.WriteLine($"이름: {student.Name}, 전공: {student.Major}, 점수: {student.Score}");
        }

        // 코드 설명:
        // 1. `students.Where(s => s.Major == "컴퓨터공학" && s.Score >= 85)`: 
        //    전공이 "컴퓨터공학"이고 점수가 85점 이상인 학생들만 필터링합니다.
        // 2. 람다 표현식을 사용하여 복잡한 조건을 간결하게 표현합니다.
        // 3. 필터링된 결과를 출력합니다.
    }
}

// 학생 클래스 정의
public class Student
{
    public string Name { get; set; }
    public string Major { get; set; }
    public int Score { get; set; }

    public Student(string name, string major, int score)
    {
        Name = name;
        Major = major;
        Score = score;
    }
}
```

##### 예시 4: 그룹화와 집계

```csharp
using System;
using System.Linq;
using System.Collections.Generic;

class GroupingAndAggregation
{
    static void Main()
    {
        // 예제 주문 데이터 리스트 생성
        List<Order> orders = new List<Order>
        {
            new Order("도서A", "고객1", 15000),
            new Order("도서B", "고객1", 20000),
            new Order("도서C", "고객2", 12000),
            new Order("도서D", "고객2", 18000),
            new Order("도서E", "고객3", 25000)
        };

        // 고객별 총 주문 금액 집계
        var groupedOrders = orders.GroupBy(o => o.Customer)
                                  .Select(g => new
                                  {
                                      CustomerName = g.Key,
                                      TotalAmount = g.Sum(o => o.Amount)
                                  });

        // 결과 출력
        Console.WriteLine("고객별 총 주문 금액:");
        foreach (var orderGroup in groupedOrders)
        {
            Console.WriteLine($"고객: {orderGroup.CustomerName}, 총 금액: {orderGroup.TotalAmount}원");
        }

        // 코드 설명:
        // 1. `orders.GroupBy(o => o.Customer)`: 고객별로 주문 데이터를 그룹화합니다.
        // 2. `.Select(g => new { ... })`: 각 그룹에 대해 고객 이름과 총 주문 금액을 계산합니다.
        // 3. `g.Sum(o => o.Amount)`: 각 그룹 내 주문 금액을 합산합니다.
        // 4. 결과를 출력하여 고객별 총 주문 금액을 확인합니다.
    }
}

// 주문 클래스 정의
public class Order
{
    public string Item { get; set; }
    public string Customer { get; set; }
    public int Amount { get; set; }

    public Order(string item, string customer, int amount)
    {
        Item = item;
        Customer = customer;
        Amount = amount;
    }
}
```

### 결론: LINQ로 데이터 마법 펼치기

LINQ는 데이터 처리를 훨씬 더 직관적이고 강력하게 만들어줍니다. 이제 복잡한 쿼리도 간결한 코드 몇 줄로 해결할 수 있게 되었어요! 여러분의 코딩 스킬이 한 단계 더 업그레이드된 마법사로 성장하길 바라며, 다음 강의에서는 더욱 심화된 주제로 만나요!

**🔥 실전 연습 시간!**

- **연습 문제 1**: 학생들의 성적 데이터 리스트가 주어졌을 때, 특정 학과의 평균 성적을 계산하는 LINQ 쿼리를 작성해보세요.
- **연습 문제 2**: 주문 내역에서 가장 많이 팔린 상품 카테고리와 그 판매량을 찾아내는 쿼리를 작성해보세요.

**💪 자신을 믿고 코딩의 마법을 펼쳐보세요!**

---

이 강의가 여러분의 LINQ 마스터리를 가속화하는 데 큰 도움이 되길 바랍니다. 더 궁금한 점이 있으면 언제든지 물어보세요! 🚀✨

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
