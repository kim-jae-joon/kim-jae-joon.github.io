---
layout: single
title: "C언어 실전: 멀티스레딩 기초"
date: 2026-07-06 21:08:55
categories: [C언어]
---

## 🚀 15강: C언어 실전! 멀티스레딩 기초 - 코드 속으로 뛰어들어보자! 🚀

안녕하세요, 코딩의 재미에 푹 빠진 초보 개발자 여러분! 오늘은 **멀티스레딩**이라는 신비로운 영역으로 여러분을 안내할게요. 🤯  '멀티스레딩'이라니, 처음 들으면 머리가 복잡해질 수도 있지만 걱정 마세요! 우리 함께라면 쉽고 재미있게 탐험할 수 있답니다. 

**"멀티스레딩이란 뭐야?"** 🧐  

쉽게 말해, **한 프로그램 안에서 여러 작업을 동시에 처리하는 마법**이에요! 마치 주방에서 동시에 스프를 끓이고 샐러드를 씻는 것처럼, 컴퓨터가 여러 스레드를 동시에 실행시켜 효율성을 극대화하는 거죠. 

**왜 멀티스레딩이 필요할까?** 🎉

- **빠른 응답 속도**: 게임이나 실시간 애플리케이션에서 끊김 없이 부드러운 경험을 제공해요! 예를 들어, 게임 캐릭터가 움직이는 동시에 배경 음악이 흘러가고 효과음이 들리는 건 멀티스레딩 덕분이랍니다.
- **자원 활용 극대화**: 현대 CPU는 멀티코어를 갖추고 있어요. 멀티스레딩을 활용하면 각 코어를 최대한 활용하여 프로그램 성능을 끌어올릴 수 있어요. 마치 여러 사람이 동시에 일을 나누어 하는 팀워크처럼요!

**초보자 폭풍 질문!** 💡
> **Q: 멀티스레딩은 복잡해서 초보자에겐 너무 어려운 건 아닌가요?**
> **A:** 처음엔 복잡해 보일 수 있지만, 기본 개념을 이해하고 꾸준히 연습하면 누구든지 마스터할 수 있어요! 오늘부터 함께 단계별로 배워가면서 자신감을 키워봅시다.

### 핵심 개념 다지기: 스레드란 무엇인가?

**스레드**는 프로그램 내에서 실행되는 독립적인 실행 흐름이라고 생각하면 돼요. 마치 한 사람이 여러 작업을 동시에 수행하는 것처럼요! 

**예시 코드: 간단한 스레드 생성**

```c
#include <stdio.h>
#include <pthread.h> // 스레드 관련 헤더 파일

// 스레드 함수 정의 (작업 내용)
void* threadFunction(void* arg) {
    int threadID = *(int*)arg; // 전달받은 스레드 ID
    printf("스레드 ID: %d, 안녕하세요!\n", threadID); // 스레드 별 메시지 출력
    // 스레드 작업 로직 추가 가능 (예: 간단한 계산, 데이터 처리 등)
    return NULL; // 함수 종료
}

int main() {
    pthread_t thread1, thread2; // 스레드 ID 변수 선언
    int threadIDs[] = {1, 2}; // 각 스레드에 할당할 ID 배열

    // 스레드 생성
    pthread_create(&thread1, NULL, threadFunction, &threadIDs[0]); // 첫 번째 스레드 생성
    pthread_create(&thread2, NULL, threadFunction, &threadIDs[1]); // 두 번째 스레드 생성

    // 스레드 종료 대기 (필수!)
    pthread_join(thread1, NULL); 
    pthread_join(thread2, NULL);

    printf("모든 스레드 작업 완료!\n");
    return 0;
}
```

**코드 해설:**

1. **헤더 파일 포함**: `#include <pthread.h>` - 멀티스레딩을 위한 핵심 라이브러리입니다.
2. **스레드 함수**: `void* threadFunction(void* arg)` - 각 스레드가 실행할 작업을 정의하는 함수입니다. `arg` 매개변수로 스레드 ID를 받습니다.
3. **스레드 생성**: `pthread_create()` - 새로운 스레드를 생성합니다. 첫 번째 인자는 생성할 스레드 ID를 저장할 변수, 두 번째 인자는 스레드 속성 (여기서는 NULL), 세 번째 인자는 실행할 함수, 네 번째 인자는 함수에 전달할 데이터입니다.
4. **스레드 동기화**: `pthread_join()` - 메인 스레드가 생성된 스레드가 완료될 때까지 기다립니다. 안정적인 프로그램 종료를 위해 필수입니다!

### 다양한 조건문과 반복문 활용하기: 스레드 제어의 핵심!

**만약 스레드가 특정 조건을 만족하면 다른 작업을 수행해야 한다면?** 🤔

