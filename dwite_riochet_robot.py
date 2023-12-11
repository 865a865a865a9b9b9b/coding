from collections import deque

def in_bounds(n):
    return 0 <= n < 10

grid = ["" for _ in range(10)]
vis = [[False] * 10 for _ in range(10)]

def solve():
    for _ in range(5):
        vis.clear()
        for i in range(10):
            s = input()
            grid[i] = s
            vis.append([False] * 10)

        s = input()
        x, y = 0, 0
        for i in range(10):
            for j in range(10):
                if grid[i][j] == 'A':
                    x, y = i, j

        q = deque([(x, y)])
        quit_flag = False
        d = 0

        while q:
            s = len(q)
            for _ in range(s):
                rs, cs = q.popleft()
                if vis[rs][cs]:
                    continue
                if grid[rs][cs] == 'B':
                    quit_flag = True
                    break

                vis[rs][cs] = True

                # move up
                r, c = rs, cs
                while in_bounds(r - 1) and grid[r - 1][c] != '#':
                    r -= 1
                q.append((r, c))

                r, c = rs, cs
                while in_bounds(r + 1) and grid[r + 1][c] != '#':
                    r += 1
                q.append((r, c))

                r, c = rs, cs
                while in_bounds(c - 1) and grid[r][c - 1] != '#':
                    c -= 1
                q.append((r, c))

                r, c = rs, cs
                while in_bounds(c + 1) and grid[r][c + 1] != '#':
                    c += 1
                q.append((r, c))

            d += 1
            if quit_flag:
                break

        print(d - 1)

if __name__ == "__main__":
    solve()
