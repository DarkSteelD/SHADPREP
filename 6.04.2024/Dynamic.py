dict_for_numbers = {
    1: [6, 8], 2: [7, 9], 3: [4, 8],
    4: [3, 0, 9], 5: [], 6: [1, 0, 7],
    7: [2, 6], 8: [1, 3], 9: [4, 2],
    0: [4, 6]
}



def solve(steps):
    prev_count = [0 if x == 0 or x == 8 else 1 for x in range (10)]
    next_count = [0] * 10
    while steps != 0:
        steps -= 1
        for i in range(10):
            for j in dict_for_numbers[i]:
                next_count[j] += prev_count[i]
        prev_count = next_count[:]
        next_count = [0] * 10
    return sum(prev_count)

steps = int(input()) - 1
print(solve(steps))

