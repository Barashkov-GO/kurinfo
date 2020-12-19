# Это решение правильное для дополненной задачи, где нужно вывести также выбранные из пар числа
def main():
    f = open('B.txt', 'r')
    # f = open('A.txt', 'r')
    n = int(f.readline())
    maxMask = 2 ** n  # маска - десятичное число в двоичном представлении
    # 0 = 00...0, значит берем из каждой пары первые числа
    # 1 = 00..01, значит берем первые числа, кроме последней пары
    # 2 = 00..10, значит берем первые числа, кроме предпоследней пары и т. д.
    #   массив масок, если к задаче добавится задача сохранения последовательности,
    #   то просто откомментируем эту (7) и 25 строчку
    arr = [[0 for j in range(2)] for i in range(n)]  # массив для ввода данных из файла

    for i in range(n):
        str = f.readline()
        a, b = map(int, str.split())
        arr[i][0] = a
        arr[i][1] = b

    sAll = 0  # максимальная подходящая сумма
    for i in range(maxMask):
        s = 0  # обнуляем локальную сумму
        iDvoich = bin(i)  # строим двоичную запись числа i
        iDvoich = iDvoich[2:]  # убираем 0b из начала строки
        iDvoich.zfill(n)  # заполняем нулями в начале строки до количества пар элементов
        for j in range(len(iDvoich)):
            s += arr[j][int(iDvoich[j])]  # если в маске 0, то добавится первый элемент из пары, если 1, то второй
        if s % 3 != 0 and sAll < s:
            sAll = s  # обновляем глобальную сумму, если подходит
            maxI = i

    maxIbin = bin(maxI)
    maxIbin = maxIbin[2:]
    maxIbin.zfill(maxMask)

    for i in range(len(maxIbin)):
        print('For {0} pair: {1}'.format(i + 1, arr[i][int(maxIbin[i])]))

    print(sAll)


if __name__ == '__main__':
    main()
