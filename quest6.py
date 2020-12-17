class dvoich(object):       # класс числа в двоичной записи

    def __init__(self, numb):   # инициализация s - строка - двочиная запись исходного числа
        self.isx = numb   # isx - исходное число - интовое значение
        self.s = bin(numb)   # revS - строка двоичной записи с инвертированными 0 и 1
        self.s = self.s[2:]   # обрезаем строку до нужного состояния, т.к. bin приписывает в начале 0b...
        self.revS = ''
        self.s = self.s.zfill(8)   # заполняем нулями сначала строки, добивая до 8 элементов
        for i in range(len(self.s)):
            if self.s[i] == '0':
                self.revS = self.revS + '1'
            else:
                self.revS = self.revS + '0'   # конструируем инвертированную строку

    def get10minus(self):   # numb - десятичная запись двоичного значения (инвертированной строки)
        numb = int(self.revS, 2)
        return numb - self.isx   # возвращаем numb - исходное число

    # def sum(self, x):   # функция считает сумму двоичных чисел на основе исчисления столбиком
    #                     # (можно использовать binary_sum, на момент написания я не знал о такой встроенной функции)
    #     str = ''
    #     per = 0         # переходящее слагаемое (то, что держим в уме)
    #     for i in range(8, -1, -1):
    #         g = int(self.s[i]) + int(x.s[i]) + per
    #         if g == 0:
    #             str = '0' + str
    #             per = 0
    #         elif g == 1:
    #             str = '1' + str
    #             per = 0
    #         elif g == 2:
    #             str = '0' + str
    #             per = 1
    #         elif g == 3:
    #             str = '1' + str
    #             per = 1
    #     return dvoich(int(str))


def solution(numb):   # решение простым перебором, т.к. исходное число ограничено 0 и 255
    for i in range(255):
        if numb == dvoich(i).get10minus():   # если введенное число равно числу от 0 до 255, проведенному по алгоритму
            return i   # то возвращаем число от 0 до 255, которое проводили по алгоритму (исходное число)


def main():
    n = int(input())
    print(solution(n))


if __name__ == '__main__':
    main()
