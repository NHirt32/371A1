def dynamic_unbounded(item_list, capacity):
    list = [0 for i in range(capacity + 1)]
    for i in range(capacity + 1):
        for item in range(len(item_list)):
            weight, value = item_list[item]
            if weight <= i:
                list[i] = max(list[i], list[i-weight] + value)

    return round(list[capacity])


item_list = [(0, 0), (2, 3), (3, 4), (4, 5), (5, 6)]

print(dynamic_unbounded(item_list, 5))
