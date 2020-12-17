def findHigh(arr, pos):
    for i in range(pos + 1, len(arr), 1):
        if arr[i] > arr[pos]:
            return i
    return -1


def findLow(arr, pos):
    for i in range(pos + 1, len(arr), 1):
        if arr[i] < arr[pos]:
            return i
    return -1


def posl(arr, posChange, pos, ans):
    if pos < posChange:
        new = findHigh(arr, pos)
        if new == -1:
            return ans
        ans += [arr[new]]
        posl(arr, posChange, new, ans)
    else:
        new = findLow(arr, pos)
        if new == -1:
            return ans
        ans += [arr[new]]
        posl(arr, posChange, new, ans)


# -3, 6, -2, 5, 2, 3, 7, 16, -5, -9, 23, 11, 14, 18, 15, 17, 22, -1, 16, 9
def main():
    arr = []
    n = int(input())
    for i in range(n):
        arr += [int(input())]

    pos = 0
    for i in range(n):
        ans = []
        posl(arr, i, pos, ans)
        print(ans)


if __name__ == '__main__':
    main()
