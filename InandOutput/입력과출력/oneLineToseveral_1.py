#한 줄로 입력 받아서 여러 줄로 출력하기

input_line = "안녕 윤진아. '인턴' 영화 재밌는데 왜 보지 않는 것이니?"
words = input_line.split()

for word in words:
    print(word)

numbers = input("숫자들을 콤마로 구분하여 입력하세여: ").split(',')
numbers = [int(num) for num in numbers]
print(numbers)