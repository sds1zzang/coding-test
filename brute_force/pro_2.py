from itertools import permutations

def solution(numbers):
    array=[]
    new_array=[]
    for i in numbers:
        array.append(str(i))

    new_array=array.copy()


    # num가 들어왔을 때 소수를 판단 (소수 - True, 소수 아니면 -False)
    # - 1이하 수가 들어오면 소수가 아니므로 False 리턴
    # - num을 2이상부터 num-1 부터 나누어서 만약 나머지가 0이면 소수가 아님 따라서 False 리턴
    # - for 문을 다 통과하면 소수인 True 리턴
    def sosu(su):
        temp=int(su)
        # print("temp",temp)
        if su[0] == '0' or temp <= 1:
            return False
        i=2
        for i in range(2,temp):
            if temp%i==0:
                # print("not sosu")
                return False
        return True

    # 중복 제거를 이용해 set을 이용한다.
    # - 첫째 자리는 문자열로 변경하고 list에 넣어준다
    # - 둘째 자리이상이면 permutations (순열)을 이용해서 모든 경우의 수를 찾는다.
    # - 이때 join() 과 map() 이용해 새로운 문자열로 바꾸고 이것을 기존 list에 extend로 합친다.
    # - 중복 제거를 이용해 set을 이용한다.
    for i in range(2,len(array)+1):

        # extend를 사용, append는 list 된것을 겹치기 때문에 extend를 사용
        # map을 사용하는 이유는

        # join() 함수 : 문자열 String 합치기
        # String 사이에 특정 문자열을 삽입하여 나뉘어져 있떤 String문자열을 새로운 문자열로 합쳐 준다.
        new_array.extend(list(map(''.join, permutations(array, i))))  # 2개의 원소로 수열 만들기

        # permutations(numbers,i)

    # print("all",new_array)
    set_array = list(set(new_array))
    # print("all_set",set_array)

    answer = 0

    # 만들 수 있는 수를 1번에서 만든 함수에 넣고 소수인지 확인한다.
    for i in range(len(set_array)):
        check=sosu(set_array[i])
        # print(check)
        if check:
            answer+=1
    return answer