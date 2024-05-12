def compute_lengths(grid, r, c):
    lh = [[0] * (c + 2) for _ in range(r + 2)]  # left_horizontal
    rh = [[0] * (c + 2) for _ in range(r + 2)]  # right_horizontal
    uv = [[0] * (c + 2) for _ in range(r + 2)]  # up_vertical
    dv = [[0] * (c + 2) for _ in range(r + 2)]  # down_vertical

    # Calculate left and right horizontal lengths
    for i in range(1, r + 1):
        cl = cr = 0  # Counters for left and right horizontal
        for j in range(1, c + 1):
            if grid[i][j] == 1:
                cl += 1
            else:
                cl = 0
            lh[i][j] = cl

        for j in range(c, 0, -1):
            if grid[i][j] == 1:
                cr += 1
            else:
                cr = 0
            rh[i][j] = cr

    # Calculate up and down vertical lengths
    for j in range(1, c + 1):
        cu = cd = 0  # Counters for up and down vertical
        for i in range(1, r + 1):
            if grid[i][j] == 1:
                cu += 1
            else:
                cu = 0
            uv[i][j] = cu

        for i in range(r, 0, -1):
            if grid[i][j] == 1:
                cd += 1
            else:
                cd = 0
            dv[i][j] = cd

    return lh, rh, uv, dv

def find_max_shape(grid, r, c, lh, rh, uv, dv):
    answer = 0
    for i in range(1, r + 1):
        for j in range(1, c + 1):
            if grid[i][j] == 1:
                dcu = lh[i][j] + rh[i][j] + uv[i][j] - 2
                hcu = lh[i][j] + rh[i][j] + dv[i][j] - 2
                vcl = uv[i][j] + dv[i][j] + lh[i][j] - 2
                vcr = uv[i][j] + dv[i][j] + rh[i][j] - 2

                possible_t = max(hcu, vcl, vcr, dcu)
                answer = max(answer, possible_t)

    return answer

def main():
    r, c = map(int, input().split())
    grid = [[0] * (c + 2) for _ in range(r + 2)]

    for i in range(1, r + 1):
        row = input().strip()
        for j in range(1, c + 1):
            grid[i][j] = 1 if row[j - 1] == '1' else 0

    lh, rh, uv, dv = compute_lengths(grid, r, c)
    result = find_max_shape(grid, r, c, lh, rh, uv, dv)
    print("The maximum size of the 'T' shape is:", result)

if __name__ == "__main__":
    main()
