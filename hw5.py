def read_single_digit(num):
    if (num == 0):
        return '영'
    elif (num == 1):
        return '일'
    elif (num == 2):
        return '이'
    elif (num == 3):
        return '삼'
    elif (num == 4):
        return '사'
    elif (num == 5):
        return '오'
    elif (num == 6):
        return '육'
    elif (num == 7):
        return '칠'
    elif (num == 8):
        return '팔'
    elif (num == 9):
        return '구'

def read_number(num):
    num1 = read_single_digit(int(num[0]))
    num2 = read_single_digit(int(num[1]))
    num3 = read_single_digit(int(num[2]))
    full_num = num1 + num2 + num3
    return full_num

number = str(input("세 자리 정수 입력: "))
kor_number = read_number(number)
print(f"{kor_number}")
