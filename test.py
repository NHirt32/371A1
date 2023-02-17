def dynamic_unbounded(item_list, capacity):
    list = [0 for i in range(capacity + 1)]
    for i in range(capacity + 1):
        for item in range(len(item_list)):
            weight, value = item_list[item]
            if weight <= i:
                list[i] = max(list[i], list[i-weight] + value)

    return round(list[capacity])


def dynamic_bounded(capacity, wt, val, n):
    K = [[0 for x in range(capacity+1)] for y in range(2)]

    for i in range(n + 1):
        for w in range(capacity + 1):
            if (i == 0 or w == 0):
                K[i % 2][w] = 0
            elif (wt[i - 1] <= w):
                K[i % 2][w] = max(
                    val[i - 1]
                    + K[(i - 1) % 2][w - wt[i - 1]],
                    K[(i - 1) % 2][w])

            else:
                K[i % 2][w] = K[(i - 1) % 2][w]

    print()
    return K[n % 2][capacity]


def knapsack_recursive(profits, weights, capacity, currentIndex):
    # base checks
    if capacity <= 0 or currentIndex >= len(profits):
        return 0

    # recursive call after choosing the element at the currentIndex
    # if the weight of the element at currentIndex exceeds the capacity, we  shouldn't process this
    profit1 = 0
    if weights[currentIndex] <= capacity:
        profit1 = profits[currentIndex] + knapsack_recursive(
            profits, weights, capacity - weights[currentIndex], currentIndex + 1)

    # recursive call after excluding the element at the currentIndex
    profit2 = knapsack_recursive(profits, weights, capacity, currentIndex + 1)

    return max(profit1, profit2)


val = [0, 3, 4, 5, 6]
wt = [1, 2, 3, 4, 5]
capacity = 5
n = len(val)

item_list = [(0, 0), (2, 3), (3, 4), (4, 5), (5, 6)]

print(knapsack_recursive(val, wt, capacity, 0))
