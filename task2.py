"""task2"""


def add(x, y):
    """Додавання"""
    return x + y


def subtract(x, y):
    """Віднімання"""
    return x - y


def multiply(x, y):
    """Множення"""
    return x * y


def divide(x, y):
    """Ділення"""
    if y == 0:
        raise ZeroDivisionError('Знаменник не може бути нулем!')
    return x / y


def exponentiation(x, y):
    """Зведення у ступінь"""
    if x == 0 and y < 0:
        raise ZeroDivisionError('Зведення нуля до від\'ємного ступеня не можливе!')
    return x ** y


def main():
    """Основна функція меню"""
    while True:
        print("\nВиберіть операцію:")
        print("1. Додавання")
        print("2. Віднімання")
        print("3. Множення")
        print("4. Ділення")
        print("5. Зведення в ступінь")
        print("6. Вихід")


        try:
            choice = input("Ваш вибір: ")

            if choice in ('1', '2', '3', '4'):
                num1 = float(input("Введіть перше число: "))
                num2 = float(input("Введіть друге число: "))

                if choice == '1':
                    print("Результат:", add(num1, num2))
                elif choice == '2':
                    print("Результат:", subtract(num1, num2))
                elif choice == '3':
                    print("Результат:", multiply(num1, num2))
                elif choice == '4':
                    print("Результат:", divide(num1, num2))
            elif choice == '5':
                num1 = float(input("Введіть число: "))
                num2 = float(input("Введіть ступінь: "))
                print("Результат:", exponentiation(num1, num2))
            elif choice == '6':
                print("Вихід...")
                break
            else:
                print("Невірний вибір. Спробуйте ще раз.")


        except ZeroDivisionError as e:
            print("Помилка:", e)
        except ValueError as e:
            print('Некоректны дані:', e)



if __name__ == "__main__":
    main()
