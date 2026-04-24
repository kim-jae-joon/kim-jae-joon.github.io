---
layout: single
title: "[Project] SafeKids SNS: AI 기반 실시간 아동 유해 콘텐츠 차단 시스템 설계"
excerpt: "결혼을 앞둔 시점, 내 아이를 위한 프로그램을 만들어보는 뜻 깊은 개발을 해보자."
# 카테고리를 [언어/기술, 성격] 형태로 분리하면 관리가 훨씬 수월해요.
categories: development
tags: [SafeKids, AI, On-device, Filtering]
sidebar:
  nav: "category_nav"
toc: true
toc_sticky: true
---
안녕하세요!

결혼을 약 1년 2개월 앞둔 시점에서, 미래에 태어날 우리 아이가 마주하게 될 디지털 환경에 대해 깊이 고민해보게 되었습니다. 현재의 SNS 환경은 알고리즘에 의해 자극적이고 유해한 콘텐츠가 너무 무방비하게 노출되는 구조적인 문제를 안고 있어요. 

그래서 시중에 있는 단순한 URL 차단 앱을 넘어, **Rust와 Python을 활용한 실시간 AI 콘텐츠 분석**을 통해 우리 아이에게 안전한 SNS 환경을 제공하는 시스템을 직접 설계하고 만들어보려고 합니다. 기술적으로는 고성능 온디바이스 필터링과 정교한 서버 사이드 ML 모델의 시너지를 내는 것을 목표로 하고 있어요. :->

---

## 1. 시스템 아키텍처 (System Architecture)

전체 시스템은 성능과 확장성을 고려해서 3계층(3-Tier) 아키텍처로 설계하려고 합니다.

1. **Mobile Client Layer**: Swift(iOS) 및 Kotlin(Android) 네이티브 코드로 구성해요. 시스템 수준의 네트워크 인터셉터와 UI를 담당합니다.
2. **Core Filtering Engine (Rust)**: 온디바이스에서 실행되는 핵심 로직입니다. 메모리 안전성과 고속 처리를 위해 Rust로 작성하고, UniFFI를 통해 모바일 네이티브 레이어와 연결하려고 합니다.
3. **Backend & ML Server (Python)**: 고수준의 분석이 필요한 경우 FastAPI 기반의 서버가 NSFW(Not Safe For Work) 분류 및 독성 텍스트 분석을 수행하도록 구성합니다.

---

## 2. 핵심 기술 스택 및 결정 근거

### 2.1 Rust (On-device Core)
* **Aho-Corasick 알고리즘**: 수만 개의 유해 키워드를 실시간으로 탐색하기 위해 O(n + m) 시간 복잡도를 보장하는 알고리즘을 사용하려고 합니다.
* **tract 크레이트**: 서버 통신 없이 기기 내부(온디바이스)에서 가벼운 ONNX 모델을 실행해서 1차 판정을 수행해요. 이렇게 하면 개인정보 보호와 성능을 동시에 잡을 수 있습니다.
* **메모리 안전성**: C/C++ 대비 런타임 오류 가능성을 원천적으로 차단해서 시스템 수준 익스텐션의 안정성을 챙기려고 합니다.

### 2.2 Python & FastAPI (Analysis Server)
* **FastAPI**: 비동기 처리를 통해 다수의 모바일 클라이언트에서 발생하는 분석 요청을 지연 없이(Low-latency) 처리합니다.
* **EVA ViT & KoBERT**: 이미지 분류를 위한 Vision Transformer와 한국어 특화 독성 분석 모델인 KoBERT를 활용해서 더 정밀한 분석 파이프라인을 구축하려고 해요.

---

## 3. 콘텐츠 분석 파이프라인 (Analysis Pipeline)

유해 콘텐츠 판정은 계층적 구조로 꼼꼼하게 진행합니다.

1. **L1 Filter (Local)**: Rust 코어에서 로컬 블랙리스트 및 키워드 매칭을 수행합니다. (목표 지연시간 < 1ms)
2. **L2 Inference (On-device ML)**: 경량화된 모델을 통해 확실한 유해물 여부를 기기 내에서 1차 판정해요.
3. **L3 Cloud Analysis (Server)**: 판정이 모호한 경우에만 서버로 데이터를 전송해서 정밀 분석을 수행합니다.

평가 로직은 파이썬으로 다음과 같이 최적화하여 구현하려고 합니다. :-)

```python
def calculate_risk_score(image_score: float, text_score: float, url_score: float) -> float:
    weights = {
        "image": 0.4,
        "text": 0.3,
        "url": 0.3
    }
    
    total_score = (
        (image_score * weights["image"]) +
        (text_score * weights["text"]) +
        (url_score * weights["url"])
    )
    
    return total_score
```

---

## 4. 플랫폼별 구현 전략

* **Android (VpnService & Accessibility)**: Android 환경에서는 `VpnService`를 통해 로컬 트래픽을 가로채고, `AccessibilityService`를 활용해 SNS 앱 화면에 렌더링되는 텍스트 및 이미지 데이터를 추출하려고 합니다.
* **iOS (Network Extension)**: iOS는 보안 정책상 제약이 많기 때문에 `NEFilterDataProvider`를 활용하여 네트워크 레벨의 필터링을 수행하고, Screen Time API를 엮어서 앱 사용을 제어하는 방향으로 구현합니다.

---

## 5. 보안 및 개인정보 보호

아이의 데이터가 외부로 유출되지 않도록 하는 것이 가장 중요하겠죠? ^^

* **Zero-knowledge Principles**: 서버에는 원본 이미지나 텍스트 대신 콘텐츠의 해시(SHA-256) 값과 판정 결과만을 저장합니다.
* **AES-256-GCM**: 기기 내부의 로그 데이터는 Rust의 `ring` 크레이트를 사용하여 강력하게 암호화해서 저장해요.
* **Data Minimization**: 분석이 완료된 데이터는 즉시 메모리에서 날려버리고, 서버 보존 기간도 최소한으로 설정하려고 합니다.

---

## 6. 앞으로의 개발 로드맵

앞으로의 계획은 크게 4단계로 나누어 진행하려고 합니다.

1. **Phase 1**: Rust 기반 키워드 매칭 엔진 및 UniFFI 바인딩 라이브러리 개발
2. **Phase 2**: Python FastAPI 서버 구축 및 ML 모델(NSFW, KoBERT) 파이프라인 최적화
3. **Phase 3**: Android VpnService 연동 및 1차 프로토타입 검증

---

## 7. 마무리하며

본업에서 다루는 C 언어나 제어 로직을 떠나서, 제가 평소 다뤄보고 싶었던 Rust와 AI 기반의 Python 생태계를 맘껏 써보는 프로젝트이기도 합니다. 상용 앱 수준의 완벽함보다는, 실제 우리 아이 스마트폰 환경에서 유효하게 동작하는 최적화된 시스템을 만드는 데 집중하려고 해요. 

관련된 모든 소스 코드와 트러블슈팅 과정은 구현이 진행되는 대로 블로그와 깃허브에 꾸준히 업데이트하겠습니다. 많은 응원 부탁드려요! :->
