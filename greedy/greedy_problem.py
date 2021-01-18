# 모험가 길드
# 모험가 N 명, 공포도 측정, 최대 몇개의 그룹
# n=map(int,input().split())
# data=list(map(int,input().split()))
# data.sort()
# print(data)
#
# group=0 # 결과 출력
# count=0 # 공포도에 따른 사람의 수
# for i in range(len(data)):
#     count+=1
#     if data[i]==count: # 여기 수정, count>=data[i]로 수정, 이유는 cou
#         group+=1
#         count=0
# print(group)

# 곱하기 혹은 더하기
# s=input()
# print(s)
# result=int(s[0])
# print(result)
#
# for i in range(1, len(s)):
#     print("s:",int(s[i]))
#     num=int(s[i])
#     if num<=1 or result<=1:
#         result+=num
#     else :
#         result*=num
# print(result)


# # 문자열 뒤집기
# ss=input()
# # 전부 0으로 뒤집는 경우
# count0=0
# # 전부 1로 뒤집는 경우
# count1=0
#
# #초기 값이 0 or 1인 경우
# if ss[0]==0:
#     count1+=1
# else :
#     count0+=1
#
# for i in range(1,len(ss)-1):
#     if ss[i]!=ss[i+1]:
#         if ss[i+1]=='0':
#             count1+=1
#         else :
#             count0+=1
#
# print("전부 0",count0, "전부 1",count1)
# result=min(count1,count0)
# print(result)
#
# # 만들수 없는 금액
# n=int(input())
# data=list(map(int,input().split()))
# data.sort()
# print(data)
# result=[]
# for i in range(0,len(data)):
#     for j in data:


# 볼링공 고르기
# n,m=map(int,input().split())
# data=list(map(int,input().split()))
# result=0
# for i in range(len(data)):
#     for j in range(i,len(data)):
#         if data[i]!=data[j]:
#             result+=1
# print(result)


# 무지의 먹방 라이브
# import time
# def solution(food_times, k):
#     answer = 0
#     tt=0
#     while True:
#         for i in range(len(food_times)):
#
#
#             print(food_times)
#
#             time.sleep(1)
#
#             if tt==k :
#                 print('when')
#                 print("i+1:",food_times[i])
#                 if food_times[i]>0:
#                     result=(i+1)
#                     print("end:",result)
#                     return result
#                 else :
#                     return -1
#
#             if food_times[i]>0:
#                 print('if')
#                 food_times[i]-=1
#                 print("index:", i,"food_time",food_times[i])
#                 tt += 1
#             elif food_times[i]==0:
#                 print('else')
#                 continue #를 하면 다음 꺼를 다음 시간에 먹기 떄문에 문제 발생
#
#
#     return answer
#
#
# solution([3,1,2],5)
