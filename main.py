from itertools import cycle


def solve(n):
    # Generator for a pattern of smaller and smaller squares of # and o alternating.
    pattern = cycle('#.')
    squares = [[[next(pattern)] * side] * side for side in range(n, 0, -2)]

    # Drawing the smaller squares inside the bigger ones on top of eachother.
    final_grid = [['x' for _ in range(n)] for y in range(n)]
    for offset, square in enumerate(squares):
        for y, row in enumerate(square):
            for x, c in enumerate(row):
                final_grid[y+offset][x+offset] = c

    for row in final_grid:
        print("".join(row))


if __name__ == "__main__":
    solve(12)