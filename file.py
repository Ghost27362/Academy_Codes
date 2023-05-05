'''class Auto:
    def __init__(self, model, color, mark, price, name):
        self._model = model
        self._color = color
        self._mark = mark
        self._price = price
        self._name = name

    def input_selection(self):
        self._model = input('Enter the model car - ')
        self._color = input('Enter the color car - ')
        self._mark = input('Enter the mark car - ')
        self._price = input('Enter the price car - ')
        self._name = input('Enter the name car - ')
        if self._model and self._color and self._mark and self._price and self._name == 1:



    def display_info(self):
        print(f'\nYour model car is - {self._model}'
              f'\nYour color car is - {self._color}'
              f'\nYour mark car is - {self._mark}'
              f'\nYour price car is - {self._price}'
              f'\nYour name car is - {self._name}')




auto = Auto('model', 'color', 'mark', 'price', 'name')
auto.input_selection()
auto.display_info()'''