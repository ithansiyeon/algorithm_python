n = int(input())

d = [0]*(31)
d[0] = 1
d[1] = 0
d[2] = 3
for i in range(3,n+1):
    if i % 2 == 1:
        d[i] = 0
    else:
        d[i] = d[i-2]*3
        for j in range(4,i+1,2):
            d[i]+=d[i-j]*2

print(d[n])


