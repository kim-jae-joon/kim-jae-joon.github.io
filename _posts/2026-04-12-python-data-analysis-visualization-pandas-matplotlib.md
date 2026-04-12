---
layout: post
title: "데이터 분석과 시각화: Pandas와 Matplotlib"
date: 2026-04-12 13:51:38
categories: [파이썬 강의]
---

**12강: 데이터 분석과 시각화: Pandas와 Matplotlib**

🚀 데이터 분석과 시각화는 데이터 과학의 핵심입니다. 하지만, 처음 시작하는 초보자들에게서는 어떻게 시작해야 할지 막막한 순간이 있습니다. 오늘은 Pandas와 Matplotlib을 활용하여 데이터를 분석하고 시각화하는 방법을 알려드리겠습니다. 💡

### 1. 왜 Pandas인가?

Pandas는 데이터 분석에 필수적인 라이브러리입니다. 다양한 자료형과 형태의 데이터를 다룰 수 있으며, 빠른 연산 속도로 데이터 처리가 가능합니다.

**Pandas 장점:**

*   다양한 자료형을 지원한다.
*   빠른 연산 속도를 제공한다.
*   데이터 분석에 적합한 API를 제공한다.

### 2. Pandas 사용법

#### 2.1 SERIES (열)

Series는 Pandas의 기본적인 자료구조입니다. 하나의 열을 표현합니다.

```python
import pandas as pd

# Series 생성
s = pd.Series([1, 2, 3, 4, 5])
print(s)
```

#### 2.2 DATAFRAME (행렬)

Dataframe은 여러 열과 행으로 구성된 자료구조입니다.

```python
import pandas as pd

# Dataframe 생성
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35]
})
print(df)
```

### 3. 데이터 분석

#### 3.1 DATAFRAME 연산

Dataframe의 열에 대한 연산이 가능합니다.

```python
import pandas as pd

# Dataframe 생성
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35]
})

# 데이터 분석 - 평균 연산
print(df['age'].mean())
```

#### 3.2 GROUPBY

GROUPBY는 행을 그룹화할 수 있습니다.

```python
import pandas as pd

# Dataframe 생성
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['Seoul', 'Busan', 'Daegu']
})

# 데이터 분석 - 그룹화
print(df.groupby('city')['age'].mean())
```

### 4. 시각화

Matplotlib은 데이터를 시각적으로 표현할 수 있는 라이브러리입니다.

#### 4.1 BAR CHART

바 차트는 데이터의 평균을 그래프로 나타낼 수 있습니다.

```python
import matplotlib.pyplot as plt
import pandas as pd

# Dataframe 생성
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35]
})

# 시각화 - 바 차트
plt.bar(df['name'], df['age'])
plt.xlabel('Name')
plt.ylabel('Age')
plt.title('Age of People')
plt.show()
```

#### 4.2 LINE CHART

선 차트는 데이터의 평균을 그래프로 나타낼 수 있습니다.

```python
import matplotlib.pyplot as plt
import pandas as pd

# Dataframe 생성
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35]
})

# 시각화 - 선 차트
plt.plot(df['name'], df['age'])
plt.xlabel('Name')
plt.ylabel('Age')
plt.title('Age of People')
plt.show()
```

### 💡 초보자 폭풍 질문!

*   왜 Pandas와 Matplotlib을 함께 사용해야 하나요?
*   SERIES와 DATAFRAME의 차이점은 무엇인가요?

### 🚨 실무주의보

*   데이터 분석과 시각화는 복잡한 작업입니다. 반드시 실무 환경에서 직접 경험하고 연습해야 합니다.
*   데이터 과학에는 다양한 라이브러리들이 있습니다. Pandas와 Matplotlib은 기본적인 라이브러리입니다.

이상으로 Pandas와 Matplotlib을 활용하여 데이터 분석과 시각화를 위한 방법을 알아보았습니다. 💡 데이터 과학은 복잡하고 실무적이며, 따라서 반드시 실무 환경에서 직접 경험하고 연습해야 합니다. 🚀

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
