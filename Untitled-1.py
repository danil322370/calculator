def main():
    # Ввод чисел с обработкой ошибок
    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
    except ValueError:
        print("Ошибка: введено не число.")
        return

    print("Выберите операцию:")
    print("1. Арифметические операторы (+, -, *, /, //, %, **)")
    print("2. Операторы сравнения (==, !=, >, <, >=, <=)")
    print("3. Логические операторы (and, or, not)")
    print("4. Побитовые операторы (&, |, ^, ~, <<, >>)")
    print("5. Операторы принадлежности (in, not in)")
    print("6. Операторы тождественности (is, is not)")

    choice = input("Введите номер выбранной категории (1-6): ")

    # Арифметические операции
    if choice == '1':
        print("Выберите конкретную операцию:")
        print("a. + (сложение)")
        print("b. - (вычитание)")
        print("c. * (умножение)")
        print("d. / (деление)")
        print("e. // (целочисленное деление)")
        print("f. % (остаток)")
        print("g. ** (возведение в степень)")
        op = input("Введите букву операции: ").lower()

        if op == 'a':
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif op == 'b':
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif op == 'c':
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        elif op == 'd':
            if num2 != 0:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
            else:
                print("Ошибка: деление на ноль.")
        elif op == 'e':
            if num2 != 0:
                result = num1 // num2
                print(f"{num1} // {num2} = {result}")
            else:
                print("Ошибка: деление на ноль.")
        elif op == 'f':
            if num2 != 0:
                result = num1 % num2
                print(f"{num1} % {num2} = {result}")
            else:
                print("Ошибка: деление на ноль.")
        elif op == 'g':
            result = num1 ** num2
            print(f"{num1} ** {num2} = {result}")
        else:
            print("Некорректная операция.")
    
    # Операторы сравнения
    elif choice == '2':
        print(f"{num1} == {num2} : {num1 == num2}")
        print(f"{num1} != {num2} : {num1 != num2}")
        print(f"{num1} > {num2} : {num1 > num2}")
        print(f"{num1} < {num2} : {num1 < num2}")
        print(f"{num1} >= {num2} : {num1 >= num2}")
        print(f"{num1} <= {num2} : {num1 <= num2}")

    # Логические операторы
    elif choice == '3':
        condition1 = num1 > 0
        condition2 = num2 > 0
        print(f"condition1 (num1 > 0) and condition2 (num2 > 0): {condition1 and condition2}")
        print(f"condition1 or condition2: {condition1 or condition2}")
        print(f"not condition1: {not condition1}")

    # Побитовые операторы
    elif choice == '4':
        a = int(num1)
        b = int(num2)
        print(f"{a} & {b} : {a & b}")
        print(f"{a} | {b} : {a | b}")
        print(f"{a} ^ {b} : {a ^ b}")
        print(f"~{a} : {~a}")
        print(f"{a} << 2 : {a << 2}")
        print(f"{a} >> 2 : {a >> 2}")

    # Операторы принадлежности
    elif choice == '5':
        sample_list = [1, 2, 3, 4, 5]
        if num1 in sample_list:
            print(f"{num1} принадлежит списку {sample_list}")
        else:
            print(f"{num1} не принадлежит списку {sample_list}")
        if num2 not in sample_list:
            print(f"{num2} не принадлежит списку {sample_list}")
        else:
            print(f"{num2} принадлежит списку {sample_list}")

    # Операторы тождественности
    elif choice == '6':
        a = num1
        b = num2
        print(f"a is b: {a is b}")
        print(f"a is not b: {a is not b}")
    else:
        print("Некорректный выбор категории.")

if __name__ == "__main__":
    main()