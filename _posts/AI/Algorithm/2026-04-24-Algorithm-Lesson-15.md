---
layout: single
title: "15강: 자동완성의 마법사, 트라이(Trie) 알고리즘"
date: 2026-04-24 01:08:55
categories: [AI, Algorithm]
---
> **🤖 AI 사용 안내:** 이 포스팅은 `gemma4:31b` 언어 모델을 활용하여 작성되었습니다.

# 15강: 자동완성의 마법사, 트라이(Trie) 알고리즘

안녕하세요! 여러분의 코딩 구원자, 재준봇입니다! 

지난 14강에서는 슬라이딩 윈도우 알고리즘을 다뤘었죠? 데이터를 한 칸씩 밀면서 효율적으로 훑는 그 느낌, 다들 기억하시나요? 어떤 분들은 "재준봇님, 윈도우가 너무 매끄럽게 밀려서 제가 정신을 못 차렸어요!"라고 하시더라고요. 하지만 걱정 마세요. 오늘 배울 내용은 그보다 훨씬 더 직관적이고, 우리가 매일 쓰는 스마트폰에서도 돌아가고 있는 아주 힙한 녀석이니까요.

자, 이제 15강의 주인공을 소개합니다. 바로 트라이(Trie) 알고리즘입니다!

## 이게 대체 왜 필요한가요?

여러분, 구글 검색창에 "파이"까지만 쳐보세요. 그러면 아래에 "파이썬", "파이차트", "파이낸셜 타임즈" 같은 추천 검색어가 촤르륵 뜨죠? 이게 바로 트라이 알고리즘의 정수입니다.

보통 우리가 문자열을 찾을 때 어떻게 하나요? 그냥 리스트에 다 넣어두고 하나하나 비교하죠. 하지만 데이터가 100만 개라면? "파이"로 시작하는 단어를 찾기 위해 100만 번을 다 검사해야 합니다. 이건 정말 비효율의 끝판왕이죠. 

트라이는 한마디로 문자열을 위한 전용 지도라고 생각하시면 됩니다. 단어들을 공통된 접두사(Prefix)끼리 묶어서 트리 형태로 저장하는 방식이에요. 덕분에 우리는 단어의 전체 길이가 아니라, 찾으려는 글자 수만큼만 내려가면 답을 찾을 수 있습니다. 진짜 신기하지 않나요?

## 오늘의 생생한 문제: "천재 검색 엔진 만들기"

여러분은 지금 세계 최고의 검색 엔진 회사의 신입 개발자가 되었습니다. 사장님이 갑자기 달려오더니 이렇게 소리를 지르십니다.

> "재준봇! 우리 서비스에 사용자가 입력한 단어가 우리 사전 데이터베이스에 있는지 0.0001초 만에 확인하고 싶어! 그리고 특정 글자로 시작하는 단어가 있는지까지 알아내야 해. 지금 당장 구현해!"

자, 여기서 우리가 해결해야 할 미션은 두 가지입니다.
1. 사전에 등록된 단어가 있는지 확인하기 (정확한 일치)
2. 입력한 글자로 시작하는 단어가 사전에 존재하는지 확인하기 (접두사 확인)

이걸 그냥 리스트로 풀면 사장님께 등짝 스매싱을 맞을 확률이 200%입니다. 하지만 트라이를 사용하면 아주 우아하게 해결할 수 있습니다.

## 트라이의 핵심 설계 원리

트라이를 이해하기 가장 좋은 비유는 바로 계단식 도서관입니다.

- 1층에는 'ㄱ, ㄴ, ㄷ...' 처럼 첫 글자별로 문이 있습니다.
- 'ㄱ' 문을 열고 들어가면, 그 다음 글자인 '가, 각, 간...' 문들이 또 나옵니다.
- 이렇게 계속 들어가다가 마지막 글자 문을 열었을 때 "여기가 단어의 끝입니다!"라는 깃발이 꽂혀 있다면, 그 단어는 사전에 존재하는 것입니다.

### 시간 복잡도 분석
- 일반적인 검색: O(N * M) (N은 단어 개수, M은 단어 평균 길이)
- 트라이 검색: O(M) (단어의 길이만큼만 확인하면 끝!)

데이터가 많아질수록 트라이의 위력은 어마어마해집니다. 이거 모르면 코딩 테스트에서 시간 초과로 광탈할 수 있으니 집중하세요!

> **초보자 폭풍 질문!**
> "재준봇님! 트라이가 이렇게 좋은데 왜 모든 검색을 다 이걸로 안 하나요?"
> 
> **재준봇의 명쾌한 답변:**
> 아주 날카로운 질문입니다! 정답은 바로 메모리 때문입니다. 각 노드마다 다음 글자를 가리키는 포인터를 많이 가지고 있어야 해서 메모리를 상당히 많이 잡아먹습니다. 즉, 시간과 메모리를 맞바꾼 알고리즘이라고 보시면 됩니다.

> **실무주의보**
> 실무에서 트라이를 구현할 때, 단순히 딕셔너리나 배열로 구현하면 메모리 낭비가 심할 수 있습니다. 데이터가 너무 방대하다면 Radix Tree(압축 트라이) 같은 변형 알고리즘을 고려해야 한다는 점, 꼭 기억하세요!

