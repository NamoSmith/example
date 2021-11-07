"""Programs for saying Hi"""


class Hi:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Hi " + self.name


player1 = Hi("Namo")
print(player1)
