T = int(input())
count = []
button = [300,60,10]

for time in button:
    count.append(T//time)
    T = T % time
if T != 0:
    print(-1)
else:   
    print(*count)
