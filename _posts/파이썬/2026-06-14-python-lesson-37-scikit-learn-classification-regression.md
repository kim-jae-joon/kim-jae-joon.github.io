---
layout: single
title: "Scikit-learn: 분류 및 회귀"
date: 2026-06-14 15:02:43
categories: [파이썬]
---

## 37강: Scikit-learn 🚀 - 분류와 회귀의 마법을 배우고, 머신러닝 개발자로 도약!

🔥 오랜만에 만나서 반가워요, 파이썬 일타 친구들!  🚨 이번 강좌는 **Scikit-learn** 을 사용해서 분류와 회귀 분석을 실천하는 방법을 알려드릴 거예요. 머신러닝 세계를 탐험하고 싶은 당신의 야망을 이루도록 최선을 다하겠습니다!

###  🤔 Scikit-learn이란? 🤔

Scikit-learn은 파이썬에서 사용하는 가장 인기 있는 머신러닝 라이브러리 중 하나예요. 마치 한국인들이 좋아하는 **'한식 뷔페'** 처럼, 다양한 알고리즘을 가지고 있어서 어떤 문제를 해결하고 싶은지에 따라 선택할 수 있도록 도와줍니다!  🤩

 Scikit-learn의 장점:

* **사용하기 간편:**  기본적인 파이썬 문법만 알면 쉽게 사용 가능해요. 처음 머신러닝을 접하는 사람도 걱정 마세요! 😎
* **다양한 알고리즘 지원:** 분류, 회귀, 군집화 등 다양한 머신러닝 작업에 필요한 알고리즘들이 모두 있어요. 🔥
* **성능이 좋음:** 전문가들이 오랫동안 개발하고 개선하여 높은 성능을 자랑합니다! 🏆

###  📊 분류: 카테고리를 구분하는 마법 ✨

Scikit-learn으로 데이터를 분석하면서 특정 카테고리에 속하는지 예측하는 것은 '분류'라고 합니다. 예를 들어, 이메일 스팸 여부 판별이나 상품 리뷰의 감정 분류 등이 있습니다! 🤔

* **예시:**  🐶🐱 애완동물 사진을 보고 개인 고양이의 이미지인지 예측하는 프로그램을 만들어 볼까요? 
   

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# iris 데이터셋 불러오기 (꽃 종류 분류)
iris = load_iris()
X = iris.data  # 특징 데이터
y = iris.target # 정답 레이블 

# 데이터를 학습용과 테스트용으로 나누기
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 로지스틱 회귀 모델 생성
model = LogisticRegression() 

# 학습 진행
model.fit(X_train, y_train)

# 테스트 데이터를 사용하여 예측 실행
y_pred = model.predict(X_test)

# 정확도 계산
accuracy = accuracy_score(y_test, y_pred)
print("정확도:", accuracy) 
```



* 코드 설명: 위 코드는 로지스틱 회귀 모델을 사용하여 꽃 종류를 분류하는 예시입니다. 데이터셋을 준비하고 학습 및 테스트 데이터로 나눕니다. 그리고 로지스틱 회귀 모델을 생성하고 학습시킨 후, 테스트 데이터에 대한 예측을 수행합니다. 마지막으로 정확도를 계산하여 모델 성능을 평가합니다.


**💡 초보자 폭풍 질문!** 🤔 이 코드에서 `X_train`, `X_test`, `y_train`, `y_test` 와 같은 변수는 무엇을 나타내고, 각각 어떤 역할을 하는가요?

###  📈 회귀: 값을 예측하는 마법 ✨

회귀 분석은 데이터의 변화 패턴을 파악하여 미래의 값을 예측하는 데 사용됩니다. 주식 가격 변동, 날씨 예보, 물류량 예측 등 다양한 분야에서 활용되고 있습니다! 📈

* **예시:**  🏠 집값 예측 모델을 만들어 볼까요? 특정 지역의 평당가를 알려주는 프로그램을 개발하는 것은 어떨까요?

```python
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# boston 데이터셋 불러오기 (부동산 가격 예측)
boston = load_boston()
X = boston.data # 특징 데이터
y = boston.target # 정답 레이블 (평당가)

# 데이터를 학습용과 테스트용으로 나누기
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 선형 회귀 모델 생성
model = LinearRegression() 

# 학습 진행
model.fit(X_train, y_train)

# 테스트 데이터를 사용하여 예측 실행
y_pred = model.predict(X_test)

# 평균 제곱 오차 계산 (성능 지표)
mse = mean_squared_error(y_test, y_pred)
print("평균 제곱 오차:", mse) 
```



* 코드 설명: 위 코드는 선형 회귀 모델을 사용하여 부동산 가격을 예측하는 예시입니다. 데이터셋을 준비하고 학습 및 테스트 데이터로 나눕니다. 그리고 선형 회귀 모델을 생성하고 학습시킨 후, 테스트 데이터에 대한 예측을 수행합니다. 마지막으로 평균 제곱 오차를 계산하여 모델 성능을 평가합니다.


**🚨 실무주의보!**  🤔 

회귀 분석에서 `mean_squared_error`는 모델의 성능을 나타내는 중요한 지표입니다. MSE 값이 작을수록 모델이 데이터에 잘 맞아 있는 것을 의미합니다.

### 🚀 당신은 머신러닝 개발자가 될 수 있습니다!


🎉 이 강좌를 통해 분류와 회귀 분석의 기본 개념과 실습 방법을 익히셨습니다! Scikit-learn의 다양한 알고리즘들을 활용하여 더욱 복잡하고 현실적인 문제에 대처하는 법을 배우는 것은 어떨까요?




<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
