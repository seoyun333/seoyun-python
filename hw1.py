def get_radius(prompt):
    r = int(input(prompt))
    return r

def get_circle_area(r):
    s = 3.14*r*r
    return s

radius = get_radius('넓이를 구하고자 하는 원의 반지름은? ')
area = get_circle_area(radius)
print('반지름 %d인 원의 넓이 = 3.14 x %d x %d = %.2f' %(radius, radius, radius, 3.14*radius*radius))
