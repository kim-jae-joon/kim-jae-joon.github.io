---
layout: single
title: "웹 스크래핑 기초: BeautifulSoup 활용"
date: 2026-07-05 18:17:45
categories: [파이썬]
---

## 16강: 웹 스크래핑 기초: BeautifulSoup으로 데이터 사냥꾼 되기

안녕하세요, 코딩의 신나는 여정을 함께 하는 여러분! 오늘은 웹 스크래핑의 세계로 여러분을 초대할게요. **이게 진짜 신기하죠? 인터넷 어딘가에 숨겨진 보물처럼 원하는 데이터를 찾아내는 기술이라니!** 마치 해적이 지도를 들고 보물섬을 찾는 것처럼, BeautifulSoup을 이용해 웹사이트의 깊은 곳에서 정보를 끌어올리는 방법을 배워볼게요. 준비됐다면, 항해를 시작해볼까요?

### 🏝️ 웹 스크래핑이란 무엇인가요?

웹 스크래핑은 웹 페이지에서 필요한 데이터를 자동으로 추출하는 기술이에요. 쉽게 말해, **인터넷을 탐색하는 디지털 보물찾기**라고 생각하면 돼요. 예를 들어, 특정 쇼핑몰의 가격 변동을 추적하거나 뉴스 사이트의 최신 기사를 모아 분석하는 것 등 다양한 용도로 활용될 수 있어요.

### 🤔 왜 BeautifulSoup인가요?

BeautifulSoup은 Python에서 웹 페이지를 파싱하고 데이터를 추출하는 데 특화된 라이브러리예요. **마치 웹 페이지를 맛있는 요리로 만들어주는 주방장 같은 역할**을 합니다. HTML과 XML 문서를 깔끔하게 해석해 주어 코드를 작성하는 우리가 쉽게 데이터를 찾아올 수 있게 돕죠.

### 📚 설치와 기본 설정

먼저, BeautifulSoup과 함께 사용할 `requests` 라이브러리를 설치해야 합니다. 터미널이나 콘솔에서 다음 명령어를 입력해 보세요:

```bash
pip install beautifulsoup4 requests
```

#### 코드 예시 1: 기본적인 웹 페이지 가져오기

```python
# 필요한 라이브러리 임포트
import requests
from bs4 import BeautifulSoup

# 웹 페이지 요청
url = 'https://example.com'  # 테스트용 URL
response = requests.get(url)

# 페이지 내용 가져오기
html_content = response.text

# BeautifulSoup 객체 생성
soup = BeautifulSoup(html_content, 'html.parser')

# 페이지 내용 출력 (간단한 확인)
print(soup.title)  # <title> 태그 내용 출력
```

**해설:**
1. `requests` 라이브러리를 사용해 웹 페이지를 가져옵니다.
2. `BeautifulSoup` 객체를 생성하여 HTML 내용을 파싱합니다.
3. `soup.title`로 페이지의 `<title>` 태그를 출력해 기본적인 파싱이 잘 되는지 확인합니다.

### 🗺️ 데이터 추출: 태그와 속성 활용하기

BeautifulSoup은 태그와 속성을 기반으로 데이터를 추출하는 데 매우 강력합니다. 다양한 방법으로 데이터를 가져올 수 있으니, 몇 가지 예제를 살펴보죠.

#### 코드 예시 2: 특정 태그의 텍스트 추출

```python
# 특정 태그 (예: <a> 태그)의 텍스트 추출
links = soup.find_all('a')  # 모든 <a> 태그 찾기

for link in links:
    print(link.text)  # 각 링크의 텍스트 출력
```

**해설:**
- `soup.find_all('a')`는 모든 `<a>` 태그를 찾아 리스트로 반환합니다.
- `for` 반복문을 사용해 각 태그의 텍스트를 출력합니다.

#### 코드 예시 3: 클래스 속성을 이용한 선택

```python
# 특정 클래스를 가진 요소 선택
product_info = soup.find_all(class_='product-info')

for info in product_info:
    print(info.find('h2').text)  # 각 제품 정보의 제목 출력
    print(info.find('p').text)  # 각 제품 정보의 설명 출력
```

**해설:**
- `class_='product-info'`는 클래스 속성을 이용해 특정 클래스를 가진 태그를 찾습니다.
- 내부 태그를 찾아 텍스트를 추출합니다 (예: `<h2>` 태그의 텍스트).

### 🏃‍♂️ 조건문과 반복문 활용하기

BeautifulSoup을 더 효과적으로 사용하려면 조건문과 반복문을 잘 이해하고 활용해야 합니다. 다양한 상황에 맞는 코드 구현 방법을 살펴볼까요?

#### 조건문 활용 예시: 특정 조건에 맞는 데이터 추출

```python
# 가격이 특정 범위 내에 있는 상품 찾기
prices = soup.find_all('span', class_='price')

for price in prices:
    price_text = price.text.strip()  # 공백 제거
    if '10,000원' <= price_text <= '50,000원':
        print(f"가격 범위 내 상품: {price_text}")
```

**해설:**
- `find_all`을 이용해 가격 정보를 담고 있는 태그를 찾습니다.
- `if` 문을 사용해 가격 범위 내의 데이터만 필터링합니다.

#### 반복문 활용 예시: 여러 페이지 데이터 수집

```python
# 여러 페이지에서 데이터 수집 (예: 페이지 번호 기반)
base_url = 'https://example.com/page-{}'
pages_to_scrape = range(1, 6)  # 1부터 5까지 페이지

for page in pages_to_scrape:
    url = base_url.format(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 각 페이지에서 데이터 추출 로직
    for item in soup.find_all('div', class_='item'):
        print(item.text)
```

**해설:**
- `range`를 사용해 여러 페이지를 순회합니다.
- 각 페이지에서 데이터를 추출하고 출력합니다.

### 💡 초보자 폭풍 질문! 🚨

**Q:** BeautifulSoup으로 데이터를 추출할 때, HTML 구조가 바뀌면 코드가 어떻게 영향을 받나요?
**A:** HTML 구조가 변경되면 해당 부분의 파싱 로직도 수정이 필요할 수 있어요. 하지만 유연한 코드 작성을 위해 태그 클래스나 ID를 주로 사용하면 구조 변경에 덜 민감해질 수 있어요. 또한, 정기적으로 코드를 검토하고 업데이트하는 습관을 들이는 게 좋아요!

### 🚨 실무주의보 💡

실제 프로젝트에서는 **로딩 시간 최적화**와 **에러 처리**가 중요합니다. 사용자 경험을 위해 빠른 로딩을 위해 캐싱 기법을 적용하고, 네트워크 요청에 대한 예외 처리를 꼭 포함시키세요. 예를 들어, 다음과 같이 예외 처리를 추가할 수 있습니다:

```python
try:
    response = requests.get(url)
    response.raise_for_status()  # HTTP 에러 체크
    soup = BeautifulSoup(response.text, 'html.parser')
except requests.RequestException as e:
    print(f"요청 오류: {e}")
```

### 📚 마무리

오늘 배운 내용으로 웹 스크래핑의 기초를 탄탄히 다졌다면, 이제 인터넷의 무한한 데이터 바다를 탐험할 준비가 된 셈이에요! 계속해서 연습하고 다양한 상황에 적용해보세요. 다음 강의에서는 더 심화된 스크래핑 기법과 데이터 처리 방법을 배워볼게요. **데이터 사냥꾼으로서의 여정, 계속됩니다!**

---

이제 여러분도 디지털 시대의 보물찾기꾼이 되었습니다! 화이팅하세요! 💪

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
