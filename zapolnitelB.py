import random


def main():
    n = 1000000
    f = open('B.txt', 'w')
    f.write(str(n) + '\n')
    for i in range(n):
        a = random.randint(0, 13)
        b = random.randint(0, 13)
        f.write(str(a) + ' ' + str(b) + '\n')

    f.close()


if __name__ == '__main__':
    main()
