def posl(arr, pos, vozr, ubyv, ans):
    if vozr == 0 and ubyv == 0 and arr[pos] < arr[pos + 1]:
        vozr = 1
        ans += [arr[pos + 1]]
        pos += 1
    elif vozr == 1 and ubyv == 0 and arr[pos] < arr[pos + 1]:
        ans += [arr[pos + 1]]
        pos += 1
    elif vozr == 1 and ubyv == 0 and arr[pos] > arr[pos + 1]:
        ans += [arr[pos + 1]]
        pos += 1
        ubyv = 1
    elif vozr == 1 and ubyv == 1 and arr[pos] > arr[pos + 1]:
        ans += [arr[pos + 1]]
        pos += 1
    elif vozr == 1 and ubyv == 1 and arr[pos] < arr[pos + 1]:
        return ans
    posl(arr, pos, vozr, ubyv, ans)


# -3, 6, -2, 5, 2, 3, 7, 16, -5, -9, 23, 11, 14, 18, 15, 17, 22, -1, 16, 9
def main():
    arr = []
    a = 0
    b = 0
    pos = 0
    ans = []
    n = int(input())
    for i in range(n):
        arr += [int(input())]

    posl(arr, pos, a, b, ans)

    print(ans)


if __name__ == '__main__':
    main()
