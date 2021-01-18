print((100//30)*30)

# 숫자 카드 게임
# 행 열 중에서 가장 높은 숫자가 쓰인 카드 한방을 뽑는 게임
n,m=map(int,input().split())
#가장 큰 수를 찾기 위해서는 가장 최솟값을 입력
maxi=0
for i in range(n):
    data=list(map(int,input().split()))
    # 가장 작은 값을 찾기 위해서는 가장 큰 값을 입력
    min_val=10001
    for a in data:
        min_val=min(min_val,a)
        print("result",min_val)
    maxi=max(min_val,maxi)
    print("maxi",maxi)


