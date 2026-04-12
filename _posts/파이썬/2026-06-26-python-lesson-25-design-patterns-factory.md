---
layout: single
title: "패턴: Factory 패턴"
date: 2026-06-26 14:59:56
categories: [파이썬]
---

##  25강: 패턴 - Factory 패턴 🚀 (코드 공장을 열고 프로젝트 생산성 UP!🔥)

안녕하세요, 파이썬 일타 강사 **김코딩**입니다! 😎 오늘은 딥다운 하기 좋은 패턴 중 하나인 **Factory 패턴**에 대해 알아볼 거예요. 15년 차 개발자로서 말씀드리면 Factory 패턴은 정말 신뢰할 수 있는 파이썬 유틸리티 같은 존재입니다!  

### 🚨 실무주의보: 어떤 프로그램에서 쓰이는지 🤔

Factory 패턴은 제품 생산라인처럼, 새로운 객체를 만들 때 주어진 종류에 맞는 객체를 생성하는 데 사용됩니다. 마치 자동차 공장처럼 각 라인마다 차량 유형이 다르고, 필요한 부품들이 다른 것과 같죠! 🚗🛠️  

### 🤔 Factory 패턴의 장점? 🤩🤩🤩

* **코드 재사용성 UP!**: 코드를 간결하게 만들어서 여러 곳에서 편리하게 사용할 수 있습니다.
* **객체 생성 방식을 분리!**: 객체 생성 로직과 다른 부분과 분리해서 코드가 더 깔끔해집니다. (🔥 깔끔한 코드는 개발자의 심장에 안정감을 준다!)

### 💡 초보자 폭풍 질문! 🔥  Factory 패턴 이해하기 어려워요? 😩

"Factory 패턴이란 무슨 의미일까?" 라고 고민하시나요? 🤔 그럼 아래 예제를 통해 Factory 패턴의 개념을 더 잘 이해해 보세요.

### ✨ 실전 코드: 🚗 자동차 공장 생산 라인! ✨

```python
class CarFactory:
    def create_car(self, type):
        if type == "sedan":
            return Sedan()  # 세단 자동차 생성
        elif type == "coupe":
            return Coupe() # 쿠페 자동차 생성
        else:
            raise ValueError("Invalid car type")

class Car:  # 모든 자동차의 기본 클래스
    def __init__(self):
        print("Car created!")

class Sedan(Car):  # 세단 자동차 클래스
    def __init__(self):
        super().__init__()
        print("Sedan car created!")

class Coupe(Car): # 쿠페 자동차 클래스
    def __init__(self):
        super().__init__()
        print("Coupe car created!")


factory = CarFactory()

# 차량 생산! 🚗💨
car1 = factory.create_car("sedan")  # 세단 자동차 생성
car2 = factory.create_car("coupe") # 쿠페 자동차 생성


```

**코드 분석 시간!**: 🤔🔍

* **`CarFactory` 클래스**: 이는 자동차 공장이라고 생각하면 됩니다.
    * `create_car(self, type)` 메서드: 주어진 차량 유형(`type`)에 맞춰  세단이나 쿠페 자동차 객체를 생성하는 역할을 합니다.
* **`Car`, `Sedan`, `Coupe` 클래스**: 자동차의 기본적인 정보와 특징을 담고 있는 클래스입니다.

**지금까지 이 부분이 이해되셨나요?** 👍 

### ✨ 나가기 전 한 마디 🚀✨


Factory 패턴은 코드를 더욱 효율적이고 유지보수하기 쉬운 방식으로 만드는 데 도움을 줍니다. 앞으로 다양한 프로젝트에서 Factory 패턴을 활용하면, 개발 시간과 노력을 줄일 수 있고, 더욱 안정적인 코드를 구축할 수 있습니다! 💪

**다음 강의에서는 더 많은 파이썬 패턴들을 알아보도록 하겠습니다. 지금부터도 댓글로 질문이나 의견을 남겨주세요!😊**

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
