def get_radius():
    r = int(input("넓이를 구하고자 하는 원의 반지름은? "))
    return r

def get_circle_area():
    rad = radius  # 반지름 값을 한 번만 입력 받음
    s = 3.14 * rad * rad
    return s

radius = get_radius()  # 반지름 값을 변수에 할당
surface = get_circle_area()  # 원의 넓이 값을 변수에 할당
print("반지름", radius, "인 원의 넓이 = 3.14 x", radius, "x", radius, "=", surface)
