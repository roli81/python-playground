from tier import Tier


class Kuh(Tier):
    def __init__(self, name):
        super().__init__(name)

    def gibLaut(self):
        return "Muuuuuuuh!"

    def melken(self):
        print(self.name + "wurde gerade gemolken")