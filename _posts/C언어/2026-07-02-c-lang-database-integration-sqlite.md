---
layout: single
title: "C언어 응용: 데이터베이스 연동 기초 (예: SQLite)"
date: 2026-07-02 21:10:00
categories: [C언어]
---

### 19강: C언어 응용: 데이터베이스 연동 기초 (SQLite 예제)

안녕하세요, 코딩 탐험가 여러분! 오늘은 C언어를 한 단계 더 업그레이드시켜주는 특별한 여정에 접어들었습니다. **데이터베이스 연동**이라는 주제로, 우리의 코드를 실제 세상과 연결시켜주는 마법 같은 기술을 배워볼 거예요. 특히 **SQLite**를 활용해서 초보자도 쉽게 이해할 수 있도록 설명드릴게요. 이거 모르면 진짜 큰일 납니다! 😉

#### 🚀 왜 데이터베이스 연동이 중요할까요?

상상해보세요. 여러분이 멋진 앱을 개발하고 있는데, 그 앱이 사용자 정보나 게임 데이터를 저장해야 한다고 가정해봅시다. 만약 모든 데이터를 단순히 파일에 넣어두면 어떻게 될까요? 복잡해지고 유지보수가 어려워지죠! 데이터베이스는 이런 문제를 깔끔하게 해결해줍니다. 마치 우리 앱의 개인 비서처럼 데이터를 정리하고, 검색하고, 수정하는 역할을 맡아요.

#### 🧩 SQLite란 무엇인가요?

**SQLite**는 가볍고 휴대성이 뛰어난 관계형 데이터베이스 관리 시스템입니다. 마치 주머니 속에 넣고 다니는 작은 클라우드 같죠! C언어와 잘 어울리면서 복잡한 설정 없이 바로 쓸 수 있는 장점이 있어요.

##### 🛠️ SQLite 연동을 위한 기본 단계

1. **라이브러리 포함**: 먼저 SQLite 라이브러리를 프로젝트에 추가해야 합니다. 일반적으로 `#include <sqlite3.h>`로 시작합니다.
2. **데이터베이스 연결**: 데이터베이스 파일을 열고 연결합니다.
3. **SQL 쿼리 실행**: 데이터를 삽입, 조회, 수정, 삭제하는 SQL 명령어를 실행합니다.
4. **자원 해제**: 작업이 끝나면 연결을 닫고 자원을 적절히 해제합니다.

### 💡 초보자 폭풍 질문! 💡

**Q**: SQLite 연결 실패 시 어떻게 해야 하나요?
**A**: 연결 실패 시 오류 코드를 확인하세요! `sqlite3*db; sqlite3_open("my_database.db", &db);`에서 `sqlite3_errmsg(db)`를 통해 오류 메시지를 확인할 수 있습니다. 이 메시지를 통해 문제를 해결할 수 있어요.

---

### # 코드 탐험: 실전 예제 1 - 데이터베이스 생성 및 연결

```c
#include <stdio.h>
#include <sqlite3.h>

int main() {
    // 데이터베이스 파일 이름 정의
    const char* dbFileName = "my_database.db";
    sqlite3* db;
    int rc;

    // 데이터베이스 연결 시도
    rc = sqlite3_open(dbFileName, &db);

    if (rc != SQLITE_OK) {
        fprintf(stderr, "Can't open database: %s\n", sqlite3_errmsg(db));
        sqlite3_close(db); // 오류 발생 시 자원 해제
        return 1;
    }

    printf("Opened database successfully!\n");

    // 연결 성공 시 데이터베이스 객체 'db'를 사용하여 쿼리 실행 가능
    sqlite3_close(db); // 작업 완료 후 연결 종료
    return 0;
}
```
**해설**:
- `#include <sqlite3.h>`: SQLite 라이브러리 포함.
- `sqlite3_open`: 데이터베이스 파일 `"my_database.db"`를 열어 `db` 변수에 연결.
- 오류 처리: `sqlite3_errmsg`로 오류 메시지 확인 후 자원 해제.

### # 코드 탐험: 실전 예제 2 - 테이블 생성

