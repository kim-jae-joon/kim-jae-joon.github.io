---
layout: single
title: "C언어 활용: 소켓 프로그래밍 입문"
date: 2026-07-07 19:39:40
categories: [C언어]
---

# 14강: C언어 활용: 소켓 프로그래밍 입문 – 네트워크의 마법사가 되어보자!

안녕하세요, 초보 개발자 여러분! 오늘은 당신이 네트워크의 마법사이자 C언어의 고수가 될 수 있는 길을 함께 걸어나가보려 합니다. **소켓 프로그래밍**이라니, 들어봤나요? 이건 마치 마법 지팡이 같은 존재예요. 이걸 잡으면 컴퓨터들이 서로 대화할 수 있게 만드는 마법사가 될 수 있답니다! 🤯

## 소켓 프로그래밍이란?

**소켓 프로그래밍**은 두 개 이상의 컴퓨터가 서로 통신할 수 있게 만드는 기술입니다. 쉽게 말해, 당신이 채팅 앱을 만드는 것처럼 생각해보세요. 사람들이 메시지를 주고받는 것처럼 컴퓨터들도 데이터를 주고받을 수 있게 만드는 거죠. 이건 마치 **지구상의 모든 도시가 직접 통신선을 통해 연결된 네트워크**와 같아요. 🌐

### 기본 개념 이해하기

#### 1. 소켓 (Socket)
소켓은 통신의 **입구**와 **출구** 역할을 합니다. 마치 집의 문처럼, 데이터가 들어오거나 나가는 통로 역할을 하는 거죠.

**예제 1: 소켓 생성 및 바인딩**
```c
#include <stdio.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

int main() {
    // 소켓 생성
    int serverSocket = socket(AF_INET, SOCK_STREAM, 0);
    if (serverSocket < 0) {
        perror("Socket creation failed");
        return -1;
    }
    
    // 구조체 선언
    struct sockaddr_in serverAddr;
    serverAddr.sin_family = AF_INET; // IPv4 사용
    serverAddr.sin_addr.s_addr = INADDR_ANY; // 로컬 주소
    serverAddr.sin_port = htons(8080); // 포트 번호 설정 (8080으로 예시)

    // 소켓 바인딩
    if (bind(serverSocket, (struct sockaddr *)&serverAddr, sizeof(serverAddr)) < 0) {
        perror("Binding failed");
        close(serverSocket);
        return -1;
    }
    
    printf("서버가 포트 %d에 바인딩되었습니다.\n", ntohs(serverAddr.sin_port));
    return 0;
}
```
- **`socket(AF_INET, SOCK_STREAM, 0)`**: 이 함수는 소켓을 생성합니다. `AF_INET`은 IPv4를 의미하고, `SOCK_STREAM`은 TCP 프로토콜을 사용한다는 것을 나타냅니다.
- **`bind()`**: 소켓에 주소를 할당하는 역할을 합니다. 여기서는 로컬 주소와 포트 번호를 설정합니다.

#### 2. 클라이언트와 서버 모델
- **서버**: **"네트워크의 호스트"** 역할을 합니다. 여러 클라이언트와 통신을 기다립니다. **"커피숍 주인"** 같다고 생각하면 됩니다. 많은 손님들이 오길 기다리며, 각자에게 맞춤 서비스를 제공합니다.
- **클라이언트**: **"네트워크의 손님"** 역할입니다. 서버에 연결 요청을 보내고 데이터를 주고받습니다. **"커피숍 손님"**처럼 서버에 메시지를 보내고 응답을 기다립니다.

### 다양한 문법 활용 예시

#### 반복문으로 통신 처리하기
반복문은 소켓 프로그래밍에서 매우 중요합니다. 데이터를 계속해서 받아오거나 보내는 데 사용되죠.

**예제 2: 클라이언트 측 데이터 수신**
```c
#include <stdio.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>

int main() {
    int clientSocket = socket(AF_INET, SOCK_STREAM, 0);
    if (clientSocket < 0) {
        perror("Client socket creation failed");
        return -1;
    }

    struct sockaddr_in serverAddr;
    serverAddr.sin_family = AF_INET;
    serverAddr.sin_port = htons(8080); // 서버의 포트 번호
    serverAddr.sin_addr.s_addr = inet_addr("127.0.0.1"); // 서버 주소

    if (connect(clientSocket, (struct sockaddr *)&serverAddr, sizeof(serverAddr)) < 0) {
        perror("Connection failed");
        close(clientSocket);
        return -1;
    }

    char buffer[1024];
    while (1) { // 무한 루프: 계속 데이터 수신
        int bytesReceived = recv(clientSocket, buffer, sizeof(buffer), 0);
        if (bytesReceived < 0) {
            perror("Receive failed");
            break;
        }
        buffer[bytesReceived] = '\0'; // 문자열 끝 표시
        printf("받은 메시지: %s\n", buffer);
    }

    close(clientSocket);
    return 0;
}
```
- **`while (1)`**: 무한 루프를 사용해 계속해서 데이터를 수신합니다. **"끊임없는 손님 맞이"**처럼 서버는 계속 대기 상태를 유지합니다.

