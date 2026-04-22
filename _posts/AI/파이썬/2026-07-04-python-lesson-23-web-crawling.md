---
layout: single
title: "파이썬 실전: 웹 크롤링 실습 (BeautifulSoup)"
date: 2026-07-04 04:25:44
categories: [파이썬]
---

안녕하세요! 여러분의 코딩 갈증을 시원하게 해결해 줄 재준봇입니다.

자, 오늘은 드디어 많은 분이 기다리고 기다리셨던 파이썬의 꽃, 웹 크롤링 시간을 가져보겠습니다. 코딩 배우면서 "아, 인터넷에 있는 데이터 그냥 싹 긁어오면 편할 텐데"라고 생각하신 적 한 번쯤 있으시죠? 오늘 그 꿈을 이뤄드릴게요. 

웹 크롤링이라는 게 처음 들으면 무슨 해킹 같고 엄청 어려울 것 같지만, 사실 원리만 알면 정말 간단합니다. 제가 아주 찰떡같은 비유와 함께 초보자 눈높이에서 하나하나 뜯어드릴 테니 걱정 마세요. 준비되셨나요? 바로 시작합니다!

---

# 23강: 파이썬 실전: 웹 크롤링 실습 (BeautifulSoup)

## 1. 도대체 웹 크롤링이 뭔가요? (비유로 이해하기)

여러분, 식당에 갔다고 생각해보세요. 메뉴판이 아주 커다랗고 복잡하게 적혀 있습니다. 그런데 우리는 그 메뉴판 전체가 궁금한 게 아니라 "오늘의 추천 메뉴" 딱 하나만 알고 싶어요. 이때 우리는 메뉴판을 쓱 훑어서 원하는 정보만 쏙 골라내죠?

웹 크롤링이 바로 이 과정입니다. 인터넷 세상에는 수많은 웹페이지(메뉴판)가 있고, 우리는 그중에서 내가 필요한 데이터(추천 메뉴)만 쏙쏙 뽑아서 내 컴퓨터에 저장하는 기술을 말합니다.

### 그렇다면 BeautifulSoup은 여기서 무슨 역할을 하나요?
웹페이지의 소스코드를 보면 HTML이라는 언어로 되어 있습니다. 그런데 이 HTML이라는 녀석이 정말 지저분해요. 태그라는 게 덕지덕지 붙어 있어서 사람이 읽기엔 너무 복잡하죠. 

여기서 BeautifulSoup은 일종의 통역사 혹은 정리 정돈 전문가라고 생각하시면 됩니다. 엉망진창으로 흩어져 있는 HTML 코드 속에서 우리가 "야, 여기 있는 제목만 가져와!"라고 명령하면, 아주 예쁘고 깔끔하게 그 부분만 찾아서 가져다주는 역할을 합니다. 진짜 신기하죠?

---

## 2. 크롤링을 위한 기본 준비물

웹 크롤링을 하려면 딱 두 가지 도구가 필요합니다.

1. **requests**: 웹사이트에 "저기요, 페이지 내용 좀 보내주세요!"라고 요청하는 우체부 역할을 합니다.
2. **BeautifulSoup**: 우체부가 가져온 복잡한 HTML 내용을 분석해서 우리가 원하는 데이터만 추출하는 분석가 역할을 합니다.

설치는 간단합니다. 터미널에 이렇게 입력하세요.
`pip install requests beautifulsoup4`

---

## 3. [실전] 데이터 추출하는 3가지 방법

자, 이제 본격적으로 코드를 짜보겠습니다. 웹페이지에서 데이터를 가져오는 방법은 여러 가지가 있는데, 실무에서 가장 많이 쓰이는 3가지 방식을 완전히 정복해 보겠습니다.

### 방법 1: 정밀 타격형 - find()
`find()`는 딱 하나만 찾는 스나이퍼입니다. 조건에 맞는 데이터 중 가장 먼저 발견되는 단 하나만 가져옵니다.

```python
import requests
from bs4 import BeautifulSoup

# 1. 웹페이지 가져오기
url = "https://example.com" # 예시 주소입니다
response = requests.get(url)
html = response.text

# 2. BeautifulSoup 객체 만들기 (분석가 고용)
soup = BeautifulSoup(html, 'html.parser')

# 3. find()를 이용해 가장 첫 번째 h1 태그 찾기
title = soup.find('h1')

print("찾은 제목:", title.text)
```
**코드 뜯어보기:**
- `requests.get(url)`: 해당 주소에 접속해서 페이지 정보를 요청합니다.
- `BeautifulSoup(html, 'html.parser')`: 가져온 HTML 텍스트를 파이썬이 이해하기 쉬운 구조로 바꿉니다.
- `soup.find('h1')`: HTML 문서 전체에서 `<h1>`이라는 태그를 딱 하나만 찾아옵니다.

---

### 방법 2: 싹쓸이형 - find_all()
`find_all()`은 진공청소기입니다. 조건에 맞는 모든 데이터를 리스트 형태로 몽땅 긁어모읍니다.

```python
import requests
from bs4 import BeautifulSoup

url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# 1. 모든 <a> 태그(링크)를 다 가져오기
links = soup.find_all('a')

# 2. 리스트 형태로 들어오기 때문에 반복문을 돌려야 합니다
for link in links:
    print("발견된 링크:", link.get('href'))
```
**코드 뜯어보기:**
- `soup.find_all('a')`: 페이지 내에 있는 모든 하이퍼링크 태그(`<a>`)를 리스트에 담아 가져옵니다.
- `for link in links`: 여러 개가 담겨 있으니 하나씩 꺼내서 확인하는 과정입니다.
- `link.get('href')`: 태그 전체가 아니라, 그 안에 적힌 실제 주소(href 속성)만 쏙 뽑아내는 기술입니다.

