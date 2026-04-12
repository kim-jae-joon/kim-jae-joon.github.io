---
layout: single
title: "C 언어 보안 고려사항"
date: 2026-06-27 18:46:26
categories: [C언어]
---

# 24강: C 언어 보안 고려사항 - 코딩의 슈퍼히어로가 되는 법

안녕하세요, 코딩의 슈퍼히어로 팀에 오신 것을 환영합니다! 오늘은 **C 언어 보안 고려사항**에 대해 이야기해볼게요. 이 주제는 마치 슈퍼히어로가 악당을 물리치듯, 여러분의 코드를 안전하게 지키는 힘을 배울 시간이 될 거예요. 준비되셨나요? 진짜 신기하죠? 시작해볼게요!

## 🤔 보안이란 무엇인가요?

보안은 마치 집에 튼튼한 자물쇠를 설치하는 것과 같아요. 외부의 나쁜 요소들이 함부로 들어올 수 없게 하는 거죠. C 언어에서는 특히 메모리 관리와 입력 처리에서 신중해야 합니다. 왜 그럴까요?

### 메모리 관리의 비밀

메모리는 코드의 중요한 자원이에요. 만약 메모리 관리를 잘못하면, **버퍼 오버플로우**나 **버퍼 언더플로우** 같은 위험한 상황이 생길 수 있어요. 비유하자면, 컵에 물을 너무 많이 부어 컵이 넘치거나 모자라서 마시지 못하는 상황이죠!

#### 예제 1: 버퍼 오버플로우 예시

```c
#include <stdio.h>
#include <string.h>

void vulnerableFunction(char *input) {
    char buffer[10];  // 안전한 크기의 버퍼
    strcpy(buffer, input);  // 문제: 입력 크기 체크 없이 복사
    printf("입력 내용: %s\n", buffer);
}

int main() {
    char dangerousInput[50];  // 큰 크기의 입력 데이터
    gets(dangerousInput);     // 위험: 입력 길이를 체크하지 않음
    vulnerableFunction(dangerousInput);
    return 0;
}
```

**설명:**
- `buffer`는 오직 10바이트만 차지할 수 있지만, `strcpy`는 더 많은 데이터를 넣으려고 시도합니다. 이는 버퍼 오버플로우를 일으키며, 잠재적으로 코드 실행을 제어하거나 시스템을 해킹할 수 있는 취약점을 만듭니다.
- **해결 방법:** `strncpy`와 함께 길이를 체크하는 로직을 추가하세요.
  ```c
  strncpy(buffer, input, sizeof(buffer) - 1);  // -1은 Null 종료 문자를 위해
  buffer[sizeof(buffer) - 1] = '\0';  // 안전하게 종료
  ```

### 입력 처리의 핵심

입력 처리는 마치 문을 열어놓고 누군가 들어오길 기다리는 것과 같아요. 보안이 취약하면 외부에서 들어오는 데이터가 시스템을 위협할 수 있어요.

#### 예제 2: 안전한 입력 처리

```c
#include <stdio.h>
#include <string.h>

void safeInputFunction(char *input) {
    // 입력 길이 체크
    size_t inputLen = strlen(input);
    if (inputLen >= 100) {  // 예시로 100바이트 이상은 차단
        printf("입력이 너무 깁니다. 다시 입력해주세요.\n");
        return;
    }

    // 안전하게 복사
    char safeBuffer[100];
    strcpy(safeBuffer, input);  // 하지만 여전히 주의 필요!
    printf("안전하게 처리된 입력 내용: %s\n", safeBuffer);
}

int main() {
    char userInput[200];
    printf("입력해주세요: ");
    fgets(userInput, sizeof(userInput), stdin);  // fgets는 안전한 입력 처리 방법
    userInput[strcspn(userInput, "\n")] = '\0';  // 줄 바꿈 문자 제거
    safeInputFunction(userInput);
    return 0;
}
```

**설명:**
- `fgets`는 입력의 길이를 제한하고 줄 바꿈 문자를 포함할 수 있으므로 더 안전합니다.
- `strcspn`을 사용해 줄 바꿈 문자를 제거하여 추가적인 보안을 확보합니다.

## 💡 초보자 폭풍 질문!

**Q:** `strcpy` 대신 `strncpy`를 사용하면 무조건 안전한가요?

