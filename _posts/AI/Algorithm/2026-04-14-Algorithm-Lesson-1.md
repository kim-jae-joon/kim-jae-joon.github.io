---
layout: single
title: "1강: 🚀 다익스트라 알고리즘: 최단 경로를 찾아서 음식 배달!"
date: 2026-04-14 00:53:46
categories: [Algorithm]
---


> **🤖 이 포스팅은 로컬 환경에서 구동되는 [EXAONE 3.5 32B AI] 모델을 활용하여 작성되었습니다.**
> (5년 차 주니어 개발자의 AI 관련 알고리즘 강의입니다!)
> 해당 블로그의 경우 댓글을 달아줄 시에 자동으로 Gemini AI 가 댓글을 달아줍니다.

<br>
# 1강: 🚀 다익스트라 알고리즘: 최단 경로를 찾아서 음식 배달!

안녕하세요, 알고리즘의 신 주니어 개발자입니다! 오늘은 코딩 세계에서 가장 인기 있는 영웅 중 한 명인 **다익스트라 알고리즘**을 소개할게요. 이 알고리즘은 마치 음식 배달 앱에서 가장 빠른 경로를 찾아주는 마법사 같은 존재랍니다. 

## 🎉 문제 상황: 음식 배달의 신이 되자!

**상황**: 당신은 인기 있는 음식 배달 앱의 개발자입니다. 도심의 복잡한 도로망에서 주문자의 위치에서 식당까지, 그리고 다시 주문자에게 돌아오는 최단 경로를 찾아야 합니다. 도로마다 교통 상황에 따라 비용(시간)이 다르다고 가정해봅시다. 

**구체적인 문제**:
- **도시 지도**: 5개의 노드(A, B, C, D, E)로 이루어진 그래프
- **시작 위치**: A (주문자 집)
- **목적지**: E (식당)
- **비용 행렬**: 각 노드 간의 이동 비용(시간)을 나타내는 행렬

예를 들어, 아래와 같은 비용 행렬이 주어졌다고 가정해봅시다:

```
비용 행렬:
   | A  B  C  D  E
--|------------
A | 0  2  5  1  ∞
B | 2  0  3  4  ∞
C | 5  3  0  2  ∞
D | 1  4  2  0  3
E | ∞  ∞  ∞  3  0
```

(여기서 `∞`는 직접 이동할 수 없는 경로를 의미합니다.)

**목표**: A에서 E까지의 최단 경로를 찾고, 그 경로와 총 비용을 출력하세요.

## 📚 개념 설명: 다익스트라 알고리즘의 비밀

### 왜 필요할까요?
- **최적 경로 찾기**: 다익스트라 알고리즘은 그래프에서 한 노드에서 다른 노드까지의 최단 경로를 효율적으로 찾는 데 사용됩니다. 특히 가중치가 있는 그래프에서 매우 유용합니다.
- **실용성**: 교통 네트워크, 네트워크 라우팅, GPS 경로 찾기 등 다양한 분야에서 활용됩니다.

### 시간 복잡도
- **최적화된 버전**: 우선순위 큐를 사용할 경우 \(O((V + E) \log V)\), 여기서 \(V\)는 노드의 수, \(E\)는 엣지의 수를 의미합니다.
- **간단한 구현**: \(O(V^2)\)로도 구현 가능하지만, 큰 그래프에서는 효율성이 떨어질 수 있습니다.

## 초보자 폭풍 질문!
- **Q**: 우선순위 큐가 뭔가요?
  - **A**: 우선순위 큐는 각 요소가 특정 우선순위를 가지고 있는 데이터 구조예요. 가장 낮은 비용(또는 가장 높은 우선순위)의 노드를 빠르게 추출할 수 있게 도와줍니다. 마치 식당에서 주문을 받을 때 우선순위대로 처리하는 것과 비슷해요!

## 🔧 문제 해결 가이드

### 접근 방법
1. **초기화**: 시작 노드(A)의 비용을 0으로 설정하고, 나머지 노드의 비용을 무한대로 설정.
2. **우선순위 큐**: 현재 노드와 그 비용을 저장하는 큐를 사용.
3. **반복**:
   - 큐에서 비용이 가장 작은 노드를 꺼냄.
   - 해당 노드의 인접 노드들을 순회하며, 더 짧은 경로가 발견되면 업데이트.
   - 업데이트된 노드를 다시 큐에 넣음.
4. **종료 조건**: 목적지 노드(E)에 도달하거나, 모든 노드를 방문할 때까지 반복.


<details markdown="1"><summary>💡 해결 방안 및 정답 코드 보기 (클릭)</summary>

### 🛠️ 해결 방안 가이드 (알고리즘 설계)
1. **비용 행렬 초기화**: 시작 노드의 비용을 0으로 설정하고, 나머지는 무한대로 초기화.
2. **우선순위 큐 사용**: 파이썬의 `heapq` 모듈을 활용해 우선순위 큐를 구현.
3. **경로 추적**: 각 노드의 이전 노드를 기록하여 최단 경로를 추적.

### 💻 파이썬 정답 코드 및 상세 해설

```python
import heapq

def dijkstra(graph, start, end):
    # 비용 행렬 초기화
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}
    priority_queue = [(0, start)]  # (비용, 노드)

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # 이미 처리된 노드는 건너뛰기
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # 더 짧은 경로 발견 시 업데이트
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    # 경로 추적
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous_nodes[current]
    path.reverse()

    return distances[end], path

# 그래프 정의 (비용 행렬을 딕셔너리로 표현)
graph = {
    'A': {'B': 2, 'C': 5, 'D': 1},
    'B': {'A': 2, 'C': 3, 'D': 4},
    'C': {'A': 5, 'B': 3, 'D': 2},
    'D': {'A': 1, 'B': 4, 'C': 2, 'E': 3},
    'E': {'D': 3}
}

# 실행
start_node = 'A'
end_node = 'E'
total_cost, shortest_path = dijkstra(graph, start_node, end_node)

print(f"최단 경로: {' -> '.join(shortest_path)}")
print(f"총 비용: {total_cost}")
```

### 🚀 한계점 및 실무 개선점
- **대규모 데이터**: 매우 큰 그래프에서는 메모리 사용량과 처리 시간이 증가할 수 있습니다. 
  - **최적화 방안**: **A* 알고리즘**과 같은 휴리스틱을 도입하여 탐색 범위를 줄일 수 있습니다.
- **동적 변화**: 실시간 교통 상황에 따라 비용이 변동될 경우, 동적 업데이트 메커니즘이 필요합니다.
  - **예외 처리**: 주기적인 재계산 또는 이벤트 기반 업데이트 시스템을 구현하여 실시간 변화에 대응할 수 있습니다.

</details>

이제 여러분도 다익스트라 알고리즘을 활용해 음식 배달 앱의 최단 경로 문제를 해결할 수 있는 마법사가 되셨습니다! 더 많은 질문이나 피드백이 있다면 언제든지 말씀해주세요. 다음 강의에서 또 만나요!
<br><br><hr>
<h3>💬 궁금한 점이 있다면 자유롭게 댓글을 남겨주세요! (AI 비서가 답변해 드립니다 🤖)</h3>
<script src="https://utteranc.es/client.js"
        repo="kim-jae-joon/kim-jae-joon.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
