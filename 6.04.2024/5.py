def count_pairs_n2(A, K):
    n = len(A)
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if abs(A[i] - A[j]) >= K:
                count += 1
    return count

def count_pairs(A, K):
    A.sort()
    n = len(A)
    count = 0
    j = 0
    for i in range(n):
        while j < n and A[j] - A[i] < K:
            j += 1
        j = max(j, i + 1)
        count += n - j
    return count



def test_count_pairs():
    assert count_pairs([1, 5, 3, 9], 4) == count_pairs_n2([1, 5, 3, 9], 4)
    assert count_pairs([1, 2, 3, 4, 5], 3) == count_pairs_n2([1, 2, 3, 4, 5], 3)
    assert count_pairs([10, 10, 10, 10], 0) == count_pairs_n2([10, 10, 10, 10], 0)
    assert count_pairs([1], 1) == count_pairs_n2([1], 1)
    assert count_pairs([], 5) == count_pairs_n2([], 5)
    assert count_pairs([1, 100, 200], 99) == count_pairs_n2([1, 100, 200], 99)
    assert count_pairs([5, 1, 3, 6, 9], 2) == count_pairs_n2([5, 1, 3, 6, 9], 2)


test_count_pairs()