---
layout: single
title: "Flask: 라우팅과 템플릿"
date: 2026-06-24 15:00:17
categories: [파이썬]
---

## 🔥 파이썬 Flask 마스터하기! (27강) 라우팅과 템플릿: 웹사이트의 심장, 당신 손안에! 🚀


**15년 차 개발자 시니어 강사가 직접 들려드릴 Flask 완벽 가이드!** 지금까지 파이썬 기초와 Flask 프레임워크를 배우면서 웹개발 열정이 뿜뿜 나오지 않았나요? 😉 오늘부터는  Flask의 진짜 심장, **라우팅과 템플릿**을 다뤄보려고 합니다! 라우팅은 사용자가 웹사이트에 요청하는 경로를 정해서 각 페이지로 이동시키는 거고, 템플릿은 화면 디자인과 데이터 표현을 위한 틀이라고 생각하면 좋아요.

### **💡 초보자 폭풍 질문!**
"라우팅과 템플릿? 어떻게 연결되는지 이해가 안 와요!" 🤔  걱정 마세요! 이 부분을 명확히 설명해드릴게요. 라우팅은 웹사이트 주소에 따라 특정 함수를 실행하고, 그 함수에서 템플릿을 사용해서 화면을 만들어 보여주는 과정이죠. 마치 레스토랑 메뉴처럼 주문(웹 요청)을 받고 요리사(Flask 함수)가 음식(페이지)을 준비하는 것과 같아요!

### **1. 라우팅: 웹사이트의 GPS🗺️**


라우팅은 사용자가 입력한 주소 (URL)에 따라 어떤 페이지를 보여줄지 결정합니다. Flask에서는 `route` 데코레이터를 사용해서 URL 경로와 함수 연결을 설정할 수 있어요!

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') 
def index():  
    return '<h1>Hello, World!</h1>'

if __name__ == '__main__':
    app.run(debug=True)
```

* `@app.route('/')`: 이 부분이 웹사이트의 루트 경로 (홈페이지)에 해당하는 규칙을 설정합니다.
* `def index()`: 'index' 라는 함수가 호출될 때 홈페이지를 표시하는 역할을 합니다.
* `return '<h1>Hello, World!</h1>'`:  이 부분이 HTML 코드를 반환하여 웹 브라우저에 표시됩니다.

**🚨 실무주의보:** 웹사이트 주소는 `/`로 시작하는 루트 경로 외에도 상품 페이지 (`/products`), 로그인 페이지 (`/login`) 등 다양하게 만들 수 있습니다!

### **2. 템플릿: HTML과 파이썬의 화합, 디자인 심화 🚀**


Flask에서는 Jinja2라는 템플릿 엔진을 사용하여 HTML 코드에 파이썬 변수를 쉽게 포함시킬 수 있어요. 🎉 이렇게 HTML과 파이썬이 함께 공동 작업하면 웹사이트 디자인을 훨씬 자유롭고 효율적으로 만들 수 있습니다!

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/user/<name>')
def user(name): 
    return render_template('user.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
```

* `render_template('user.html', name=name)`: 'user.html'라는 파일을 읽어와서  `name` 변수의 값을 대입하여 화면을 생성합니다. 


**templates/user.html:**

```html
<!DOCTYPE html>
<html>
<head>
    <title>{{ name }}님, 환영합니다!</title>
</head>
<body>
    <h1>안녕하세요, {{ name }}님!</h1> 
</body>
</html>
```

* `{{ name }}`: Jinja2 문법으로 파이썬 변수 `name`의 값을 대입하여 표시합니다.


**💡 초보자 팁:**  Flask는 정규 표현식을 사용하는 라우팅과 템플릿 변수 매칭 등 강력한 기능을 제공해 더욱 효율적인 웹 개발을 가능하게 합니다!

### **🎉 Flask 마스터를 향하여 발걸음 다지세요!**


라우팅과 템플릿은 Flask로 웹사이트를 구축하는 기본이자 가장 중요한 부분입니다. 이 두 가지 개념을 이해하면 더욱 복잡하고 진짜 대단한 웹 애플리케이션을 만들 수 있답니다! 🚀🔥






<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
