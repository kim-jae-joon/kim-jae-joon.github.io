---
layout: single
title: "Scikit-learn: 모델 평가 및 성능 분석"
date: 2026-06-11 15:03:31
categories: [파이썬]
---

##  🔥40강: Scikit-learn - 모델 평가 및 성능 분석!🔥 (결국, 내 모델은 얼마나 좋아요?!)

안녕하세요! 파이썬 일타 강사 최고의 선생님 🎤(자신감에 폭발!) 이라고 불리는 저 여기는 바로 **시니어 개발자** 🎉으로서 15년 동안 코딩을 하고 살아왔습니다. 오랜 시간 축적한 경험과 유머 감각으로 이번 강의에서는 **Scikit-learn 모델 평가 및 성능 분석**에 대해 알려드릴게요!

모델이 만들어졌는데, 그게 얼마나 잘 나오는지 딱 보는 방법이 없다면 😥 마치 운동하고 "내 근육량은 어느 정도?"만 물으며 체력 트레이닝을 하듯이 아무런 성과를 판단할 수 없죠! 모델 평가와 성능 분석은 우리가 코딩의 진짜 목표인 **효율성**과 **정확성**을 확보하는 데 필수적인 요소입니다. 🚀

### 🎯 기본 개념: 정확도 vs. 오차

우선 우리는 '모델이 얼마나 정확한지' 판단하기 위해 **정확도(Accuracy)**와 **오차(Error)**라는 두 가지 중요한 개념을 알아야 합니다! 😎

>**예시:**
> 🐈🐶 사진 분류 모델이 있어요. 이 모델은 '고양이' 사진 100개 중 95개를 정확히 분류하고, '강아지' 사진 100개 중 92개를 정확히 분류했습니다. 이 경우:
> * **정확도:** (95 + 92) / 200 = 93.5% 🎉
> * **오차:** (5 + 8) / 200 = 0.065  (이 값은 작을수록 좋겠죠? 🤔)

### 📊 평가 지표: 여러 가지 옵션을 활용! 🧰

Scikit-learn은 모델의 성능을 평가하는 데 다양한 지표를 제공합니다.  🔥

* **Accuracy:** 가장 기본적인 평가 지표입니다! 전체 예측 결과 중 맞춘 비율로, 분류 문제에서 자주 사용됩니다.
* **Precision(정밀도):**  모델이 예측했던 '긍정' 클래스 중 실제로 '긍정'인 것의 비율을 나타냅니다. 🎯 (예: 바이러스 감염 예측 모델의 경우, 정확히 바이러스가 있다고 예측한 중 얼마나 진짜 바이러스였는지)
* **Recall(재현율):** 실제 '긍정' 클래스를 모두 찾아내었는 비율을 나타냅니다. 🏹 (예: 위 바이러스 감염 모델의 경우, 실제로 바이러스가 있는 사람들을 모두 찾았는지)
* **F1-Score:** Precision과 Recall의 조화 평균으로, 두 지표를 동시에 고려하여 모델 성능을 측정합니다. ⚖️

💡 초보자 폭풍 질문! : "어떻게 이 모든 지표들을 활용하면 좋을까요?" 🤔

---
### 📈  코드로 배우기: Scikit-learn 평가하기!

지금부터 실제 코드를 통해 모델 평가 방법을 알아보겠습니다. 🎉  다음은 로지스틱 회귀 모델을 사용하여 영화 리뷰 감정 분류 문제를 해결하는 예시입니다. 🎬

```python
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# 데이터 로드 및 전처리 (생략) ...

# 데이터를 학습용과 테스트용으로 분할
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42  # 랜덤 상태 설정은 반복성을 위해 중요합니다!
)

# 로지스틱 회귀 모델 생성 및 학습
model = LogisticRegression()
model.fit(X_train, y_train)

# 테스트 데이터로 예측 진행
y_pred = model.predict(X_test)

# 성능 지표 계산
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

# 결과 출력
print(f"Accuracy: {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1-Score: {f1:.4f}")

```

> 코드 설명: 위 코드는 먼저 데이터를 학습용과 테스트용으로 분할하고, 로지스틱 회귀 모델을 생성하여 학습합니다.  학습된 모델로 테스트 데이터에 대한 예측을 수행하고,  `accuracy_score`, `precision_score`, `recall_score`, `f1_score` 함수를 사용하여 성능 지표를 계산하여 출력합니다.

**🚨 실무주의보:** 

어떤 지표가 가장 중요한지는 문제 유형과 목적에 따라 다릅니다! 예를 들어, 바이러스 감염 모델에서는 Recall이 더 중요하게 여겨질 수 있습니다. 😉


### 🚀 다음 강의 전망: 심화 학습으로 가다! 😎

오늘은 Scikit-learn을 사용하여 모델 평가 및 성능 분석에 대해 알아보았습니다! 📈  다음 강의에서는 더욱 심화된 지표와 그 활용법을 배우며 프로젝트에서 실제로 적용할 수 있는 스킬을 키울 것입니다. 🔥

**기억하세요! 데이터 과학자는 단순히 코드를 작성하는 것이 아니라, 데이터를 통해 세상을 이해하고 문제를 해결하는 **마법사**입니다! ✨





<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
