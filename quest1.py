def main():
    n = int(input())
    a = int(input())
    k = int(input())
    i = 0
    while n != 0:
        if a == n % 10:
            i += 1
        n = n // 10
    if i > k:
        print("yes")
    else:
        print("no")


if __name__ == '__main__':
    main()

