from queue import PriorityQueue

# Graph with heuristic values
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}

# Heuristic values (h(n))
heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 5,
    'E': 2,
    'F': 1,
    'G': 0
}

def greedy_best_first_search(start, goal):
    visited = set()
    pq = PriorityQueue()

    # Put start node with heuristic value
    pq.put((heuristic[start], start))

    while not pq.empty():
        h, node = pq.get()

        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            if node == goal:
                print("\nGoal Reached!")
                return

            for neighbor, cost in graph[node]:
                if neighbor not in visited:
                    pq.put((heuristic[neighbor], neighbor))

    print("\nGoal Not Found!")

# Driver Code
start = 'A'
goal = 'G'

print("Traversal using Greedy Best-First Search:")
greedy_best_first_search(start, goal)
