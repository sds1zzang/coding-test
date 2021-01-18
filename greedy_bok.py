
# 숫자 카드 게임
n,m=map(int,input().split())
maxi=0
for i in range(n):
    mini=10001
    data = list(map(int, input().split()))
    for j in range(len(data)):
        mini=min(mini,data[j])
    result=max(maxi,mini)

print(result)