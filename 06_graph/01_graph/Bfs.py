from collections import deque

def bfs(graph, start_v):
    q = deque(start_v)
    visited = [start_v]
    while q:
        cur_v = q.popleft()
        for v in graph[cur_v]:
            if v not in visited:
                visited.append(v)
                q.append(v)
    return visited

if __name__ == "__main__":
    graph_data = {
        "A": ["B", "D", "E"],
        "B": ["A", "C", "D"],
        "C": ["B"],
        "D": ["A", "B"],
        "E": ["A"],
    }

    print(bfs(graph_data, "A"))

