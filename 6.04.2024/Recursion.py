
from functools import lru_cache

dict_for_numbers = {
    1: [6, 8], 2: [7, 9], 3: [4, 8],
    4: [3, 0, 9], 5: [], 6: [1, 0, 7],
    7: [2, 6], 8: [1, 3], 9: [4, 2],
    0: [4, 6]
}

@lru_cache(maxsize=None)
def solve(number: int, depth: int, max_depth: int) -> int:
    if depth + 1 > max_depth:
        if depth + 1 == max_depth:
            return len(dict_for_numbers[number])
        else:
            return 1
    cnt = 0
    for i in dict_for_numbers[number]:
        cnt += solve(i, depth + 1, max_depth)
    return cnt

sum_of_elem = 0
depth = int(input())
for i in range(0, 10):
    if i != 0 and i != 8:
        sum_of_elem += solve(i, 1, depth)

print(sum_of_elem)
