---
layout: single
title: "C언어 응용: 웹 스크래핑 프로젝트"
date: 2026-07-01 19:41:22
categories: [C언어]
---

### 20강: C언어 응용 - 웹 스크래핑 프로젝트: 인터넷 탐험대 되어보기

**안녕하세요, 코딩 탐험가 여러분!**  
오늘은 C언어로 **웹 스크래핑** 프로젝트를 진행하며, 인터넷 세상에서 보물을 찾아내는 **디지털 보물찾기**를 함께 탐험해볼게요! 🤯 마치 모험가처럼 데이터의 섬을 찾아 떠나는 거죠. C언어의 힘을 빌려, 우리는 단순한 코드 작성자가 아닌 **인터넷 데이터 탐사대**가 될 거예요. 준비됐나요? 시작해볼까요!

---

#### 🚀 웹 스크래핑이란 무엇인가요?

웹 스크래핑은 웹사이트에서 필요한 정보를 자동으로 추출하는 기술이에요. 생각해보세요, 매일 업데이트되는 뉴스나 특정 데이터를 수동으로 복사해서 넣는 대신, 우리는 **로봇**처럼 동작해 자동화를 구현하는 거죠. 

**예시:**  
- **뉴스 웹사이트**에서 최신 기사 제목과 내용을 자동으로 수집해 데이터베이스에 저장하기
- **가격 비교 사이트**에서 특정 상품의 가격 데이터를 정기적으로 업데이트하기

**왜 이걸 해야 할까요?**  
- **시간 절약**: 반복적인 작업 자동화로 시간 효율성 극대화
- **정확성 향상**: 수동 입력에 따른 오류 최소화
- **데이터 분석**: 대량의 데이터를 빠르게 수집하여 분석 가능

---

### 💻 기본 개념 이해하기

#### 1. **HTML 이해하기**
웹 페이지는 주로 **HTML**(HyperText Markup Language)로 구성되어 있어요. 마치 **건물의 구조**처럼 생각하면 쉽습니다:
- **태그**(`<div>`, `<p>`, `<a>`)는 건물의 벽과 문과 같아요.
- **속성**(`class`, `id`)은 특정 부분을 구분하는 라벨이나 번호 같은 거죠.

**예제 코드:**
```c
#include <stdio.h>
#include <libcurl/curl.h> // CURL 라이브러리 사용을 위한 헤더

int main() {
    CURL *curl;
    CURLcode res;
    char output[1024]; // 웹 페이지 내용을 저장할 버퍼

    // CURL 초기화
    curl = curl_easy_init();
    if(curl) {
        // 웹사이트 URL 지정
        curl_easy_setopt(curl, CURLOPT_URL, "https://example.com");
        
        // 응답 내용 저장 설정
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, NULL); // 기본 함수 사용
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, output); // 버퍼 지정
        
        // 요청 실행
        res = curl_easy_perform(curl);
        
        if(res == CURLE_OK) {
            printf("웹 페이지 내용:\n%s\n", output);
            // HTML 구조 분석 시작
            analyzeHTML(output); // 추후 함수 구현 예정
        } else {
            fprintf(stderr, "CURL 에러: %s\n", curl_easy_strerror(res));
        }
        
        curl_easy_cleanup(curl); // 자원 해제
    }
    return 0;
}

// 추후 분석 함수 예시
void analyzeHTML(const char *html) {
    // 여기서는 간단히 텍스트 검색 예시
    if (strstr(html, "<h1>") != NULL) {
        printf("제목 태그 발견:\n");
        // 제목 태그 내용 추출 로직 추가
    }
}
```
**설명:**
- **CURL 라이브러리**를 사용해 웹 페이지를 가져오고 있습니다.
- `curl_easy_setopt` 함수로 URL과 응답 버퍼를 설정합니다.
- `curl_easy_perform`로 요청을 실행하고 결과를 출력합니다.
- `analyzeHTML` 함수는 HTML 내용을 분석하여 필요한 데이터를 추출합니다 (추후 구현 예정).

#### 2. **정규표현식 이해하기**
HTML에서 특정 정보를 찾을 때 정규표현식(Regular Expression)이 큰 도움이 돼요. **데이터를 찾아내는 마법 지팡이**라고 생각해보세요!

