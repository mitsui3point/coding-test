graph = {
        "A": ["B", "D", "E"],
        "B": ["A", "C", "D"],
        "C": ["B"],
        "D": ["A", "B"],
        "E": ["A"],
    }
visited = []

def dfs(curr_v):
    visited.append(curr_v)
    for next_v in graph[curr_v]:
        if (next_v not in visited):
            dfs(next_v)

if __name__ == "__main__":
    graph_data = {
        "A": ["B", "D", "E"],
        "B": ["A", "C", "D"],
        "C": ["B"],
        "D": ["A", "B"],
        "E": ["A"],
    }
    dfs("A")
    print(visited)
