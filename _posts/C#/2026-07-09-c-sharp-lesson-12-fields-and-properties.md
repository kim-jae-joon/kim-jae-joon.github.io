---
layout: single
title: "필드와 프로퍼티: 데이터 접근"
date: 2026-07-09 16:58:54
categories: [C#]
---

## 12강: 필드와 프로퍼티 - 데이터 접근의 마법사! ✨

**안녕하세요, C# 초보 개발자 여러분! 👋  오늘은 프로그램 안에 데이터를 저장하고 읽는 '필드'와 '프로퍼티'에 대해 알아볼 거예요. 🧙‍♂️ 데이터 접근이란 뭐지? 잠깐 설명하면, 프로그램에서 필요한 정보를 손쉽게 얻고 수정할 수 있는 기술인데요, 마치 게임의 아이템을 사용하거나 캐릭터 스킬을 업그레이드하는 것과 같죠! 🚀**

### 필드: 데이터의 안전하고 개인적인 공간

어쩌면 '필드'라는 단어를 먼저 들었을 때 땅, 경기장 같은 것을 떠올렸지요? 🤔 그렇지만 프로그래밍에서는 '필드'는 프로그램 내부에 저장된 데이터 정보의 이름이라고 생각하면 됩니다. 마치 우리 집 안에서 생활하는 물건들과 비슷한데요, 각 물건은 하나의 필드와 같은 개념이고, 이 속에 그 물건의 특징들이 담겨있죠!

* **예시:** 만약 우리가 '사람' 객체를 만들었다면? 🤔 이름, 나이, 주소같은 정보들을 저장할 필요가 있겠네요. 이런 정보들은 각각의 필드로 정의됩니다!

```csharp
public class Person {
    // 이름을 저장하는 필드 
    public string Name; 

    // 나이를 저장하는 필드
    public int Age; 

    // 주소를 저장하는 필드
    public string Address;  
}

```

* **설명:** `public` 키워드는 필드가 다른 부분에서 접근 가능하다는 의미를 나타냅니다. 이렇게 데이터를 직접 읽고 쓸 수 있는 방법을 **'직접 접근 방식'**이라고 합니다. 

**💡 초보자 폭풍 질문!**

* 필드는 언제 쓰면 좋나요?
* 필드와 같이 사용할 수 있는 다른 데이터 저장 방법은 있을까요? 🤔


### 프로퍼티: 필드의 스타일리쉬 변신! 😎

프로퍼티는 마치 필드의 더 세련된 버전처럼 생각하면 되는데요. 😊 옷장에 있는 멋진 셔츠를 입을 때처럼, 겉으로 보기에는 잘 차려입은 모습만 보이지만 그 안에는 여전히 원하는 정보가 들어있죠! 😎

**프로퍼티는 필드 값에 접근할 때 몇 가지 추가적인 기능을 제공합니다.** 예를 들어, 데이터 입력 시 유효성 검사나 특정 형식으로 변환하는 작업을 수행할 수 있습니다. 마치 자동차의 GPS처럼, 우리가 원하는 경로를 설정하고 도착까지 안내해주는 역할이죠! 🚗

* **예시:** 'Person' 클래스에 프로퍼티를 추가하면 다음과 같습니다:


```csharp
public class Person {
    private string _name; // private 키워드로 필드 접근 제한
    // 이름 프로퍼티 정의 (getter와 setter)
    public string Name {
        get { return _name; } // 'Name'을 읽는 방법
        set {
            if (string.IsNullOrEmpty(value)) {
                throw new ArgumentException("이름은 공백일 수 없습니다."); 
            }
            _name = value;
        }
    }

    // 나이 프로퍼티 정의 (getter와 setter)
    private int _age;
    public int Age {
        get { return _age; }
        set {
            if (value < 0) {
                throw new ArgumentException("나이는 음수일 수 없습니다.");
            }
            _age = value;
        }
    }

    // 주소 프로퍼티 정의 (getter와 setter)
    private string _address;
    public string Address {
        get { return _address; }
        set { _address = value; } 
    }
}
```

* **설명:** 이제 우리는 'Name'과 'Age' 프로퍼티를 통해 데이터에 접근할 수 있습니다. 단순히 값만 가져오는 것(getter)뿐 아니라, 새로운 값을 저장할 때 유효성 검사까지 자동으로 해주기 때문에 더 안전하고 효율적입니다!

**🚨 실무주의보:**

프로퍼티를 사용하면 데이터의 변경이 제한되어 프로그램 오류를 줄이는 데 도움이 됩니다.


### 결론: 필드와 프로퍼티, 함께하는 데이터 마법! ✨

필드와 프로퍼티는 C# 프로그램에서 데이터를 관리하는 가장 기본적인 방법입니다. 각각 장단점을 이해하고 상황에 맞게 활용하면 더욱 효율적이고 안전한 코드를 작성할 수 있습니다. 💪 이제 까지 배운 내용들을 가지고 다양한 프로젝트에 적용해보고, 자신만의 데이터 마법을 만들어 보세요! 🚀




<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