**예제 코드:**
```c
#include <regexp.h> // 정규표현식 라이브러리 포함

void extractData(const char *html) {
    regexp_t regex;
    regmatch_t pmatch[1]; // 매치 정보 저장용
    const char *pattern = "<div class=\"item\">(.*?)</div>"; // 예시 패턴
    int ret;

    // 정규표현식 컴파일
    ret = regexp_compile(&regex, pattern, REG_EXTENDED);
    if (ret == REG_OK) {
        // 매치 시도
        ret = regexp_exec(&regex, html, 0, NULL, NULL, pmatch);
        if (ret == REG_OK) {
            printf("데이터 추출 성공:\n");
            printf("%.*s\n", pmatch[0].rm_eo - pmatch[0].rm_so, html + pmatch[0].rm_so);
        } else {
            printf("매치 실패: %s\n", regexp_error(&regex));
        }
        regexp_free(&regex); // 자원 해제
    } else {
        printf("컴파일 실패: %s\n", regexp_error(&regex));
    }
}
```
**설명:**
- **정규표현식 라이브러리**를 사용해 HTML 문자열에서 특정 패턴을 찾아냅니다.
- `<div class="item">(.*?)</div>` 패턴으로 클래스가 "item"인 `<div>` 태그 내의 내용을 추출합니다.
- `regexp_exec` 함수로 매치를 시도하고, 성공 시 해당 내용을 출력합니다.

---

### 🛠️ 실제 코딩 실습: 웹 스크래핑 프로젝트 진행하기

#### **실습 1: 간단한 뉴스 스크래핑**
**목표**: 뉴스 웹사이트에서 최신 기사 제목과 내용을 추출합니다.

**코드 예시:**
```c
#include <stdio.h>
#include <libcurl/curl.h>
#include <string.h>

void printNews(const char *title, const char *content) {
    printf("제목: %s\n", title);
    printf("내용: %s\n", content);
}

int main() {
    CURL *curl;
    CURLcode res;
    char output[1024]; // 웹 페이지 내용을 저장할 버퍼

    curl = curl_easy_init();
    if(curl) {
        curl_easy_setopt(curl, CURLOPT_URL, "https://news.naver.com/"); // 뉴스 사이트 URL
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, NULL); // 기본 함수 사용
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, output); // 버퍼 지정
        
        res = curl_easy_perform(curl);
        
        if(res == CURLE_OK) {
            // HTML 분석 로직 추가 (예: 정규표현식 사용)
            const char *title = "<h1>(.*?)</h1>"; // 예시 패턴
            const char *content = "<div class=\"article\">(.*?)</div>"; // 예시 패턴
            extractAndPrint(output, title, content, printNews);
        } else {
            fprintf(stderr, "CURL 에러: %s\n", curl_easy_strerror(res));
        }
        
        curl_easy_cleanup(curl);
    }
    return 0;
}

// 추출 및 출력 함수 예시
void extractAndPrint(const char *html, const char *titlePattern, const char *contentPattern, void (*printFunc)(const char *, const char *)) {
    regexp_t regexTitle, regexContent;
    regmatch_t pmatchTitle[1], pmatchContent[1];
    int retTitle, retContent;

    // 제목 패턴 컴파일
    retTitle = regexp_compile(&regexTitle, titlePattern, REG_EXTENDED);
    // 내용 패턴 컴파일
    retContent = regexp_compile(&regexContent, contentPattern, REG_EXTENDED);

    if (retTitle == REG_OK && retContent == REG_OK) {
        // 제목 추출
        retTitle = regexp_exec(&regexTitle, html, 0, NULL, NULL, pmatchTitle);
        if (retTitle == REG_OK) {
            const char *title = html + pmatchTitle[0].rm_so;
            printf("추출된 제목:\n%.*s\n", pmatchTitle[0].rm_eo - pmatchTitle[0].rm_so, title);
        }

        // 내용 추출
        retContent = regexp_exec(&regexContent, html, 0, NULL, NULL, pmatchContent);
        if (retContent == REG_OK) {
            const char *content = html + pmatchContent[0].rm_so;
            printf("추출된 내용:\n%.*s\n", pmatchContent[0].rm_eo - pmatchContent[0].rm_so, content);
        }

        regexp_free(&regexTitle);
        regexp_free(&regexContent);
    } else {
        printf("컴파일 실패: %s\n", regexp_error(&regexTitle));
    }
}
```
**설명:**
1. **CURL**을 사용해 웹 페이지 내용을 가져옵니다.
2. **정규표현식**으로 HTML에서 특정 패턴을 찾아 제목과 내용을 추출합니다.
3. `extractAndPrint` 함수에서 추출된 데이터를 출력합니다.

#### **실습 2: 가격 데이터 스크래핑**
**목표**: 전자 상거래 사이트에서 특정 상품의 가격 데이터를 추출합니다.

