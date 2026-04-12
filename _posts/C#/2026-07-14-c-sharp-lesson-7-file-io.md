---
layout: single
title: "파일 입출력 및 스트림 처리"
date: 2026-07-14 18:09:57
categories: [C#]
---

# 7강: 파일 입출력 & 스트림 처리 – 코딩의 보물 창고 탐험하기

안녕하세요, 코딩의 모험가 여러분! 오늘은 **파일 입출력 및 스트림 처리**에 대해 함께 탐험해볼 시간입니다. 마치 해적들이 보물을 찾아내는 것처럼, 컴퓨터도 데이터의 보물 창고인 파일을 읽고 쓰는 기술을 배우게 될 거예요. 준비되셨나요? **진짜 신기하죠?**

## 파일 입출력의 기초: 왜 중요한 걸까요?

### 왜 파일 입출력이 필요한가요?

- **데이터 보관**: 사용자 정보, 로그, 설정 등 다양한 데이터를 안전하게 보관합니다.
- **데이터 공유**: 여러 프로그램 간에 데이터를 주고받는 데 필수적입니다.
- **백업 및 복구**: 중요한 정보를 백업하고 필요할 때 복구할 수 있어요.

### 기본 개념 설명

파일 입출력은 크게 **읽기(Reading)**와 **쓰기(Writing)**로 나뉩니다. 이 두 가지를 통해 프로그램은 외부 세계와 소통하게 되죠. 스트림(Stream)은 데이터를 연속적인 바이트 스트림으로 처리하는 방법입니다. 이해하기 쉽게 설명하자면, 스트림은 **물줄기**와 같아요. 데이터가 원활하게 흐르는 것처럼, 스트림을 통해 데이터가 컴퓨터 내부에서 외부로, 또는 반대로 이동하는 거죠.

## C#에서 파일 읽기와 쓰기

### 읽기: 파일 내용을 한눈에!

#### 예제 코드 1: 텍스트 파일 읽기

```csharp
using System;
using System.IO;

class FileReaderExample
{
    static void Main()
    {
        // 파일 경로 지정
        string filePath = @"C:\example\sample.txt";

        // 파일이 존재하는지 확인
        if (File.Exists(filePath))
        {
            // 파일 읽기 - 텍스트 파일인 경우 StreamReader 사용
            using (StreamReader reader = new StreamReader(filePath))
            {
                string content = reader.ReadToEnd(); // 파일 전체 내용 읽기
                Console.WriteLine("파일 내용:");
                Console.WriteLine(content); // 내용 출력
            }
        }
        else
        {
            Console.WriteLine("파일이 존재하지 않습니다!");
        }
    }
}
```

**코드 설명:**
- `StreamReader` 클래스는 텍스트 파일을 읽기 위해 사용됩니다. `using` 문으로 자동 리소스 해제를 보장합니다.
- `File.Exists` 메서드로 파일 존재 여부를 확인하고, 존재하면 `ReadToEnd` 메서드로 전체 내용을 한 번에 읽어옵니다.

#### 읽기: 다양한 방법으로 접근하기

1. **for 루프를 활용한 라인별 읽기**
   ```csharp
   using (StreamReader reader = new StreamReader(filePath))
   {
       string line;
       while ((line = reader.ReadLine()) != null)
       {
           Console.WriteLine(line); // 각 라인 출력
       }
   }
   ```
   **설명:** `ReadLine`을 반복적으로 호출하여 파일의 각 줄을 순차적으로 읽어옵니다. 이 방법은 큰 파일을 효율적으로 처리할 때 유용합니다.

2. **while 루프를 이용한 수동 제어**
   ```csharp
   using (StreamReader reader = new StreamReader(filePath))
   {
       while (!reader.EndOfStream)
       {
           string line = reader.ReadLine();
           Console.WriteLine(line);
       }
   }
   ```
   **설명:** `EndOfStream` 속성을 확인하며 수동으로 루프를 제어합니다. 이 방법은 더 세밀한 제어가 필요할 때 유용합니다.

### 쓰기: 나만의 데이터 보물함 만들기

#### 예제 코드 2: 텍스트 파일 쓰기

```csharp
using System;
using System.IO;

class FileWriterExample
{
    static void Main()
    {
        string filePath = @"C:\example\newfile.txt";

        // 파일이 이미 존재하는 경우 덮어쓰기 설정
        bool overwrite = true;
        if (File.Exists(filePath) && !overwrite)
        {
            Console.Write("기존 파일이 존재합니다. 덮어쓰기 하시겠습니까? (y/n): ");
            string response = Console.ReadLine();
            if (response != "y")
            {
                Console.WriteLine("작성 취소되었습니다.");
                return;
            }
        }

        // 텍스트 쓰기 - StreamWriter 사용
        using (StreamWriter writer = new StreamWriter(filePath, overwrite))
        {
            writer.WriteLine("안녕하세요, 새로운 파일입니다!");
            writer.WriteLine("이 데이터는 당신의 손길로 만들어졌습니다.");
        }

        Console.WriteLine("파일 작성 완료!");
    }
}
```

**코드 설명:**
- `StreamWriter` 클래스는 파일에 텍스트를 쓸 때 사용됩니다. `overwrite` 플래그로 기존 파일을 덮어쓸지 결정합니다.
- `WriteLine` 메서드를 사용해 텍스트를 파일에 씁니다. 이 방법으로 원하는 내용을 쉽게 추가할 수 있어요.

#### 쓰기: 다양한 상황에 대비하기

1. **for 루프를 활용한 반복 쓰기**
   ```csharp
   using (StreamWriter writer = new StreamWriter(filePath, true)) // append 모드
   {
       string[] lines = { "라인 1", "라인 2", "라인 3" };
       foreach (string line in lines)
       {
           writer.WriteLine(line);
       }
   }
   ```
   **설명:** `foreach` 루프를 사용해 여러 줄을 순차적으로 쓸 수 있습니다. `StreamWriter`의 `append` 모드로 파일 끝에 내용을 추가할 수도 있어요.

2. **while 루프를 이용한 조건부 쓰기**
   ```csharp
   using (StreamWriter writer = new StreamWriter(filePath))
   {
       int count = 0;
       while (count < 5) // 예시 조건
       {
           writer.WriteLine($"조건부 라인 {count + 1}");
           count++;
       }
   }
   ```
   **설명:** 특정 조건에 따라 데이터를 쓰는 경우 `while` 루프를 활용할 수 있습니다. 이 방법은 복잡한 조건 처리에 유용합니다.

## 실무 주의사항 🚨 실무주의보

- **파일 경로 주의**: 절대 경로를 잘못 입력하면 프로그램이 실행되지 않을 수 있어요. 상대 경로나 환경 변수를 활용해 안전하게 경로를 지정하는 습관을 들이세요.
- **오류 처리**: 파일 작업 중 예외가 발생할 수 있으니 `try-catch` 블록을 활용해 안정적인 코드 작성이 필요합니다.
  ```csharp
  try
  {
      using (StreamReader reader = new StreamReader(filePath))
      {
          string content = reader.ReadToEnd();
          Console.WriteLine(content);
      }
  }
  catch (IOException ex)
  {
      Console.WriteLine($"파일 읽기 오류: {ex.Message}");
  }
  ```

## 초보자 폭풍 질문! 💡

- **Q**: 파일 경로를 어떻게 안전하게 지정할 수 있을까요?
  - **A**: 사용자 입력을 받거나 환경 변수를 활용해 경로를 동적으로 설정할 수 있습니다. 예를 들어, `Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments)`로 사용자의 문서 폴더 경로를 가져올 수 있어요.
  
- **Q**: 만약 파일이 이미 존재하는 경우 어떻게 처리해야 할까요?
  - **A**: 덮어쓰기 여부를 묻는 대화형 인터페이스를 구현하거나, `StreamWriter`의 `Append` 플래그를 사용해 기존 내용 뒤에 추가할 수 있습니다. 상황에 맞게 선택하시면 됩니다.

### 마무리: 코딩의 보물상자를 열어보세요!

오늘 배운 파일 입출력과 스트림 처리 기술로 여러분은 데이터의 보물 창고를 열 수 있는 멋진 개발자가 되셨어요! **이거 모르면 큰일 납니다!** 실제 프로젝트에서 파일을 다루는 방법을 익혀나가다 보면, 복잡한 문제 해결 능력도 향상될 거예요. 계속 연습하고 탐험하세요! 다음 강의에서 또 만나요! 🚀

---

이 강의가 여러분의 코딩 여정에 큰 도움이 되길 바랍니다. 계속해서 질문하고 도전하며 성장해나가세요! 👍

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
