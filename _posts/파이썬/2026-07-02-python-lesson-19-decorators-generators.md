---
layout: single
title: "데코레이터와 제너레이터 이해하기"
date: 2026-07-02 18:18:26
categories: [파이썬]
---

### 19강: 데코레이터와 제너레이터 이해하기 - 코딩의 마법사가 되어보자!

안녕하세요, 코딩의 마법사 여러분! 오늘은 마법의 망토를 펼쳐보자구요. 바로 **데코레이터**와 **제너레이터**입니다. 이 두 친구는 파이썬 코드 세계에서 엄청나게 강력한 마법을 부리는데요, 처음엔 어려울 수 있지만 익숙해지면 코딩이 훨씬 더 재미있어질 거예요! 🌟

#### **데코레이터: 코드의 옷장 마스터**

데코레이터는 코드에 장식을 더하는 마법 같은 도구랍니다. 마치 옷을 입듯이 함수에 특별한 능력을 부여해주는 거죠! 진짜 신기하죠?

##### 개념 이해하기

**데코레이터란 무엇인가요?**
- **정의**: 함수를 감싸는 다른 함수로, 기존 함수의 동작을 확장하거나 변경하는 역할을 합니다. 쉽게 말해, 기존 함수에 추가적인 기능을 입혀주는 거죠.
- **목적**: 코드의 재사용성 향상과 유지보수를 쉽게 만듭니다. 예를 들어, 로깅 기능을 추가하거나 입력 검증을 자동화할 수 있어요.

##### 코드로 알아보기

###### 예제 1: 간단한 로깅 데코레이터
```python
def logger_decorator(func):
    def wrapper(*args, **kwargs):
        # 함수 실행 전 로깅
        print(f"Calling function '{func.__name__}' with arguments {args} {kwargs}")
        result = func(*args, **kwargs)  # 실제 함수 호출
        # 함수 실행 후 로깅
        print(f"Function '{func.__name__}' returned {result}")
        return result
    return wrapper

@logger_decorator
def add(a, b):
    return a + b

# 함수 호출 예시
print(add(3, 5))
```
**코드 설명**:
1. **logger_decorator 함수**: 데코레이터 역할을 하는 함수입니다. 입력받은 함수 `func`를 감싸는 `wrapper` 함수를 정의합니다.
2. **wrapper 함수**: 실제 함수 호출 전에 실행 전과 후의 로깅 메시지를 출력합니다.
3. **add 함수**: 데코레이터가 적용된 함수입니다. 호출 시 로깅 메시지가 함께 출력됩니다.
   - **출력 결과**:
     ```
     Calling function 'add' with arguments (3, 5) {}
     Function 'add' returned 8
     8
     ```

###### 예제 2: 반복 횟수 제한 데코레이터
```python
def limit_calls(max_calls):
    def decorator_with_limit(func):
        call_count = 0
        def wrapper(*args, **kwargs):
            nonlocal call_count
            if call_count < max_calls:
                call_count += 1
                return func(*args, **kwargs)
            else:
                print("Function call limit reached!")
                return None
        return wrapper
    return decorator_with_limit

@limit_calls(3)
def shout(message):
    print(f"Shouting: {message}")

# 함수 호출 예시
shout("HELLO")
shout("WORLD")
shout("PYTHON")
shout("AGAIN")  # 3번 이상 호출 시 제한 메시지 출력
```
**코드 설명**:
1. **limit_calls 데코레이터**: 최대 호출 횟수를 제한하는 데코레이터입니다.
2. **wrapper 함수**: 호출 횟수를 추적하고 제한을 초과하면 메시지를 출력합니다.
3. **shout 함수**: 데코레이터가 적용되어 호출 횟수가 제한됩니다.
   - **출력 결과**:
     ```
     Shouting: HELLO
     Shouting: WORLD
     Shouting: PYTHON
     Function call limit reached!
     ```

#### **제너레이터: 무한한 데이터의 바다**

