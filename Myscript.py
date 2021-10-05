# Палитра команд: Ctrl+Shift+P
# Закомментировать участок: Ctrl + /
# Автоформатирование кода: Alt + Shift + F
# Сдвинуть строку: Alt + вверх/вниз
# Символы: Alt + NumPad (26 →, 25 ↓)
# Запустить код: F5
# Подсказка: Ctrl + Space
# Перенос строки \n

import numpy
import matplotlib.pyplot as plt

x = numpy.arange(-15, 16)
y = x ** 2

plt.plot(x, y)
plt.show()

