---
layout: single
title: "네트워킹 기초: 소켓 프로그래밍"
date: 2026-07-03 18:44:43
categories: [C언어]
---

## 🚀 18강: 네트워킹 기초: 소켓 프로그래밍 - 우리 코드가 네트워크를 넘어서다!

안녕하세요, 코딩 모험가 여러분! 오늘은 🌐 **소켓 프로그래밍**이라는 마법의 세계로 여러분을 안내할게요. 이 주제는 처음 들으면 좀 딱딱하고 어렵게 느껴질 수 있지만, 사실은 우리의 코드가 사람과 사람, 컴퓨터와 컴퓨터 사이를 연결하는 마법의 지팡이와 같은 역할을 하게 해주는 거예요. 준비되셨나요? 그럼 출발해볼까요!

### 🌟 소켓 프로그래밍이란 무엇인가요?

**소켓 프로그래밍**은 마치 **우주선의 통신 장비** 같아요. 각 컴퓨터를 우주선의 별로 생각해보세요. 소켓은 이 별들 사이를 연결하는 **특수한 통신 파이프**라고 할 수 있어요. 이를 통해 데이터를 보내고 받을 수 있죠. 간단하게 말하면, 소켓은 네트워크 상에서의 대화 창구 역할을 합니다.

#### 예시 코드 1: 소켓 생성 및 바인딩

```c
#include <stdio.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

int main() {
    // 1. 소켓 생성
    int serverSocket = socket(AF_INET, SOCK_STREAM, 0);
    if (serverSocket < 0) {
        printf("소켓 생성 실패!\n");
        return -1;
    }
    printf("소켓 생성 성공!\n");

    // 2. 주소 구조체 초기화
    struct sockaddr_in serverAddr;
    serverAddr.sin_family = AF_INET;      // IPv4 사용
    serverAddr.sin_addr.s_addr = INADDR_ANY; // 로컬 IP로 바인딩
    serverAddr.sin_port = htons(8080);    // 포트 번호 설정 (8080 사용)

    // 3. 바인딩
    if (bind(serverSocket, (struct sockaddr*)&serverAddr, sizeof(serverAddr)) < 0) {
        printf("바인딩 실패!\n");
        return -1;
    }
    printf("바인딩 성공!\n");

    // 4. 소켓 리스닝 준비
    listen(serverSocket, 5); // 5개의 연결 대기
    printf("리스닝 모드로 진입!\n");

    return 0;
}
```

**해설:**
- **socket(AF_INET, SOCK_STREAM, 0):** 여기서 `AF_INET`은 IPv4를 의미하고, `SOCK_STREAM`은 TCP 프로토콜을 사용한다는 뜻입니다. 마치 우주선이 특정 주파수로 통신 채널을 설정하는 것과 같아요!
- **bind()**: 우주선이 특정 궤도에서 특정 위치에 정착하는 것처럼, 이 코드는 로컬 IP와 포트에 소켓을 바인딩합니다.
- **listen()**: 우주선이 손님을 받아들일 준비를 하는 것처럼, 이 함수는 클라이언트의 연결 요청을 기다리는 상태로 만듭니다.

### 🚀 다양한 통신 방법: 소켓의 여러 문들

네트워크 통신에서 **문**이 여러 가지가 있어요! 각 문을 통해 다양한 상황에 대응할 수 있어요.

#### 반복문: 클라이언트 연결 수락

```c
while (1) { // 무한 루프: 계속해서 연결 수락
    struct sockaddr_in clientAddr;
    socklen_t clientAddrLen = sizeof(clientAddr);
    int clientSocket = accept(serverSocket, (struct sockaddr*)&clientAddr, &clientAddrLen);
    
    if (clientSocket < 0) {
        printf("연결 수락 실패!\n");
        continue;
    }
    printf("새로운 클라이언트 연결 성공!\n");

    // 여기서 클라이언트와의 통신 로직을 추가할 수 있어요!
    close(clientSocket); // 연결 종료 후 소켓 닫기
}
```

**해설:**
- **while (1):** 마치 우주 정거장이 계속해서 방문객을 맞이하는 것처럼, 무한 루프를 통해 계속해서 새로운 클라이언트 연결을 기다립니다.
- **accept():** 클라이언트가 연결 요청을 보내면, 이 함수는 실제 연결을 수락하고 클라이언트 소켓을 반환합니다.

#### 조건문: 안전한 연결 처리

```c
if (clientSocket >= 0) {
    printf("클라이언트와 연결 성공!\n");
    // 데이터 수신 및 전송 로직 추가
    close(clientSocket); // 작업 완료 후 연결 종료
} else {
    printf("클라이언트 연결 실패!\n");
}
```

