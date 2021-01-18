# 그리디
# 현재 상황에서 지금 당장 좋은 것만 고르는 방법
# 주로 정렬 알고리즘과 짝을 이루어 출제됨

# ex 1) 거스름돈 문제
# n = 1260, 큰 화폐부터 거스름돈을 거슬러주고, 최소한의 거스름 동전의 갯수를 구하여라
# 동전은 500, 100, 50, 10원 으로 구성
n=1260
coin=[500,100,50,10]
count=0

for i in coin:
    print("i",i)
    count+=n//i #n의 갯수
    print("count",count)
    #count += n
    print("n", n)
    n=n%i # 이게 나머지

print(count)

# 거스름돈 문제가 그리디 알고리즘으로 해결 할 수 있는 이유는 가지고 잇는 동전 중에서 가장 큰 단위가 항상 작은 단위의 배수이므로 작은 동전들을 종합해 다른 해가 나올 수 없기 떄문
# 만약 거스름돈이 500, 400, 100원이고 800원을 거슬러 줘야 한다면, 일반적으론 500 1개 100원 3개 but, 400, 400원이 최적의 해가 됨
# 따라서 그리디 알고리즘은 큰 단위가 항상 작은 단위의 배수 형태일때 사용


# 큰 수의 법칙
# 입력 조건 N M K (5 8 3) // N는 리스트, 숫자가 더해지는 횟수 M, K는 연속해서 더할수 있는 횟수
# 입력 예시
# 5 8 3
# 2 4 5 4 6
# # 중요한 생각은 이 문제는 가장 큰 숫자와 2번째 숫자만을 고려해서 더하면 큰 수가 나옴
# 왜냐하면 반복이 허용하기 때문, 즉 가장 큰 수를 k번 더하고 2분째로 큰 수를 1번 더하는 연산을 반복
n,m,k=map(int,input().split())
# 여러 개의 숫자를 입력받을때 많이 사용, input()으로 입력받은 문자열을 split()을 이용해 공백으로 나눈 리스트로 바꾼 뒤에, map을 이용해 해당 리스트의 모든 원소의 int() 함수를 적용
data=list(map(int,input().split()))
# 3개 이상일때 list로 한번 더 저장, 이는 해당 리스트를 하나씩 꺼낼때 사용

# 1번 방법
data.sort()
print(data)
first=data[-1]
second=data[-2]
print("first",first,"second",second)
result=0

while True:
    for i in range(k):
        result=result+first
        m=m-1
        if m==0:
            break
    result=result+second
    m=m-1
    if m==0:
        break

print(result)

# 2번 방법, M의 크키가 100억 이상 처럼 커진다면 문제 발생, 따라서 규칙을 찾아서 곱하기로 변경
# (6,6,6,5) + 6,6,6,5 ... 규칙성이 보임
# 가장 큰 수의 합인 18을 찾고 이를 몇번 곱할것인가?! 이는 count=m//k+1로 구할 수 있음
# 만약 몫이 정수가 아니라면 나머지를 이용해 count=m%k 이용해 몇번 곱할 것인지 알 수 있음
# 2분째 큰 수는 m-


# N, M, K를 공백을 기준으로 구분하여 입력 받기
n, m, k = map(int, input().split())
# N개의 수를 공백을 기준으로 구분하여 입력 받기
data = list(map(int, input().split()))

data.sort()  # 입력 받은 수들 정렬하기
first = data[n - 1]  # 가장 큰 수
second = data[n - 2]  # 두 번째로 큰 수

result=0
# 가장 큰 수가 더해지는 횟수 계산
count=m%(k+1)
if count==0:
    first_count=m//(k+1)
    second_count=m//(k+1)
    result+=(first*k+second)*(first_count)
    print('1')
else :
    second_count=m//(k+1)
    na=count
    print("na", na)
    result+=((first*k+second)*(second_count))+first*na
    print('2')
print("result",result)