# [BOJ]_2842_집배원 한상덕 (DFS)

### 문제

![image-20211101171005093]([BOJ]_2842_집배원한상덕.assets/image-20211101171005093.png)

### 입력

![image-20211101171014853]([BOJ]_2842_집배원한상덕.assets/image-20211101171014853.png)

### 출력

![image-20211101171023145]([BOJ]_2842_집배원한상덕.assets/image-20211101171023145.png)

### 풀이

- 모든 K를 방문할때까지 경로를 찾는다.
- 찾은 경로 중에서 피로도가 가장 작은 루트를 선택한다
- 경로를 찾아갈때 피로도를 기준으로 가지치기가 가능하다.

```python
import sys
sys.setrecursionlimit(100000)
# 상 하 좌 우  남동  남서  북서 북동
dx = [-1, 1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, -1, 1, 1, -1, -1, 1]

# 시작점 찾아요~ 집 갯수 세어봐요...
def find_p():
    re_x, re_y = 0, 0
    house = 0
    for x in range(N):
        for y in range(N):
            if MAP[x][y] == 'P':
                re_x = x
                re_y = y
            elif MAP[x][y] == 'K':
                house += 1
	# 시작점의 x, y와 집의 갯수 리턴!
    return (re_x, re_y, house)

#탐색 출발 (현재 x, y, 찾은 집 갯수,   현재 경로상 최소높이, 최대높이)
def dfs(nowx, nowy, K, min, max):
    global gap

    now_k = K
    minner = min
    maxxer = max
    #현재 위치가 경로중에 제일 높니?
    if HILL[nowx][nowy] > maxxer:
        maxxer = HILL[nowx][nowy]
    #현재 위치가 경로중에 제일 낮니?
    if HILL[nowx][nowy] < minner:
        minner = HILL[nowx][nowy]
	#현재 경로 갭 
    now_gap = maxxer - minner
	# 전에 찾은 경로보다 갭이 크면 그만 가봐..
    if now_gap >= gap:
        return
	#현재점이 집이면 집 카운트 증가!
    if MAP[nowx][nowy] == 'K':
        now_k += 1
	#집 다 찾았으면 갱신! 위에서 피로도를 검사했음!
    if now_k == K_cnt:
        gap = now_gap
        return
	# 8방향으로 가보자
    for add in range(8):
        nx = nowx + dx[add]
        ny = nowy + dy[add]
        #맵 밖으로 안나간다면.
        if 0 <= nx < N and 0 <= ny < N:
            #이번 경로에 가보지 않았다면
            if Find_k_map[nx][ny] == 0:
                Find_k_map[nx][ny] = 1
                # 자 가보자.
                dfs(nx, ny, now_k, minner, maxxer)
                Find_k_map[nx][ny] = 0

#입력받기
N = int(sys.stdin.readline())
#우체국과 집관련 맵 입력
MAP = [sys.stdin.readline().rstrip() for _ in range(N)]
#높이 맵 입력
HILL = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
Find_k_map = [[0] * N for _ in range(N)]

#시작점과 집 갯수 찾아오자
post = find_p()
# 집 갯수만....
K_cnt = post[2]
#시작점의 높이부터 가즈아
pp =HILL[post[0]][ post[1]]
#출력용 차이
gap = float('inf')
#시작점 방문 체크
Find_k_map[start_x][start_y] = 1
#탐험 가자.
dfs(post[0],  post[1], 0, pp, pp)
#그래서 피로도는?
print(gap)
```



