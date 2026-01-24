def total_distance(n):
    distance = 10
    total = 0

    for i in range(n):
        total += distance
        distance *= 1.1

    return total