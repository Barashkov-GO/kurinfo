def dividers(n, d):
    r = []  # объявляем массив r
    r += [1]  # добавляем в него 1 и само число
    r += [n]
    i = 2  # далее пойдем циклом с двойки, в цикле проверяем число на делителя n
    while i * i <= n:  # идем до квадратного корня из n,
        if n % i == 0:  # т.к. будем обрабатывать делители попарно (если 10 делится на 2, то оно делится и на 10/2=5)
            # соотв., для числа, например, 36 достаточно дойти до sqrt(36)==6,
            # а последующие делители уже будут к тому моменту добавлены в массив
            if i > d:  # проверяем больше ли найденный делитель, чем d
                r += [i]  # если так, то добавляем его в массив
            k = n // i  # это пара первого делителя
            if k != i and k > d:  # если второй делитель больше d, то добавляем в массив и его
                r += [k]
        i += 1
    return r


# МАССИВ ДЕЛАТЬ НЕОБЯЗАТЕЛЬНО, МОЖНО ПРОСТО СЧИТАТЬ ЭЛЕМЕНТЫ СЧЕТЧИКОМ
# (в начале функции объявим cnt = 0, r += [i] и r += [k] ЗАМЕНИМ НА cnt += 1, и вернем его в конце функции)
# Я НАПИСАЛ РЕШЕНИЕ С МАССИВОМ С ЗАДЕЛОМ НА СЛЕДУЮЩИЕ ЗАДАЧИ, ОПИРАЮЩИЕСЯ НА ЭТУ


# в мейне вводим два числа, потом выводим длину массива, который получаем при исполнении функции dividers (делители)
def main():
    n = int(input())
    d = int(input())
    print(len(dividers(n, d)))


if __name__ == '__main__':
    main()
