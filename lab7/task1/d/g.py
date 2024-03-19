n = int(input())
a = list(map(int, input().split()))
start = 0
end = n - 1
while start < end:
    a[start], a[end] = a[end], a[start]
    start += 1
    end -= 1
print(*a)