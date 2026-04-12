---
layout: single
title: "C 언어 멀티스레딩 및 병렬 처리"
date: 2026-06-20 19:11:32
categories: [Rust C 언어]
---

### 31강: C 언어 멀티스레딩 및 병렬 처리 – 당신의 코드가 슈퍼 히어로로 변신하는 비결

안녕하세요, 멋진 코딩 모험가 여러분! 오늘은 C 언어의 세계에서 가장 강력하고 트렌디한 기술 중 하나인 **멀티스레딩 및 병렬 처리**에 대해 함께 탐험해볼게요. 이 기술을 익히면, 여러분의 프로그램이 단순한 영웅에서 **슈퍼 히어로**로 변신할 수 있습니다! 진짜 신기하죠? 😎

#### 🚀 멀티스레딩이란 무엇인가요?

멀티스레딩은 마치 **슈퍼히어로 팀**처럼 작동합니다. 각 스레드는 독립적으로 동작하면서도 하나의 프로세스 내에서 협업합니다. 예를 들어, **DC 코믹스의 Justice League**처럼 다양한 능력을 가진 멤버들이 각자의 임무를 수행하면서도 공동의 목표를 향해 나아가는 것과 비슷합니다.

##### 개념 설명

- **스레드**: 프로세스 내에서 실행되는 독립적인 경로입니다. 하나의 프로세스는 여러 스레드를 가질 수 있습니다.
- **동기화**: 여러 스레드가 공유 자원에 접근할 때 발생할 수 있는 문제를 해결하기 위한 메커니즘입니다. 예를 들어, **Captain America의 팀 회의**에서 모두가 한 공간에서 동시에 움직이려 할 때의 혼란을 방지하는 것과 같습니다.

#### 📚 기본 설정 및 라이브러리

C 언어에서 멀티스레딩을 구현하기 위해 주로 **POSIX Threads (pthreads)** 라이브러리를 사용합니다. 설치와 설정이 필요하니, 아래와 같이 준비해봅시다.

```c
#include <stdio.h>
#include <pthread.h>

// 스레드 생성 함수 정의
void* threadFunction(void* threadid) {
    int threadNo = *(int*)threadid; // 스레드 ID 받아오기
    printf("스레드 %d 실행 중\n", threadNo);
    // 스레드 작업 로직 여기에 추가
    return NULL;
}

int main() {
    pthread_t threads[5]; // 5개의 스레드 생성 준비
    int threadIDs[5] = {1, 2, 3, 4, 5}; // 각 스레드에 할당될 ID

    // 스레드 생성
    for (int i = 0; i < 5; i++) {
        pthread_create(&threads[i], NULL, threadFunction, &threadIDs[i]); // 스레드 생성 및 함수 전달
    }

    // 모든 스레드 종료 대기
    for (int i = 0; i < 5; i++) {
        pthread_join(threads[i], NULL); // 각 스레드 종료 대기
    }

    printf("모든 스레드가 완료되었습니다.\n");
    return 0;
}
```

**코드 해설:**

1. **`#include <pthread.h>`**: pthread 라이브러리를 포함합니다.
2. **`void* threadFunction(void* threadid)`**: 스레드가 실행할 함수입니다. `threadid`는 스레드의 고유 ID를 전달합니다.
3. **`pthread_create()`**: 새로운 스레드를 생성하고, 함수와 인자를 전달합니다.
4. **`pthread_join()`**: 메인 스레드가 다른 스레드가 완료될 때까지 기다립니다.

#### ⚡ 동기화 기법: 뮤텍스와 세마포어

공유 자원에 대한 충돌을 방지하기 위해 **뮤텍스**와 **세마포어**를 사용합니다. 이들은 **슈퍼히어로 팀의 지휘 시스템**과 같습니다.

##### 예제 1: 뮤텍스를 이용한 동기화

```c
#include <stdio.h>
#include <pthread.h>

pthread_mutex_t mutex; // 뮤텍스 선언

void* threadFunctionMutex(void* threadid) {
    pthread_mutex_lock(&mutex); // 뮤텍스 잠금
    printf("스레드 %d 접근 중\n", *(int*)threadid);
    // 공유 자원 접근 로직
    pthread_mutex_unlock(&mutex); // 뮤텍스 해제
    return NULL;
}

int main() {
    pthread_mutex_init(&mutex, NULL); // 뮤텍스 초기화
    pthread_t threads[3];
    int threadIDs[3] = {101, 102, 103};

    for (int i = 0; i < 3; i++) {
        pthread_create(&threads[i], NULL, threadFunctionMutex, &threadIDs[i]);
    }

    for (int i = 0; i < 3; i++) {
        pthread_join(threads[i], NULL);
    }

    pthread_mutex_destroy(&mutex); // 뮤텍스 해제
    return 0;
}
```