**예시 코드: 스레드 간 조건 기반 작업**

```c
#include <stdio.h>
#include <pthread.h>
#include <unistd.h> // sleep 함수를 위해 포함

// 공유 변수 (스레드 간 소통)
int sharedCounter = 0;

void* incrementCounter(void* arg) {
    for (int i = 0; i < 5; i++) { // 5번 반복
        printf("스레드 ID: %ld, 카운터: %d\n", pthread_self(), sharedCounter);
        sharedCounter++; // 공유 변수 업데이트
        sleep(1); // 잠깐 대기 (실행 흐름 조절)
    }
    return NULL;
}

int main() {
    pthread_t thread1, thread2;
    pthread_create(&thread1, NULL, incrementCounter, NULL); // 스레드 생성
    pthread_create(&thread2, NULL, incrementCounter, NULL); // 다른 스레드 생성

    // 스레드 종료 대기
    pthread_join(thread1, NULL);
    pthread_join(thread2, NULL);

    printf("모든 스레드 작업 완료! 최종 카운터: %d\n", sharedCounter);
    return 0;
}
```

**코드 해설:**

1. **공유 변수**: `sharedCounter` - 여러 스레드가 동시에 접근하고 변경할 수 있는 변수입니다. 멀티스레드 환경에서 주의해야 할 점! 올바른 동기화 메커니즘 (예: 뮤텍스)을 사용해야 데이터 일관성을 유지할 수 있어요.
2. **반복문**: `for (int i = 0; i < 5; i++)` - 각 스레드가 5번 반복하며 작업을 수행합니다.
3. **조건 기반 업데이트**: 스레드 내부에서 공유 변수를 증가시키며, `sleep()` 함수를 사용하여 실행 속도를 조절하고 다른 스레드와의 상호작용을 시뮬레이션합니다.

### 실무 주의보! 🚨  스레드 안전성 유지하기

멀티스레딩의 매력 속에는 **데이터 충돌**이라는 위험이 숨어있어요! 여러 스레드가 동시에 같은 데이터에 접근하면 예상치 못한 결과가 발생할 수 있답니다. 🚨

**해결책**:

- **뮤텍스 (Mutex)**: 상호 배제 메커니즘으로, 한 번에 하나의 스레드만 공유 자원에 접근할 수 있도록 제어합니다.
- **세마포어 (Semaphore)**: 자원 접근 제한을 위한 카운터로, 스레드 간 자원 공유를 안전하게 관리합니다.

**예시 코드: 뮤텍스를 이용한 데이터 보호**

```c
#include <stdio.h>
#include <pthread.h>
#include <unistd.h>

pthread_mutex_t mutex; // 뮤텍스 변수 선언
int sharedData = 0;

void* safeIncrement(void* arg) {
    pthread_mutex_lock(&mutex); // 뮤텍스 잠금
    sharedData++; // 데이터 안전하게 증가
    printf("스레드 ID: %ld, 공유 데이터: %d\n", pthread_self(), sharedData);
    pthread_mutex_unlock(&mutex); // 뮤텍스 해제
    return NULL;
}

int main() {
    pthread_mutex_init(&mutex, NULL); // 뮤텍스 초기화

    pthread_t thread1, thread2;
    pthread_create(&thread1, NULL, safeIncrement, NULL);
    pthread_create(&thread2, NULL, safeIncrement, NULL);

    pthread_join(thread1, NULL);
    pthread_join(thread2, NULL);

    printf("모든 스레드 작업 완료! 최종 공유 데이터: %d\n", sharedData);
    pthread_mutex_destroy(&mutex); // 뮤텍스 해제
    return 0;
}
```

**코드 해설:**

1. **뮤텍스 선언**: `pthread_mutex_t mutex;` - 뮤텍스 변수를 선언합니다.
2. **뮤텍스 잠금**: `pthread_mutex_lock(&mutex);` - 공유 자원에 접근하기 전에 뮤텍스를 잠그어 다른 스레드의 접근을 차단합니다.
3. **데이터 수정**: `sharedData++;` - 뮤텍스 잠금 상태에서 안전하게 데이터를 수정합니다.
4. **뮤텍스 해제**: `pthread_mutex_unlock(&mutex);` - 작업 완료 후 뮤텍스를 해제하여 다른 스레드의 접근을 허용합니다.

### 마무리: 멀티스레딩, 꾸준히 연습이 핵심!

오늘 배운 내용을 바탕으로 다양한 프로젝트에 적용해 보세요! 처음에는 어려울 수 있지만, 꾸준히 연습하고 실제 코드를 작성하며 경험을 쌓아가면 멀티스레딩 마스터가 될 거예요. 💪

**💡 추가 질문이 있다면 언제든지 물어보세요! 함께 성장하는 즐거움을 느껴봐요!** 🚀

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
