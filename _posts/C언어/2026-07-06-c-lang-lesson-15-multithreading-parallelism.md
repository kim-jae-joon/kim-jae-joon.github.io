---
layout: single
title: "C언어 심화: 멀티스레딩 및 병렬 처리"
date: 2026-07-06 19:39:57
categories: [C언어]
---

## 15강: C언어 심화 - 멀티스레딩 & 병렬 처리: 컴퓨터의 슈퍼히어로를 만나보세요!

**진짜 신기하죠?** 우리가 지금까지 다뤄왔던 단일 스레드 코드들이 마치 한 명의 슈퍼히어로처럼 멋진 일들을 해냈다면, 지금부터 살펴볼 멀티스레딩과 병렬 처리는 **팀워크의 챔피언**이라고 생각하시면 됩니다!  단일 코어에서 벗어나 여러 코어를 활용해 훨씬 빠르고 강력한 프로그램을 만드는 비법을 배우러 떠나볼까요?

### 멀티스레딩: 여러 영웅의 힘을 모아!

**"이거 모르면 큰일 납니다!"** 단일 스레드에서 벗어나 여러 스레드를 동시에 실행하는 멀티스레딩은 마치 팀 스포츠와 같습니다. 각자 맡은 역할을 수행하면서도 서로 협력하는 것이죠. 

#### 기본 개념 탐험

* **스레드란 무엇일까요?** 스레드는 프로그램 내에서 실행되는 **독립적인 실행 흐름**입니다. 마치 팀 프로젝트에서 각자 역할을 맡아 동시에 작업하는 팀원들과 같습니다. 하나의 프로세스 내에서 여러 스레드가 공존하며 자원을 공유하면서 실행될 수 있습니다.

* **왜 멀티스레딩이 필요할까요?** 현대 컴퓨터는 멀티코어 프로세서를 갖추고 있죠. 하지만 단일 스레드만 사용한다면 모든 코어를 활용하지 못하는 상황이 발생합니다. 멀티스레딩을 통해 각 코어에 스레드를 할당하면 **병렬 처리**가 가능해져 성능 향상을 극대화할 수 있습니다! 예를 들어, 비디오 편집 프로그램에서 인코딩과 렌더링을 동시에 처리할 수 있게 됩니다.

#### 코드로 배우는 멀티스레딩

**💡 초보자 폭풍 질문!**

* 멀티스레딩 코드를 작성할 때 주의해야 할 점은 무엇일까요?

**🚨 실무주의보**

멀티스레딩은 강력하지만, **데이터 경쟁** 문제를 조심해야 합니다. 여러 스레드가 동일한 데이터에 접근하고 수정할 때 발생하는 문제죠. 예시 코드를 통해 자세히 살펴보겠습니다.

**예제 1: 간단한 스레드 생성**

```c
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

// 스레드 함수 정의
void* threadFunction(void* arg) {
    int threadId = *(int*)arg; // 스레드 ID 저장
    printf("스레드 %d: 시작!\n", threadId);
    // 간단한 작업 수행 (예: 2초 대기)
    sleep(2); 
    printf("스레드 %d: 작업 완료!\n", threadId);
    return NULL;
}

int main() {
    pthread_t threads[2]; // 스레드 ID 저장을 위한 변수 2개 생성
    int threadIds[2] = {1, 2}; // 각 스레드의 ID

    // 스레드 생성
    for (int i = 0; i < 2; i++) {
        pthread_create(&threads[i], NULL, threadFunction, &threadIds[i]); // 함수 포인터, 인자 전달
    }

    // 모든 스레드 종료 대기
    for (int i = 0; i < 2; i++) {
        pthread_join(threads[i], NULL);
    }

    printf("모든 스레드 종료!\n");
    return 0;
}
```

**코드 해설**

