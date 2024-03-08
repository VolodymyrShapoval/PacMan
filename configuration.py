import argparse

class Configuration:
    """
    Клас, що визначає конфігурацію гри.

    Атрибути:
    - difficulty (str): Рівень складності гри.

    Методи:
    - __init__(self): Конструктор класу. Ініціалізує об'єкт Configuration зі значенням рівня складності за замовчуванням.
    - set_difficulty(self): Встановлює рівень складності з командного рядка.
    - get_difficulty(self): Повертає поточний рівень складності гри.
    """

    def __init__(self):
        """
        Конструктор класу Configuration.

        Ініціалізує об'єкт Configuration зі значенням рівня складності за замовчуванням.
        """
        self.difficulty = "medium"

    def set_difficulty(self):
        """
        Встановлює рівень складності з командного рядка.
        """
        parser = argparse.ArgumentParser(description='Configuration game')
        parser.add_argument('-diff', '--difficulty', type=str, help='Set difficulty level', default='medium')
        args = parser.parse_args()
        self.difficulty = args.difficulty

    def get_difficulty(self):
        """
        Повертає поточний рівень складності гри.

        Повертає:
        - str: Рівень складності гри.
        """
        return self.difficulty

