visited = []


def dfs(graph, curr_v, visited=[]):

    curr = graph[curr_v]
    next = None
    if curr_v is None:
        return
    for next_v in curr:
        # if result :
        #     return
        next = graph[next_v]
        print("-" * 50)
        print("curr_v", curr_v, ',', curr)
        print("next_v", next_v, ',', next)
        print('prev visited', visited)
        if (curr_v not in visited):
            visited.append(curr_v)
            dfs(graph, next_v, visited)
            continue
        if (curr_v in visited):
            continue
        print('after visited', visited)
    return visited
    # print("-"*50)
    # print("start_v", start_v)
    # print("v", v)
    # print("0visited", visited)


if __name__ == "__main__":
    graph_data = {
        "A": ["B", "D", "E"],
        "B": ["A", "C", "D"],
        "C": ["B"],
        "D": ["A", "B"],
        "E": ["A"],
    }
    print(dfs(graph_data, "A"))
