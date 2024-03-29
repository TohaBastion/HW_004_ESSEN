"""task3"""


class Employee:
    """Клас співробітників"""
    def __init__(self, first_name, last_name, department, start_year):
        if not first_name.isalpha() or not last_name.isalpha():
            raise ValueError("Прізвище та ім\'я мають складатися з літер.")
        if not isinstance(start_year, int) or start_year < 2000:
            raise ValueError("Рік початку роботи має бути цілим числом, та не раніше 2000р.")
        self.first_name = first_name
        self.last_name = last_name
        self.department = department
        self.start_year = start_year


employees = []


while True:
    try:
        inp_first_name = input("Введіть ім'я співробітника (або Enter для завершення введення): ")
        if not inp_first_name:
            break
        inp_last_name = input("Введіть прізвище співробітника: ")
        inp_department = input("Введіть відділ співробітника: ")
        inp_start_year = int(input("Введіть рік початку роботи співробітника: "))
        employees.append(Employee(inp_first_name, inp_last_name, inp_department, inp_start_year))
    except ValueError as ex:
        print("Помилка:", ex)
        print("Будь ласка, спробуйте знову.")


while True:
    try:
        filter_year = int(input("Введіть рік, після якого потрібно вивести працівників: "))
        print("Співробітники, які були прийняті після", filter_year, "року:")
        for i, emp in enumerate(employees, start=1):
            if emp.start_year > filter_year:
                print(f"{i}. {emp.first_name} {emp.last_name} "
                      f"(відділ {emp.department}) - {emp.start_year}рік")
        break
    except ValueError:
        print("Рік повинен бути цілим числом.")