**코드 예시 (간략화된 버전):**
```c
#include <stdio.h>
#include <libcurl/curl.h>
#include <string.h>

void printPrice(const char *productName, float price) {
    printf("상품명: %s\n", productName);
    printf("가격: ₩ %.2f\n", price);
}

int main() {
    CURL *curl;
    CURLcode res;
    char output[1024];

    curl = curl_easy_init();
    if(curl) {
        curl_easy_setopt(curl, CURLOPT_URL, "https://example-ecommerce.com/products"); // 예시 사이트 URL
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, NULL); // 기본 함수 사용
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, output); // 버퍼 지정
        
        res = curl_easy_perform(curl);
        
        if(res == CURLE_OK) {
            const char *pricePattern = "<span class=\"price\">(.*?)</span>"; // 가격 패턴
            extractAndPrintPrice(output, pricePattern, printPrice);
        } else {
            fprintf(stderr, "CURL 에러: %s\n", curl_easy_strerror(res));
        }
        
        curl_easy_cleanup(curl);
    }
    return 0;
}

// 가격 추출 및 출력 함수 예시
void extractAndPrintPrice(const char *html, const char *pricePattern, void (*printFunc)(const char *, float)) {
    regexp_t regexPrice;
    regmatch_t pmatchPrice[1];
    int ret;

    regexp_compile(&regexPrice, pricePattern, REG_EXTENDED);
    ret = regexp_exec(&regexPrice, html, 0, NULL, NULL, pmatchPrice);
    
    if (ret == REG_OK) {
        const char *priceStr = html + pmatchPrice[0].rm_so;
        float price = atof(priceStr); // 문자열을 실수로 변환
        printFunc("상품명 예시", price); // 상품명은 예시로 고정
    } else {
        printf("가격 추출 실패: %s\n", regexp_error(&regexPrice));
    }

    regexp_free(&regexPrice);
}
```
**설명:**
- **CURL**을 사용해 웹 페이지 내용을 가져옵니다.
- **정규표현식**으로 상품 가격 패턴을 찾아 추출합니다.
- `extractAndPrintPrice` 함수에서 추출된 가격을 출력합니다.

---

### 💡 초보자 폭풍 질문!

**Q1:** CURL 라이브러리를 설치하는 방법이 궁금해요.
- **A1:** 대부분의 Linux 환경에서는 `sudo apt-get install libcurl4-openssl-dev` (Debian 기반) 또는 `sudo yum install curl-devel` (Red Hat 기반) 명령어로 설치 가능합니다. Windows에서는 MinGW나 Visual Studio의 패키지 관리자를 통해 설치할 수 있습니다. 자세한 설치 방법은 시스템 환경에 따라 다를 수 있으니, 구체적인 가이드는 인터넷 검색이나 공식 문서를 참고해보세요!

**Q2:** 정규표현식을 처음 접하는데 어떻게 시작해야 할까요?
- **A2:** 정규표현식은 마치 **마법 주문** 같아요! 시작하기 좋은 사이트로는 [Regex101](https://regex101.com/)이 있습니다. 여기서 다양한 패턴을 실험해보고 결과를 바로 확인할 수 있어요. 기본 패턴들 (`.*`, `\d`, `\w`, `^`, `$`)부터 시작해보세요. 그리고 **간단한 예제부터 시작**하는 것이 중요해요. 예를 들어, 이메일 주소나 전화번호 형식을 찾는 패턴부터 연습해보세요!

---

### 🚨 실무주의보

**주의사항:**  
웹 스크래핑을 진행할 때는 **사이트의 **`robots.txt` 파일을 반드시 확인**해야 합니다. 이 파일은 웹사이트 운영자가 스크래핑을 허용하는지, 허용 범위는 어디까지인 지를 알려줍니다. 무분별한 스크래핑은 법적 문제나 서비스 제한을 초래할 수 있으니, **항상 윤리적이고 합법적인 방식으로 진행**하시길 권합니다.

---

### 마무리

오늘의 **디지털 보물찾기** 미션을 통해 C언어로 웹 스크래핑을 구현해보는 경험을 쌓았어요. 앞으로 더 많은 데이터를 자동으로 수집하고 분석하는 능력을 키워나가면, 당신은 진정한 **코딩 탐험가**가 될 거예요!  

**다음 강의에서는 더 복잡한 데이터 처리와 데이터베이스 연동 방법을 배워볼게요. 그럼 그때까지, 계속해서 코딩 탐험을 즐겨보세요!** 🚀✨

---

**추가 연습 사항:**
- 다양한 웹사이트에서 데이터를 추출해보세요.
- 추출한 데이터를 CSV나 JSON 파일로 저장하는 기능을 추가해보세요.
- 실제 프로젝트에 적용해보며 실력을 향상시켜보세요!

**함께 성장하는 코딩 여정, 응원합니다!** 👏

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