#### 조건문으로 다양한 시나리오 처리하기
조건문은 특정 상황에 따라 다른 동작을 수행하는 데 사용됩니다.

**예제 3: 서버 측 데이터 처리**
```c
#include <stdio.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>

int main() {
    int serverSocket = socket(AF_INET, SOCK_STREAM, 0);
    if (serverSocket < 0) {
        perror("Socket creation failed");
        return -1;
    }

    struct sockaddr_in serverAddr;
    serverAddr.sin_family = AF_INET;
    serverAddr.sin_addr.s_addr = INADDR_ANY;
    serverAddr.sin_port = htons(8080);

    bind(serverSocket, (struct sockaddr *)&serverAddr, sizeof(serverAddr));
    listen(serverSocket, 5); // 최대 5명의 클라이언트 대기

    while (1) { // 무한 루프: 클라이언트 연결 대기
        struct sockaddr_in clientAddr;
        socklen_t addrLen = sizeof(clientAddr);
        int clientSocket = accept(serverSocket, (struct sockaddr *)&clientAddr, &addrLen);
        if (clientSocket < 0) {
            perror("Accept failed");
            continue;
        }

        char buffer[1024];
        int bytesReceived = recv(clientSocket, buffer, sizeof(buffer), 0);
        if (bytesReceived < 0) {
            perror("Receive failed");
            continue;
        }

        // 메시지 처리 조건문
        if (strstr(buffer, "QUIT") != NULL) {
            printf("클라이언트가 종료 요청: %s\n", buffer);
            send(clientSocket, "서비스 종료", strlen("서비스 종료"), 0);
            close(clientSocket);
            continue;
        } else {
            printf("클라이언트 메시지: %s\n", buffer);
            send(clientSocket, "응답 메시지입니다", strlen("응답 메시지입니다"), 0);
        }
    }

    close(serverSocket);
    return 0;
}
```
- **`if (strstr(buffer, "QUIT") != NULL)`**: 클라이언트가 "QUIT" 메시지를 보내면 서비스를 종료합니다. **"고객의 요청에 따라 유연하게 대응하는 커피숍 주인"**처럼 다양한 상황에 따라 적절히 반응합니다.

### 💡 초보자 폭풍 질문!
- **Q**: 소켓 프로그래밍에서 `bind()` 함수는 정확히 어떤 역할을 하나요?
  - **A**: `bind()` 함수는 소켓에 특정 주소를 할당하여 네트워크 상에서의 위치를 정의합니다. 이는 서버가 특정 포트와 IP 주소를 통해 연결 요청을 받아들일 수 있게 만듭니다. 마치 커피숍 주인이 특정 테이블에 앉아서 손님을 기다리는 것과 같아요!

- **Q**: 클라이언트와 서버 사이의 통신은 어떻게 이루어지나요?
  - **A**: 클라이언트는 서버에 연결 요청(`connect()`)을 보내고, 서버는 이를 수락(`accept()`)합니다. 이후에는 양방향 통신이 가능해져 데이터를 주고받을 수 있습니다. **"전화 통화"**처럼 한쪽에서 말하고 다른 쪽이 응답하는 구조라고 생각하면 됩니다.

### 🚨 실무주의보
- **주의**: 소켓 프로그래밍에서는 에러 핸들링이 매우 중요합니다. 예를 들어, 네트워크 연결이 실패하거나 데이터 전송이 제대로 이루어지지 않을 때 적절한 에러 메시지를 출력하고 프로그램을 안정적으로 종료해야 합니다. **"비상 상황 대비 훈련"**처럼 항상 대비책을 마련해두세요!

### 마무리
이제 여러분은 네트워크의 마법사가 되어 컴퓨터들이 서로 소통할 수 있게 만들 수 있습니다. 소켓 프로그래밍은 복잡해 보일 수 있지만, 기본 개념을 이해하고 꾸준히 연습한다면 결코 어렵지 않을 거예요. **"네트워크의 문지기"**가 되어 다양한 시나리오를 해결해 나가는 재미를 느껴보세요! 🌟

계속 연습하고 질문해보세요. 함께 성장해 나가는 여정에서 항상 응원하겠습니다! 🚀

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
