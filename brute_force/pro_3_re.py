# 카펫

def solution(brown, yellow):
    # 1. 패턴 찾기 (그림 그려가면서 규칙성 확인)
    # 2. brown을 이용해 가질 수 있는 모든 경우의 수 찾기
    #     - brown으로 하는 이유는 brown의 최대값이 5000 이하이므로 경우의 수가 작기 때문
    #     - i는 가로의 개수 *2
    #     - j는 세로, +2는 가장 자리 개수 *2
    # 3. 패턴 찾기 (그림 그려가면서 규칙성 확인)
    for i in range(brown,0,-1):
        for j in range(1,brown+1):
            if i>=j and (i*2)+(j+2)*2==brown:

                # print(i,j)

                yellow_row=i
                yellow_col=j

                if yellow_row*yellow_col==yellow:
                    answer=[yellow_row+2,yellow_col+2]
                    return answer


    # yellow는 너무 범위가 크기 떄문에 시간초과
    # for i in range(yellow,0,-1):
    #     for j in range(1,yellow+1):
    #         if i*j==yellow and i>=j:
    #             # print(i,j)
    #             # temp=(i,j)
    #             # yellow_array.append(temp)
    #
    #             yellow_row=i
    #             yellow_col=j
    #
    #             brown_row=i*2
    #             brown_col=(j+2)*2
    #
    #             if brown_row+brown_col==brown:
    #                 # print("asdfadf")
    #
    #                 answer=[yellow_row+2,yellow_col+2]
    #                 return answer




print(solution(10,2))
print(solution(24,24))
print(solution(8,1))