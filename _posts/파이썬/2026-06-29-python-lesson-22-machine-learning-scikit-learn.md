---
layout: single
title: "머신러닝 입문: scikit-learn을 이용한 기초"
date: 2026-06-29 18:19:10
categories: [파이썬]
---

### 22강: 머신러닝 입문: scikit-learn을 이용한 기초

안녕하세요, 코딩 초보자 여러분! 오늘은 진짜 신기한 여정에 여러분을 초대하고 싶어요. **scikit-learn**이라는 친구와 함께 머신러닝의 세계로 떠나볼 거예요. 상상해보세요, 여러분이 마법사의 지팡이를 얻은 것 같죠? 이제 마법처럼 데이터를 이해하고 예측하는 능력을 갖추게 되는 거예요! 🪄

#### 🌟 시작하기 전에: 머신러닝이란 무엇인가요?

**머신러닝**이란 컴퓨터에게 데이터를 학습시켜 스스로 패턴을 찾아내고 미래를 예측하는 능력을 주는 기술이에요. 쉽게 말해, 컴퓨터가 사람처럼 학습하고 성장하는 거죠! 마치 학교에서 수학 문제를 풀면서 점점 더 빠르게 정답을 찾는 것처럼요.

**scikit-learn**은 파이썬에서 머신러닝을 쉽게 시작할 수 있게 해주는 강력한 도구상자 같아요. 이 도구상자 안에는 다양한 알고리즘들이 들어있어요. 이제 그 도구상자를 열어보도록 하죠!

### 1. scikit-learn 설치하기

먼저, 이 친구를 여러분의 프로젝트에 초대해야 해요. 터미널이나 콘솔에서 다음 명령어를 입력해보세요:

```python
# pip를 이용해 scikit-learn 설치
!pip install scikit-learn
```

**설명:**
- `!pip install`: 터미널에서 패키지를 설치할 때 사용하는 명령어입니다.
- `scikit-learn`: 머신러닝 알고리즘과 데이터 전처리 도구를 제공하는 패키지입니다.

설치가 완료되면, 마치 마법사의 지팡이를 손에 넣은 것처럼 설레는 마음이 들 거예요!

### 2. 기본 개념 이해하기

#### 2.1 데이터 준비하기

데이터는 머신러닝의 연료와도 같아요. 좋은 연료 없이는 마법을 펼칠 수 없죠! 간단한 예제로 데이터를 준비해볼게요.

```python
import pandas as pd

# 가상의 데이터프레임 생성
data = {
    '나이': [25, 30, 35, 40, 45],
    '소득': [3000, 4000, 5000, 6000, 7000],
    '구매여부': ['아니오', '예', '예', '예', '예']
}
df = pd.DataFrame(data)

# 데이터 확인
print(df)
```

**설명:**
- `pandas` 라이브러리는 데이터를 쉽게 다루는 데 사용됩니다.
- `DataFrame`은 데이터를 표 형태로 정리해줍니다.
- `print(df)`로 데이터를 확인하면서 구조를 이해할 수 있어요.

#### 2.2 데이터 전처리

데이터 전처리는 마법을 펼치기 전에 마법사가 준비하는 단계예요. 결측치 처리, 스케일링 등이 포함됩니다.

```python
from sklearn.preprocessing import StandardScaler

# 결측치 처리 (이 예제에서는 간단히 건너뛰지만, 실제에서는 중요!)
# df.fillna(0, inplace=True)  # 예시로 결측치를 0으로 채움

# 스케일링 적용
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df[['나이', '소득']])  # '구매여부'는 범주형 데이터라 제외

# 스케일링된 데이터프레임으로 변환
df_scaled = pd.DataFrame(df_scaled, columns=['나이', '소득'])
print(df_scaled)
```

**설명:**
- `StandardScaler`는 데이터를 평균 0, 표준편차 1로 조정하여 모델 학습을 돕습니다.
- `fit_transform`은 데이터를 학습하고 동시에 스케일링합니다.

### 3. 모델 학습하기

#### 3.1 분류 모델: 로지스틱 회귀 (Logistic Regression)

이제 마법사의 지팡이로 마법을 펼쳐볼게요! 로지스틱 회귀는 이진 분류에 널리 사용되는 모델입니다.

```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# 데이터 분할
X = df_scaled[['나이', '소득']]  # 특성
y = df['구매여부'].map({'아니오': 0, '예': 1})  # 레이블 (0 또는 1로 변환)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 모델 생성 및 학습
model = LogisticRegression()
model.fit(X_train, y_train)

# 예측 및 평가
y_pred = model.predict(X_test)
print(f"정확도: {accuracy_score(y_test, y_pred)}")
```

**설명:**
- `train_test_split`로 데이터를 학습 세트와 테스트 세트로 나눕니다.
- `LogisticRegression` 모델을 생성하고 학습합니다.
- `fit` 메서드로 학습을 진행하고, `predict`로 예측을 수행한 후 `accuracy_score`로 정확도를 확인합니다.

#### 다양한 접근법 비교

**반복문으로 데이터 처리하기:**
```python
# for문 예시: 데이터의 각 행을 수동으로 처리
for index, row in df_scaled.iterrows():
    print(f"행 {index}: 나이={row['나이']}, 소득={row['소득']}")
```

**조건문으로 분류 기준 설정하기:**
```python
# if-else 문으로 예측 조건 설정
for i in range(len(X_test)):
    if model.predict([X_test[i]])[0] == 1:
        print(f"예측 결과: 구매 예정")
    else:
        print(f"예측 결과: 구매 불확실")
```

### 💡 초보자 폭풍 질문! 💡

**Q1:** 데이터 전처리를 왜 해야 하나요?
**A1:** 전처리는 데이터의 품질을 향상시키고 모델 학습을 안정적으로 만드는 데 필수적입니다. 결측치 처리나 스케일링 없이는 모델이 잘못된 패턴을 학습할 수 있어요.

**Q2:** 로지스틱 회귀 외에 다른 분류 모델은 무엇이 있나요?
**A2:** 결정 트리 (Decision Tree), 랜덤 포레스트 (Random Forest), 서포트 벡터 머신 (SVM) 등이 있습니다. 각각의 모델은 특정 상황에서 더 효과적일 수 있어요. 실험을 통해 가장 적합한 모델을 찾아보세요!

### 🚨 실무주의보 🚨

실제 프로젝트에서는 데이터의 복잡성과 다양성이 훨씬 더 높을 거예요. 따라서 데이터 탐색과 전처리 단계에서 더욱 신경 써야 합니다. 특히, 범주형 데이터의 인코딩이나 더 복잡한 스케일링 방법 (예: MinMaxScaler)을 고려해보세요.

---

이제 여러분은 머신러닝의 기본을 탄탄히 다지셨어요! 다음 강의에서는 더 복잡한 알고리즘과 실제 프로젝트 적용 사례를 다뤄볼게요. 여러분의 코딩 여정, 지금부터 더욱 빛나길 바라요! 🌟

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
