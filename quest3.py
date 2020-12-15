def main():
    mas = [0] * 15
    for i in range(15):
        mas[i] = int(input())
    for i in range(2):
        print(mas[i])
    for i in range(8, 1, -1):
        print(mas[i])
    for i in range(9, 15, 1):
        print(mas[i])


if __name__ == '__main__':
    main()

