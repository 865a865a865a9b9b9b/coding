N = 12

def dfs(x, y, st, dist, candy):
    global mc
    global md

    st2 = [row[:] for row in st]
    
    if st2[x][y] == '*':
        candy += 1
        mc = max(mc, candy)
        md[candy] = min(md[candy], dist)
        
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if st2[i][j] == 'a' and candy >= 1:
                    st2[i][j] = '.'
                if st2[i][j] == 'b' and candy >= 2:
                    st2[i][j] = '.'
                if st2[i][j] == 'c' and candy >= 3:
                    st2[i][j] = '.'
                if st2[i][j] == 'd' and candy >= 4:
                    st2[i][j] = '.'
                if st2[i][j] == 'e' and candy >= 5:
                    st2[i][j] = '.'
                if st2[i][j] == 'f' and candy >= 6:
                    st2[i][j] = '.'
                if st2[i][j] == 'B':
                    st2[i][j] = '.'

    st2[x][y] = 'B'

    if st2[x - 1][y] == '.' or st2[x - 1][y] == '*':
        dfs(x - 1, y, st2, dist + 1, candy)
    if st2[x + 1][y] == '.' or st2[x + 1][y] == '*':
        dfs(x + 1, y, st2, dist + 1, candy)
    if st2[x][y - 1] == '.' or st2[x][y - 1] == '*':
        dfs(x, y - 1, st2, dist + 1, candy)
    if st2[x][y + 1] == '.' or st2[x][y + 1] == '*':
        dfs(x, y + 1, st2, dist + 1, candy)

for k in range(5):
    st = [['#' for _ in range(N)] for _ in range(N)]
    md = [float('inf')] * 101
    mc = 0
    md[0] = 0

    n = int(input())
    for i in range(1, n + 1):
        row = input()
        for j in range(1, n + 1):
            st[i][j] = row[j - 1]
            if st[i][j] == 'B':
                x0 = i
                yy0 = j
                st[i][j] = '.'

    dfs(x0, yy0, st, 0, 0)
    print(f"{mc} {md[mc]}")