**A:** 네, 맞습니다! 하지만 주의해야 할 점이 있어요. `strncpy`를 사용할 때는 반드시 Null 종료 문자를 명시적으로 추가해야 합니다. 그렇지 않으면 부분적으로 Null 종료가 되지 않은 문자열이 생겨 예기치 않은 오류를 일으킬 수 있어요.

## ### 조건문과 보안

조건문을 잘 활용하면 보안 취약점을 줄일 수 있어요. 예를 들어, **파일 처리**나 **네트워크 통신**에서 유효한 입력을 검사하는 것이 중요합니다.

#### 예제 3: 파일 처리 시 유효성 검사

```c
#include <stdio.h>
#include <stdlib.h>

void processFile(const char *filename) {
    FILE *file = fopen(filename, "r");  // 파일 열기
    if (file == NULL) {
        perror("파일 열기 실패");
        return;
    }

    // 파일 크기 검사 (예시)
    fseek(file, -4L, SEEK_END);  // 마지막 4바이트 위치로 이동
    long fileSize = ftell(file);  // 파일 크기 확인
    rewind(file);  // 원래 위치로 돌아오기

    if (fileSize > 1000000) {  // 예시로 1MB 이상은 차단
        printf("파일이 너무 큽니다. 다른 파일을 사용해주세요.\n");
        fclose(file);
        return;
    }

    // 파일 읽기 및 처리 로직
    char buffer[256];
    while (fgets(buffer, sizeof(buffer), file)) {
        printf("파일 내용: %s", buffer);
    }
    fclose(file);
}

int main() {
    char filePath[100];
    printf("파일 경로를 입력해주세요: ");
    scanf("%99s", filePath);  // 안전한 입력 처리
    processFile(filePath);
    return 0;
}
```

**설명:**
- 파일 크기를 검사하여 큰 파일이 시스템에 부담을 주지 않도록 합니다.
- `scanf`에서 `sizeof(...)`를 사용하여 버퍼 오버플로우를 방지합니다.

#### 예제 4: 네트워크 연결 시 유효성 검사

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

int establishConnection(const char *serverIP, int port) {
    // 소켓 생성
    int sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd < 0) {
        perror("소켓 생성 실패");
        return -1;
    }

    // 소켓 옵션 설정 (간단 예시)
    struct sockaddr_in serverAddr;
    memset(&serverAddr, 0, sizeof(serverAddr));
    serverAddr.sin_family = AF_INET;
    serverAddr.sin_port = htons(port);

    // IP 주소 연결 (안전한 입력 처리)
    if (inet_pton(AF_INET, serverIP, &serverAddr.sin_addr) <= 0) {
        perror("IP 주소 변환 실패");
        close(sockfd);
        return -1;
    }

    // 연결 시도
    if (connect(sockfd, (struct sockaddr *)&serverAddr, sizeof(serverAddr)) < 0) {
        perror("연결 실패");
        close(sockfd);
        return -ERROR;
    }

    return sockfd;
}

int main() {
    char serverIP[50];
    printf("서버 IP 주소를 입력해주세요: ");
    scanf("%49s", serverIP);  // 안전한 입력 처리
    int port = 8080;  // 예시 포트
    int connection = establishConnection(serverIP, port);
    if (connection == -1) {
        printf("연결 실패.\n");
    } else {
        printf("성공적으로 연결되었습니다.\n");
        close(connection);
    }
    return 0;
}
```

**설명:**
- 네트워크 연결 시 유효한 IP 주소와 포트 번호를 검사하여 시스템을 보호합니다.
- `inet_pton`을 사용해 IP 주소 변환이 성공했는지 확인합니다.

## 🚨 실무주의보

**주의사항:** 단순히 코드를 작성하는 것 이상으로, 보안 패치와 최신 라이브러리 업데이트에 항상 주의를 기울여야 합니다. 외부 라이브러리 사용 시에도 보안 취약점에 대한 최신 정보를 확인하는 습관을 들이세요!

---

이렇게 C 언어에서 보안을 강화하는 방법들을 함께 살펴봤어요. 여러분도 이제 슈퍼히어로처럼 코드를 안전하게 지키는 기술을 갖추셨어요! 💪 실전에서도 이 지식을 활용하여 안전하고 견고한 프로그램을 만들어보세요. 초보자 폭풍 질문이나 실무 관련 궁금증이 있으면 언제든지 물어봐주세요!

함께 코딩의 세계를 더 안전하게 만들어가요! 🚀

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
