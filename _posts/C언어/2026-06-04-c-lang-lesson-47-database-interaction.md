---
layout: single
title: "데이터베이스 연결 및 SQL 문 처리 (SQLite)"
date: 2026-06-04 16:03:16
categories: [C언어]
---

## 🔥47강: 데이터베이스 연결 및 SQL 문 처리 (SQLite) - 코드로 세상 바꾸는 마법사가 되자!🔥


**안녕하세요, C언어 일타의 신비로운 선생님이에요! 🧙‍♂️**  오늘은 데이터베이스를 이용해서 우리 프로그램을 진짜 강력한 힘을 가진 영웅으로 만들어 보겠습니다. 🤩 정말 신나죠? 🚀

데이터베이스는 마치 **문제 해결의 마법 지팡이** 같은 거랍니다. 어떤 문제든 데이터를 잘 저장하고 관리하면, 프로그램이 훨씬 쉽게 일을 처리할 수 있도록 도와줍니다!

오늘부터 우리는 **SQLite**라는 데이터베이스 시스템을 배우겠습니다. SQLite는 컴퓨터에 스스로 설치되어 있어서 사용하기 간편한 데이터베이스입니다. 마치 아주 좋은 친구처럼 항상 우리 곁에서 도움을 주고 있죠! 🥰

### 💡 초보자 폭풍 질문! 👾
"데이터베이스? 어떻게 작동하는 걸까요?" "SQL이 무엇인가요?" 🤔  걱정 마세요! 선생님께서 친절하게 설명해 드릴게요. 😉

** 데이터베이스는 정보를 저장하고 관리하는 프로그램입니다.**  그래도, 그냥 단순히 정보를 놓아두는 것이 아니라, **계층적으로 정리된 방식으로 데이터를 저장하고 빠르게 찾거나 수정할 수 있도록 해주는 마법 같은 기능**을 가지고 있습니다! ✨

**SQL (Structured Query Language)**은 데이터베이스와 대화하는 언어입니다. 우리가 "이 정보를 찾아줘!" 혹은 "새로운 정보를 추가해줘!" 라고 말하는 것처럼, **SQL 코드를 사용해서 데이터베이스에 명령을 내릴 수 있습니다.** 🚀

###  🔌 C언어로 SQLite 연결하기 - 마법 지팡이 준비!

SQLite3 라이브러리를 사용하여 C 언어에서 SQLite 데이터베이스를 연결합니다. 

```c
#include <stdio.h>
#include "sqlite3.h" // SQLite3 헤더 파일을 포함

int main() {
  // 1. 데이터베이스 연결하기 - 마법 지팡이 만들기!
  sqlite3 *db;
  char *zErrMsg = 0;
  int rc = sqlite3_open("mydatabase.db", &db); // "mydatabase.db" 파일을 연동
  if (rc) {
    fprintf(stderr, "Can't open database: %s\n", sqlite3_errmsg(db));
    return(1);
  } else {
    printf("Database opened successfully!\n"); 
  }

  // ... SQLite 작업 후 데이터베이스 연결 해제!

  sqlite3_close(db); // 마법 지팡이 정리!

  return 0;
} 
```

** 코드 설명:**

* `#include <stdio.h>`: C 표준 입출력 라이브러리를 포함하여 화면에 출력할 수 있도록 합니다.
* `#include "sqlite3.h"`: SQLite3 헤더 파일을 포함하여 SQLite 함수를 사용할 수 있게 합니다.

*  `sqlite3_open("mydatabase.db", &db)`:  "mydatabase.db"라는 이름의 데이터베이스 파일을 열고, 연결 객체 (`db`)에 저장합니다. 만약 해당 파일이 존재하지 않으면 새로운 데이터베이스 파일이 생성됩니다!
* `sqlite3_errmsg(db)` : 오류 메시지를 가져오는 함수입니다.


###  💪 SQL 문 처리 - 데이터 마법사에게 명령 내리기!

SQLite와 C언어를 연결하면, **SQL 문을 통해 데이터베이스에 직접 명령을 내릴 수 있게 됩니다.** 🧙‍♂️✨

* **`CREATE TABLE`**: 테이블 생성 
   ```c
   const char *sql = "CREATE TABLE IF NOT EXISTS employees (id INTEGER PRIMARY KEY, name TEXT, salary REAL);"; // 'employees' 테이블 생성
   rc = sqlite3_exec(db, sql, 0, 0, &zErrMsg); // SQL 문 실행!
   ```

* **`INSERT INTO`**: 데이터 추가하기!
   ```c
   const char *sql = "INSERT INTO employees (name, salary) VALUES ('John Doe', 50000);";
   rc = sqlite3_exec(db, sql, 0, 0, &zErrMsg); // John Doe를 테이블에 추가!
   ```

* **`SELECT`**: 데이터 검색하기!

   ```c
   const char *sql = "SELECT * FROM employees;"; 
   sqlite3_stmt *stmt;
   rc = sqlite3_prepare_v2(db, sql, -1, &stmt, NULL); // SQL 문 준비
   while (sqlite3_step(stmt) == SQLITE_ROW) { // 데이터를 한 행씩 읽기!
     printf("ID: %d, Name: %s, Salary: %.2f\n", 
            sqlite3_column_int(stmt, 0), 
            sqlite3_column_text(stmt, 1), 
            sqlite3_column_double(stmt, 2));
   }

   sqlite3_finalize(stmt); // 준비된 SQL 문 해제
   ```


** 코드 설명:**

* `sqlite3_exec`: 실행 가능한 SQL 문을 데이터베이스에 보냅니다.
* `sqlite3_prepare_v2`:  SQL 문을 분석하여 컴파일하고, `sqlite3_stmt` 포인터를 반환합니다.
* `sqlite3_step`:  SQL 문 결과 행 단위로 처리하며, 각 행에서 값을 가져오기 위한 함수입니다.


### 🚀 실무주의보!

실제 프로젝트에서는 데이터베이스 연결과 SQL 문 처리 과정은 더욱 복잡하고 다양한 방법으로 구현될 수 있습니다. 🚨  이번 강의는 데이터베이스와 C언어의 기본적인 연동 방식을 보여주고, 이를 바탕으로 실제 프로젝트에서 사용할 수 있는 다양한 기술들을 심화적으로 학습할 수 있도록 도울 것입니다!

**자료 찾기:**  SQLite 공식 문서는 매우 자세하고 유용하니 꼭 참고하세요. https://www.sqlite.org/



### 🎉  다음 시간에는 더욱 복잡하고 성능 좋은 데이터베이스 연동 기술들을 배우겠습니다. 기대 해 주세요! 🤩

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
