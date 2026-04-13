---
layout: single
title: "2강: 음식 배달의 신, **A* 알고리즘**"
date: 2026-04-14 00:50:58
categories: [Algorithm]
---


> **🤖 이 포스팅은 로컬 환경에서 구동되는 [EXAONE 3.5 32B AI] 모델을 활용하여 작성되었습니다.**
> (5년 차 주니어 개발자의 AI 관련 알고리즘 강의입니다!)
> 해당 블로그의 경우 댓글을 달아줄 시에 자동으로 Gemini AI 가 댓글을 달아줍니다.

<br>
# 2강: 음식 배달의 신, **A* 알고리즘**

안녕하세요, 알고리즘의 신이자 5년 차 주니어 개발자인 저입니다! 이번 강의에서는 여러분이 일상에서 자주 마주치는 상황을 통해 **A* 알고리즘**을 배워볼 거예요. 상상해보세요, 맛있는 음식을 배달하는 로봇이 있다면 어떨까요? 이 로봇은 최단 경로로 빠르게 음식을 배달해야 하는데, 이때 바로 A* 알고리즘이 활약합니다.

## 🍽️ 문제 상황: 최단 경로 음식 배달

**상황:** 도심의 작은 배달 로봇 '푸드봇'이 여러 음식점에서 주문받은 음식을 고객에게 배달해야 합니다. 하지만 도심은 복잡한 도로망으로 이루어져 있어, 최적의 경로를 찾는 것이 중요합니다. 푸드봇이 **(0, 0)**에서 시작하여 **(5, 5)**에 있는 고객에게 **가장 빠른 경로**로 음식을 배달하도록 도와줘야 합니다. 도로망은 격자 형태로, 각 칸은 이동 가능한 블록이며, 일부 블록은 장애물(건물 등)로 막혀 있을 수 있습니다.

**입력:**
- 시작 위치: `(start_x, start_y) = (0, 0)`
- 도착 위치: `(goal_x, goal_y) = (5, 5)`
- 격자 맵 (2D 리스트): 0은 이동 가능, 1은 장애물

**예시 격자 맵:**
```
[
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
```

**목표:** 푸드봇이 장애물을 피해 가장 빠른 경로로 도착하도록 A* 알고리즘을 구현하세요.

---

## 초보자 폭풍 질문!

**Q: A* 알고리즘이 왜 필요한가요?**  
A* 알고리즘은 **최적 경로 탐색**에 특화되어 있어요. 단순히 거리만 고려하는 것이 아니라, 목표까지의 예상 비용(heuristic)을 함께 고려하여 더 효율적인 경로를 찾을 수 있습니다. 이는 실제 배달이나 로봇 경로 계획 등에서 매우 유용합니다!

**Q: Heuristic 함수는 어떻게 정의해야 하나요?**  
Heuristic 함수는 현재 위치에서 목표 위치까지의 **예상 비용**을 계산합니다. 가장 간단한 방법은 맨해튼 거리(격자에서 수평/수직 이동만 고려)나 유클리드 거리를 사용하는 거예요. 예를 들어, 맨해튼 거리는 `|x1 - x2| + |y1 - y2|`로 계산할 수 있습니다.

---

<details markdown="1">
<summary>💡 해결 방안 및 정답 코드 보기 (클릭)</summary>

### 🛠️ 해결 방안 가이드 (알고리즘 설계)

1. **데이터 구조 준비**:
   - **Open List**: 방문할 노드들을 저장하는 우선순위 큐 (F(n) = g(n) + h(n) 기준).
   - **Closed List**: 이미 방문한 노드들을 저장하는 집합.
   - **부모 노드 맵**: 경로 추적을 위한 맵.

2. **Heuristic 함수 정의**:
   - 여기서는 맨해튼 거리를 사용합니다: `h(n) = |x - goal_x| + |y - goal_y|`.

3. **A* 알고리즘 실행**:
   - 시작 노드를 Open List에 추가.
   - Open List가 빌 때까지 반복:
     - F(n) 값이 가장 낮은 노드 선택.
     - 선택된 노드를 Closed List로 이동.
     - 이웃 노드들에 대해:
       - 장애물이 아니고, Closed List에 없으면,
       - g(n) 계산 (현재 노드까지의 실제 비용).
       - F(n) = g(n) + h(n) 계산.
       - 만약 이웃 노드가 이미 Open List에 있다면, 더 낮은 F(n) 값으로 업데이트.
     - 목표 노드에 도달하면 경로 추적.

### 💻 파이썬 정답 코드 및 상세 해설

```python
import heapq

def heuristic(a, b):
    """맨해튼 거리 heuristic 함수"""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star_search(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_list = []
    heapq.heappush(open_list, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1]  # 경로를 역순으로 반환

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # 상하좌우 이동
            neighbor = (current[0] + dx, current[1] + dy)
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and grid[neighbor[0]][neighbor[1]] == 0:
                tentative_g_score = g_score[current] + 1  # 각 이동 비용은 1로 가정

                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                    heapq.heappush(open_list, (f_score[neighbor], neighbor))

    return None  # 경로를 찾지 못한 경우

# 예시 사용
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
start = (0, 0)
goal = (5, 5)

path = a_star_search(grid, start, goal)
print("최적 경로:", path)
```

### 🚀 한계점 및 실무 개선점

**한계점:**
- **메모리 사용량**: 대규모 맵에서는 Open List와 부모 노드 맵이 많은 메모리를 소비할 수 있습니다.
- **Heuristic의 정확성**: Heuristic 함수가 너무 낙관적이거나 비관적이면 최적 경로를 찾는 데 영향을 줄 수 있습니다.

**실무 개선점:**
- **메모리 최적화**: 메모리 제한이 있는 환경에서는 노드를 효율적으로 관리하거나, 부분적인 맵만 메모리에 로드하는 방식을 고려할 수 있습니다.
- **다중 Heuristic**: 복잡한 환경에서는 여러 heuristic을 결합하여 더 정확한 예측을 할 수 있습니다.
- **병렬 처리**: 대규모 데이터셋에서는 병렬 처리를 통해 계산 속도를 향상시킬 수 있습니다.

---

이제 A* 알고리즘을 통해 푸드봇이 빠르고 효율적으로 음식을 배달할 수 있게 되었어요! 알고리즘의 힘을 느껴보셨나요? 다음 강의에서도 더 재미있는 알고리즘으로 찾아올게요!
<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