**코드 해설:**

1. **`pthread_mutex_init()`**: 뮤텍스를 초기화합니다.
2. **`pthread_mutex_lock()`**: 뮤텍스를 잠그고 접근 권한을 얻습니다.
3. **`pthread_mutex_unlock()`**: 뮤텍스를 해제하여 다른 스레드의 접근을 허용합니다.

##### 예제 2: 세마포어를 이용한 동기화

```c
#include <stdio.h>
#include <pthread.h>

int semaphore; // 세마포어 선언 (초기값: 허용 개수)
pthread_sem_t sem;

void* threadFunctionSemaphore(void* threadid) {
    pthread_sem_wait(&sem); // 세마포어 잠금 (대기)
    printf("스레드 %d 접근 중\n", *(int*)threadid);
    // 공유 자원 접근 로직
    pthread_sem_post(&sem); // 세마포어 해제 (허용)
    return NULL;
}

int main() {
    semaphore = 2; // 최대 2개 스레드 동시 접근 가능
    pthread_sem_init(&sem, 0, semaphore); // 세마포어 초기화
    pthread_t threads[4];
    int threadIDs[4] = {1001, 1002, 1003, 1004};

    for (int i = 0; i < 4; i++) {
        pthread_create(&threads[i], NULL, threadFunctionSemaphore, &threadIDs[i]);
    }

    for (int i = 0; i < 4; i++) {
        pthread_join(threads[i], NULL);
    }

    pthread_sem_destroy(&sem); // 세마포어 해제
    return 0;
}
```

**코드 해설:**

1. **`pthread_sem_wait()`**: 세마포어 값을 감소시키며 스레드가 대기합니다.
2. **`pthread_sem_post()`**: 세마포어 값을 증가시켜 다른 스레드의 접근을 허용합니다.

#### 💡 초보자 폭풍 질문! 🚀

**질문 1:** 뮤텍스와 세마포어 중 어떤 상황에서 어떤 것을 사용해야 하나요?

**답변:** 뮤텍스는 단일 자원에 대한 잠금이 필요할 때 사용합니다 (예: 파일 접근). 세마포어는 여러 스레드의 동시 접근을 제한하는 데 적합합니다 (예: 특정 개수의 스레드만 동시에 작업 가능한 경우).

**질문 2:** 병렬 처리가 프로그램 성능에 어떤 영향을 미치나요?

**답변:** 병렬 처리는 CPU 리소스를 효율적으로 활용하여 복잡한 작업을 빠르게 처리할 수 있게 합니다. 하지만 오버헤드와 동기화 문제로 인해 잘못 사용하면 성능 저하가 발생할 수 있으니 주의해야 합니다.

#### 🏆 실무주의보 🛡️

멀티스레딩과 병렬 처리는 강력하지만, 잘못 다루면 **시간 여행을 떠나는 위험한 버그**를 만들어낼 수 있습니다. 특히 **데이터 경쟁 조건**이나 **데드락**에 주의해야 합니다. 여러 스레드가 동시에 같은 자원에 접근하려고 할 때 발생하는 문제들입니다. **예외 처리와 철저한 테스트**를 통해 이러한 이슈를 사전에 방지하세요!

#### 🎯 실전 적용 사례

**사례 1: 비디오 스트리밍 앱**
- **문제**: 비디오 프레임 처리와 네트워크 데이터 수신을 동시에 수행해야 합니다.
- **해결책**: 두 개의 스레드를 생성하여 각각 프레임 처리와 네트워크 데이터 수신을 담당합니다. 뮤텍스를 사용해 공유 자원(예: 버퍼)에 대한 접근을 안전하게 관리합니다.

**사례 2: 실시간 주식 분석 시스템**
- **문제**: 주식 데이터 수집과 실시간 분석을 동시에 수행해야 합니다.
- **해결책**: 세 개 이상의 스레드로 데이터 수집, 분석, 결과 출력을 분리하여 병렬로 처리합니다. 세마포어를 통해 분석 작업의 동시 접근을 제한합니다.

#### 마무리

오늘 배운 멀티스레딩과 병렬 처리는 당신의 코드를 슈퍼 히어로로 변신시키는 마법의 주문입니다! 다양한 상황에서 이 기술을 활용해보세요. 아직 궁금한 점이 있다면 언제든지 질문해주세요! 함께 성장해나가요, 코딩 모험가 여러분! 🎉

---

이렇게 상세하고 친근한 강의를 통해 초보자들도 멀티스레딩과 병렬 처리의 핵심 개념과 실용적인 적용 방법을 쉽게 이해할 수 있도록 도와드리고자 했습니다. 질문과 코너를 통해 참여도를 높이고, 다양한 예제를 통해 실제 코딩 경험을 제공했습니다.

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
