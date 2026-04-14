---
layout: single
title: "4강: 보물찾기의 달인, **A* 알고리즘**"
date: 2026-04-14 23:03:13
categories: [Algorithm]
---

# 4강: 보물찾기의 달인, **A* 알고리즘**

안녕하세요, 초보 개발자 김재준님! 이번 강의에서는 보물 찾기의 달인이 되기 위한 핵심 도구, **A* 알고리즘**에 대해 알아볼 거예요. 이 알고리즘은 마치 보물지도를 따라 보물을 찾아가는 모험가와 같아요. 일상에서도 게임 내 경로 찾기나 로봇의 자율 주행 등에서 자주 쓰이는 마법 같은 알고리즘이죠.

### 보물찾기 미션: 미로 속 보물 추적

**상황**: 
당신은 고대 유적지의 복잡한 미로 속에서 황금 보물을 찾아야 합니다. 미로는 격자 형태로 되어 있고, 각 칸에는 벽이 있을 수도, 통로가 있을 수도 있어요. 목표는 시작점에서 보물이 있는 칸까지 최단 경로를 찾아내는 것입니다. 하지만, 단순히 최단 경로만 찾는 게 아니라, 보물까지의 '예상 거리'도 고려해야 합니다.

**입력**:
- `maze`: 2차원 리스트로 표현된 미로 (`0`은 통로, `1`은 벽)
- `start`: 시작 좌표 `(x, y)`
- `treasure`: 보물 좌표 `(x, y)`

**출력**:
- 보물까지의 최단 경로를 나타내는 좌표 리스트 (예: `[(0, 0), (1, 0), ...]`)

### 알고리즘의 필요성
A* 알고리즘은 **최단 경로 탐색**에 있어서 매우 효율적입니다. 다른 알고리즘들과 달리, A*는 **heuristic 함수**를 사용하여 현재 위치에서 목표까지의 '예상 비용'을 고려합니다. 이를 통해 더 빠르게 목표에 도달할 수 있어요. 시간 복잡도는 일반적으로 O(E + V log V) 정도로, E는 간선의 수, V는 정점의 수를 의미합니다.

### 개념 설명
- **g(n)**: 시작 노드에서 현재 노드까지의 실제 비용
- **h(n)**: 현재 노드에서 목표 노드까지의 추정 비용 (heuristic 함수)
- **f(n) = g(n) + h(n)**: 총 비용, 이 값을 기준으로 노드를 선택합니다.

### 초보자 폭풍 질문!
- **Q**: heuristic 함수는 어떻게 정의하나요?
  - **A**: 간단하게는 맨해튼 거리(격자에서 가로+세로 거리)를 사용할 수 있어요. 예를 들어, `(x1, y1)`에서 `(x2, y2)`까지의 맨해튼 거리는 `|x1 - x2| + |y1 - y2|`로 계산합니다.

### 해결 방안 및 정답 코드 보기 (클릭)

<details markdown="1">
<summary> 해결 방안 및 정답 코드 보기 (클릭)</summary>

### 해결 방안 가이드 (알고리즘 설계)
1. **초기 설정**:
   - 시작 노드를 열린 리스트에 추가합니다.
   - 각 노드에 대한 `g(n)`, `f(n)` 값 초기화.
   
2. **반복**:
   - 열린 리스트에서 `f(n)` 값이 가장 작은 노드를 선택.
   - 선택된 노드를 닫힌 리스트로 이동.
   - 선택된 노드의 모든 인접 노드를 검사하며, 더 나은 경로가 발견되면 업데이트.
   - 목표 노드에 도달하면 경로를 추적하여 반환.

3. **Heuristic 함수**:
   - 여기서는 맨해튼 거리를 사용합니다.

### 파이썬 정답 코드 및 상세 해설
```python
import heapq

def heuristic(a, b):
    """맨해튼 거리 계산"""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star_search(maze, start, treasure):
    rows, cols = len(maze), len(maze[0])
    open_set = []
    heapq.heappush(open_set, (0, start))  # (f(n), (x, y))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, treasure)}

    while open_set:
        _, current = heapq.heappop(open_set)
        
        if current == treasure:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1]  # 경로 역순으로 반환

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # 상하좌우
            neighbor = (current[0] + dx, current[1] + dy)
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and maze[neighbor[0]][neighbor[1]] == 0:
                tentative_g_score = g_score[current] + 1
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristic(neighbor, treasure)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))
    
    return None  # 경로를 찾지 못한 경우

# 예시 사용
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]
start = (0, 0)
treasure = (4, 4)

path = a_star_search(maze, start, treasure)
print("보물까지의 경로:", path)
```

### 한계점 및 실무 개선점
- **대규모 미로**: 대규모 미로에서는 메모리 사용량과 계산 시간이 증가할 수 있습니다. 이를 개선하기 위해 **메모리 제한을 고려한 경로 분할**이나 **병렬 처리** 기법을 적용할 수 있습니다.
- **복잡한 Heuristic**: 실제 환경에서는 더 정교한 heuristic 함수를 사용해야 할 수 있습니다. 예를 들어, 장애물의 밀도나 동적 환경 변화를 고려한 heuristic을 도입하면 더 효율적일 수 있습니다.
- **예외 처리**: 미로 내에 경로가 없는 경우나 시작/목표 위치가 벽인 경우를 체크하고 적절히 처리해야 합니다.

이제 김재준님도 보물찾기의 달인이 될 준비가 되셨겠죠? 실전에서도 이런 알고리즘들이 어떻게 활용되는지 이해하셨기를 바랍니다!
<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
