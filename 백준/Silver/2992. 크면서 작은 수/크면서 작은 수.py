import sys
input = sys.stdin.readline

def DFS(L):
    global answer
    if L == N:
        num = int(''.join(res))
        if num > role:
            answer = min(answer, num)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            res[L] = lst[i]
            DFS(L+1)
            visited[i] = False

if __name__ == '__main__':
    lst = list(input().rstrip())
    
    role = int(''.join(lst))
    N = len(lst)
    res = [0] * N
    visited = [0] * N
    answer = 214700000

    DFS(0)
    
    if answer == 214700000:
        print(0)
    else:
        print(answer)