def f1(a, b, c=0):
    return a + b + c

if __name__ == "__main__":
    print("Executing main\n")

    x = float(input("x = "))
    y = float(input("y = "))

    # Выводим результат
    print("%f + %f = %f" % (x, y, f1(x, y)))
