# count, k = map(int, input().split())
# ls = list(map(int, input().split()))
# temp = []
# for x in ls:
#     if x < k:
#         temp.append(x)
# print(" ".join(map(str, temp)))

# 리스트컴프리헨션
# count, k = map(int, input().split())
# ls = list(map(int, input().split()))
# temp = [x for x in ls if x < k]
# print(" ".join(map(str, temp)))

# 모듈
# def main():
#     count, k = map(int, input().split())
#     ls = list(map(int, input().split()))
#     result = [x for x in ls if x < k]
#     print(" ".join(map(str, result)))

# if __name__ == "__main__":
#     main()


# filter and lambda
def main():
    count, k = map(int, input().split())
    ls = list(map(int, input().split()))
    result = filter(lambda x: x < k, ls)
    print(" ".join(map(str, result)))
    """
    filter 함수
    filter 함수는 파이썬 내장 함수 중 하나로, 주어진 조건을 만족하는 요소들로 이루어진 iterator를 반환합니다. 
    이 함수는 두 개의 인자를 받습니다:
        함수 (function): 각 요소에 대해 평가될 조건을 정의하는 함수.
        iterable: 리스트, 튜플, 문자열 등 반복 가능한 객체.
        
    filter(function, iterable)
    """

    """ 
    'lambda' 함수는 파이썬에서 익명함수( 즉. 이름이 없는 함수)를 정의하는 데 사용.
    일반 함수와 달리 , 'lambda' 함수는 간단하게 정의할 . 수있어 특정 상황에서 유용
    1. 간결함
    2. 일시적인 사용 : 일회성 또는 일시적으로 필요한 간단한 기능을 정의할 때 유용.
    3. 익명함수 : 이름을 정의할 필요가 없으므로, 코드의 특정 위치에서만 사용되는 작은 함수를 정의할 때 편리.
    filter 함수와 lamda 함수를 이용한

    result = filter(lambda n: n % 2 == 0,numbers)
    """
