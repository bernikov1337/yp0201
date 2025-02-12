def f1(a, b, c=0):
    return a + b + c

def f2(a, b):
    return a * b

if __name__ == "__main__":
    print("Executing main\n")

    x = float(input("x = "))
    y = float(input("y = "))

    # Выводим результат сложения
    print("%f + %f = %f" % (x, y, f1(x, y)))

    # Выводим результат произведения
    print("%f * %f = %f" % (x, y, f2(x, y)))
