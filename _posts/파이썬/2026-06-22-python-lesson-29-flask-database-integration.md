---
layout: single
title: "Flask: 데이터베이스 연동"
date: 2026-06-22 15:00:45
categories: [파이썬]
---

## 29강: Flask 🚀 데이터베이스 연동 - 당신의 웹 애플리케이션을 💥 진정한 강력함으로!

안녕하세요, 파이썬 일타 최고 MVP (물론 제가죠!) 😎  15년 차 시니어 개발자, **[당신의 이름]**입니다! 🔥  요즘에는 '웹 개발'이 사람들 입에서 자주 나오는 단어죠. 

그래서 오늘은 Flask를 사용하여 데이터베이스 연동을 하는 방법을 배우도록 하겠습니다! 💻

처음엔 어려워 보일 수도 있지만, 제가 가르쳐드릴게요!  걱정 마세요, 저는 '코딩 설명의 천재'라고 불리는 이유는 바로 당신이 이해하기 쉽게 설명하는 거예요! 😉


### 데이터베이스 연동? 무슨 말인지 🤔

먼저, 데이터베이스란 **데이터를 저장하고 관리하는 시스템**입니다. 우리가 인터넷에서 사용하는 모든 웹사이트들은 실제로는 데이터베이스에 많은 정보들을 저장하고 있습니다. 

예를 들어, 좋아하는 온라인 스토어에서 상품을 구매했거나, 친구와 소통하는 SNS에서 글을 올리면, 이러한 행위들이 데이터베이스에 저장됩니다. 😎

그리고 Flask는 웹 애플리케이션을 만들 때 사용하는 프레임워크입니다. 즉, **웹사이트처럼 복잡한 프로그램을 만드는 데 도움이 되는 도구**라고 생각하면 됩니다. 👍


### 왜 데이터베이스 연동이 필요할까요?

말 그대로, Flask를 사용해서 웹 애플리케이션을 만들 때에는 데이터베이스와 연결하여 데이터를 관리해야 합니다! 💪

만약 데이터베이스가 없다면, 웹사이트는 매우 제한적인 기능만 제공할 수 있습니다. 🤯 예를 들어, 상품 목록이 고정되어 있고, 사용자 정보도 저장될 수 없는 사이트라고 생각해보세요.  기본적으로 구매 처리도 불가능하죠!

### Flask와 데이터베이스 연동하는 방법

Flask에서 가장 많이 사용되는 데이터베이스 연동 라이브러리는 **SQLAlchemy**입니다. 🚀 SQLAlchemy는 Python을 통해 SQL 쿼리를 작성하고 실행할 수 있게 해주는 강력한 도구입니다. 💪


#### 1. 설치하기

먼저, pip를 이용하여 SQLAlchemy를 설치해야 합니다. 다음 명령어를 터미널에 입력하면 됩니다.

```bash
pip install sqlalchemy
```

### 2. 코드 예시 🤯

그럼 실제로 Flask와 SQLAlchemy를 사용하여 데이터베이스 연동하는 방법을 보여드리겠습니다! 🤩

**예시:  Flask 웹 애플리케이션에서 사용자 목록 보기**

1. **데이터베이스 설정:**
   ```python
   from flask import Flask, render_template
   from sqlalchemy import create_engine, Column, Integer, String
   from sqlalchemy.ext.declarative import declarative_base
   from sqlalchemy.orm import sessionmaker

   app = Flask(__name__)

   # 데이터베이스 연결 설정
   engine = create_engine('sqlite:///users.db')  # sqlite 연동 (기본값) 
   Base = declarative_base()  # SQLAlchemy 기반 클래스 정의
   SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

   class User(Base):
       __tablename__ = 'users' # 테이블 이름
       id = Column(Integer, primary_key=True, index=True) 
       name = Column(String, unique=True, nullable=False)  # 사용자 이름 (중복 X)

   ```

2. **DB 연결 및 데이터 생성:**

 ```python
   def get_db():
       db = SessionLocal()
       try:
           yield db
       finally:
           db.close() 

   @app.route('/')  # 루트 URL 요청 시 실행
   def index():
       db = get_db()
       users = db.query(User).all() 
       return render_template('index.html', users=users) # 'index.html' 파일 전달

   if __name__ == '__main__':
       Base.metadata.create_all(engine)  # 테이블 생성
       app.run(debug=True)
   ``` 



**3. 코드 분석:** 🚀🚀🚀

* `create_engine`: 데이터베이스 연결을 설정합니다. 여기에서는 SQLite를 사용했지만, MySQL이나 PostgreSQL과 같은 다른 데이터베이스도 가능합니다!
* `declarative_base`: SQLAlchemy에서 테이블의 구조를 정의하는 데 사용되는 기본 클래스입니다. 🤯  생각해 보시면, 우리는 이 부분에서 SQL문을 작성하지 않고 직접 데이터베이스와 상호 작용하는 방식을 이용하게 되는데요!
* `Column`: 각 테이블에 있는 열(컬럼)의 정보를 정의합니다. 예를 들어, "id", "name"과 같은 컬럼 이름과 데이터 타입 등을 지정합니다. 🤩  이 부분은 SQL문처럼 직접 작성하지 않고 Python 코드로 간결하게 정의할 수 있다는 점이 큰 매력이죠!
* `SessionLocal`: 데이터베이스와 연결하는 세션을 생성하고 관리합니다. 

### Flask-SQLAlchemy: 데이터베이스 연동의 최고 파트너🔥

Flask-SQLAlchemy를 사용하면 데이터베이스 연동이 더욱 간편해집니다! 💪  더 많은 기능과 편리함을 제공하기 때문에, 웹 애플리케이션 개발 초보자도 쉽게 사용할 수 있습니다. 👍


### 마무리 🚀🚀🚀

오늘은 Flask와 데이터베이스 연동에 대해 알아보았습니다. 🎉   데이터베이스는 웹 애플리케이션의 필수적인 부분이며, Flask-SQLAlchemy를 사용하면 데이터베이스 관리가 훨씬 쉬워집니다! 💪


 다음 강좌에서는 SQLAlchemy를 사용하여 더욱 복잡한 데이터 처리 방식을 알아보도록 하겠습니다. 🔥  자 이제 파이썬 개발의 세계로 함께 뛰어들어봐요! 😎





<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
