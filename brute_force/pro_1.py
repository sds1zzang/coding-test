# 완탐

def solution(answers):

    # 1. 패턴 찾기
    A=[1,2,3,4,5]
    B=[2,1,2,3,2,4,2,5]
    C=[3,3,1,1,2,2,4,4,5,5]

    answer_len=len(answers)

    if answer_len<=0:
        return []

    # 1-1. 각 ABC 패턴 별 재구성
    if len(A)<answer_len:
        di=answer_len//len(A)
        na=answer_len%len(A)

        A=di*A
        for i in range(na):
            A.append(A[i])

    if len(B)<answer_len:
        di=answer_len//len(B)
        na=answer_len%len(B)

        B=di*B
        for i in range(na):
            B.append(A[i])


    if len(C)<answer_len:
        di=answer_len//len(C)
        na=answer_len%len(C)

        C=di*C
        for i in range(na):
            C.append(C[i])

    # 2. ABC패턴과 답이 맞을 경우 각 result ++1로 추가
    result_A=0
    result_B=0
    result_C=0
    result=[]

    for i in range(answer_len):

        if A[i]==answers[i]:
            result_A+=1

        if B[i] == answers[i]:
            result_B += 1

        if C[i] == answers[i]:
            result_C += 1

    result.append(result_A)
    result.append(result_B)
    result.append(result_C)

    # 최대값을 찾고 값이 같을 경우 오름차순으로 한다.
    max_list=[]
    maxi=max(result)
    for i in range(len(result)):

        if maxi<=result[i]:
            maxi=result[i]
            max_list.append(i+1)

    max_list.sort()
    return max_list

print(solution([4,5,4]))
print(solution([2,1,2,3,2,4,2,5]))

print(solution([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))