1. **`#include <pthread.h>`:** POSIX 스레드 라이브러리를 포함하여 멀티스레딩 기능을 사용할 수 있도록 합니다.
2. **`void* threadFunction(void* arg)`:** 각 스레드가 실행할 함수를 정의합니다. `arg`는 스레드 ID를 저장하는 포인터입니다.
3. **`pthread_t threads[2];`:** 스레드 ID를 저장할 변수들을 선언합니다.
4. **`pthread_create()`:** 새로운 스레드를 생성합니다. 함수 포인터로 실행할 함수를 지정하고, 스레드 ID를 전달합니다.
5. **`pthread_join()`:** 메인 스레드가 모든 스레드가 종료될 때까지 기다립니다.

**다양한 반복 방식: 조건문과 함께!**

멀티스레딩에서 스레드 간 동기화는 매우 중요합니다. 예를 들어, 공유 자원에 대한 접근을 제어하기 위해 **뮤텍스(Mutex)**를 사용할 수 있습니다. 뮤텍스는 일종의 잠금 장치로, 한 번에 하나의 스레드만 공유 자원을 수정할 수 있도록 합니다.

**예제 2: 뮤텍스를 이용한 동기화**

```c
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h> // sleep 함수 사용

pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER; // 뮤텍스 생성
int sharedCounter = 0; // 공유 자원

void* incrementCounter(void* arg) {
    for (int i = 0; i < 1000; i++) {
        // 뮤텍스 잠금
        pthread_mutex_lock(&mutex); 
        sharedCounter++; // 공유 자원 수정
        printf("스레드 %ld: 카운터 = %d\n", *(long*)arg, sharedCounter);
        // 뮤텍스 해제
        pthread_mutex_unlock(&mutex);
        // 짧은 대기
        sleep(0.01);
    }
    return NULL;
}

int main() {
    pthread_t threads[2];
    long threadIDs[2] = {1L, 2L};

    // 스레드 생성
    for (int i = 0; i < 2; i++) {
        pthread_create(&threads[i], NULL, incrementCounter, &threadIDs[i]);
    }

    // 모든 스레드 종료 대기
    for (int i = 0; i < 2; i++) {
        pthread_join(threads[i], NULL);
    }

    printf("최종 카운터 값: %d\n", sharedCounter);
    return 0;
}
```

**코드 해설**

1. **`pthread_mutex_t mutex`:** 뮤텍스 변수를 선언하여 동기화를 위한 잠금 장치를 만듭니다.
2. **`pthread_mutex_lock()` & `pthread_mutex_unlock()`:** 스레드가 공유 자원에 접근하기 전에 뮤텍스를 잠그고, 작업 후에는 잠금을 해제합니다. 이렇게 하면 동시 접근으로 인한 오류를 방지합니다.

### 병렬 처리: 슈퍼파워 업그레이드!

멀티스레딩은 훌륭하지만, 더 강력한 성능을 원한다면 **병렬 처리**로 나아가야 합니다! 병렬 처리는 **GPU**나 **멀티코어 프로세서**를 활용하여 훨씬 더 많은 코어를 동시에 사용하는 기술입니다. 특히 대규모 데이터 처리나 고성능 컴퓨팅에서 획기적인 속도 향상을 이끌어냅니다.

#### 병렬 처리 라이브러리 활용: OpenMP

C에서 병렬 처리를 쉽게 구현할 수 있도록 **OpenMP** 라이브러리를 소개합니다. 마치 슈퍼 히어로 팀의 코치처럼 복잡한 병렬 작업을 단순화해줍니다!

**예제 3: OpenMP를 이용한 배열 처리**

```c
#include <stdio.h>
#include <omp.h> // OpenMP 라이브러리 포함

int main() {
    int arraySize = 100;
    int array[arraySize];

    // 초기화 (간단히 랜덤 값으로 채움)
    for (int i = 0; i < arraySize; i++) {
        array[i] = rand() % 100;
    }

    printf("원본 배열:\n");
    for (int i = 0; i < arraySize; i++) {
        printf("%d ", array[i]);
    }
    printf("\n");

    // 병렬 처리 시작 (omp_parallel_for)
    #pragma omp parallel for // 병렬 처리 지시어
    for (int i = 0; i < arraySize; i++) {
        // 각 스레드가 배열 요소를 두 배로 만듭니다.
        array[i] *= 2; 
        // 간단한 출력 (선택 사항)
        // printf("스레드 %d: 배열 요소 %d 수정\n", omp_get_thread_num(), array[i]);
    }

    printf("병렬 처리 후 배열:\n");
    for (int i = 0; i < arraySize; i++) {
        printf("%d ", array[i]);
    }
    printf("\n");

    return 0;
}
```