이제 사장님의 등짝 스매싱을 피하기 위한 마법의 코드를 공개하겠습니다.

<details markdown="1"><summary> 해결 방안 및 정답 코드 보기 (클릭)</summary>

### 해결 방안 가이드 (알고리즘 설계)

1. **노드 설계**: 각 노드는 자식 노드들을 저장할 딕셔너리(`children`)와, 해당 노드가 단어의 끝인지 표시하는 불리언 값(`is_end`)을 가집니다.
2. **삽입(Insert) 로직**:
   - 단어의 글자를 하나씩 확인합니다.
   - 현재 노드의 자식 중에 해당 글자가 없다면 새 노드를 생성합니다.
   - 해당 글자의 노드로 이동한 후, 마지막 글자에 도달하면 `is_end`를 True로 설정합니다.
3. **검색(Search) 로직**:
   - 글자를 하나씩 따라 내려갑니다.
   - 중간에 글자가 끊기면 없는 단어입니다.
   - 끝까지 내려왔을 때 `is_end`가 True여야만 완벽한 단어로 인정합니다.
4. **접두사 확인(Starts With) 로직**:
   - 검색 로직과 비슷하지만, 마지막에 `is_end`를 확인할 필요 없이 끝까지 도달하기만 하면 True를 반환합니다.

### 파이썬 정답 코드 및 상세 해설

```python
class TrieNode:
    def __init__(self):
        # 자식 노드들을 저장하는 딕셔너리 (키: 문자, 값: TrieNode)
        self.children = {}
        # 이 노드에서 단어가 끝나는지 표시하는 플래그
        self.is_end = False

class Trie:
    def __init__(self):
        # 트라이의 시작점인 루트 노드 생성
        self.root = TrieNode()

    def insert(self, word):
        # 루트부터 시작해서 단어를 한 글자씩 삽입
        current = self.root
        for char in word:
            # 현재 글자가 자식에 없으면 새로 만들어줌
            if char not in current.children:
                current.children[char] = TrieNode()
            # 다음 글자 노드로 이동
            current = current.children[char]
        # 단어의 마지막 글자 노드에 '끝' 표시를 남김
        current.is_end = True

    def search(self, word):
        # 단어가 정확히 존재하는지 확인
        current = self.root
        for char in word:
            if char not in current.children:
                return False # 중간에 끊기면 없는 단어!
            current = current.children[char]
        # 끝까지 왔더라도 is_end가 True여야 완벽한 단어임
        return current.is_end

    def starts_with(self, prefix):
        # 특정 접두사로 시작하는 단어가 있는지 확인
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False # 접두사조차 없으면 당연히 False
            current = current.children[char]
        # 여기까지만 오면, 뒤에 뭐가 더 있든 일단 이 접두사로 시작하는 단어가 있는 것!
        return True

# --- 실행 테스트 ---
my_trie = Trie()

# 사전 데이터 삽입
words = ["apple", "apply", "append", "banana", "bandana"]
for w in words:
    my_trie.insert(w)

print(f"apple이 있나요?: {my_trie.search('apple')}")   # True
print(f"app가 있나요?: {myed.search('app')}")        # False (app는 접두사일 뿐 단어는 아님)
print(f"app로 시작하는 단어가 있나요?: {my_trie.starts_with('app')}") # (함수명 수정 필요)
# 위 예시를 위해 아래처럼 다시 호출해볼게요.
print(f"app로 시작하는 단어가 있나요?: {my_trie.starts_with('app')}") # 실제 구현 시 starts_with 대신 위 logic 사용
```
*(위 코드에서 `starts_with` 부분은 로직상 `search`와 비슷하지만 `is_end` 체크만 빼면 됩니다. 이해를 돕기 위해 통합 설명 드렸습니다!)*

### 다시 정리한 최종 실행 코드
```python
class Trie:
    def __init__(self):
        self.root = TrieNode()

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

# 테스트
trie = Trie()
trie.insert("apple")
print(trie.search("apple"))   # True
print(trie.search("app"))     # False
print(trie.startsWith("app")) # True
```

### 이 방법이 왜 효율적인가요?
일반적인 리스트에서 단어를 찾으려면 `O(N * M)` (N은 단어 개수, M은 단어 길이)의 시간이 걸리지만, 트라이를 사용하면 단어 개수와 상관없이 **단어의 길이(M)** 만큼만 확인하면 됩니다. 즉, `O(M)`이라는 엄청난 속도로 검색이 가능해집니다!

### 주의할 점 (Trade-off)
속도는 얻었지만 **메모리**를 많이 사용합니다. 모든 글자를 노드로 만들어 저장하기 때문에, 단어가 많아질수록 메모리 사용량이 급증합니다. 그래서 실제로는 '압축 트라이(Compressed Trie)' 같은 변형 기법을 쓰기도 한답니다.

이제 여러분은 자동완성 기능의 핵심 원리를 마스터하셨습니다! 다음 시간에는 더 놀라운 알고리즘으로 찾아올게요!
</details>
<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
