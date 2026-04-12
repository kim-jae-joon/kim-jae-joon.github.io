---
layout: post
title: "웹开发: Flask와 Django"
date: 2026-04-12 13:51:38
categories: [파이썬 강의]
---

**11강: 웹 개발 - Flask와 Django, 두 거북이의 춤**

안녕하세요, 파이썬을 배우는 모든 분들! 오늘은 웹 개발에 대한 내용을 알려드리겠습니다. 웹 개발은 보통 3단계로 나누어 설명합니다: FRONTEND(클라이언트 사이드), BEHIND (서버 사이드) 그리고 DATABASE(데이터베이스). 이중 Flask와 Django는 서버 사이드 프레임워크입니다.

**Flask vs Django**

두 거북이의 이름부터가 그다지 유명하지 않습니까? Flask는 가벼운 거북이를 말합니다. 가볍고 빠른 개발을 위한 프레임워크로, 작은 프로젝트에 적합합니다. Django는 큰 거북이를 말합니다. 강력하고 완전한 기능을 제공하는 프레임워크로, 대규모 프로젝트에 적합합니다.

**Django**

Django를 먼저 설명할게요!

### 장점

- 빠른 개발: 
  - ORM (Object Relational Mapping)을 사용하여 데이터베이스와 객체를 쉽게 연결할 수 있습니다. 
  - View Function을 이용해 URL과 View를 연결하는 코드를 작성할 수 있기 때문에, URL을 생성하는 부분에서 시간을 많이 절약할 수 있습니다.

- 보안:
  - Django는 기본적으로 CSRF token이 발급되어 있어, CSRF 공격으로부터 보호됩니다. 
  - 또한, 로그인/로그아웃 기능을 쉽게 구현하여 사용자의 인증을 관리할 수 있습니다.

- 확장성: 
  - Django는 ORM과 View Function을 사용하여 개발하기 때문에, 데이터베이스의 종류나 프로젝트 규모에 따라서도 변경이 용이합니다. 

### 단점

- 학습 곡선:
  - Django는 완전한 기능을 제공하는 프레임워크로, 새로운 개발자에게는 상당히 어렵습니다. 
  - 또한, Django의 공식 문서가 영어로 되어 있어, 한국어를 사용하지 못하거나 번역이 되지 않은 부분이 있습니다.

- 추세:
  - Django는 2019년부터는 큰 프로젝트에 적합하지만, 작은 프로젝트에는 Flask가 더 적합합니다. 

### 예제

```python
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello, world!")
```

위의 코드를 작성하여, URL을 생성하는 방법입니다.

*   `request`는 HTTP 요청을 받고있는 객체입니다. 
*   `HttpResponse` 객체에 문자열 `"Hello, world!"`를 넣어주는 것입니다.
*   `return` 문에 이 객체를 반환합니다. 

위의 코드가 실행되면, 브라우저에서 http://127.0.0.1:8000/ 에 접속하면 "Hello, world!" 가 나타납니다.

### 결론

Django는 완전한 기능을 제공하는 프레임워크로, 큰 프로젝트에 적합합니다. 그러나 작은 프로젝트에는 Flask가 더 적합합니다. 새로운 개발자들은 Django의 공식 문서를 참고하여 학습하시길 바랍니다.

---

**Flask**

이제 Flask에 대해 알려드리겠습니다!

### 장점

- 빠른 개발:
  - 라우팅을 위한 디코레이터(decorator)를 사용하여, 간단하게 URL과 View를 연결할 수 있습니다. 
  - 이와 같이 View Function으로 URL을 생성하는 코드를 작성할 수 있기 때문에, URL을 생성하는 부분에서 시간을 많이 절약할 수 있습니다.

- 가벼움:
  - Django보다 가볍고 빠르다. 

- 쉬운 학습:
  - Flask는 Django에 비해 어려움이 적습니다. 

### 단점

- 보안:
  - CSRF token이 발급되지 않아, CSRF 공격으로부터 보호되지 않습니다.

- 확장성:
  - 데이터베이스의 종류나 프로젝트 규모에 따라서도 변경이 용이하지 않습니다.

### 예제

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'
```

위의 코드를 작성하여, URL을 생성하는 방법입니다.

*   `Flask` 객체 인스턴스를 만들었습니다. 
*   이 객체의 `route()` 함수에 경로가 `/`, 그리고 view function이 `index()`인 곳에서 실행하도록 설정했습니다.
*   `return` 문에 문자열 `"Hello World"`를 반환합니다. 

위의 코드가 실행되면, 브라우저에서 http://127.0.0.1:5000/ 에 접속하면 "Hello World" 가 나타납니다.

### 결론

Flask는 Django보다 가볍고 빠르며, 작은 프로젝트에 적합합니다. 그러나 큰 프로젝트에는 Django가 더 적합합니다. 새로운 개발자들은 Flask의 공식 문서를 참고하여 학습하시길 바랍니다.

---

이 모든 내용이 웹 개발의 세계에서 가장 중요한 부분입니다!

### 마무리

웹 개발은 FRONTEND(클라이언트 사이드), BEHIND (서버 사이드) 그리고 DATABASE(데이터베이스)으로 나누어 설명할 수 있습니다. Flask와 Django는 서버 사이드 프레임워크로, 각각 작은 프로젝트와 큰 프로젝트에 적합합니다. 새로운 개발자들은 공식 문서를 참고하여 학습하시길 바랍니다.

---

**실무주의보**

웹 개발을 하시기 전에, 보안에 대한 생각과 확장성에 대한 생각을 항상 하시길 바랍니다!

### 끝

이제 끝났습니다! 👏🎉😊

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
