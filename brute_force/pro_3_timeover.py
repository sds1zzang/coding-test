# 카펫

def solution(brown, yellow):

    yellow_array=[]


    for i in range(yellow,0,-1):
        for j in range(1,yellow+1):
            if i*j==yellow and i>=j:
                # print(i,j)
                temp=(i,j)
                yellow_array.append(temp)


    # print(yellow_array)

    for i in yellow_array:
        # print("i",i)
        # print("i[0]",i[0])
        # print("i[1]", i[1])
        row=i[0]
        col=i[1]

        brown_row=i[0]*2
        brown_col=(i[1]+2)*2

        if brown_row+brown_col==brown:
            break

    print(row,col)

    # print(brown_row,brown_col)

    answer = [row+2,col+2]
    return answer


print(solution(10,2))
print(solution(24,24))
print(solution(8,1))