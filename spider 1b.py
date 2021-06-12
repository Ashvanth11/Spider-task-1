n = int(input())
a = input()

ans = 0
mid = n // 2


def check(m):
        flag=0
        for x in range(0, m):
            if a[x] == a[m + x]:
                flag=1
            else:
                flag=-1
                break

        if flag==-1:
            return 0
        elif flag==1:
            return 1

check(mid)
while check(mid) == 1:
        ans += 1
        mid = mid // 2
        check(mid)

print(ans)