**해설:**
- **if-else 구조:** 이는 마치 우주선 조종사가 안전 절차를 철저히 확인하는 것처럼, 클라이언트 연결 상태를 검사하고 적절한 조치를 취합니다.

### 🌐 실무에서의 활용: 네트워크 게임 서버 만들기

소켓 프로그래밍은 **온라인 게임 서버**를 구현하는 데도 필수적이죠! 예를 들어, **"우주 전투 게임"**을 만든다고 상상해보세요.

#### 게임 서버 코드 예시

```c
#include <stdio.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>

#define MAX_CLIENTS 10

void broadcastMessage(int serverSocket, struct sockaddr_in* clientAddr, char* message) {
    int sock;
    struct sockaddr_in broadcastAddr;
    broadcastAddr.sin_family = AF_INET;
    broadcastAddr.sin_addr.s_addr = INADDR_BROADCAST;
    broadcastAddr.sin_port = htons(8080);

    for (int i = 0; i < MAX_CLIENTS; i++) {
        if (i != clientAddr->sin_addr.s_addr) { // 본인 제외
            sock = socket(AF_INET, SOCK_STREAM, 0);
            connect(sock, (struct sockaddr*)&broadcastAddr, sizeof(broadcastAddr));
            send(sock, message, strlen(message), 0);
            close(sock);
        }
    }
}

int main() {
    int serverSocket = socket(AF_INET, SOCK_STREAM, 0);
    struct sockaddr_in serverAddr;
    serverAddr.sin_family = AF_INET;
    serverAddr.sin_addr.s_addr = INADDR_ANY;
    serverAddr.sin_port = htons(8080);

    bind(serverSocket, (struct sockaddr*)&serverAddr, sizeof(serverAddr));
    listen(serverSocket, MAX_CLIENTS);

    struct sockaddr_in clientAddr;
    socklen_t clientAddrLen = sizeof(clientAddr);
    int clientSocket;

    while (1) {
        clientSocket = accept(serverSocket, (struct sockaddr*)&clientAddr, &clientAddrLen);
        if (clientSocket >= 0) {
            printf("클라이언트 연결 성공!\n");
            char buffer[256];
            while (true) {
                read(clientSocket, buffer, sizeof(buffer));
                broadcastMessage(serverSocket, &clientAddr, buffer);
            }
            close(clientSocket);
        }
    }

    return 0;
}
```

**해설:**
- **broadcastMessage 함수:** 게임 내 모든 플레이어에게 메시지를 전달하는 역할을 합니다. 마치 우주 전투에서 모든 우주선에 동일한 명령을 보내는 것과 같죠!
- **while (1) 루프:** 서버는 계속해서 새로운 연결을 수락하고 클라이언트와의 통신을 관리합니다.

### 💡 초보자 폭풍 질문!

**Q1: 소켓 프로그래밍에서 가장 어려운 부분은 무엇인가요?**
**A1:** 처음에는 **네트워크의 복잡성**이 힘들 수 있어요. 특히 에러 핸들링과 보안 설정이 그렇죠. 하지만 기본 개념을 잘 이해하고 연습하다 보면 점점 쉬워집니다. **에러 코드 체크**와 **적절한 예외 처리**를 습관화하는 것이 중요해요!

**Q2: 클라이언트와 서버 간의 연결을 어떻게 유지하나요?**
**A2:** **지속적인 통신**이 핵심입니다. 클라이언트는 정기적으로 **하트비트 패킷**을 보내 연결 상태를 유지하고, 서버는 이 패킷을 통해 연결이 끊어지지 않았는지 확인해요. 마치 우주 정거장에서 정기적인 통신 체크처럼요!

### 🚨 실무 주의보

**주의사항:**
- **보안 설정:** 네트워크 프로그래밍에서는 **데이터 암호화**와 **인증 메커니즘**을 꼭 고려해야 합니다. 보안 취약점은 큰 문제를 일으킬 수 있어요.
- **에러 처리:** 네트워크 통신은 예측 불가능한 요소가 많아요. 항상 **강력한 에러 처리 로직**을 구현하세요.

이렇게 소켓 프로그래밍의 세계로 들어왔으니, 이제 여러분의 코드는 네트워크라는 거대한 우주를 자유롭게 여행할 수 있게 되었어요! 계속 연습하고 실험하며 더 큰 우주로 나아가세요. 🚀🌟

지금까지 [당신의 이름]이었습니다. 다음 강의에서 다시 만나요!

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
