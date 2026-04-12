---
layout: post
title: "모듈과 패키지"
date: 2026-04-12 13:51:38
categories: [파이썬 강의]
---

**8강: 모듈과 패키지** 🔥

안녕하세요! 여러분! 파이썬 세계에서 가장 중요하고 매력적인 주제 중 하나인 **모듈과 패키지** 에 대해 가르쳐드리겠습니다. 🔓 이 강의는 여러분이 파이썬 개발자를 꿈꾸는 초보자부터 고수-level 개발자까지 모두에게 도움이 될 것입니다! 😊

**1. 모듈 이란? 🤔**

모듈은 파이썬에서 **코드를 재사용하기 위한 조각 단위**입니다. 모듈은 하나의 파일로 존재하고, 내부에 있는 함수, 변수, 클래스 등을 다른 프로그램에서 import하여 사용할 수 있습니다. 예를 들어, `math` 모듈은 trigonometry 관련 함수를 포함하고 있습니다.

**1.1. 모듈의 이점 🔥**

모듈을 사용하는 이점은 다음과 같습니다:

* **코드 재사용성**: 동일한 기능을 수행하는 코드를 여러 번 작성하지 않아도 됩니다.
* **유지보수 용이**: 하나의 파일로 존재하므로, 소스 코드 관리가 용이합니다.
* **명확성**: 관련된 함수와 변수들을 하나의 파일에 집합하여 명확하게 볼 수 있습니다.

**2. 패키지 이란? 🌐**

패키지는 모듈을 하나 이상 포함하고 있는 **집합**입니다. 패키지를 사용하면, 관련된 모듈들을 하나의 위치에서 관리할 수 있어, 코드 재사용성을 높일 수 있습니다.

**2.1. 패키지의 구조 🔗**

패키지 내부에는 다음과 같은 구조가 있습니다:

* `__init__.py` 파일: 패키지를 정의하고, 모듈을 포함하는 파일입니다.
* `module1.py`, `module2.py`: 패키지에 포함된 모듈 파일입니다.

**3. 모듈과 패키지 import 🔗**

모듈과 패키지를 사용하려면 import 문법이 필요합니다. 예를 들어:

```python
import math  # math 모듈을 import
```

또는:

```python
from math import sin, cos  # 특정 함수만 import
```

**4. 패키지 만들기 🔩**

패키지를 만들고 싶으면, 폴더를 하나 생성하고, `__init__.py` 파일을 포함하여 패키지를 정의하면 됩니다.

예를 들어:

```python
mypackage/
    __init__.py
    module1.py
    module2.py
```

이러한 패키지는 다른 프로그램에서 import 할 수 있습니다.

```python
import mypackage  # mypackage 패키지에 포함된 모듈을 import
```

**5. 실무 활용 💡**

실무에서 모듈과 패키지를 사용하는 예시를 살펴보겠습니다.

예를 들어, `weather` 모듈이 있다고 합시다. 이 모듈은 날씨 데이터를 제공하는 함수들을 포함하고 있습니다.

```python
# weather.py (weather 모듈)
def get_weather(city):
    # 날씨 데이터 조회 API 호출 등...
    return weather_data

def convert_to_celsius(fahrenheit):
    # 섭씨 온도 변환 함수...
    return celsius_value
```

이러한 `weather` 모듈을 다른 프로그램에서 import할 수 있습니다.

```python
# main.py (main 프로그램)
import weather  # weather 모듈 import

city = '서울'
fahrenheit = 25
celsius = weather.convert_to_celsius(fahrenheit)  # 섭씨 온도 변환
print(f'{city} 현재 온도: {celsius} 도')
```

이러한 예시로, 모듈과 패키지의 실무 활용을 살펴보았습니다.

**6. 마치며 🎉**

모듈과 패키지는 파이썬 개발자로서, 코드 재사용성, 유지보수 용이, 명확성을 높일 수 있는 매우 중요한 개념입니다. 이러한 기술을 잘 알고 사용하면, 개발 과정이 훨씬 쉬워질 것입니다! 😊

**💡 초보자 폭풍 질문! 🤔**

모듈과 패키지에 대한 질문 있으신가요? 저에게 물어보세요!

**🚨 실무주의보 🔴**

실무에서 모듈과 패키지를 사용할 때, 주의해야 할 사항들을 다음과 같습니다:

* **중복 정의**: 동일한 이름의 변수나 함수가 이미 정의되어 있으면 오류가 발생합니다. 💡
* **권장 명명법**: 패키지와 모듈의 이름은 모두 소문자로 시작하는 것이 권장됩니다.

이러한 주의사항을 잘 기억하고, 실무에서 모듈과 패키지를 사용하세요! 🔩

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
