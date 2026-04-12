---
layout: single
title: "Pandas: 데이터 처리 및 분석"
date: 2026-06-18 15:01:42
categories: [파이썬]
---

## 33강: Pandas - 데이터 처리 및 분석 🚀 : 마법같은 파이썬 도구로 데이터 불리다!

**안녕하세요, 프로그래밍 천재가 될 당신을 위한 최고의 파이썬 강사, 15년 차 시니어 개발자 [이름]!** 🔥  오늘부터 Pandas를 배우는 여정에 함께 갈게요! Pandas? 말 그대로 데이터 가공과 분석에 쓰이는 파이썬 라이브러리인데, 이걸 아는 건 마치 불을 피우는 법이나 만드는 요리를 하는 능력처럼 중요해요. 😋

**Pandas? 그냥 배울 필요 없는 거 아니야? 🤯**

아닙니다! 데이터 분석은 오늘날에 없어서는 안 되는 필수 과목이지요! 마치 어린 시절 수학을 배우던 것처럼, Pandas를 통해 데이터의 숨겨진 이야기를 읽어내고 앞으로 나갈 방향을 예측하는 법을 배울 거예요. 🕵️‍♀️

### 1. Pandas: 데이터 불리기 🤸‍♀️

Pandas는 데이터를 정돈하고 처리하기 위한 강력한 도구인데, 가장 기본적인 기능 중 하나가 바로 데이터 '불러오기' 입니다. Excel 파일이든 CSV 파일이든 Pandas는 편안하게 불러올 수 있어요! 마치 요리에 필요한 재료들을 차근차근 모아서 조리하기 시작하는 것과 같죠. 🍲

```python
import pandas as pd  # Pandas 라이브러리 불러오기

df = pd.read_csv("data.csv") # "data.csv" 파일을 불러와 DataFrame으로 저장 (Pandas는 데이터를 담고 있는 'DataFrame'라는 개념으로 관리해요)
print(df) 
```

💡 초보자 폭풍 질문! 🤔

*  `import pandas as pd` 에서 `pd` 는 왜 사용하는 걸까? 🤔


### 2. DataFrame: 데이터의 세계, 한눈에 보기! 👀

Pandas에서 가장 기본적인 자료구조는 바로 'DataFrame'이라고 불리죠. 이건 여러 행과 열로 구성된 테이블과 같고, 각각의 값은 "index"와 "columns" 라는 이름으로 관리됩니다. 🤯 마치 Excel표처럼 데이터를 잘 정돈하고 보기 편하게 나열해서 사용 가능한 거예요! 💪

```python
import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 28],
        'City': ['Seoul', 'Busan', 'Incheon']}

df = pd.DataFrame(data)  # 'data'를 DataFrame으로 변환!
print(df)
```

🚨 실무주의보! ⚠️

* Pandas는 데이터 분석에서 매우 중요한 역할을 하기 때문에, 이걸 잘 이해하는 게 큰 도움이 될 거예요! 💪


### 3. 데이터 선택하기: 원하는 정보만 집중적으로 보기 👀

Pandas는 'loc'와 'iloc'라는 두 가지 방식으로 특정 행과 열을 선택하는 기능을 제공합니다.  'loc' 는 인덱스를 기준으로 선택하고, 'iloc' 는 숫자 순서를 기준으로 선택하세요! 마치 책의 페이지 번호를 찾는 것처럼 원하는 정보에 직접 접근할 수 있는 강력한 도구죠! 🚀

```python
import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 28],
        'City': ['Seoul', 'Busan', 'Incheon']}

df = pd.DataFrame(data)

# loc: 인덱스 기준으로 선택 (예: Alice의 정보)
alice_info = df.loc[0]  # 첫 번째 행을 선택!
print(alice_info) 

# iloc: 숫자 순서 기준으로 선택 (예: 두 번째 열인 'Age' )
ages = df.iloc[:, 1] # 모든 행의 두 번째 열 (Index 1)를 선택
print(ages) 
```

###  4. 데이터 조작: Pandas가 마법을 걸어줄 거예요! ✨

Pandas는 데이터 조작 기능이 엄청나게 많죠! 🎉 새로운 열 추가, 기존 열 삭제, 행 합치기 등 복잡한 작업도 간단하게 처리할 수 있어요! 😎  마치 레고 블록처럼 다양한 형태로 데이터를 재구성하는 놀라운 경험을 선사합니다. 🧱

```python
import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 28],
        'City': ['Seoul', 'Busan', 'Incheon']}

df = pd.DataFrame(data)

# 새로운 열 추가 (예: Country)
df['Country'] = ['Korea', 'Korea', 'Korea']  
print(df)

# 행 삭제 (예: Bob을 삭제)
df = df.drop([1]) # 2번째 인덱스 행 삭제 (Python에서 인덱싱은 0부터 시작!)
print(df)
```



### 5. 데이터 정리와 변환: 데이터를 미니컬럽으로! ✨

Pandas는 불필요한 데이터를 제거하고 형태를 바꾸는 데에도 탁월합니다. 마치 편안하게 입기 좋은 옷을 만들듯이, 데이터의 '길이'나 '유형' 등을 조정하여 분석에 필요한 형태로 변환하는 기능을 가지고 있습니다. ✂️

```python
import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 28],
        'City': ['Seoul', 'Busan', 'Incheon']}

df = pd.DataFrame(data)

# 데이터 유형 변환 (예: 문자열을 숫자로)
df['Age'] = pd.to_numeric(df['Age'])  # Age 열의 값을 숫자 형태로 변경
print(df) 


```




### 마무리 🚀


Pandas는 데이터 분석의 기본 지식이 되어줄 훌륭한 도구죠! 오늘 배운 내용들을 적극 활용해서 다양한 데이터 분석 프로젝트를 시작해보세요. 당신은 이미 프로그래밍 천재로 향해 나아가고 있답니다! 😎





<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
