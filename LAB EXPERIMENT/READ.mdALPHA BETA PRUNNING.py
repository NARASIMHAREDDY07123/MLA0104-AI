import math

# Alpha-Beta Pruning Function
def alpha_beta(depth, nodeIndex, maximizingPlayer, values, alpha, beta, height):

    # Base Case
    if depth == height:
        return values[nodeIndex]

    if maximizingPlayer:
        best = -math.inf

        for i in range(2):
            value = alpha_beta(depth + 1, nodeIndex * 2 + i, False,
                               values, alpha, beta, height)
            best = max(best, value)
            alpha = max(alpha, best)

            # Beta Cutoff
            if beta <= alpha:
                break

        return best

    else:
        best = math.inf

        for i in range(2):
            value = alpha_beta(depth + 1, nodeIndex * 2 + i, True,
                               values, alpha, beta, height)
            best = min(best, value)
            beta = min(beta, best)

            # Alpha Cutoff
            if beta <= alpha:
                break

        return best


# Driver Code
values = [3, 5, 6, 9, 1, 2, 0, -1]

height = int(math.log2(len(values)))

result = alpha_beta(
    0,              # Depth
    0,              # Root Node
    True,           # Maximizing Player
    values,
    -math.inf,      # Alpha
    math.inf,       # Beta
    height
)

print("The optimal value is:", result)
