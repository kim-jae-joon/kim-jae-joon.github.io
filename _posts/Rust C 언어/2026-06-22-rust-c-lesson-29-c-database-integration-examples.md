---
layout: single
title: "C 언어 데이터베이스 연동 예제"
date: 2026-06-22 19:10:58
categories: [Rust C 언어]
---

### 29강: C 언어로 데이터베이스와 춤추기 - 초보자도 빛나는 데이터베이스 연동 마스터하기

안녕하세요, 여러분의 친절한 코딩 멘토 **💻 코딩의 마법사**입니다! 오늘은 C 언어로 데이터베이스와 완벽하게 연동하는 방법을 배워볼게요. 이 강의를 통해 여러분은 복잡해 보이는 데이터베이스 시스템도 편안하게 다룰 수 있게 될 거예요. 준비되셨나요? 그럼 시작해볼까요!

#### 🌟 데이터베이스란 무엇인가요?
데이터베이스는 **정보의 중앙 저장소**라고 생각하면 됩니다. 마치 거대한 책장처럼, 필요한 정보를 효율적으로 정리하고 빠르게 검색할 수 있도록 설계된 시스템이죠. 우리가 매일 사용하는 스마트폰 앱이나 온라인 쇼핑몰도 결국 이 책장 뒤에서 정보를 찾아옵니다.

#### 🛠️ 준비 단계: 필요한 도구와 라이브러리
데이터베이스와 C 언어를 연결하려면 몇 가지 중요한 도구들이 필요해요:
- **SQL (Structured Query Language)**: 데이터를 읽고 쓰는 데 사용되는 표준 언어입니다.
- **C 라이브러리 (예: MySQL Connector/C, SQLite3)**: C 프로그램에서 데이터베이스와 상호작용할 수 있게 해주는 인터페이스입니다.

오늘은 **SQLite**를 예시로 사용해볼게요. SQLite는 가볍고 설치가 쉬운 오픈 소스 데이터베이스 시스템으로, 초보자에게 이상적입니다.

### 1. SQLite 데이터베이스 설정하기
먼저 SQLite를 사용하기 위한 기본 설정을 해볼게요.

#### 예제 코드 1: SQLite 데이터베이스 생성 및 연결
```c
#include <stdio.h>
#include <sqlite3.h>  // SQLite 라이브러리 포함

int main() {
    sqlite3 *db;  // 데이터베이스 핸들러 선언
    char *err_msg = 0;  // 오류 메시지 저장 변수
    int rc;  // 함수 반환 코드

    // 데이터베이스 연결
    rc = sqlite3_open("mydatabase.db", &db);  // "mydatabase.db" 파일 생성 또는 열기
    if (rc != SQLITE_OK) {
        fprintf(stderr, "Can't open database: %s\n", sqlite3_errmsg(db));
        sqlite3_close(db);
        return 1;
    }
    printf("Opened database successfully!\n");  // 성공 메시지 출력

    // 데이터 삽입 예시
    const char *sql_insert = "CREATE TABLE IF NOT EXISTS Users ("
                            "ID INTEGER PRIMARY KEY AUTOINCREMENT, "
                            "Name TEXT NOT NULL, "
                            "Age INTEGER NOT NULL);";
    rc = sqlite3_exec(db, sql_insert, NULL, NULL, &err_msg);
    if (rc != SQLITE_OK) {
        fprintf(stderr, "SQL error: %s\n", err_msg);
        sqlite3_free(err_msg);
    } else {
        printf("Table created successfully!\n");
    }

    sqlite3_close(db);  // 연결 종료
    return 0;
}
```

**코드 해설:**
- **`sqlite3 *db;`**: 데이터베이스 연결을 위한 핸들러 선언.
- **`sqlite3_open("mydatabase.db", &db);`**: "mydatabase.db" 파일을 생성하거나 열어 데이터베이스 연결을 설정합니다.
- **`CREATE TABLE IF NOT EXISTS Users`**: 이미 테이블이 존재하지 않으면 새로운 `Users` 테이블을 생성합니다. 여기서 `ID`는 자동 증가형 기본 키입니다.
- **`sqlite3_close(db);`**: 연결을 종료하고 자원을 해제합니다.

#### 🧩 개념 설명: 데이터베이스 테이블 생성
테이블은 데이터베이스의 핵심 구조입니다. 위 예제에서 `Users` 테이블은 세 가지 필드를 가지고 있습니다:
- `ID`: 자동 증가하는 기본 키 (unique identifier)
- `Name`: 사용자 이름 (Text 타입)
- `Age`: 나이 (Integer 타입)