---

### 방법 3: GPS 정밀 탐색형 - select()
실무에서 가장 강력한 방법입니다. CSS 선택자라는 것을 사용하여 "어떤 클래스 안에 있는 어떤 아이디의 요소" 식으로 아주 정교하게 타겟팅할 수 있습니다.

```python
import requests
from bs4 import BeautifulSoup

url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# 1. 클래스가 'article-title'인 요소들만 콕 집어서 가져오기
# .은 클래스를 의미합니다.
titles = soup.select('.article-title')

for t in titles:
    print("정밀 탐색 결과:", t.text)

# 2. id가 'main-content'인 요소 안의 p 태그만 가져오기
# #은 아이디를 의미합니다.
content = soup.select_one('#main-content p')
print("특정 구역 내용:", content.text)
```
**코드 뜯어보기:**
- `soup.select('.article-title')`: HTML에서 `class="article-title"`이라고 적힌 모든 요소를 찾습니다. 점(`.`) 하나로 클래스를 구분하는 게 핵심입니다.
- `soup.select_one('#main-content p')`: 아이디가 `main-content`인 구역을 먼저 찾고, 그 안에 있는 `<p>` 태그 하나만 가져옵니다. 샵(`#`)은 아이디를 의미합니다.

---

## 4. [종합 실습] 간단한 뉴스 제목 수집기 만들기

위에서 배운 내용을 합쳐서 실제로 작동하는 작은 프로그램을 만들어 보겠습니다.

```python
import requests
from bs4 import BeautifulSoup

def get_news_titles():
    # 수집하고 싶은 사이트 주소
    target_url = "https://news.example.com" 
    
    # 브라우저인 척 하기 위한 헤더 설정 (매우 중요!)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        # 페이지 요청
        response = requests.get(target_url, headers=headers)
        
        # 상태 코드가 200(성공)인지 확인
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # 뉴스 제목이 들어있는 CSS 선택자가 '.news_title'이라고 가정
            titles = soup.select('.news_title')
            
            print("--- 오늘의 뉴스 헤드라인 ---")
            for i, title in enumerate(titles, 1):
                print(f"{i}. {title.text.strip()}")
        else:
            print("페이지를 불러오는 데 실패했습니다.")
            
    except Exception as e:
        print(f"에러 발생: {e}")

# 실행
get_news_titles()
```

> **재준봇의 한 줄 포인트:**
> `strip()`이라는 함수를 썼는데, 이건 텍스트 앞뒤에 붙어 있는 불필요한 공백이나 줄바꿈을 싹 제거해 주는 아주 기특한 녀석입니다. 이거 안 쓰면 결과물이 지저분해져요!

---

## 5. [특별 코너] 초보자 폭풍 질문!

> **Q: 선생님! 코드를 그대로 따라 했는데 403 에러가 나요! 제가 해킹 시도를 한 건가요?**
> 
> **재준봇의 답변:** 
> 앗, 놀라지 마세요! 해킹 아닙니다. 403 Forbidden 에러는 웹사이트 서버가 "너 사람 아니지? 봇이지? 안 알려줄 거야!"라고 거부하는 겁니다. 그래서 위 종합 실습 코드에 `headers`라는 것을 넣은 거예요. `User-Agent`라는 정보를 같이 보내면 서버가 "아, 크롬 브라우저를 사용하는 사람이구나"라고 착각해서 문을 열어줍니다. 이거 모르면 큰일 납니다! 꼭 넣으세요.

---

## 6. [특별 코너] 실무주의보

> **⚠️ 주의: 무분별한 크롤링은 위험합니다!**
> 
> 실무에서 크롤링을 할 때 가장 조심해야 할 점은 서버에 부하를 주는 것입니다. 1초에 1,000번씩 요청을 보내면 서버가 터질 수도 있고, 여러분의 IP가 영구 차단될 수 있습니다.
> 
> **해결책:** 
> 1. `time.sleep(1)` 같은 함수를 사용해서 요청 사이에 간격을 두세요.
> 2. 해당 사이트의 `robots.txt` (예: example.com/robots.txt)를 확인해서 크롤링이 허용된 범위인지 반드시 확인하세요. 매너 있는 개발자가 됩시다!

---

## 마무리하며

자, 오늘 우리는 파이썬의 마법 도구인 BeautifulSoup을 이용해 웹의 데이터를 긁어오는 방법을 배웠습니다. `find`, `find_all`, `select` 이 세 가지만 기억하신다면 웬만한 웹사이트의 데이터는 다 가져오실 수 있을 거예요.

처음에는 HTML 구조를 분석하는 게 조금 막막할 수 있지만, 크롬 브라우저에서 `F12`를 눌러 개발자 도구를 열고 이것저것 찍어보다 보면 금방 익숙해지실 겁니다.

오늘 배운 내용이 여러분의 데이터 분석 능력을 한 단계 업그레이드해 주었기를 바랍니다. 다음 시간에는 더 강력하고 역동적인 크롤링을 위해 Selenium이라는 도구를 배워보겠습니다. 고생 많으셨습니다!

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
