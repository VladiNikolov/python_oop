from project.dark_knight import DarkKnight

class BladeKnight(DarkKnight):
    def __init__(self, username: str, level: int):
        super().__init__(username, level)

# hero = Hero("H", 4)
# print(hero.username)
# print(hero.level)
# print(str(hero))
# elf = Elf("E", 4)
# print(str(elf))
# print(elf.__class__.__bases__[0].__name__)
# print(elf.username)
# print(elf.level)
