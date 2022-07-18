from sys import stdin
from collections import deque

input = stdin.readline

def solve():
    N, M, K = map(int, input().split())
    if N == 1 and M == 1:
        return 1
    arr = [input()[:-1] for _ in range(N)]
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    crack_count = [[K + 1] * M for _ in range(N)]
    crack_count[0][0] = 0

    # (x, y, 벽 부순 횟수)
    que = deque([(0, 0, 0)])

    N_, M_ = N - 1, M - 1
    ans = 1
    while que:
        l = len(que)
        for _ in range(l):
            ox, oy, crack = que.popleft()

            if ox == N_ and oy == M_:
                return ans

            elif crack == crack_count[ox][oy]:
                for dx, dy in d:
                    x = ox + dx
                    y = oy + dy
                    if 0 <= x < N and 0 <= y < M:
                        if crack < crack_count[x][y]:
                            # 다음 칸이 빈칸인 경우
                            # 낮이든 밤이든 상관없다
                            if arr[x][y] == '0':
                                crack_count[x][y] = crack
                                que.append((x, y, crack))

                            # 다음 칸이 벽인 경우
                            else:
                                if crack + 1 >= crack_count[x][y]:
                                    continue

                                # 낮인 경우만 벽을 부술 수 있다
                                elif ans & 1:
                                    crack_count[x][y] = crack + 1
                                    que.append((x, y, crack + 1))

                                # 밤인 경우 제자리에 머무른다
                                else:
                                    que.append((ox, oy, crack))

        ans += 1

    return -1

print(solve())