---
layout: single
title: "File I/O: 파일 읽고 쓰기"
date: 2026-06-26 16:13:48
categories: [C#]
---

## 25강: File I/O - 파일 읽고 쓰기 🔥  

안녕하세요 여러분! 👋 C# 마스터 강사, 당신의 코드 선생님이에요! 🕶️ 오늘은 **파일 I/O**에 대해 알아보도록 할 거예요. 바로 💻컴퓨터와 실제 세계를 연결하는 기술이라고 생각하면 딱 맞겠죠? 😎

저는 이 강의가 끝나면, 파일을 읽고 쓰기 때문에 어떤 힘을 가지고 있고, 어떻게 사용할 수 있는지 완벽하게 이해하게 될 거예요! 💪


### 💡 파일 I/O: 컴퓨터와 세계를 연결하는 마법 ✨

"파일이란 무엇일까?" 🤔  간단히 말하면, 우리가 스스로 만든 정보들을 저장하고 관리할 수 있는 공간이죠. 문서나 사진, 코드까지 다양한 형태의 데이터를 담을 수 있고, 나중에 필요할 때마다 꺼내 사용하는 거예요! 🚀

### 💻 C#에서 파일 읽고 쓰는 방법 🤔

C#에서는 `File` 클래스와 함께 파일 I/O 작업을 할 수 있어요. 어떻게 하는지 알아보자면, 마법과 같은 느낌이 들어오실 거예요! ✨


**1. 파일 쓰기:** `StreamWriter`를 사용하여 쉽게 파일로 데이터를 저장할 수 있어요.

```csharp
using System;
using System.IO; // 파일 작업을 위한 namespace 

public class Example
{
    public static void Main(string[] args)
    {
        // 파일 이름 지정 (파일이 없으면 생성)
        string filePath = "hello_world.txt"; 

        // FileWriter 객체 생성 - 파일에 쓰기
        using (StreamWriter writer = new StreamWriter(filePath))
        {
            writer.WriteLine("Hello, World!"); // 파일에 문구를 쓰는 법!
            writer.WriteLine("This is a file."); // 여러 줄을 쓰고 싶다면? 

        }
        Console.WriteLine($"{filePath} 파일이 생성되었습니다!");  
    }
}
```

**설명:**
* `using System.IO;` : 파일 작업에 필요한 기능들을 사용할 수 있도록 합니다. 💪
* `string filePath = "hello_world.txt";`: 'hello_world.txt'라는 이름의 파일에 내용을 저장할 거예요. 🎉
* `using (StreamWriter writer = new StreamWriter(filePath))`: 파일에 데이터를 쓸 수 있는 객체인 `StreamWriter`를 생성합니다. `using` 문은 자원 관리에 중요한 역할을 합니다! ✨

**2. 파일 읽기:** `StreamReader`를 사용하여 파일의 내용을 읽어올 수 있어요.

```csharp
using System;
using System.IO; 

public class Example
{
    public static void Main(string[] args)
    {
        // 파일 이름 지정
        string filePath = "hello_world.txt";

        // 파일을 읽는 객체 생성
        using (StreamReader reader = new StreamReader(filePath))
        {
            string line; // 한 줄씩 읽기 위한 변수
            while ((line = reader.ReadLine()) != null)
            {
                Console.WriteLine(line); // 파일에 저장된 문구를 화면에 출력! 🎉
            }
        }
    }
}
```

**설명:**
* `StreamReader` 객체는 파일을 읽어오도록 돕죠. 🤓
* `reader.ReadLine()` 함수는 한 줄씩 읽고, null이면 파일의 끝을 의미합니다. 😎

### 🚨 실무주의보: 파일 I/O 시 주의할 점! ⚠️

* **파일 경로**: 파일 위치를 정확하게 알려야 작업이 가능합니다! 😊
* **예외 처리**: 파일 읽기 또는 쓰기 중 문제가 발생하면 예외를 처리해야 안전하고 효율적인 코드를 작성할 수 있습니다. 🤔



### 🚀 숙제: 당신의 창작을 파일로 저장하세요! ✏️

- C# 프로그램을 활용하여 자신의 이름과 연령, 좋아하는 음식 등 정보를 담은 새로운 파일을 생성해보세요!
- 이 파일을 열어 확인하고, 위에서 배운 내용들을 적용하여 다른 데이터를 추가하거나 수정해보세요.





<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
