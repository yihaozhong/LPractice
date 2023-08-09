nrows, ncols = len(grid), len(grid[0])
directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
for x, y in shots:
    if grid[x][y] == '.':
        res.append("Missed")
        continue

    if len(grid[x][y]) == 1:

        find = False
        for dx, dy in directions:
            if find:
                break
            cur_x = x + dx
            cur_y = y + dy
            if cur_x in range(nrows) and cur_y in range(ncols) and grid[cur_x][cur_y] == grid[x][y]:
                find = True

        if find:
            update = "Attacked ship " + grid[x][y]
            res.append(update)
            grid[x][y] = update
        else:
            res.append("Ship " + grid[x][y] + " sunk")
            # grid[x][y] = "."
    else:
        res.append("Already attacked")
print(res)
return res
