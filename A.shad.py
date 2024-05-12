def compute_rows_cols(rows, cols, grid):
    row_lengths = [[0] * (cols + 2) for _ in range(rows + 2)]
    col_lengths = [[0] * (cols + 2) for _ in range(rows + 2)]
    
    # Compute horizontal lengths (row-wise connectivity)
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            if grid[i][j] == 1:
                row_lengths[i][j] = row_lengths[i][j - 1] + 1
            else:
                row_lengths[i][j] = 0
    
    # Compute vertical lengths (column-wise connectivity)
    for j in range(1, cols + 1):
        for i in range(1, rows + 1):
            if grid[i][j] == 1:
                col_lengths[i][j] = col_lengths[i - 1][j] + 1
            else:
                col_lengths[i][j] = 0
    
    return row_lengths, col_lengths

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    rows, cols = int(data[0]), int(data[1])
    grid = [[0] * (cols + 2) for _ in range(rows + 2)]
    
    index = 2
    for i in range(1, rows + 1):
        row = data[index]
        index += 1
        for j in range(1, cols + 1):
            grid[i][j] = 1 if row[j - 1] == '1' else 0
    
    row_lengths, col_lengths = compute_rows_cols(rows, cols, grid)
    
    answer = 0
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            if grid[i][j] == 1:
                # Sum the lengths of the rows and columns passing through each cell, minus 1 to not double count the central cell
                total = row_lengths[i][j] + col_lengths[i][j] - 1
                answer = max(answer, total)
    
    print(answer)

if __name__ == "__main__":
    main()
