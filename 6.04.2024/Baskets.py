from itertools import product

n = int(input())
seen = set()
seen_A = set()
seen_B = set()
seen = set()

for x in product([0, 1], repeat=n):
    A = tuple(1 for i in range(n) if x[i] == 0)
    B = tuple(1 for i in range(n) if x[i] == 1)
    if tuple(sorted(A)) not in seen_A and tuple(sorted(B)) not in seen_B:
        seen_A.add(tuple(sorted(A)))
        seen_B.add(tuple(sorted(B)))
        if tuple(sorted([A,B])) not in seen:
            seen.add(tuple(sorted([A,B])))
            print(f"A: {A}, B: {B}")

