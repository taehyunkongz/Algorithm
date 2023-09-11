import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

def DFS(start):
    global answer
    if start == N:
        cnt = 0
        for i in range(N):
            if eggs[i][0] <= 0:
                cnt += 1
        answer = max(answer, cnt)
        return
    if eggs[start][0] <= 0:
        DFS(start+1)
        return

    check = False
    for i in range(N):
        if start == i:
            continue
        if eggs[i][0] > 0:
            check = True

    if not check:
        answer = max(answer, N-1)
        return

    for i in range(N):
        if start == i or eggs[i][0] <= 0:
            continue
        eggs[start][0] -= eggs[i][1]
        eggs[i][0] -= eggs[start][1]
        DFS(start+1)
        eggs[start][0] += eggs[i][1]
        eggs[i][0] += eggs[start][1]

if __name__ == '__main__':
    N = int(input())
    eggs = [list(map(int, input().split())) for _ in range(N)]
    answer = -214700000

    DFS(0)
    print(answer)