제너레이터는 마치 무한한 데이터 바다에서 필요한 만큼만 끌어오는 마법의 배입니다. 코드에서 메모리 효율성과 무한 시퀀스 생성에 정말 유용해요! 이건 정말 모르면 큰일 납니다! 😱

##### 개념 이해하기

**제너레이터란 무엇인가요?**
- **정의**: 함수가 한 번 호출되면 값을 반환하지만, 완전한 실행을 멈추고 다음 호출 시 이어서 실행되는 특수한 함수입니다.
- **목적**: 메모리 사용을 최적화하고 큰 데이터 세트를 효율적으로 처리할 수 있게 합니다. 예를 들어, 무한한 숫자 시퀀스를 생성하거나 큰 파일을 줄 단위로 읽을 때 유용합니다.

##### 코드로 알아보기

###### 예제 1: 간단한 숫자 제너레이터
```python
def infinite_counter():
    num = 0
    while True:
        yield num  # 현재 값을 반환하고 상태 유지
        num += 1

# 제너레이터 사용 예시
counter = infinite_counter()
print(next(counter))  # 출력: 0
print(next(counter))  # 출력: 1
print(next(counter))  # 출력: 2
# 무한히 계속될 수 있음
```
**코드 설명**:
1. **infinite_counter 함수**: 제너레이터 함수로, 무한히 숫자를 생성합니다.
2. **yield 키워드**: 현재 값을 반환하고 함수 실행을 일시 중지합니다.
3. **next(counter)**: 제너레이터 객체에서 다음 값을 가져옵니다.
   - **출력 결과**:
     ```
     0
     1
     2
     ```

###### 예제 2: 파일 줄 제너레이터
```python
def read_file_lines(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            yield line.strip()  # 각 줄을 반환하며 파일 객체 상태 유지

# 제너레이터 사용 예시
file_path = 'example.txt'
for line in read_file_lines(file_path):
    print(line)  # 파일 내용 출력
    if line == "":  # 빈 줄이면 종료
        break
```
**코드 설명**:
1. **read_file_lines 함수**: 파일의 각 줄을 제너레이터로 생성합니다.
2. **yield 키워드**: 각 줄을 읽고 반환하면서 파일 객체의 상태를 유지합니다.
3. **for 루프**: 제너레이터를 통해 파일 내용을 한 줄씩 읽어 처리합니다.
   - **예시 출력** (`example.txt` 내용에 따라 다름):
     ```
     첫 번째 줄 내용
     두 번째 줄 내용
     ...
     ```

#### 💡 초보자 폭풍 질문! 💡

**Q**: 데코레이터와 제너레이터 모두 함수를 사용하는 거 같은데, 차이점이 뭔가요?
**A**: 맞아요! 둘 다 함수를 사용하지만 목적이 다르죠:
- **데코레이터**: 기존 함수에 추가적인 기능을 부여해 확장합니다. 예를 들어 로깅이나 권한 검사를 쉽게 추가할 수 있어요.
- **제너레이터**: 반복 가능한 객체를 생성하여 메모리 효율성을 높입니다. 특히 큰 데이터 세트를 다룰 때 유용해요.

#### 🚨 실무주의보 🚨

데코레이터와 제너레이터를 잘 활용하면 코드의 가독성과 효율성이 크게 향상됩니다. 하지만 과도한 사용은 유지보수를 어렵게 만들 수 있으니 적절히 적용하는 것이 중요합니다. 특히 제너레이터는 무한 시퀀스를 다룰 때 주의가 필요하며, 자원 관리에 신경 써야 합니다.

이제 여러분도 데코레이터와 제너레이터의 마법을 익혀보세요! 코딩의 세계가 훨씬 더 풍요롭고 재미있어질 거예요. 도전해보세요, 마법사 여러분! 🧙‍♂️💪

---

이렇게 상세하고 친근한 스타일로 데코레이터와 제너레이터에 대해 설명드렸습니다. 궁금한 점이나 추가로 알고 싶은 내용이 있으면 언제든지 물어보세요! 👍

<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
