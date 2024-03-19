if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    p = sorted(set(arr), reverse=True)
    print(p[1])