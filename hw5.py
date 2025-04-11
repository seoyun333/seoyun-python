def read_single_digit(digit):
    korean_digits = ["영", "일", "이", "삼", "사", "오", "육", "칠", "팔", "구"]
    print(korean_digits[digit])

def read_number(num):
    num_str = str(num)
    for ch in num_str:
        read_single_digit(int(ch))


user_input = input("세 자리 이하의 10진 정수를 입력하세요: ")

read_number(int(user_input))
