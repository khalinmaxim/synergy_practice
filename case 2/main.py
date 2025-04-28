import datetime
from datetime import date


def get_weekday(day, month, year):
    """Определяет день недели для заданной даты"""
    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    return days[date(year, month, day).weekday()]


def is_leap_year(year):
    """Проверяет, является ли год високосным"""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def calculate_age(birth_date):
    """Вычисляет текущий возраст пользователя"""
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age


def print_digital_style(date_str):
    """Выводит дату в стиле электронного табло с увеличенным разрешением"""
    digits = {
        '0': [
            ' ***** ',
            '*     *',
            '*     *',
            '*     *',
            '*     *',
            '*     *',
            ' ***** '
        ],
        '1': [
            '   *   ',
            '  **   ',
            '   *   ',
            '   *   ',
            '   *   ',
            '   *   ',
            ' ***** '
        ],
        '2': [
            ' ***** ',
            '*     *',
            '      *',
            '     * ',
            '   *   ',
            ' *     ',
            '*******'
        ],
        '3': [
            ' ***** ',
            '*     *',
            '      *',
            '  **** ',
            '      *',
            '*     *',
            ' ***** '
        ],
        '4': [
            '*    * ',
            '*    * ',
            '*    * ',
            ' ******',
            '     * ',
            '     * ',
            '     * '
        ],
        '5': [
            '*******',
            '*      ',
            '*      ',
            '****** ',
            '      *',
            '*     *',
            ' ***** '
        ],
        '6': [
            ' ***** ',
            '*     *',
            '*      ',
            '****** ',
            '*     *',
            '*     *',
            ' ***** '
        ],
        '7': [
            '*******',
            '     * ',
            '    *  ',
            '   *   ',
            '  *    ',
            ' *     ',
            '*      '
        ],
        '8': [
            ' ***** ',
            '*     *',
            '*     *',
            ' ***** ',
            '*     *',
            '*     *',
            ' ***** '
        ],
        '9': [
            ' ***** ',
            '*     *',
            '*     *',
            ' ******',
            '      *',
            '*     *',
            ' ***** '
        ],
        ' ': [
            '       ',
            '       ',
            '       ',
            '       ',
            '       ',
            '       ',
            '       '
        ],
        '-': [
            '       ',
            '       ',
            '       ',
            ' ***** ',
            '       ',
            '       ',
            '       '
        ]
    }

    # Разбиваем дату на символы
    chars = list(date_str)

    # Печатаем построчно
    for line in range(7):
        for char in chars:
            print(digits.get(char, ['       '])[line], end=' ')
        print()


def main():
    """Основная функция программы"""
    print("Введите дату вашего рождения")
    day = int(input("День: "))
    month = int(input("Месяц: "))
    year = int(input("Год: "))

    birth_date = date(year, month, day)

    # Проверка корректности даты
    try:
        datetime.datetime(year=year, month=month, day=day)
    except ValueError:
        print("Ошибка: Некорректная дата!")
        return

    print("\nРезультаты:")
    print(f"День недели: {get_weekday(day, month, year)}")
    print(f"Год {'високосный' if is_leap_year(year) else 'не високосный'}")
    print(f"Вам {calculate_age(birth_date)} лет")

    # Форматируем дату для вывода в цифровом стиле
    date_str = f"{day:02d}-{month:02d}-{year}"
    print("\nДата рождения в цифровом стиле:")
    print_digital_style(date_str)


if __name__ == "__main__":
    main()