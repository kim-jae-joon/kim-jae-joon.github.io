---
layout: single
title: "C언어 심화: 배열 포인터와 함수 매개변수"
date: 2026-07-13 19:37:35
categories: [C언어]
---

# 8강: C언어 심화 - 배열 포인터와 함수 매개변수: 코딩 마스터로의 도약!

안녕하세요, 코딩 초보자 여러분! 오늘은 C언어의 매력을 한층 더 깊게 탐험해볼 시간입니다. 🤯 **배열 포인터와 함수 매개변수**라는 주제로, 여러분이 이제 코딩의 고수로 한 걸음 더 나아갈 수 있도록 안내해드릴게요. 이걸 마스터하면 코딩에서 느껴지는 벽이 조금은 낮아질 거예요. 그럼 시작해볼까요?

## 🌟 배열 포인터: 데이터의 마법사

### 개념 이해하기

**배열 포인터**는 마치 마법 지팡이 같아요. 한 번 휘두르면 여러 데이터를 한 번에 다룰 수 있어요! 예를 들어, 학교에서 친구들과의 사진 앨범을 관리한다고 상상해보세요. 각 사진이 배열의 요소이고, 앨범 전체를 가리키는 포인터가 있는 셈이죠. 🖼️

#### 기본 예제: 배열 포인터 활용

```c
#include <stdio.h>

int main() {
    // 배열 선언
    int numbers[] = {10, 20, 30, 40, 50};
    // 배열 포인터 선언
    int *ptr = numbers;  // 포인터가 배열의 첫 번째 요소를 가리키게 함

    // 배열 포인터를 이용한 출력
    printf("배열의 첫 번째 요소: %d\n", *ptr);  // *ptr은 포인터가 가리키는 값을 가져옴
    printf("배열 요소들:\n");
    for (int i = 0; i < 5; i++) {
        printf("%d ", *(ptr + i));  // 포인터를 이용해 배열 요소 접근
    }
    printf("\n포인터가 가리키는 마지막 요소: %d\n", *(ptr + 4));  // 포인터로 마지막 요소 접근

    return 0;
}
```

**코드 설명:**
- `int *ptr = numbers;` : `ptr`이라는 포인터가 `numbers` 배열의 첫 번째 요소를 가리키게 됩니다.
- `*ptr` : 포인터가 가리키는 첫 번째 요소를 출력합니다.
- `*(ptr + i)` : 포인터를 통해 배열의 각 요소에 접근합니다. 여기서 `ptr + i`는 배열의 i번째 요소를 가리키는 포인터를 생성합니다.

### 실제 활용 사례

**💡 초보자 폭풍 질문!**
- **질문**: 포인터로 배열을 다룰 때 왜 `*(ptr + i)`를 사용해야 하나요?
- **답변**: `ptr`은 배열의 첫 번째 요소를 가리킵니다. 따라서 `ptr + i`는 배열의 i번째 요소를 가리키는 위치를 찾아주고, `*` 연산자는 그 위치의 값을 가져옵니다. 이 방식은 배열의 동적 접근을 가능하게 해줍니다.

## 📚 함수 매개변수: 코드의 효율성 극대화

함수 매개변수는 마치 코딩의 툴킷 같아요. 필요한 데이터를 정확하게 전달하여 코드의 유연성과 재사용성을 높여줍니다. 🧰

### 다양한 함수 호출 방식

함수 매개변수를 다양한 방식으로 사용해보겠습니다. 각각의 방법이 어떤 상황에서 유용한지 살펴보겠습니다.

#### 1. 기본 매개변수 전달

```c
#include <stdio.h>

// 기본 매개변수를 사용한 함수
void greet(char *name, const char *defaultName = "친구님") {
    printf("안녕하세요, %s!\n", name ? name : defaultName);  // 이름이 없으면 기본값 사용
}

int main() {
    greet("민준");  // 이름 제공
    greet();        // 기본값 사용
    return 0;
}
```

**코드 설명:**
- `const char *defaultName = "친구님";` : 매개변수에 기본값을 설정합니다. 함수 호출 시 이름을 전달하지 않으면 기본 이름이 사용됩니다.
- `name ? name : defaultName` : 조건 연산자를 이용해 이름이 있는지 확인하고 적절한 값을 출력합니다.

#### 2. 여러 매개변수 전달

```c
#include <stdio.h>

// 여러 매개변수를 사용한 함수
void calculateStats(int num[], int size, double *sum, double *avg) {
    *sum = 0;
    *avg = 0;
    for (int i = 0; i < size; i++) {
        *sum += num[i];  // 합계 계산
    }
    *avg = *sum / size;  // 평균 계산
}

int main() {
    int numbers[] = {10, 20, 30, 40, 50};
    int size = sizeof(numbers) / sizeof(numbers[0]);
    double total, average;

    calculateStats(numbers, size, &total, &average);
    printf("총합: %.2f, 평균: %.2f\n", total, average);
    return 0;
}
```

**코드 설명:**
- `double *sum, *avg;` : 함수 내에서 직접 합계와 평균을 계산하고, 이를 함수 호출 시 포인터를 통해 전달합니다.
- `*sum += num[i];` : 포인터를 통해 합계를 누적합니다.
- `*avg = *sum / size;` : 평균을 계산하고 포인터를 통해 반환합니다.

#### 3. 가변 매개변수 사용 ( 가변 길이 인자 )

```c
#include <stdio.h>

// 가변 매개변수 사용 예제
void printNumbers(int count, ...) {
    va_list args;  // 가변 인자 리스트 초기화
    va_start(args, count);  // count 이후의 인자들을 args에 연결

    printf("전달된 숫자 개수: %d\n", count);
    for (int i = 0; i < count; i++) {
        int num = va_arg(args, int);  // args에서 int 타입의 값을 가져옴
        printf("%d ", num);
    }
    va_end(args);  // 가변 인자 처리 완료
}

int main() {
    printNumbers(3, 10, 20, 30);
    return 0;
}
```

**코드 설명:**
- `va_list args;`, `va_start`, `va_arg`, `va_end` : 가변 인자 처리를 위한 표준 라이브러리 함수들입니다.
- `va_arg(args, int)` : 가변 인자 리스트에서 `int` 타입의 값을 하나씩 꺼내 사용합니다.

### 실무 주의사항 🚨

- **메모리 관리**: 포인터를 사용할 때는 메모리 누수나 잘못된 접근을 조심하세요. 특히 동적 메모리 할당(`malloc`, `free`)은 주의가 필요합니다.
- **예외 처리**: 함수 매개변수에 대한 유효성 검사를 잊지 마세요. 잘못된 입력은 프로그램 오류를 초래할 수 있습니다.

### 마무리: 코딩 마스터로의 도약!

배열 포인터와 함수 매개변수를 잘 다루면 코드의 효율성과 유연성이 극대화됩니다. 이제 여러분도 데이터를 효과적으로 관리하고, 코드를 더욱 간결하고 강력하게 만들 수 있어요! 🚀

**💡 초보자 폭풍 질문!**
- **질문**: 포인터와 함수 매개변수를 함께 사용하면 어떤 이점이 있나요?
- **답변**: 포인터를 통해 동적으로 메모리를 관리하고, 함수 매개변수를 통해 코드의 재사용성을 높일 수 있어요. 예를 들어, 함수가 다양한 크기의 배열을 처리할 수 있게 되어 코드의 유연성이 크게 향상됩니다.

이제 여러분도 이 강력한 기술을 활용해 더 멋진 프로그램을 만들어보세요! 🎉 코딩의 세계는 끝이 없어요. 계속 배우고 탐험하세요!

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
