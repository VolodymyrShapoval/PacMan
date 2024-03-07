class Configuration:
    def __init__(self):
        self.difficulty = "medium"  # Рівень складності за замовчуванням

    def set_difficulty(self):
        print("Оберіть рівень складності:")
        print("1. Легкий")
        print("2. Середній")
        print("3. Важкий")

        choice = input("Ваш вибір (введіть номер): ")

        if choice == "1":
            self.difficulty = "easy"
        elif choice == "2":
            self.difficulty = "medium"
        elif choice == "3":
            self.difficulty = "hard"
        else:
            print("Невірний вибір. Встановлено середній рівень складності.")

    def get_difficulty(self):
        return self.difficulty

