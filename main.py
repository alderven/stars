import pyxel

import constants
from stars import Stars


class App:
    def __init__(self):

        # 1. Инициализируем приложение Pyxel
        pyxel.init(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, title=constants.TITLE, quit_key=pyxel.KEY_ESCAPE)
        pyxel.mouse(True)
        pyxel.fullscreen(True)

        # 2. Создаём звёзды
        self.stars = Stars()

        # 3. Запускаем объект "Pyxel"
        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):

        # 1. Очищаем экран
        pyxel.cls(pyxel.COLOR_BLACK)

        # 2. Рисуем звёзды
        self.stars.draw()


App()
