from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
from kivy.uix.label import Label
from kivy.uix.popup import Popup

Config.set('kivy', 'keyboard_mode', 'systemanddock')


def is_square(x):
    return (int(x ** 0.5)) ** 2 == x


def ferma_factorization(n, max_iteration=100):
    a = 2
    while n % a != 0:
        a += 1
    if a == n:
        return 1, n, 'Prime number', 0

    if n <= 1:
        return None, None, 'Error: Must be > 0', 0

    if n % 2 == 0:
        return None, None, 'Error: must be odd', 0

    if is_square(n):
        return int(n ** 0.5), int(n ** 0.5), 'Successful', 0

    x = int(n ** 0.5) + 1
    c = 0
    while not is_square(x * x - n):
        x += 1
        c += 1
        if c > max_iteration:
            return None, None, 'Error: cannot calculate', max_iteration

    y = int((x * x - n) ** 0.5)
    a, b = x - y, x + y

    return a, b, 'Successful', c


class Container(GridLayout):
    def calculation(self):
        try:
            inp_number = int(self.number_input.text)
            a, b, message, iter_n = ferma_factorization(inp_number, int(self.iteration_input.text))
            self.first_number.text, self.second_number.text, self.state_factorization.text = str(a), str(b), message
            Popup(title="Iterations count", title_align="center",
                  content=Label(text="{:d} iterations".format(iter_n)),
                  size_hint=(.5, .5)).open()
        except:
            self.state_factorization.text = 'Invalid value'


class Lab3_1App(App):
    def build(self):
        return Container()


if __name__ == "__main__":
    Lab3_1App().run()
