a = float(input("a를 입력하시오: "))
b = float(input("b를 입력하시오: "))
c = float(input("c를 입력하시오: "))

r = b ** 2 -4 * a * c

if (r > 0):
    x = (-b -((b ** 2 - 4 * a * c) ** 0.5)) / (2*a)
    y = (-b +((b ** 2 - 4 * a * c) ** 0.5)) / (2*a)
    print("실근은 %lf와 %lf입니다." %(x, y))

if (r == 0):
    x = 2 * a / -b
    print("중근은 %lf입니다." %x)
else:
    print("실근은 존재하지 않습니다.")
