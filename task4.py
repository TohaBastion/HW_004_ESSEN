"""task4"""
MUSICAL_NOTES = ["до", "ре", "мі", "фа", "соль", "ля", "сі"]

class MyError(Exception):
    """Клас вийнятку"""
    pass


def has_string_symbols(string, symbols):
    """Функція перевірики наявності в списку"""
    if string in symbols:
        print(f'"{string}" це {MUSICAL_NOTES.index(string) + 1} нота')
    else:
        raise MyError('Не вигадуйте нові ноти їх всього 7')


def user_input_check():
    """Функція перевірки введених дпних"""
    while True:
        user_string = (input("Введіть ноту: ")).lower()
        try:
            has_string_symbols(user_string, MUSICAL_NOTES)
            break
        except MyError as ex:
            print(ex)


if __name__ == '__main__':
    user_input_check()