**코드 해설**

1. **`#include <omp.h>`:** OpenMP 라이브러리를 포함하여 병렬 처리 기능을 사용합니다.
2. **`#pragma omp parallel for`:** 이 지시어는 루프를 여러 스레드로 분할하여 병렬로 실행하도록 지시합니다.
3. **`omp_get_thread_num()`:** 현재 실행 중인 스레드의 ID를 반환합니다 (디버깅 목적으로 유용).

**다양한 조건문 활용**

병렬 처리에서 조건문은 각 스레드가 특정 작업을 수행할지 결정하는 데 중요한 역할을 합니다.

**예제 4: 조건문을 활용한 병렬 검색**

```c
#include <stdio.h>
#include <omp.h>

#define ARRAY_SIZE 1000
int array[ARRAY_SIZE];

// 랜덤 데이터 채우기
for (int i = 0; i < ARRAY_SIZE; i++) {
    array[i] = rand() % 1000;
}

int target = 42; // 찾을 값

int main() {
    #pragma omp parallel // 병렬 영역 시작
    {
        int threadId = omp_get_thread_num(); // 각 스레드 ID

        // 각 스레드가 특정 범위의 데이터를 검색하도록 합니다.
        #pragma omp for // 조건문 없이 병렬 반복
        for (int i = threadId * (ARRAY_SIZE / omp_get_num_threads()); 
             i < (threadId + 1) * (ARRAY_SIZE / omp_get_num_threads()); i++) {
            
            if (array[i] == target) {
                printf("스레드 %d: 타겟 값 %d 찾음!\n", threadId, target);
                // 추가 작업 수행 (예: 플래그 설정)
                break; // 찾으면 루프 종료
            }
        }
    }

    printf("타겟 값 %d 검색 완료!\n", target);
    return 0;
}
```

**코드 해설**

1. **`#pragma omp parallel`:** 전체 코드 블록을 병렬 영역으로 지정합니다.
2. **`#pragma omp for`:** 특정 루프를 스레드 간에 분산하여 병렬 처리합니다.
3. **조건문 (`if`):** 각 스레드가 타겟 값을 찾았는지 확인합니다. 찾으면 메시지를 출력하고 루프를 종료합니다.

### 실전 적용 & 주의사항

**💡 초보자 폭풍 질문!**

* 멀티스레딩과 병렬 처리를 실제로 프로젝트에 적용할 때 가장 큰 어려움은 무엇일까요?

**🚨 실무주의보**

* **데이터 일관성 유지:** 여러 스레드가 공유 자원을 수정할 때 발생하는 문제는 **캐시 일관성** 문제 등으로 이어질 수 있습니다. 신중한 설계와 적절한 동기화 기법이 필수입니다.
* **오버헤드 고려:** 스레드 생성 및 관리에는 일정한 오버헤드가 발생합니다. 너무 작은 작업을 병렬로 처리하려 하면 오히려 성능 저하가 발생할 수 있습니다. 적절한 작업 분할이 중요합니다.

**마무리**

멀티스레딩과 병렬 처리는 C 프로그래밍의 진정한 슈퍼파워입니다! 복잡한 문제를 효율적으로 해결하고 프로그램 성능을 극대화하는 열쇠가 되죠. 끊임없이 배우고 실험하며 자신만의 병렬 처리 전문가가 되어보세요! 🚀

이제 여러분도 컴퓨터의 슈퍼히어로 팀을 이끌 준비가 되었나요? 🦸‍♀️🦸‍♂️

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
