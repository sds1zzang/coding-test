result=[113,113,222]
result=[2,2,5]
result=[3,1,3]
result=[10,1,5]
result=[10,0,-1]
max_list = []
maxi = max(result)
for i in range(len(result)):
    # if result[i]==0:
    #     max=[]

    if maxi <= result[i]:
        maxi = result[i]
        max_list.append(i + 1)

max_list.sort()
print(max_list)