#### 💡 초보자 폭풍 질문!
**Q:** 만약 테이블이 이미 존재하면 어떻게 될까요?
**A:** 위 코드의 `IF NOT EXISTS` 부분 덕분에 이미 존재하는 테이블에 대해선 아무 동작도 하지 않습니다. 덕분에 중복 생성 오류를 피할 수 있어요!

### 2. 데이터 삽입 및 조회하기
데이터베이스에 정보를 넣고 꺼내는 것도 중요해요. 다양한 방법으로 이를 수행할 수 있습니다.

#### 예제 코드 2: 데이터 삽입
```c
#include <stdio.h>
#include <sqlite3.h>

int main() {
    sqlite3 *db;
    char *err_msg = 0;
    int rc;

    // 데이터베이스 연결
    rc = sqlite3_open("mydatabase.db", &db);
    if (rc != SQLITE_OK) {
        fprintf(stderr, "Can't open database: %s\n", sqlite3_errmsg(db));
        sqlite3_close(db);
        return 1;
    }

    // 데이터 삽입 쿼리
    const char *sql_insert = "INSERT INTO Users (Name, Age) VALUES ('Alice', 25);";
    rc = sqlite3_exec(db, sql_insert, NULL, NULL, &err_msg);
    if (rc != SQLITE_OK) {
        fprintf(stderr, "SQL error: %s\n", err_msg);
        sqlite3_free(err_msg);
    } else {
        printf("Record inserted successfully!\n");
    }

    sqlite3_close(db);
    return 0;
}
```

**코드 해설:**
- **`INSERT INTO Users (Name, Age) VALUES ('Alice', 25);`**: `Users` 테이블에 새로운 레코드를 추가합니다. 여기서 `'Alice'`는 이름, `25`는 나이입니다.

#### 예제 코드 3: 데이터 조회하기
데이터를 조회하는 방법도 비슷합니다.

```c
#include <stdio.h>
#include <sqlite3.h>

void fetch_data(sqlite3 *db) {
    sqlite3_stmt *stmt;
    const char *sql = "SELECT * FROM Users;";
    int rc = sqlite3_prepare_v2(db, sql, -1, &stmt, NULL);

    if (rc != SQLITE_OK) {
        fprintf(stderr, "Failed to prepare query: %s\n", sqlite3_errmsg(db));
        return;
    }

    while ((rc = sqlite3_step(stmt)) == SQLITE_ROW) {
        int id = sqlite3_column_int(stmt, 0);  // ID 컬럼 값 가져오기
        const char *name = (const char *)sqlite3_column_text(stmt, 1);  // Name 컬럼 값 가져오기
        int age = sqlite3_column_int(stmt, 2);  // Age 컬럼 값 가져오기

        printf("ID: %d, Name: %s, Age: %d\n", id, name, age);
    }

    sqlite3_finalize(stmt);  // 준비된 문장 종료
}

int main() {
    sqlite3 *db;
    int rc;

    rc = sqlite3_open("mydatabase.db", &db);
    if (rc != SQLITE_OK) {
        fprintf(stderr, "Can't open database: %s\n", sqlite3_errmsg(db));
        sqlite3_close(db);
        return 1;
    }

    fetch_data(db);  // 데이터 조회 함수 호출

    sqlite3_close(db);
    return 0;
}
```

**코드 해설:**
- **`sqlite3_prepare_v2`**: 쿼리 실행 준비
- **`sqlite3_step`**: 쿼리 결과를 한 행씩 가져옵니다.
- **`sqlite3_column_int` 및 `sqlite3_column_text`**: 각 컬럼 값을 추출합니다.

### 🚨 실무주의보
**실제 프로젝트에서는 데이터베이스 연결을 안전하게 관리해야 합니다:**
- **자원 해제**: 모든 연결 및 리소스를 적절히 해제하는 습관을 들이세요.
- **오류 처리**: 데이터베이스 연결 및 쿼리 실행 시 발생할 수 있는 오류를 철저히 확인하고 처리하세요.

### 🔗 추가 학습 자료
- **SQLite 공식 문서**: [SQLite Documentation](https://www.sqlite.org/docs.html)
- **C와 SQLite 통합 튜토리얼**: [C Programming SQLite Integration Tutorial](https://www.sqlitetutorial.net/c-sqlite/)

#### 마무리 말씀
오늘 배운 내용으로 데이터베이스와의 춤을 시작하셨어요! 처음엔 어려울 수 있지만, 꾸준히 연습하면 데이터베이스 관리가 훨씬 쉬워질 거예요. 혹시 궁금한 점이 있으면 언제든지 **💬 질문 댓글** 남겨주세요! 여러분의 코딩 여정이 빛나길 바랍니다. **🌟 코딩의 마법사와 함께 성장하세요!**

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