```c
#include <stdio.h>
#include <sqlite3.h>

int main() {
    sqlite3* db;
    int rc;
    const char* sql_create_table = "CREATE TABLE IF NOT EXISTS users ("
                                  "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                                  "name TEXT NOT NULL, "
                                  "email TEXT NOT NULL);";

    // 데이터베이스 연결
    rc = sqlite3_open("my_database.db", &db);
    if (rc != SQLITE_OK) {
        fprintf(stderr, "Can't open database: %s\n", sqlite3_errmsg(db));
        sqlite3_close(db);
        return 1;
    }

    // SQL 쿼리 실행: 테이블 생성
    rc = sqlite3_exec(db, sql_create_table, NULL, NULL, NULL);
    if (rc != SQLITE_OK) {
        fprintf(stderr, "SQL error: %s\n", sqlite3_errmsg(db));
    } else {
        printf("Table created successfully!\n");
    }

    sqlite3_close(db); // 연결 종료
    return 0;
}
```
**해설**:
- `CREATE TABLE IF NOT EXISTS`: 이미 존재하는 테이블은 무시.
- `id INTEGER PRIMARY KEY AUTOINCREMENT`: 자동 증가 ID 생성.
- `sqlite3_exec`: 쿼리 실행 함수로, 테이블 생성 성공 여부 확인.

### # 코드 탐험: 실전 예제 3 - 데이터 삽입 및 조회

#### 데이터 삽입 예시

```c
#include <stdio.h>
#include <sqlite3.h>

void insertUser(sqlite3* db) {
    const char* sql_insert = "INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com');";
    char* errMsg = NULL;
    int rc = sqlite3_exec(db, sql_insert, NULL, NULL, &errMsg);
    if (rc != SQLITE_OK) {
        fprintf(stderr, "INSERT ERROR: %s\n", errMsg);
        sqlite3_free(errMsg); // 오류 메시지 해제
    } else {
        printf("New record created successfully\n");
    }
}

int main() {
    sqlite3* db;
    int rc;

    // 데이터베이스 연결
    rc = sqlite3_open("my_database.db", &db);
    if (rc != SQLITE_OK) {
        fprintf(stderr, "Can't open database: %s\n", sqlite3_errmsg(db));
        sqlite3_close(db);
        return 1;
    }

    insertUser(db); // 함수 호출로 데이터 삽입

    sqlite3_close(db); // 연결 종료
    return 0;
}
```
**해설**:
- `INSERT INTO`: 데이터 삽입 쿼리.
- `sqlite3_exec`: 쿼리 실행 함수.
- 오류 처리: `sqlite3_free`로 오류 메시지 해제.

#### 데이터 조회 예시

```c
#include <stdio.h>
#include <sqlite3.h>

void queryUsers(sqlite3* db) {
    sqlite3_stmt* stmt;
    const char* sql_query = "SELECT * FROM users;";

    // 준비된 문장 실행
    rc = sqlite3_prepare_v2(db, sql_query, -1, &stmt, NULL);
    if (rc != SQLITE_OK) {
        fprintf(stderr, "Failed to prepare query: %s\n", sqlite3_errmsg(db));
        return;
    }

    while ((rc = sqlite3_step(stmt)) == SQLITE_ROW) {
        int id = sqlite3_column_int(stmt, 0); // 컬럼 접근
        const char* name = (const char*) sqlite3_column_text(stmt, 1);
        const char* email = (const char*) sqlite3_column_text(stmt, 2);
        printf("ID: %d, Name: %s, Email: %s\n", id, name, email);
    }

    sqlite3_finalize(stmt); // 준비된 문장 종료
}

int main() {
    sqlite3* db;
    int rc;

    // 데이터베이스 연결
    rc = sqlite3_open("my_database.db", &db);
    if (rc != SQLITE_OK) {
        fprintf(stderr, "Can't open database: %s\n", sqlite3_errmsg(db));
        sqlite3_close(db);
        return 1;
    }

    queryUsers(db); // 데이터 조회 함수 호출

    sqlite3_close(db); // 연결 종료
    return 0;
}
```
**해설**:
- `SELECT * FROM users;`: 모든 사용자 정보 조회 쿼리.
- `sqlite3_prepare_v2`: 쿼리 준비 함수.
- `sqlite3_step`: 각 행을 순회하며 데이터 추출.
- `sqlite3_finalize`: 준비된 문장 종료 및 자원 해제.

### 🚨 실무주의보 🚨

**주의사항**:
- **오류 처리**: SQLite에서 발생하는 모든 오류를 체크하고 적절히 처리하는 것이 중요합니다. 오류 메시지를 확인하고 적절한 조치를 취해야 합니다.
- **자원 관리**: 데이터베이스 연결과 준비된 문장은 반드시 종료해야 합니다 (`sqlite3_close`, `sqlite3_finalize`). 이는 메모리 누수를 방지하고 안정적인 프로그램 실행을 보장합니다.

---

오늘 배운 내용으로 여러분의 앱이 데이터와 더욱 원활하게 소통할 수 있게 되었을 겁니다! 실전에서 적용해보면서 자신감을 키워보세요. 혹시 궁금한 점이 있으면 언제든지 댓글로 물어봐주세요! 🚀 함께 성장해 나가요!

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
