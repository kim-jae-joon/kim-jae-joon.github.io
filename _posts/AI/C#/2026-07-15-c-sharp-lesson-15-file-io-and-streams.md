---
layout: single
title: "C# 활용: 파일 입출력과 스트림 처리"
date: 2026-07-15 00:01:54
categories: [C#]
---

안녕하세요! 여러분의 코딩 구원투수, 재준봇입니다!

자, 여러분. 드디어 우리가 15강까지 왔습니다. 여기까지 따라오신 분들이라면 이미 기초 체력은 충분히 길러진 상태라고 생각합니다. 하지만 오늘 배울 내용은 조금 결이 다릅니다. 지금까지 우리는 프로그램을 실행하는 동안에만 데이터가 살아있는 '휘발성' 세상에 살았어요. 하지만 생각해보세요. 게임을 열심히 했는데 저장 기능이 없어서 껐다 켤 때마다 1레벨부터 시작한다면? 아마 그 게임은 바로 삭제 리스트에 올라가겠죠?

그래서 오늘은 프로그램이 종료되어도 데이터가 영원히(혹은 우리가 지울 때까지) 남게 만드는 마법, 바로 파일 입출력과 스트림 처리를 배워보겠습니다. 준비되셨나요? 바로 들어갑니다!

# 15강: C# 활용 - 파일 입출력과 스트림 처리

## 1. 파일 입출력이 대체 뭐길래 이렇게 난리인가요?

먼저 개념부터 잡고 가시죠. 코딩 초보자분들이 가장 많이 헷갈려 하는 게 바로 메모리(RAM)와 저장장치(HDD/SSD)의 차이입니다.

> **재준봇의 찰떡 비유 타임!**
> 여러분의 컴퓨터 메모리(RAM)는 '책상 위'라고 생각하세요. 책상 위에서는 펜도 있고 노트도 있어서 작업 속도가 굉장히 빠릅니다. 하지만 책상이 좁아서 다 올려둘 수 없고, 무엇보다 퇴근할 때(전원을 끌 때) 청소 아주머니가 책상 위를 싹 치워버립니다. 
> 반면, 하드디스크나 SSD 같은 저장장치는 '서류 캐비닛'입니다. 책상보다는 꺼내는 속도가 느리지만, 엄청나게 많은 양의 서류를 보관할 수 있고, 퇴근하고 다음 날 출근해도 서류들이 그대로 들어있죠.

즉, 파일 입출력이란 **책상 위에 있는 데이터를 서류 캐비닛에 집어넣거나(출력/Write), 캐비닛에 있는 서류를 다시 책상 위로 꺼내오는(입력/Read)** 과정이라고 보시면 됩니다.

---

## 2. '스트림(Stream)'이라는 녀석의 정체

파일 입출력을 배우다 보면 무조건 '스트림'이라는 단어가 나옵니다. 이게 대체 뭘까요? 영어로 Stream은 '시냇물'이나 '흐름'을 뜻합니다.

데이터를 옮길 때, 한꺼번에 덩어리로 툭 던지는 게 아니라 **빨대 같은 통로를 만들어서 데이터를 졸졸졸 흐르게 만드는 방식**을 스트림이라고 합니다. 왜 이렇게 하냐고요? 파일이 10GB라면 이걸 한 번에 메모리에 올리는 순간 컴퓨터가 비명을 지르며 멈출 겁니다. 하지만 스트림을 이용하면 조금씩 나누어 읽어올 수 있기 때문에 메모리를 효율적으로 쓸 수 있습니다.

---

## 3. 파일에 데이터 쓰기 (Write) - 3가지 방법

자, 이제 본격적으로 코드를 짜봅시다. 파일에 글자를 적는 방법은 여러 가지가 있습니다. 상황에 따라 골라 써야 하니 눈 크게 뜨고 보세요!

### 방법 1: File.WriteAllText (한 방에 끝내기 모드)
가장 간단한 방법입니다. "내용이 적으니까 그냥 한 번에 다 써버려!" 할 때 사용합니다.

```csharp
using System;
using System.IO; // 파일 입출력을 하려면 반드시 이 네임스페이스가 필요합니다!

class Program
{
    static void Main()
    {
        string path = "my_diary.txt"; // 저장할 파일 경로와 이름
        string content = "오늘은 재준봇 덕분에 파일 입출력을 마스터했다. 정말 쉽다!"; // 저장할 내용

        // 파일이 없으면 만들고, 있으면 내용을 덮어씁니다.
        File.WriteAllText(path, content);

        Console.WriteLine("파일 작성이 완료되었습니다. 확인해보세요!");
    }
}
```
**코드 뜯어보기**
- `using System.IO;`: IO는 Input/Output의 약자입니다. 파일 시스템을 건드리려면 이 친구가 꼭 있어야 합니다.
- `File.WriteAllText(path, content);`: 이 메서드는 파일을 열고, 내용을 쓰고, 파일을 닫는 모든 과정을 한 줄로 처리합니다. 정말 편리하죠? 하지만 주의할 점은 기존 내용이 있다면 싹 다 지우고 새로 쓴다는 점입니다.

### 방법 2: StreamWriter (정밀 제어 모드)
데이터를 조금씩, 혹은 여러 줄에 걸쳐 쓰고 싶을 때 사용합니다. 마치 메모장에 한 줄 한 줄 적는 것과 비슷합니다.

```csharp
using System;
using System.IO;

class Program
{
    static void Main()
    {
        string path = "log.txt";

        // using 문을 사용하는 이유는 사용 후 자동으로 '빨대(스트림)'를 제거하기 위해서입니다.
        using (StreamWriter writer = new StreamWriter(path))
        {
            writer.WriteLine("첫 번째 로그: 프로그램 시작됨");
            writer.WriteLine("두 번째 로그: 사용자 로그인 성공");
            writer.WriteLine("세 번째 로그: 데이터 처리 완료");
        }

        Console.WriteLine("로그 파일 작성이 완료되었습니다!");
    }
}
```
**코드 뜯어보기**
- `using (StreamWriter writer = ...)`: 이게 진짜 중요합니다! 파일을 열었으면 반드시 닫아줘야 합니다. `using` 블록을 사용하면 블록이 끝나는 순간 자동으로 파일을 닫아줍니다. 안 닫으면 다른 프로그램이 이 파일을 못 건드리는 불상사가 생깁니다.
- `writer.WriteLine()`: 텍스트를 쓰고 자동으로 줄 바꿈을 해줍니다.

### 방법 3: File.AppendAllText (덧붙이기 모드)
기존 내용을 유지하면서 끝에 내용을 추가하고 싶을 때 사용합니다. 일기장이나 로그 파일에 딱이죠.

```csharp
using System;
using System.IO;

class Program
{
    static void Main()
    {
        string path = "memo.txt";
        string newMemo = "\n추가 메모: 내일은 C# 복습을 해야겠다.";

        // 기존 파일 끝에 내용을 추가합니다. 파일이 없으면 새로 만듭니다.
        File.AppendAllText(path, newMemo);

        Console.WriteLine("메모가 성공적으로 추가되었습니다!");
    }
}
```
**코드 뜯어보기**
- `File.AppendAllText()`: `WriteAllText`와 비슷하지만, 덮어쓰지 않고 '뒤에 붙여넣기'를 합니다. 
- `\n`: 줄 바꿈 문자입니다. 이걸 넣지 않으면 기존 내용 바로 뒤에 딱 붙어서 글자가 써지니 주의하세요!

---

## 4. 파일에서 데이터 읽기 (Read) - 3가지 방법

이제 서류 캐비닛에서 서류를 꺼낼 차례입니다. 읽는 방법 역시 상황에 따라 다릅니다.

### 방법 1: File.ReadAllText (통째로 읽기 모드)
파일 전체 내용을 하나의 거대한 문자열로 가져옵니다. 파일 크기가 작을 때 매우 유용합니다.

```csharp
using System;
using System.IO;

class Program
{
    static void Main()
    {
        string path = "my_diary.txt";

        if (File.Exists(path)) // 파일이 있는지 먼저 확인하는 센스!
        {
            string allContent = File.ReadAllText(path);
            Console.WriteLine("파일 내용 출력:");
            Console.WriteLine(allContent);
        }
        else
        {
            Console.WriteLine("파일이 존재하지 않습니다.");
        }
    }
}
```
**코드 뜯어보기**
- `File.Exists(path)`: 파일이 없는데 읽으려고 하면 프로그램이 뻗어버립니다(예외 발생). 그래서 읽기 전에는 항상 확인하는 습관을 들여야 합니다.
- `File.ReadAllText(path)`: 파일의 처음부터 끝까지 모든 내용을 한 번에 가져와 변수에 담습니다.

### 방법 2: StreamReader (한 줄씩 읽기 모드)
파일이 너무 커서 한 번에 읽기 부담스러울 때, 혹은 한 줄씩 처리해야 할 때 사용합니다.

```csharp
using System;
using System.IO;

class Program
{
    static void Main()
    {
        string path = "log.txt";

        using (StreamReader reader = new StreamReader(path))
        {
            string line;
            // 더 이상 읽을 줄이 없을 때까지 반복합니다.
            while ((line = reader.ReadLine()) != null)
            {
                Console.WriteLine("읽어온 줄: " + line);
            }
        }
    }
}
```
**코드 뜯어보기**
- `reader.ReadLine()`: 한 줄을 읽고 커서를 다음 줄로 옮깁니다. 더 이상 읽을 내용이 없으면 `null`을 반환합니다.
- `while` 문: `null`이 나올 때까지 무한히 읽어오는 구조입니다. 대용량 파일을 읽을 때 표준적으로 사용하는 방식입니다.

### 방법 3: File.ReadAllLines (배열로 읽기 모드)
파일의 각 줄을 문자열 배열(`string[]`)로 만들어 줍니다. 몇 번째 줄에 어떤 내용이 있는지 인덱스로 접근하고 싶을 때 최고입니다.

```csharp
using System;
using System.IO;

class Program
{
    static void Main()
    {
        string path = "log.txt";

        if (File.Exists(path))
        {
            string[] lines = File.ReadAllLines(path);
            Console.WriteLine($"총 {lines.Length}줄의 데이터를 읽었습니다.");
            
            // 두 번째 줄만 출력해보고 싶다면?
            if (lines.Length >= 2)
            {
                Console.WriteLine("두 번째 줄 내용: " + lines[1]);
            }
        }
    }
}
```
**코드 뜯어보기**
- `File.ReadAllLines(path)`: 내부적으로 파일을 다 읽어서 줄 바꿈 기준으로 쪼갠 뒤 배열에 넣어줍니다.
- `lines[1]`: 배열이므로 인덱스를 통해 특정 행에 바로 접근할 수 있다는 것이 가장 큰 장점입니다.

---

## 5. 초보자 폭풍 질문!

**Q: 재준봇님! `using` 문을 꼭 써야 하나요? 그냥 쓰면 안 되나요?**

**재준봇의 답변:** 
이거 정말 많이 물어보시는데, 결론부터 말씀드리면 **무조건 쓰세요!**
파일을 여는 행위는 윈도우 운영체제에게 "내가 이 파일을 사용하겠다"라고 권한을 요청하는 것입니다. 그런데 `using` 없이 파일을 열고 제대로 닫지 않으면, 프로그램이 종료될 때까지 운영체제는 "아직 재준봇이 이 파일을 쓰고 있구나"라고 생각해서 파일을 잠가버립니다. 

이렇게 되면 다른 프로그램에서 그 파일을 수정하려 할 때 "다른 프로세스에서 사용 중이므로 액세스할 수 없습니다"라는 무시무시한 에러 메시지를 보게 될 겁니다. `using`은 "작업 끝나면 바로 권한 반납할게!"라고 약속하는 안전장치라고 생각하시면 됩니다.

---

## 6. 실무주의보

**주의: 절대 경로 vs 상대 경로**

실무에서 가장 많이 하는 실수 중 하나가 경로 설정입니다.

- **상대 경로 (`"my_diary.txt"`)**: 현재 프로그램이 실행되는 폴더를 기준으로 파일을 찾습니다. 개발할 때는 편하지만, 실행 파일의 위치가 바뀌면 파일을 못 찾을 수 있습니다.
- **절대 경로 (`"C:\Users\Admin\Documents\my_diary.txt"`)**: 컴퓨터의 뿌리부터 정확한 위치를 지정합니다. 확실하지만, 이 프로그램을 다른 사람의 컴퓨터로 옮기면 그 사람 컴퓨터에는 저 경로가 없을 확률이 100%입니다.

**해결책:**
실무에서는 보통 `AppDomain.CurrentDomain.BaseDirectory` 같은 명령어를 사용해서 프로그램이 설치된 폴더 경로를 동적으로 가져온 뒤, 그 뒤에 파일 이름을 붙여서 사용합니다. 이렇게 해야 어떤 컴퓨터에서 실행하든 파일 위치를 정확히 잡을 수 있습니다.

---

## 마무리하며

오늘 우리는 C#의 파일 입출력이라는 강력한 도구를 배웠습니다. 데이터를 단순히 메모리에 올리는 수준을 넘어, 파일로 저장하고 읽어오는 능력을 갖추게 된 것입니다. 이제 여러분은 간단한 메모장 프로그램, 로그 기록 시스템, 혹은 게임의 세이브 파일 시스템까지 직접 구현하실 수 있게 되었습니다.

오늘 배운 내용을 요약하자면 이렇습니다.
1. **간단하게 쓰고 싶을 땐?** `File.WriteAllText` / `File.ReadAllText`
2. **내용을 추가하고 싶을 땐?** `File.AppendAllText`
3. **대용량 파일을 정밀하게 다루고 싶을 땐?** `StreamWriter` / `StreamReader`
4. **줄 단위로 인덱스 접근이 필요할 땐?** `File.ReadAllLines`
5. **가장 중요한 것?** `using` 문 사용해서 자원 해제하기!

자, 이제 눈으로만 보지 말고 직접 코드를 타이핑해서 파일이 생성되는 그 쾌감을 느껴보세요. 다음 강의에서는 더 흥미진진한 내용으로 돌아오겠습니다. 지금까지 여러분의 코딩 멘토, 재준봇이었습니다!

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
