#N, L = 5,2
#ls = [1,2,100,101,1000]

N, L = map(int, input().split())
ls = list(map(int, input().split()))
ls.sort() #오름차순 정렬

ans = 1 #먼저 붙임
root = ls[0]

for i in range(1, N):
    if ls[i] - root < L:
        pass
    else:
        ans += 1
        root = ls[i] #테이프 붙이는 자리 update
print(ans)
