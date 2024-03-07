import argparse


class Configuration:
    def __init__(self):
        self.difficulty = "medium"  # Рівень складності за замовчуванням

    def set_difficulty(self):
        self.parser = argparse.ArgumentParser(description='Configuration game')
        self.parser.add_argument('-diff', '--difficulty', type=str, help='Set difficulty level', default='medium')
        self.args = self.parser.parse_args()
        self.difficulty = self.args.difficulty

    def get_difficulty(self):
        return self.difficulty

