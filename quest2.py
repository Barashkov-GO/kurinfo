def main():
    n = int(input())
    a = n // 10
    flag = 1
    while a != 0:
        if a % 10 <= n % 10:
            flag = 0
        n = n // 10
        a = a // 10
    if flag == 1:
        print("yes")
    else:
        print("no")


if __name__ == '__main__':
    main()

