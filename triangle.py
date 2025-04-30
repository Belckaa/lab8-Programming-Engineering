import math
def triangle_area(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Неможливі сторони трикутника")
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

if __name__ == "__main__":
    a = float(input("Введіть сторону a: "))
    b = float(input("Введіть сторону b: "))
    c = float(input("Введіть сторону c: "))
    try:
        result = triangle_area(a, b, c)
        print(f"Площа трикутника: {result:.2f}")
    except ValueError as e:
        print("Помилка:", e)
