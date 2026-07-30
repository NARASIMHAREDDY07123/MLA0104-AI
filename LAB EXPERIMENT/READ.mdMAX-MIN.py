import math

# Minimax Function
def minimax(depth, nodeIndex, isMax, values, height):

    # Base case: leaf node reached
    if depth == height:
        return values[nodeIndex]

    if isMax:
        return max(
            minimax(depth + 1, nodeIndex * 2, False, values, height),
            minimax(depth + 1, nodeIndex * 2 + 1, False, values, height)
        )
    else:
        return min(
            minimax(depth + 1, nodeIndex * 2, True, values, height),
            minimax(depth + 1, nodeIndex * 2 + 1, True, values, height)
        )

# Driver Code
values = [3, 5, 2, 9, 12, 5, 23, 23]

height = int(math.log2(len(values)))

result = minimax(0, 0, True, values, height)

print("The optimal value is:", result)
