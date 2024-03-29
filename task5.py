"""task5"""


class TrainerNotFoundException(Exception):
    """Клас вийняток"""
    pass


class SportComplex:
    """Клас спортивного комплексу"""
    def __init__(self):
        self.sports_info = {
            "Футбол": (["Пн. Ср. Пт. - 17.00", "Петров", 100],
                       ["Вт. Чт. Сб. - 13.00", "Іванченко", 120]),
            "Волейбол": (["Пн. Ср. Пт. - 15-00", "Іванов", 80],),
            "Бейсбол": (["Сб. - 11.30", "Петров", 120], ["Пн. Чт. - 18.00", "Сидоров", 110])
        }

    def show_sports(self):
        """Функція переліку видів спорту"""
        print("Перелік видів спорту:")
        for sport in self.sports_info:
            print(sport)

    def show_coaches(self):
        """Функція пелеліку тренерів"""
        print("Команда тренерів:")
        for sport, info in self.sports_info.items():
            for _, coach, _ in info:
                print(f"{coach} - {sport}")

    def show_schedule(self):
        """Функція розкладу"""
        print("Розклад тренувань:")
        for sport, info in self.sports_info.items():
            print(f"{sport}:")
            for schedule, _, _ in info:
                print(f"\t{schedule}")

    def show_price(self, sport):
        """Функція ціни"""
        if sport in self.sports_info:
            print(f"Вартість тренувань з {sport}:")
            for _, _, price in self.sports_info[sport]:
                print(f"\t{price} грн")
        else:
            print(f"Вартість тренувань з {sport} не визначена")

    def find_trainer(self, surname):
        """Функція пошуку тренера"""
        found = False
        for sport, info in self.sports_info.items():
            for schedule, coach, _ in info:
                if coach == surname:
                    print(f"Тренер {coach} працює у секції {sport} за розкладом: ({schedule})")
                    found = True
        if not found:
            raise TrainerNotFoundException(f"Тренера з прізвищем '{surname}' не знайдено")


def main():
    """Функція меню"""
    sport_complex = SportComplex()

    while True:
        print("\nМеню:")
        print("1 - Перелік видів спорту")
        print("2 - Команда тренерів")
        print("3 - Розклад тренувань")
        print("4 - Вартість тренування")
        print("5 - Пошук тренера за прізвищем")
        print("0 - Вихід")

        choice = input("Виберіть пункт меню: ")

        if choice == "1":
            sport_complex.show_sports()
        elif choice == "2":
            sport_complex.show_coaches()
        elif choice == "3":
            sport_complex.show_schedule()
        elif choice == "4":
            sport = (input("Введіть вид спорту: ")).capitalize()
            sport_complex.show_price(sport)
        elif choice == "5":
            surname = (input("Введіть прізвище тренера: ")).capitalize()
            try:
                sport_complex.find_trainer(surname)
            except TrainerNotFoundException as e:
                print(e)
        elif choice == "0":
            print("До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
