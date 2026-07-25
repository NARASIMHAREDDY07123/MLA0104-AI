**1. Breadth First Search (BFS)**

Breadth First Search explores all neighboring nodes before moving to the next level. It guarantees the shortest path in an unweighted graph.

**Pseudocode**

BFS(Graph, Start)

Create an empty queue
Create a visited set

Enqueue(Start)
Mark Start as visited

While queue is not empty

    Node = Dequeue()

    Print Node

    For each Neighbor of Node

        If Neighbor is not visited

            Mark Neighbor as visited
            Enqueue(Neighbor)

End

**Explanation**
Start from the source node.
Add it to the queue.
Visit every adjacent node.
Continue level by level.
Stop when all nodes are visited.
Use Cases
GPS Navigation
Social Network Friend Suggestions
Shortest Path in Unweighted Graphs
Web Crawlers


**2. Depth First Search (DFS)**
Description

Depth First Search explores one branch completely before backtracking.

**Pseudocode**
DFS(Node)

Mark Node as visited

Print Node

For each Neighbor

    If Neighbor is not visited

        DFS(Neighbor)

End
**Explanation**
Visit the starting node.
Go as deep as possible.
Backtrack when no child exists.
Repeat until all nodes are visited.

Use Cases:
Maze Solving
Topological Sorting
Cycle Detection
Puzzle Solving

**3. Uniform Cost Search (UCS)**
Description

Uniform Cost Search expands the node with the lowest cumulative path cost.

**Pseudocode**
Insert Start into Priority Queue

While Queue is not empty

    Remove node with minimum cost

    If Goal found

        Return Path

    Expand neighbors

    Update cost

    Insert into Queue

End

**Explanation**
Uses a Priority Queue.
Always expands the cheapest path.
Guarantees optimal solution.

**Use Cases**
Route Planning
GPS Navigation
Robotics
Logistics
**4. Greedy Best First Search (GBFS)**
Description

GBFS selects the node having the smallest heuristic value.

**Pseudocode**
Insert Start into Priority Queue

While Queue not empty

    Remove node with lowest heuristic

    If Goal reached

        Stop

    Expand neighbors

    Insert neighbors using heuristic

End

**Explanation**
Uses heuristic function h(n).
Chooses the node closest to goal.
Does not consider path cost.
Formula
f(n) = h(n)

**Use Cases**
Robot Navigation
Video Game AI
Path Finding
Network Routing

****5. A* Search****
Description

A* Search combines actual path cost and heuristic value.

**Pseudocode**
Insert Start into Open List

While Open List not empty

    Remove node with lowest f(n)

    If Goal reached

        Stop

    Expand neighbors

    Calculate

        g(n)

        h(n)

        f(n)=g(n)+h(n)

    Update Open List

End

**Explanation**
Combines actual cost and estimated cost.
Produces optimal path.
Faster than Uniform Cost Search.
Formula
f(n)=g(n)+h(n)

**Use Cases**
Google Maps
GPS Systems
Robot Navigation
Game Development**

**6. Min-Max Algorithm****
Description

Min-Max is used in two-player games where one player tries to maximize the score while the other minimizes it.

**Pseudocode**
MINIMAX(Node, Depth, MaxPlayer)

If Leaf Node

    Return Value

If MaxPlayer

    Return Maximum of Children

Else

    Return Minimum of Children

End

**Explanation**
MAX chooses highest value.
MIN chooses lowest value.
Continues recursively.
Returns optimal move.

**Use Cases**
Chess
Tic Tac Toe
Checkers
Connect Four
**7. Alpha-Beta Pruning**
Description

Alpha-Beta Pruning improves Min-Max by eliminating unnecessary branches.

Pseudocode
AlphaBeta(Node, Alpha, Beta)

If Leaf

    Return Value

If Maximizer

    Update Alpha

Else

    Update Beta

If Beta <= Alpha

    Prune branch

Return Best Value

**Explanation**
Uses Alpha and Beta values.
Skips unnecessary branches.
Produces same result as Min-Max with fewer computations.
Formula
Alpha = Best value for MAX

Beta = Best value for MIN

Prune when

Beta <= Alpha

**Use Cases**
Chess Engines
Game AI
Checkers
Tic Tac Toe

**8. Water Jug Problem**
Description

The Water Jug Problem is a classic state-space search problem used in Artificial Intelligence.

**Pseudocode**
Start

Fill either jug

Empty either jug

Pour water from one jug to another

Repeat until target amount is reached

Stop

**Explanation**
Represents every water level as a state.
Uses state-space search.
Goal is obtaining required quantity.
Use Cases
AI State Space Problems
Puzzle Solving
Robot Planning
Constraint Satisfaction

