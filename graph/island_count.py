def island_count(grid):
    r = 0
    for r < len(grid):
        r += 1
        c = 0
        for c < len(grid[0]):
            c += 1
            explore(grid, r, cw)